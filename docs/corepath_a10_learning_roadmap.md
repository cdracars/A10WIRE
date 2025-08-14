# CorePath – A10 Build Learning Roadmap

This roadmap sequences modifications to the Geeetech A10 with the goal of **maximizing skill-building** while progressing toward a CoreXZ (Switchwire) conversion, and optionally a future CoreXY build.

Each phase lists:

* **Goal** – What you’re learning
* **Difficulty** – Estimated based on mechanical/electrical complexity
* **Part Reusability** – Whether the mod’s parts carry over to later stages

---

## Phase 0: Baseline & Documentation

**Goal:** Establish reference performance for all future changes.
**Difficulty:** ★☆☆☆☆
**Part Reusability:** N/A (knowledge-based)
**Actions:**

* Stock hotend & electronics
* Run calibration prints (Benchy, cube, tall tower)
* Photograph & log results

---

## Phase 1: Ergonomics & Usability

**Goal:** Improve usability and prep for later mods.
**Difficulty:** ★☆☆☆☆
**Part Reusability:** LCD, wiring harness
**Actions:**

* Relocate LCD to top/front enclosure
* Add cable guides and PSU dust filter
* Print PLA riser feet (40–60 mm) for clearance test
* **Optional:** Replace glass bed with 235 mm × 235 mm magnetic PEI sheet

  * Improves adhesion and first-layer consistency
  * Works well with Klipper bed mesh leveling
  * Adds ~2 mm height – requires Z-offset recalibration

---

## Phase 2: Electronics Relocation

**Goal:** Learn safe mains wiring, harness design, and modular mounting.
**Difficulty:** ★★★☆☆
**Part Reusability:** All electronics, wiring
**Options:**

* **External Box** – PSU + board in single enclosure (RatRig/CR-10 style)
* **Under-Printer DIN Rail** – Compact footprint with heat shield
  **Actions:**
* Add quick-disconnect harness
* Separate mains & logic airflow paths

---

## Phase 3: Hero Me Learning Phase

**Goal:** Gain toolhead mounting, cooling, and probe integration skills.
**Difficulty:** ★★☆☆☆
**Part Reusability:** Toolhead plate, probe, fans
**Actions:**

* Ender 3 gantry plate swap
* Install Hero Me Gen 7 (4010 hotend fan, single 5015 blower)
* Experiment with single/dual blower, fan voltage, probe positions

---

## Phase 4: Linear Rail Upgrades

**Goal:** Learn rail alignment, preload, and lubrication.
**Difficulty:** ★★★☆☆
**Part Reusability:** All rails usable in CoreXZ/CoreXY
**Actions:**

* X-axis rail first (most visible improvement)
* Y-axis rail for bed stability
* Optional Z-axis rail for vertical rigidity

---

## Phase 5: Hotend Experiments

**Goal:** Understand hotend thermal limits, cooling needs, and flow rates.
**Difficulty:** ★★★☆☆
**Part Reusability:** Chosen final hotend moves forward
**Actions:**

* Test stock, Revo Six, Dragonfly, Rapido
* Log quality, speed limits, cooling changes

---

## Phase 6: CoreXZ Conversion (Switchwire)

**Goal:** Learn belt routing, dual-Z sync, and kinematic tuning.
**Difficulty:** ★★★★☆
**Part Reusability:** Rails, electronics, hotend/toolhead
**Actions:**

* Install dual Z motors and pulleys
* Tune CoreXZ motion in Klipper

---

## Phase 7: Stealthburner Transition

**Goal:** Finalize toolhead with CANbus, LEDs, Voron-style features.
**Difficulty:** ★★★☆☆
**Part Reusability:** Final toolhead carries to CoreXY
**Actions:**

* Install final hotend from Phase 5 results
* Add integrated lighting and cable management

---

## Phase 8: CoreXY Transition (Optional Future)

**Goal:** Apply all learned skills to a fixed-bed, dual-belt kinematic system.
**Difficulty:** ★★★★★
**Part Reusability:** Rails, electronics, toolhead, hotend
**Actions:**

* Build new frame or heavily modify A10
* Transfer existing precision components

---

## Tracking Progress

Mark each phase complete in your project tracker or README, and attach:

* Before/after print comparisons
* Notes on challenges and solutions
* Lessons learned for future builds

For upgrade strategy, compatibility, and reuse notes, refer to the **upgrade_plan.md**.

---
