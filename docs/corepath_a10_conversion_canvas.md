# 🛠️ CorePath – A10 Build · Enderwire/CoreXZ Conversion Canvas (Learning-First, Modular Path)

This canvas reflects the updated **learning-first** approach for converting a Geeetech A10 into a Klipper-powered CoreXZ "Enderwire"-style 3D printer, while leaving the door open for a future **CoreXY** build.
It also introduces earlier **electronics relocation**, **linear rails before dual Z**, and **under-printer DIN mounting** as part of the skill-building path.

---

## 🎯 Objective

Use the CorePath – A10 Build build as a hands-on learning platform for:

* Mechanical mods (linear rails, dual Z, kinematic changes)
* Electronics relocation & harness building
* Toolhead modularity & cooling duct design
* Hotend performance comparisons
* CoreXZ tuning and eventual CoreXY transition

---

## 🔍 Frame & Compatibility Overview

| Feature         | Status               | Notes                                                                 |
| --------------- | -------------------- | --------------------------------------------------------------------- |
| Frame Size      | ✅ Ender 3-like       | Standard 220×220×250; 2020 extrusion                                  |
| Z Mounts        | ⚠️ Base-mounted      | Needs printed or tapped extrusion mounts for CoreXZ                   |
| PSU & Mainboard | ❌ Two bulky housings | Relocate externally OR mount under printer with DIN rail + heatshield |
| X Gantry Plate  | ⚠️ Proprietary holes | Replace with Ender 3-compatible plate (Hero Me & future toolheads)    |
| LCD Mount       | ❌ Flush-mount metal  | Relocate to 2020 extrusion or front/top panel                         |

---

## 🛠️ Phased Upgrade Plan (Updated)

### Phase 0: Baseline & Documentation

* Stock A10 hotend + electronics
* Baseline calibration prints (Benchy, cube, tall tower)
* Photograph & log results for comparison

### Phase 1: Ergonomics & Usability

* Relocate LCD to top/front enclosure (in progress)
* Optional: Add PLA riser feet for clearance test under frame
* Minor cable management & PSU dust filter
* Optional: Replace glass bed with **235×235 mm magnetic PEI sheet**

  * Improves adhesion and bed mesh consistency
  * Adds ~2 mm height – requires Z-offset recalibration

### Phase 2: Electronics Relocation

* **Option A:** External combined PSU + board box (RatRig/CR-10 style)
* **Option B:** Under-printer DIN rail mount with heatshield & risers
* Add quick-disconnect harness between printer and electronics

### Phase 3: Hero Me Learning Phase

* Swap to Ender 3 gantry plate
* Install Hero Me Gen 7 with:

  * 4010 axial hotend fan
  * Single 5015 blower duct
* Keep stock hotend for cooling impact isolation
* Experiment: single vs dual blower, fan voltages, probe mounting

### Phase 4: Linear Rail Upgrades

* Start with X-axis, then Y-axis, optionally Z-axis
* Learn preload, shimming, lubrication
* Prepare for heavier/faster gantry

### Phase 5: Hotend Trials

* Test V6, Revo Six, Dragonfly, Rapido
* Log speed limits, cooling needs, thermal behavior

### Phase 6: CoreXZ (Switchwire) Conversion

* Install dual Z motors and pulleys (after rails)
* Route belts, tune motion
* Maintain Hero Me during CoreXZ learning

### Phase 7: Stealthburner Integration

* Install final hotend choice from Phase 5
* Add LEDs, CANbus, Voron-style features

### Phase 8: CoreXY Transition (Optional Future)

* Build new CoreXY frame or heavily modify A10 frame
* Transfer rails, toolhead, electronics

---

## 🔩 Parts Storage Plan

| Group                  | Dimensions (mm/in)    | Notes             |
| ---------------------- | --------------------- | ----------------- |
| X Gantry Screws        | 150×100×50 (6×4×2")   | Small bin or tray |
| Z Mount Hardware       | 180×125×75 (7×5×3")   | Box or drawer     |
| Bed Hardware           | 180×125×65 (7×5×2.5") | Lidded bin        |
| Control Box Parts      | 230×150×100 (9×6×4")  | With ESD pouch    |
| Endstop/Probe Wires    | 100×100×40 (4×4×1.5") | Cable pouch       |
| Misc. Screws           | 150×40 (6" tray)      | Magnetic tray     |
| Extruder/Hotend (opt.) | 200×150×75 (8×6×3")   | Padded box        |

---

## 🧪 Baseline Print Tracking

Use `baseline_print_report_template.md` to log:

* Filament & slicer profile
* Print time (est. vs actual)
* Dimensional accuracy
* Artifacts
* Images (front, top, side)

---

## 🗃️ Directory Structure (Planned)

corepath-a10/
├── README.md
├── upgrade_plan.md
├── learning_roadmap.md
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

* [ ] Print PLA riser feet & test under-bed clearance
* [ ] Decide on external vs under-printer electronics relocation
* [ ] Order Ender 3-style gantry plate
* [ ] Download Hero Me Gen 7 STLs for 4010 + single 5015
* [ ] Run baseline stock hotend prints
* [ ] Begin Hero Me cooling experiments
* [ ] Document all duct/hotend swap results
