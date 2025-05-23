
PA-AMR Hardware Specifications (Engineering Overview)
=====================================================

This document provides detailed specifications for the PA-AMR hardware variants with a focus on engineering-critical details. It includes physical dimensions, load capacities, electrical requirements, and hardware features across generations.

.. contents::
   :local:
   :depth: 2

Gen2 (Discontinued)
-------------------
**Physical Characteristics**

- Tray dimensions: 482 mm (W) × 340 mm (D)
- Extended tray: 542 mm (W) × 383 mm (D)
- Tote volume per tray: 50L
- Maximum load: 45 kg (with tote)

**Electrical**

- Power input: 24V DC system (from internal battery)
- Auto-charging: Not supported

**Features**

- Barcode scanner: Yes
- Touchscreen: Yes
- PTL (Put-To-Light): Not supported
- Auto wheel release: Not supported

---

Gen3 / Gen3.1
-------------

**Physical Characteristics**

- Tray dimensions: 542 mm (W) × 383 mm (D)
- Extended tray: Not available for Gen3
- Tote volume per tray: 60L
- Maximum load: 45 kg (with tote)

**Electrical**

- Operating voltage: 24V nominal
- Battery pack: 24V, 10Ah or higher
- Auto-charging:
  - Gen3: Not supported
  - Gen3.1: Optional
- Dock connector height: 375 mm

**Features**

- Barcode scanner: Yes
- Touchscreen: Yes
- PTL: Optional
- Auto wheel release: Optional

---

Gen3 XL
-------

**Physical Characteristics**

- Tray dimensions: 610 mm (W) × 470 mm (D)
- Extended tray: 700 mm (W) × 470 mm (D)
- Tote volume per tray: 75L
- Maximum load: 45 kg (with tote)

**Electrical**

- Operating voltage: 24V
- Power input via dock or manual charger
- Auto-charging: Not supported
- Dock connector height: 375 mm

**Features**

- Barcode scanner: Yes
- Touchscreen: Yes
- PTL: Not supported
- Auto wheel release: Optional

---

Gen3 XXL / Gen3.1 XXL
----------------------

**Physical Characteristics**

- Tray dimensions: 610 mm (W) × 470 mm (D)
- Extended tray: 700 mm (W) × 470 mm (D)
- Tote volume per tray: 75L
- Maximum load: 39.2 kg (with tote)

**Electrical**

- Voltage: 24V nominal
- Current Draw: Depends on load (base ~2.5A, peak ~7A)
- Auto-charging:
  - Gen3: Not supported
  - Gen3.1: Optional
- Docking clearance:
  - Required area: 1.845m (L) × 1.19m (W)
  - Gap between docks: ~0.74 m

**Features**

- Barcode scanner: Yes
- Touchscreen: Yes
- PTL: Not supported
- Auto wheel release: Optional

---

Notes
-----
- All AMRs use a 2-wheel differential drive layout with active wheel suspension.
- AMR mounting tolerances for docking stations should be maintained within ±5 mm.
- For precise localization during docking, ensure all top cameras are well-aligned and calibrated.
