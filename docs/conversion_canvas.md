# 🛠️ A10WIRE - Geeetech A10 to Enderwire Conversion Canvas (Learning-First)

This canvas reflects the updated **learning-first** approach for converting a Geeetech A10 into a Klipper-powered CoreXZ "Enderwire"-style 3D printer, adding a **Hero Me** phase before moving to Stealthburner.

---

## 🎯 Objective
Use the A10WIRE build as a learning platform for:
- Toolhead modularity
- Cooling duct design
- Hotend performance
- Gantry plate geometry
- CoreXZ motion tuning

---

## 🔍 Frame & Compatibility Overview

| Feature             | Status                      | Notes                                                |
|---------------------|-----------------------------|------------------------------------------------------|
| Frame Size          | ✅ Ender 3-like              | Standard 220×220×250; 2020 extrusion                 |
| Z Mounts            | ⚠️ Base-mounted              | Needs printed or tapped extrusion mounts             |
| Control Box         | ❌ Side-blocking CoreXZ path | Relocate electronics externally                      |
| X Gantry Plate      | ⚠️ Proprietary holes         | Replace with Ender 3-compatible plate (Hero Me req.) |
| LCD Mount           | ❌ Flush-mount metal         | Reuse with bracket or replace with Mini12864         |

---

## 🛠️ Phased Upgrade Plan (Updated)

### Phase 1: Initial Setup
- Stock A10 hotend + electronics
- Baseline calibration prints
- Document print quality

### Phase 2: Hero Me Learning Phase
- Swap to Ender 3 gantry plate
- Install Hero Me Gen 7 with:
  - 4010 axial hotend fan
  - Single 5015 blower duct
- Keep stock hotend to isolate cooling impact
- Experiment with:
  - Single vs dual blower ducts
  - Fan voltages and speeds
  - Probe mounting options

### Phase 3: Hotend Trials
- Test V6, Revo Six, Dragonfly, Rapido
- Log performance, speed, and cooling differences

### Phase 4: CoreXZ Conversion
- Install dual Z motors and pulleys
- Drill/tap or replace gantry plate if needed
- Route belts, tune motion system
- Continue Hero Me experiments in CoreXZ mode

### Phase 5: Stealthburner Integration
- Install final hotend choice from Phase 3 data
- Add LEDs, CANbus, and Voron-style features
- Retire Hero Me after final learning cycle

---

## 🔩 Parts Storage Plan

| Group                   | Dimensions (mm/in)          | Notes                        |
|-------------------------|-----------------------------|------------------------------|
| X Gantry Screws         | 150×100×50mm (6×4×2")       | Small bin or tray            |
| Z Mount Hardware        | 180×125×75mm (7×5×3")       | Box or drawer                |
| Bed Hardware            | 180×125×65mm (7×5×2.5")     | Lidded bin                   |
| Control Box Parts       | 230×150×100mm (9×6×4")      | With ESD pouch               |
| Endstop/Probe Wires     | 100×100×40mm (4×4×1.5")     | Cable pouch                  |
| Misc. Screws            | 150×40mm (6" tray)          | Magnetic tray                |
| Extruder/Hotend (opt.)  | 200×150×75mm (8×6×3")       | Padded box recommended       |

---

## 🧪 Baseline Print Tracking
Use `baseline_print_report_template.md` to document:
- Filament & slicer profile
- Print time (est. vs actual)
- Dimensional accuracy
- Artifacts (ringing, stringing, curling)
- Images (front, top, side)

---

## 🗃️ Directory Structure (Planned)

a10-to-enderwire/
├── README.md
├── conversion_analysis.md
├── docs/
│   ├── build_guide.md
│   ├── images/
│   ├── print_tests/
│   │   └── baseline_print_report_template.md
│   └── teardown_storage_checklist.pdf
├── stls/
├── cad/
├── firmware/
│   └── printer.cfg

---

## 🧠 Next Actions
- [ ] Order Ender 3-style gantry plate
- [ ] Download Hero Me Gen 7 STLs for 4010 + single 5015
- [ ] Run baseline stock hotend prints
- [ ] Begin Hero Me cooling experiments
- [ ] Document all duct/hotend swap results
