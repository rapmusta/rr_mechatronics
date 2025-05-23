
Autocharging System - Master Manual (Gen3.1 + XXL)
===================================================

.. contents::
   :local:
   :depth: 2

1. Standard Operating Procedure (SOP) – Installation & Handling
---------------------------------------------------------------

1.1 Positioning and Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Place docking stations as per specified dimensions (see layout diagrams).
- Ensure minimum space per robot type (Gen3 to XXL). Refer to the formula section for required clearances.
- Use 20kg concrete blocks behind stations for stability — stations are not to be wall-mounted.

1.2 Power & Electrical Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Each station consumes: **7A @ 100V AC**
- Max 2 stations per outlet with **15A fuse**
- Plug in power, turn knob to “Auto” to activate station

1.3 Initial Calibration
~~~~~~~~~~~~~~~~~~~~~~~
- Dock robot manually, then switch to auto mode
- SSH into the robot container:
  ::

    dectl exec amr bash
    rosrun sootballs_autodock dock_pose_config_writer.py

- Restart robot for calibration to apply
- This stores “AR board to dock pose” offset unique to each robot’s top camera

1.4 Inspection Before Use
~~~~~~~~~~~~~~~~~~~~~~~~~
- Confirm connector alignment: **375mm from ground**
- Protective plates must not block connectors
- Clean AR markers, ensure adequate lighting
- Use height templates to ensure consistent alignment

2. Operational Guidelines (Robot + Dock Station)
------------------------------------------------

2.1 Charging Area Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Keep docking path and charge spot **clear of obstacles/people**
- Maintain clean, visible AR board — avoid glare/clutter
- AR board ID and AR marker config must match `markers.yaml` in `rapyuta.io`

2.2 Robot Handling Rules
~~~~~~~~~~~~~~~~~~~~~~~~
- Do **not** dock/undock in **Manual** or **Emergency Stop** mode
- If set to manual while docking, move robot back **0.6m**, then reset to auto
- Robots in emergency/maintenance must be moved from dock zones

2.3 Localization & Navigation Criticality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Robots rely on AR marker-based localization for docking
- Bad localization → blocking, failed docking, or stuck robots
- Use AR markers on floor → charge spot → dock station

2.4 Retry & Error Handling
~~~~~~~~~~~~~~~~~~~~~~~~~~
- Current software retries docking if undocked cleanly
- **Known issue**: stuck rotation due to IMU noise during dock → blocks retries
- LED + sound signals:
  - **Docking**: white LED, loop travel pulse
  - **Charging**: blue LED, single ding
  - **Undocking**: yellow LED, loop travel pulse

3. Robot & Software Configuration
---------------------------------

3.1 Required Files to Update:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- `robots.json`: `"autocharging_enabled": true`
- `sites.json`: `docking_board_id` schema
- `maps.json`: metadata entry per charge spot

3.2 Minimum Docking Area Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+----------+----------+----------------+-----------+
| Robot Type | Length L | Width W  | Gap b/w Docks  | Area (A)  |
+============+==========+==========+================+===========+
| Gen3       | ~1.65m   | ~0.81m   | ~0.36m         | ~1.34m²   |
| Gen3 XL    | ~1.76m   | ~1.0m    | ~0.55m         | ~1.76m²   |
| Gen3 XXL   | ~1.845m  | ~1.19m   | ~0.74m         | ~2.20m²   |
+------------+----------+----------+----------------+-----------+

4. Improvement Notes and Known Issues
-------------------------------------

- Robot Misalignment due to bent Realsense or poor mounting = overheat + dock failures
- 5cm margin between docks is acceptable with accurate approach
- AR board offset calibration is mandatory — affected by top camera variation
- Robots with bad localization may:
  - Miss dock
  - Misclassify charge spot
  - Block other robots
- IMU drift during charging may make robots think they’re rotating → get stuck

Additional Resources
--------------------

- `autocharging_software_design.docx`
- Marker board IDs setup (via `rapyuta.io`)
- AR marker printing template (`autocharging_pnl_interfaces`)
- Calibration tool: `dock_pose_config_writer.py`
