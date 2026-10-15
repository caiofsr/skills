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

## Clean output

Use a few named groups when they help edits. Remove editor metadata and unused definitions. Retain enough coordinate precision to preserve shared edges, typically 2–3 decimals after construction. An optimizer must preserve viewBox, accessible names, ID references, and visible appearance. Compare renders after optimization.

For inline informative SVG, provide a title and a unique `aria-labelledby`. Decorative SVG can use `aria-hidden="true"` and `focusable="false"`. For `<img>`, the consuming HTML supplies `alt`; an internal SVG title does not replace it.

## Structural verification

Parse the XML, check the root/viewBox, find duplicate IDs, and resolve local fragment references. Inspect root bounds and filter regions separately. Reject external resources and active content. Parsing confirms syntax only; it cannot establish silhouette, depth, or useful detail.

The example uses fixed `box-*` IDs for a standalone file. Rename them per instance if embedding the raw SVG repeatedly. Use the React reference's `useId` pattern for components.
