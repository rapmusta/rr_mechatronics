
Autocharging System - Technical Engineering Manual (Gen3.1 + XXL)
==================================================================

This document provides engineering-specific insights into the mechatronics, configuration, and calibration of the autocharging infrastructure for Gen3.1 and XXL Sootballs AMRs.

.. contents::
   :local:
   :depth: 2

1. Mechanical & Electrical Specifications
-----------------------------------------

1.1 Electrical Load
~~~~~~~~~~~~~~~~~~~
- Input Voltage: **100 VAC**
- Current Draw: **7A per docking station**
- **Max 2 docking stations per 15A fused outlet**

1.2 Mechanical Assembly
~~~~~~~~~~~~~~~~~~~~~~~
- **Docking connector height on robot:** 375 mm from ground
- **Dock station dimensions:** 0.453 m (L) × 0.425 m (W)
- **Stabilization:** 20 kg concrete block behind each dock
- **Not wall-mounted** – dock must not be moved post-alignment

1.3 Recommended Installation Clearances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- See section 3.2 for full area clearance formulas
- Lighting should be uniform and shadow-free
- AR board visibility is critical (avoid occlusions or glossy reflections)

2. Docking System Calibration
-----------------------------

2.1 Robot Calibration Script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Performed once per robot to store dock pose offset for its top camera:

Steps:
- Manually dock robot
- Set robot to auto mode (locks wheels)
- SSH into robot container:
  ::

    dectl exec amr bash
    rosrun sootballs_autodock dock_pose_config_writer.py

- Restart the robot
- Stores AR board to dock pose offset on filesystem

2.2 AR Marker Board Setup
~~~~~~~~~~~~~~~~~~~~~~~~~
- Marker board must have a valid ID registered in `rapyuta.io` config
- Consists of 4 AR markers:
  - bottom_left
  - top_right
  - top_left
  - bottom_right
- Example config:
  ::

    1000:
      position: [-0.473, 13.72, 0.37]
      orientation: [.0, 0.0, 90.0]
      marker_config:
        bottom_left:
          id: 600
        ...

3. Spatial Requirements & Area Calculations
-------------------------------------------

3.1 Clearance Formula
~~~~~~~~~~~~~~~~~~~~~
::

  L = 0.425 + 0.32 - 0.07 + 0.5 + robot_radius + 0.15
  W = 2 * robot_radius + 0.15
  A = L * W
  G = W - 0.453

Where:
- `robot_radius` = circumscribed radius of the robot
- 0.15 m = combined navigation + localization margin

3.2 Dimension Table

+-------------+----------+---------+--------+---------+
| Robot Type  | Length L | Width W | Gap G  | Area A  |
+=============+==========+=========+========+=========+
| Gen3        | 1.65 m   | 0.81 m  | 0.36 m | 1.34 m² |
| Gen3 XL     | 1.76 m   | 1.00 m  | 0.55 m | 1.76 m² |
| Gen3 XXL    | 1.845 m  | 1.19 m  | 0.74 m | 2.20 m² |
+-------------+----------+---------+--------+---------+

4. Robot Configuration Requirements
-----------------------------------

4.1 Descriptors
~~~~~~~~~~~~~~~
`robots.json` must include:
::

  "robot_descriptors": {
    "meta_data": {
      "autocharging_enabled": true
    }
  }

4.2 Map Metadata
~~~~~~~~~~~~~~~~
- `sites.json`: Add schema for `docking_board_id`
- `maps.json`: Charge spots must include:
::

  "meta_data": {
    "docking_board_id": "1001"
  }

5. Software Component Overview
------------------------------

5.1 LBC Bridge
~~~~~~~~~~~~~~
- Handles docking, undocking, charging states
- Sends signals to signal server:
  - **Docking**: White LED, travel pulse
  - **Charging**: Blue LED, single ding
  - **Undocking**: Yellow LED, travel pulse
- Responsible for retry and overheat error handling

5.2 Autodocking Library
~~~~~~~~~~~~~~~~~~~~~~~
- Consumes AR board pose → calculates dock trajectory
- Suppresses localization noise during precise docking

5.3 Base Controller Inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~
- Autocharge plug detection
- Overheat monitoring
- Battery status reporting

5.4 Perception and Localization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- AR marker detection (position + orientation)
- AMCL and fallback localization for docking

6. Known Failure Modes and Engineering Notes
--------------------------------------------

- Misaligned docking due to:
  - Bent camera mount
  - Wrong dock height
  - Calibration not done
- Overheating under tight dock fit or high ambient temps
- Dock stuck due to IMU drift (robot believes it's rotating)
- Poor localization causes robot to block dock lanes
- Re-docking during recovery may be necessary

7. Suggested Improvements (Engineering)
---------------------------------------

- Add a rigid, adjustable height template to align docks easily
- Enforce min. dock gap via planning constraints
- Use IMU + AR fusion to resolve stuck-docking states
- Implement retry strategy after overheat

Appendix
--------

- Tool: `dock_pose_config_writer.py`
- AR Marker: `autocharging_pnl_interfaces.pdf`
- Site Config: `rapyuta.io -> Marker Config Page`
- Reference Document: `autocharging_software_design.docx`
