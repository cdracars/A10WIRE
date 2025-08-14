# 🛠️ CorePath – A10 Build (Geeetech A10 Learning-to-CoreXZ/CoreXY) – Upgrade Plan

This document consolidates the original `conversion_analysis.md` and updated `a10wire_upgrade_plan` into a unified **upgrade plan** for the Geeetech A10. It reflects the full learning-first modular path, addressing hardware compatibility, part reuse, performance gains, and decision tradeoffs like PEI upgrades and Klipper adoption.

---

## 🎯 Project Purpose

Transform a stock Geeetech A10 into a **learning-first CoreXZ machine**, while preparing for a potential **future CoreXY** conversion.

Focus areas:

* CoreXZ mechanics and linear motion upgrades
* Electronics relocation and harness building
* Modular toolhead experimentation (Hero Me → Stealthburner)
* Klipper firmware setup and tuning
* Optional transition to CoreXY with precision components reused

---

## ⚙️ Compatibility Overview

| Problem Area          | Challenge                           | Solution                                                        |
| --------------------- | ----------------------------------- | --------------------------------------------------------------- |
| Control Box Layout    | PSU on side, mainboard under bed    | Relocate externally or DIN rail mount with risers + heat shield |
| Z Motor Mounts        | Mounted to base, not extrusion      | Print CoreXZ-compatible mounts or tap 2020 extrusions           |
| X Gantry Plate        | Proprietary pattern                 | Replace with Ender 3-style gantry for Hero Me and mods          |
| GT2560 Board Mounting | No stock mounting after removal     | Mount to DIN rail or inside external electronics box            |
| Endstop Positions     | Y max homing (rear), X/Z normal     | Update Klipper config for Y max homing                          |
| LCD Mount             | Side mount metal bracket            | Relocate to 2020 extrusion or front/top enclosure               |
| Z Probe               | Stock 3D Touch (Klipper-compatible) | Retain for use with Hero Me and mesh leveling                   |

Confirmed hardware:

* GT2560 V3.0 board (Klipper-compatible, limited long term)
* 3D Touch probe installed
* LCD: 12864-style screen, usable with Klipper or upgrades

---

## 🔁 Incremental Upgrade Path (with Skill Focus)

### ✅ Step 1: Klipper on Stock A10

* **Board**: GT2560 (Klipper-compatible)
* **Benefits**: 30–50% faster prints, pressure advance, mesh leveling
* **Learning**: Firmware install, printer.cfg, macros, tuning

### ✅ Step 2: PEI Bed Upgrade (Optional)

* **Size**: 235 × 235 mm — fits A10’s aluminum bed
* **Pros**: Strong adhesion, improved first layer, mesh consistency
* **Cons**: Adds ~2 mm Z height, requires Z offset recalibration
* **Best Time**: During or after Klipper setup

### ✅ Step 3: Belt-Driven Dual Z (Optional Mid-Path)

* **Mod**: Kevinakasam’s belt Z system
* **Benefits**: Eliminates Z-banding, enables G34 tramming
* **Compatibility**: **Not reusable** in CoreXZ; becomes e-waste
* **Cost**: ~$60–80

### ✅ Step 4: CoreXZ Conversion (Switchwire Style)

* **Motion**: CoreXZ (X and Z linked with belts)
* **Learning**: Belt routing, motor sync, kinematics tuning
* **Reuses**: Linear rails, Hero Me toolhead, PEI bed, motors
* **Tools**: Klipper config with `[kinematics: corexz]`, input shaping

### ✅ Step 5: Stealthburner Integration

* **Toolhead**: LED lighting, CANbus, clean cable routing
* **Hotend**: Final choice from Phase 5 testing
* **Learning**: CAN setup, firmware tuning, cable management

### ✅ Optional Step 6: CoreXY Platform

* **When**: Once CoreXZ is mastered
* **Frame**: Custom CoreXY with fixed bed
* **Reuses**: Rails, electronics, toolhead, firmware

---

## 🔩 Part Reuse Summary

| Part                   | Dual Z Compatible | Switchwire Compatible | Notes                        |
| ---------------------- | ----------------- | --------------------- | ---------------------------- |
| Linear Rails (MGN12H)  | ✅                 | ✅                     | Fully transferable           |
| GT2560 Mainboard       | ✅                 | ✅ (limited)           | Klipper-compatible           |
| Stepper Motors         | ✅                 | ✅                     | Reused in new configurations |
| 3D Touch / BLTouch     | ✅                 | ✅                     | Ideal for mesh leveling      |
| PEI Magnetic Plate     | ✅                 | ✅                     | Recommended: 235 × 235 mm    |
| Belt-Driven Z Hardware | ✅                 | ❌                     | Not used in CoreXZ           |
| Dual Z Mounts          | ✅                 | ❌                     | Physically incompatible      |

---

## 📊 Print Performance Comparison

| Metric             | Stock A10 | Dual Z       | Switchwire CoreXZ |
| ------------------ | --------- | ------------ | ----------------- |
| Outer perimeter    | 40 mm/s   | 60 mm/s      | 120+ mm/s         |
| Infill speed       | 80 mm/s   | 100 mm/s     | 300 mm/s          |
| Z-axis speed       | 8 mm/s    | 25 mm/s      | 50–100 mm/s       |
| Z artifacts        | ❌ Yes     | ✅ Eliminated | ✅ Eliminated      |
| Print time savings | —         | 20–30%       | 3–5× faster       |

---

## 🧠 Recommendations

* **Start with Klipper + PEI** → Immediate gains, builds firmware skills
* **Skip Dual Z if going Switchwire** → Investment becomes obsolete
* **Linear Rails Early** → Benefit both Dual Z and CoreXZ upgrades
* **Plan for Reuse** → Save cost by choosing upgrade paths with forward-compatible parts

---

*Maintained as part of the CorePath – A10 Build project – a hands-on CoreXZ learning platform.*
