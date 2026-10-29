# Lighting and shadows

## One light direction

Place the apparent light above and left in screen space. Keep top faces light, screen-left faces medium, and screen-right faces darker. A face gradient should reinforce this ordering. Use `gradientUnits="userSpaceOnUse"` when the direction must stay consistent across differently sized faces.

A curved surface can have a broad highlight along its light-facing region. Keep cast shadows directed down and right. Do not add a different highlight direction to make a particular face brighter.

## Ground shadow

Use a flattened ellipse or a simplified projected footprint beneath the contact point. Start with opacity 0.10–0.16, blur `stdDeviation` 2–3 units, and a 2–5 unit offset toward the lower right. These are canvas-space defaults for 128 units, not pixels at every display size.

Anchor the nearest edge to the object's base. An oversized gap makes a resting object appear to float. Floating objects can use a wider, lighter shadow with a deliberate gap. A compact darker contact shadow may help a heavy object, but use it only where contact occurs.

## SVG filter bounds

Explicit bounds prevent clipped blur. Prefer `filterUnits="userSpaceOnUse"` for a known canvas and size the region around the shadow geometry, not just the object. Allow roughly two blur standard deviations beyond its visible shape, plus offsets, at the shadow opacities used here. The third standard deviation falls below 1/255 and reads as transparent, so the viewBox may trim it without a visible seam. The simplest safe region is the whole canvas; a tighter region must never cut the blur while it is still visible.

Use one ground blur for the example family. Add `feDropShadow` only when a distinct overlapping object needs separation. Default filter boxes may clip. Stacked drop shadows make every part look detached.

If filters are unsupported in the target exporter or render poorly at small sizes, replace the blur with a low-opacity ellipse or a layered footprint and inspect that fallback. Avoid claiming identical appearance across renderers without checking them.
