# Geeetech A10 to Enderwire Conversion Analysis (Learning-First Path)

## Objective
Evolve the Geeetech A10 into a CoreXZ (Enderwire-style) machine through a **learning-first** phased upgrade plan, prioritizing hands-on experimentation with toolheads, cooling systems, and hotends.  
The new plan introduces a **Hero Me** phase before moving to a Stealthburner to maximize practical learning in mechanical, cooling, and hotend behavior.

---

## Overview
The Geeetech A10 is an Ender 3–style printer with ~85% component compatibility. While not a perfect clone, small printed adapters and minor drilling make it viable for an Enderwire build. The updated approach uses this compatibility to experiment with modular toolhead designs before the full CoreXZ conversion.

---

## Problem / Solution Summary

| Problem Area             | Description                                          | Solution                                                              |
| ------------------------ | ---------------------------------------------------- | --------------------------------------------------------------------- |
| **Control Box Position** | Side-mounted PSU + board obstructs CoreXZ belt paths | Remove control box and relocate electronics externally                |
| **Z Motor Mounts**       | Mounted to base, not extrusion sides                 | Drill/tap existing extrusions or print CoreXZ-compatible motor mounts |
| **X Gantry Plate**       | Proprietary layout, lacks belt/toolhead anchors      | Replace with Ender 3-style plate to enable Hero Me and future upgrades|
| **GT2560 Mounting**      | No frame mount after removing box                    | Print board tray for SKR/Manta and mount externally                   |
| **Endstop Positions**    | Y endstop is at back; X/Z are standard               | Adjust Klipper config for Y max homing                                |
| **Z Probe**              | 3D Touch probe already installed                     | Retain for Hero Me and later phases                                   |
| **LCD Frame Mounting**   | Side metal mount                                     | Relocate to 2020 extrusion mount or front panel                       |

---

## Confirmed Hardware Details
* **3D Touch Probe**: Installed, Klipper-compatible
* **Y Endstop**: Rear-mounted (requires inverted homing in config)
* **X/Z Endstops**: Standard Ender 3 positions
* **Mainboard**: GT2560 V3.0 (Klipper-compatible but limited — upgrade recommended later)
* **LCD**: 12864-style, suitable for remount or later replacement

---

## Updated Technical Path

**New Core Element** → Add a **Hero Me Gen 7** toolhead phase before Stealthburner:
- Requires Ender 3-compatible gantry plate
- Supports hotend swaps (V6, Revo, Dragon, etc.)
- Allows part cooling experiments (single/dual 5015 blowers)
- Teaches mounting geometry, duct aerodynamics, and hotend thermal tuning

---

## Recommended Upgrade Path (Learning-First)

### Phase 1: Baseline
- Stock A10 electronics + hotend
- Run calibration prints (Benchy, XYZ cube, “Bency Dog”)
- Document results

### Phase 2: Hero Me Integration
- Swap to Ender 3-style gantry plate
- Install Hero Me with 4010 hotend fan + single 5015 blower duct
- Keep current hotend for baseline comparisons
- Experiment: swap ducts, try dual blowers, adjust fan speeds

### Phase 3: Hotend Experiments
- Swap between stock hotend, Revo Six, Dragonfly, or Rapido
- Record print quality, speed limits, and tuning differences

### Phase 4: CoreXZ Conversion
- Install dual Z motors and pulleys
- Route belts, rehome axes
- Maintain Hero Me during CoreXZ learning period

### Phase 5: Stealthburner Transition
- Final toolhead for long-term setup
- Select hotend based on Hero Me test data
- Integrate LEDs, CANbus, and Voron-style features

---

## Conclusion
By adding a Hero Me learning phase, this plan turns the A10WIRE build into a controlled environment for experimenting with toolhead mechanics, airflow, and hotend performance — all before committing to the final Stealthburner setup.
