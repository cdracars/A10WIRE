# 🧰 A10WIRE Build Guide

> **Version:** Phase 1 (CoreXZ motion, stock GT2560, no enclosure)

---

## 🛠️ Table of Contents

1. [Required Tools](#required-tools)
2. [Teardown Steps](#teardown-steps)
3. [Mechanical Modifications](#mechanical-modifications)
4. [Printed Parts](#printed-parts)
5. [Motion System Assembly](#motion-system-assembly)
6. [Wiring Notes](#wiring-notes)
7. [Firmware Setup (Klipper)](#firmware-setup-klipper)
8. [Initial Calibration](#initial-calibration)
9. [Baseline Print Test](#baseline-print-test)
10. [What’s Next](#whats-next)

---

## 🧰 Required Tools

- M2/M3 hex keys
- Flush cutters
- 10mm wrench (for eccentric nuts)
- Soldering iron (optional, probe wire fixes)

---

## 🔧 Teardown Steps

> Photos of each step should go in `docs/images/`.

1. Power off and unplug the printer
2. Remove bed and bed wiring
3. Detach X gantry and top extrusion
4. Label all wiring (or photograph)
5. Store hardware using `teardown_storage_checklist.pdf`

---

## 🦾 Mechanical Modifications

- X Gantry Plate: drill new holes or swap to Ender 3 plate
- Belt Path: install new Z belt anchors
- Z Stepper Mounts: printed mounts or remixed A10-compatible version

---

## 🖨 Printed Parts (Phase 1)

- `x_gantry_bracket_v1.stl`
- `z_belt_anchor_left.stl`
- `z_motor_mount_right.stl`
- Optional: `corexz_test_frame_clip.stl`

All files live in `/stls/`.

---

## 🧵 Motion System Assembly

1. Mount CoreXZ steppers
2. Route belts with proper crossing pattern
3. Tension belts and check pulley alignment
4. Install carriage and check for slop

---

## ⚡ Wiring Notes

- GT2560 can be flashed for Klipper
- BTT Pi v1.2 used for USB connection + Klipper host
- Reuse 3D Touch probe wiring

---

## 🧠 Firmware Setup (Klipper)

1. Flash GT2560 for Klipper (STM32F103)
2. Clone or write `printer.cfg`
3. Set up `/dev/serial/by-id/...` for USB device
4. Test homing and endstops

---

## 📏 Initial Calibration

- PID tune hotend
- Level bed manually
- Run test square print
- Check for CoreXZ slippage or skipping

---

## 🧪 Baseline Print Test

Results and notes should be added to `docs/print_tests/`.

---

## 🚀 What’s Next

See `conversion_canvas.md` to track what’s planned for Phase 2:
- New controller board (e.g., Manta M4P/CB1)
- Direct drive upgrade
- Full enclosure

