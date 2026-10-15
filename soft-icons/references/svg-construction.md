# SVG construction

## Portable source

Use an SVG root with `xmlns="http://www.w3.org/2000/svg"` and `viewBox="0 0 128 128"`. Preserve editable paths, polygons, ellipses, gradients, and small native filters. Use an empty canvas for transparency. Prefer descriptive filenames such as `cloud-upload.svg`.

Put gradients, filters, and clips in `<defs>`. Prefix IDs with the icon name for separately authored assets, and make them instance-unique for repeated inline use. Every `url(#...)`, `href="#..."`, and accessibility reference must resolve to the intended element.

Use explicit fill values or documented theme variables. Avoid scripts, event handlers, remote URLs, embedded raster images, and `foreignObject` in distributable icons. Convert essential lettering to paths only when licensing permits; usually remove tiny text and keep the shape recognizable without it.

## Construction order

1. Ground shadow.
2. Rear or occluded parts.
3. Visible side faces.
4. Top and front details in their actual overlap order.
5. Restrained highlights and contact shading.

Use local face coordinates for badges and markings, then project them with the face. A front-facing badge pasted over an angled face breaks the projection. Prefer clipping for a detail that must stay within a face, with a clip path matching that face.

## Surface placement and occlusion

Before placing a detail, identify its supporting face, the usable region of that face, and any foreground part that can hide it. Project the detail and its full frame, sill, bevel, and shadow in the supporting face's coordinates. Screen-space bounding boxes alone do not establish containment on an angled wall.

Keep attached details inside the usable region, including their frame and effects. Leave a visible margin from neighboring parts at the intended display size. For a house, place the complete window below the projected underside of the eave, not merely below the roof ridge. Lower or resize it when the complete frame does not fit.

Use paint order to express physical depth. Draw a wall, then its window, then any roof/eave that lies in front of that window. This is a local dependency, not a universal rule that every roof must be last. Split groups when different parts need different overlap orders.

Clip face-bound details to the visible supporting face when containment requires it. A wall clip alone is insufficient when the roof covers part of that wall; also apply the foreground occluder through paint order or a mask. Keep genuinely projecting parts, such as a sill, outside the face clip when appropriate, while still respecting roof occlusion.

Resolve placement before hiding overflow. Moving the roof in front can repair depth ordering but leave half a window hidden. Unless that partial occlusion is intentional, reposition or resize the window so it reads as a complete architectural feature. Preserve purposeful intersections, such as a chimney passing through a roof, with a coherent joint and contact shading.

## Clean output

Use a few named groups when they help edits. Remove editor metadata and unused definitions. Retain enough coordinate precision to preserve shared edges, typically 2–3 decimals after construction. An optimizer must preserve viewBox, accessible names, ID references, and visible appearance. Compare renders after optimization.

For inline informative SVG, provide a title and a unique `aria-labelledby`. Decorative SVG can use `aria-hidden="true"` and `focusable="false"`. For `<img>`, the consuming HTML supplies `alt`; an internal SVG title does not replace it.

## Structural verification

Run the bundled `scripts/validate_svg.py` on every delivered SVG. Its restricted static SVG subset rejects raster/image content, active content, external references, duplicate IDs, and broken local references. Expand its supported vocabulary deliberately if a legitimate vector feature needs it; do not bypass a reported error.

Parse the XML, check the root/viewBox, find duplicate IDs, and resolve local fragment references. Inspect root bounds and filter regions separately. Reject external resources and active content. Parsing confirms syntax only; it cannot establish silhouette, depth, or useful detail.

The example uses fixed `box-*` IDs for a standalone file. Rename them per instance if embedding the raw SVG repeatedly. Use the React reference's `useId` pattern for components.
