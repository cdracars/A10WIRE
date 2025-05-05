# Geeetech A10 to Enderwire Conversion Analysis

## Objective

Evaluate the Geeetech A10 as a foundation for a phased CoreXZ conversion (Enderwire-style), focusing on reuse of stock parts, compatibility issues, and long-term upgrade planning.

---

## Overview

The Geeetech A10 is a derivative of the Ender 3, sharing a similar frame size and motion system but with several layout and component differences. While not a 1:1 clone, it offers \~85% compatibility with Ender 3 components and mods. With a few mechanical adjustments and printed adapters, it can serve as a solid foundation for an Enderwire build.

---

## Problem / Solution Summary

| Problem Area             | Description                                          | Solution                                                              |
| ------------------------ | ---------------------------------------------------- | --------------------------------------------------------------------- |
| **Control Box Position** | Side-mounted PSU + board obstructs CoreXZ belt paths | Remove control box and relocate electronics externally                |
| **Z Motor Mounts**       | Mounted to base, not extrusion sides                 | Drill/tap existing extrusions or print CoreXZ-compatible motor mounts |
| **X Gantry Plate**       | Proprietary layout, lacks belt anchors               | Drill/tap current plate or replace with Ender 3-style gantry plate    |
| **GT2560 Mounting**      | No frame mount after removing box                    | Print board tray for SKR/Manta and mount externally                   |
| **Endstop Positions**    | Y endstop is at back; X/Z are standard               | Adjust Klipper config for Y max homing                                |
| **Z Limit Switch**       | Located at toolhead (top mount)                      | Already replaced by 3D Touch probe                                    |
| **LCD Frame Mounting**   | Right-side flush metal mount, not extrusion-mounted  | Remove LCD and reuse in a printed front-mount or panel enclosure      |

---

## Confirmed Hardware Details

* **3D Touch Probe**: Installed and Klipper-compatible
* **Y Endstop**: Rear-mounted (Klipper will require inverted Y homing logic)
* **X/Z Endstops**: Located in standard Ender 3 positions (left/bottom)
* **Mainboard**: GT2560 V3.0 (not ideal for Klipper, upgrade recommended)
* **LCD**: 12864-style with encoder, can be remounted or upgraded later

---

## Technical Validation and Findings

* **Control Box**: Not a blocker — typically removed in Switchwire builds. A10’s side box is functional short-term, but relocation is essential during enclosure and CoreXZ phase.
* **Z Motor Mounting**: A10 uses base-mount Z stepper. Enderwire assumes extrusion-mount. Remapping via drilling or printing compatible mounts is straightforward.
* **X Gantry**: Stock A10 plate uses proprietary hole pattern. Most Enderwire STLs expect Ender 3 hole layout. Options: tap/mod stock plate, or drop in a Creality-style gantry.
* **GT2560 V3.0 + Klipper**: Technically compatible with Klipper but not recommended. Lacks performance and integration features. Upgrade to 32-bit board early in project.
* **Endstops**: Only Y is inverted (at rear). Klipper allows config fix. X and Z (now replaced with probe) are already compatible.
* **Z Probe**: 3D Touch is fully compatible with Klipper and expected for Switchwire.
* **LCD**: Side mount will conflict with belts/enclosure. Solution: reuse board in printed 2020-mount enclosure, or upgrade to Mini12864.

---

## Recommended Upgrade Path (Phased)

### Phase 1: Reuse Stock Electronics

* Keep GT2560 and 12864 LCD temporarily
* Begin printing parts and testing fitment of Enderwire STL mods

### Phase 2: Upgrade Electronics

* Replace GT2560 with SKR Mini E3 or Manta M4P
* Relocate board outside enclosure
* Reuse 12864 or upgrade to Mini12864 or touchscreen

### Phase 3: Convert to CoreXZ (Enderwire)

* Install dual Z motors and pulleys
* Replace or drill X gantry plate
* Implement belt paths and rehome axes

### Phase 4: Enclosure & Refinement

* Mount electronics externally
* Add front panel LCD or remote touchscreen
* Finalize Klipper `printer.cfg`

---

## Final Conclusion

The Geeetech A10 is a strong candidate for a cost-efficient Enderwire build. While not a direct Ender 3 clone, it requires only modest mechanical adjustments — most of which can be solved with printed parts and small drilling operations. Leveraging its stock components in early stages allows for a staged, low-cost CoreXZ upgrade path into a full Switchwire-style machine.

This document summarizes the full analysis, problem breakdown, and upgrade roadmap for converting the Geeetech A10 to a modern CoreXZ printer platform using open-source Enderwire/Switchwire components.

