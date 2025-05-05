# 🛠️ A10WIRE - Geeetech A10 to Enderwire Conversion Canvas

This canvas summarizes all key data, plans, and files from the conversion of a Geeetech A10 into a Klipper-powered CoreXZ "Enderwire"-style 3D printer. It serves as the authoritative artifact for tracking the build process, documentation, and reusable assets.

---

## 🎯 Objective
Transition the Geeetech A10 into a modern CoreXZ motion printer using open-source mods, Klipper firmware, and a phased approach that prioritizes hardware reuse and documentation.

---

## 🔍 Frame & Compatibility Overview

| Feature             | Status                      | Notes                                                |
|---------------------|-----------------------------|------------------------------------------------------|
| Frame Size          | ✅ Ender 3-like              | Standard 220×220×250; 2020 extrusion                 |
| Z Mounts            | ⚠️ Base-mounted              | Needs printed or tapped extrusion mounts             |
| Control Box         | ❌ Side-blocking CoreXZ path | Relocate electronics externally                      |
| X Gantry Plate      | ⚠️ Proprietary holes         | Modify or replace with Ender 3-compatible plate      |
| LCD Mount           | ❌ Flush-mount metal         | Reuse with bracket or replace with Mini12864         |

---

## 🛠️ Phased Upgrade Plan

### Phase 1: Initial Setup
- Clean & inspect frame
- Run baseline prints (Benchy, XYZ cube, “Bency Dog”)
- Document results

### Phase 2: Teardown & Reorganization
- Label, organize, and store parts
- Extract GT2560 & LCD
- Begin printing conversion components

### Phase 3: CoreXZ Conversion
- Install new motor mounts
- Drill/tap or replace gantry plate
- Add CoreXZ belts + tensioners

### Phase 4: Electronics & Firmware
- Install SKR Mini E3 / Manta M4P + CB1
- Flash Klipper & configure endstops/probe
- Tune printer.cfg

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
- Filament, slicer profile
- Print time (est. vs actual)
- Dimensional accuracy
- Artifacts (ringing, stringing, curling)
- Images (front, top, side)

> ❗ Do not redistribute the “Bency Dog” STL — include photos only.

---

## 🗃️ Directory Structure (Planned)

a10-to-enderwire/
├── README.md
├── conversion_analysis.md
├── docs/
│ ├── build_guide.md
│ ├── images/
│ ├── print_tests/
│ │ └── baseline_print_report_template.md
│ └── teardown_storage_checklist.pdf
├── stls/
├── cad/
├── firmware/
│ └── printer.cfg


---

## 🧠 Next Actions

- [ ] Extract image stills from teardown/cleaning video
- [ ] Add photos of calibration prints
- [ ] Populate `/stls/` and `/cad/` with custom part remixes
- [ ] Publish GitHub repo & README
- [ ] Begin YouTube build log (Episode 0)

---

Project by: **Dracars Designs**  
Machine Code Name: `A10WIRE`


