# Passive Microfluidic Mixing via Chaotic Advection at Low Reynolds Number
**CLL770 Course Project** — Rahul Kumar (2023CH10260), Divyanshu Sharma (2023CH10947), Nayan Kumar (2023CH10557)

## Summary
Two liquids flowing side by side in a 200 × 80 µm microchannel (Re ≈ 0.2, Pe ≈ 2000) mix only by slow diffusion.
We compared passive groove designs on the channel floor using 3D COMSOL Multiphysics 5.4 simulations
(Creeping Flow + Transport of Diluted Species) under identical conditions.

| Design | Outlet mixing index M | Pressure drop |
|---|---|---|
| 1. Plain channel | 0.40 | ≈ 8.5 Pa (theory) |
| 2. Straight grooves (90°) | 0.36 | 7.99 Pa |
| 3. V-grooves, irregular tip (our design) | 0.54 | 7.48 Pa (3.2 mm) |
| **4. Slanted grooves (45°) — best** | **0.69** | 7.93 Pa |

Mixing index: M = 1 − √⟨(c − 0.5)²⟩ / 0.5 (area average on a cross-section; 0 = unmixed, 1 = fully mixed).

## Full COMSOL models (with solutions)
The solved `.mph` files (up to 76 MB) are on Google Drive: https://drive.google.com/drive/folders/1BOy4lDNPuHf0UMfzr48Nav9yOlE01zY5
The copies in `comsol_models/` here are the same models; the larger ones have their solution and mesh cleared to fit GitHub (open in COMSOL 5.4 and click Compute).

## Repository contents
- `comsol_models/` — COMSOL 5.4 model files: `plainpipe`, `straightgrooves`, `vshapedirregular`, `slantedgrooves` (large files as `_light` copies without the solution; click Compute to re-solve).
- `results/` — screenshots: geometry, mesh, concentration slices, outlet profiles, result tables.
- `figures/` — design top views and comparison charts.
- `analysis/` — Python scripts used to make the figures.

## Simulation settings (all designs)
Channel 200 µm × 80 µm × 3.4 mm (3.2 mm for Design 3); grooves 16 µm deep, 50 µm wide, 100 µm pitch, 45°;
water, U = 1 mm/s; inlet c = 1 (left half) / 0 (right half); D = 1e-10 m²/s; outlet p = 0; Normal mesh.

## References
1. Stroock et al., "Chaotic mixer for microchannels", Science 295 (2002) 647.
2. Aref, "Stirring by chaotic advection", J. Fluid Mech. 143 (1984) 1.
3. Nguyen & Wu, "Micromixers—a review", J. Micromech. Microeng. 15 (2005) R1.
