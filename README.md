# 🛠️ A10WIRE – Geeetech A10 CoreXZ Conversion
### by Dracars Designs · maintained by [cdracars](https://github.com/cdracars)

A10WIRE is a fully documented, budget-conscious conversion of the Geeetech A10 3D printer into a CoreXZ machine inspired by the Voron Switchwire and Enderwire projects. Designed with progressive upgrade phases, this project allows hobbyists to reuse stock components while transitioning toward a Klipper-powered, enclosed printer.

> ⚙️ **Open Source. Built in public. Modular by design.**

---

## 📌 Project Objectives

- 🔁 Reuse stock GT2560 board, LCD, 3D Touch probe (initial phase)
- ✅ Convert to CoreXZ using Enderwire-style mechanics
- 📦 Add enclosure and external electronics in later phases
- ✍️ Fully documented design, firmware, BOMs, teardown, and testing

---

## 🔄 Working Phases

| Phase | Focus |
|-------|-------|
| 1     | CoreXZ motion w/ stock electronics, open-frame |
| 2     | Klipper board + toolhead upgrade (e.g. Manta + CB1) |
| 3     | Flexplate & frame bracing |
| 4     | Full enclosure (ACM/acrylic) + wiring |
| 5+    | QoL mods (nozzle cleaning, CANbus, camera, auto-off) |

---

## 🗂 Repo Layout

```
build_phases.md – Full upgrade roadmap and phase breakdown

docs/a10_vs_enderwire.md – Hardware breakdown and compatibility notes

docs/ – Print tests, teardown notes, BOMs

stls/ – Printable parts per phase

firmware/ – Klipper configs + macros

cad/ – Source parts (STEP, SCAD, Fusion)

scripts/ – Optional helpers (e.g. BOM gen)

changelog.md – Version tracking for working phases
```

---

## 🔗 Attribution & Licensing

This project builds on work from:

- [Voron Switchwire](https://github.com/VoronDesign/Voron-Switchwire) – CC BY-SA 4.0
- [Ender_SW Rev.2](https://github.com/boubounokefalos/Ender_SW) – CC BY-NC-SA 4.0
- [enderwire_nonpro](https://github.com/thomasfjen/enderwire_nonpro) – CC BY-NC-SA 4.0
- [RobotRogue/Enderwire_Docs](https://github.com/RobotRogue/Enderwire_Docs) – MIT

All remixed files, design derivatives, and new documentation are © 2025 Dracars Designs and licensed under **CC BY-NC-SA 4.0** unless otherwise stated.

---

## 📺 Watch the Build

Follow the build progress, time-lapses, and teardown over on the **Dracars Designs YouTube channel**:
🎥 _[link coming soon]_

Want to contribute, remix, or report issues? Feel free to open a PR or Discussion!