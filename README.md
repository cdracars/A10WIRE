# CorePath – A10 Build
_Geeetech A10 learning-first path → CoreXZ (Enderwire style) → optional CoreXY_

CorePath is a reusable, **skills-first** approach to evolving a 3D printer through staged upgrades.  
**This build** documents the Geeetech A10 journey from stock → Klipper → toolhead & motion upgrades → CoreXZ → (optionally) CoreXY, with a strong focus on part reusability and structured documentation.

> ✳️ Former name: **A10WIRE**. This repo keeps the same mission but no longer assumes Switchwire is the final form.

---

## Why CorePath?
- **Learning-first:** Each phase lists goals, difficulty, and what knowledge/components carry forward.
- **Modular:** Choose paths that **reuse** parts (rails, hotend, electronics).
- **Documented:** Baselines, checklists, storage plans, and print logs for each step.

---

## Phase Snapshot
1. Baseline & Documentation  
2. Ergonomics & Usability (LCD relocation, risers, PEI)  
3. Electronics Relocation (external box or under-printer DIN)  
4. Hero Me Learning Phase (Ender 3 gantry plate, 4010 + 5015)  
5. Linear Rails (X → Y → optional Z)  
6. Hotend Trials (V6, Revo, Dragonfly, Rapido)  
7. CoreXZ (Switchwire) Conversion (dual Z, belts, tune)  
8. Stealthburner Integration (LEDs, CANbus)  
9. Optional CoreXY Platform (new frame, parts reuse)

For full details, see the documents below.

---

## Documents
- **Learning Roadmap:** `docs/corepath_a10_learning_roadmap.md`  
- **Conversion Canvas:** `docs/corepath_a10_conversion_canvas.md`  
- **Upgrade Plan:** `docs/corepath_a10_upgrade_plan.md`  
- **Master Reference (all-in-one):** `docs/corepath_a10_master_reference.md`

---

## Repo Structure (proposed)
```
corepath-a10/
├─ README.md
├─ docs/
│  ├─ corepath_a10_master_reference.md
│  ├─ corepath_a10_learning_roadmap.md
│  ├─ corepath_a10_conversion_canvas.md
│  └─ corepath_a10_upgrade_plan.md
├─ stls/
├─ cad/
├─ firmware/
│  └─ printer.cfg
└─ images/
```

---

## Quick Start
1. **Capture baseline:** Benchy, 20 mm cube, tall tower; log times/dimensions and artifacts.  
2. **Phase 1 (Ergonomics):** LCD relocation to 2020, print risers, cable tidy, optional 235×235 mm PEI.  
3. **Phase 2 (Electronics):** Decide **external box** vs **under-frame DIN**. Add quick‑disconnect harness.  
4. **Phase 3–5:** Hero Me experiments → Linear rails → Hotend trials (log results).  
5. **Phase 6+:** CoreXZ conversion; later Stealthburner; evaluate CoreXY path.

---

## Status & TODO
- [ ] Decide electronics relocation strategy (external vs under-printer DIN).
- [ ] Order Ender 3 gantry plate + Hero Me G7 STLs (4010 + single 5015).
- [ ] Print PLA risers; verify under‑bed clearance & airflow.
- [ ] Run baseline prints; start print log in `docs/`.
- [ ] Prepare parts storage bins per dimensions in Conversion Canvas.

---

## License
Proprietary/Other (per project owner).

---

### Credits
- Inspired by Voron Switchwire, Enderwire and the broader 3D printing community.
- Maintained by @cdracars.
