---
name: soft-icons
description: >-
  Create, edit, and review custom Soft Isometric 3D icons as editable SVG, with optional React/TypeScript SVG components. Use when a task requests isometric or soft 3D SVG icons, an illustrated icon set, or new custom UI icons where this visual style is requested or already established, including icons needed while building a screen. Preserve existing icon libraries and other visual styles unless the user asks to replace them. Raster image generation and unrelated SVG fixes are outside this skill.
---

# Soft isometric icons

Produce editable vector icons with consistent projection, matte materials, and soft lighting. Use SVG geometry and native effects. Respect the project's icon conventions and the user's visual direction.

## Required output and compliance

Every generated icon must have a standalone editable `.svg` deliverable. React/TypeScript output is an optional wrapper that renders native SVG elements and preserves that geometry. PNG or other raster previews accompany the SVG; they cannot replace it. Build the artwork as vector geometry with native SVG gradients, clips, masks, and filters. Embedded raster artwork, image-generation output, canvas screenshots, and CSS-only drawings do not satisfy this skill.

Follow every applicable requirement in this file and the references reached by the workflow. Defaults below are configurable design parameters; format, construction integrity, and verification are completion requirements. Honor explicit user instructions over skill rules and disclose any resulting deviation. If a project constraint conflicts with a requirement, resolve it before treating the result as complete. Never silently skip a required check or describe an unavailable check as passed.

## Workflow

1. Inspect the destination's icons, tokens, framework, and expected display sizes. Identify the subject and its distinguishing silhouette. When a target image is supplied, read its silhouette, orientation, proportions, and depth relationships before selecting the projection. Reuse an established palette and projection where compatible with that target. When none exists, use the defaults below. Ask only when an unresolved choice materially changes the requested result.
2. Before drawing new geometry, read [geometry](references/geometry.md). For a new visual family, also read [colors and materials](references/colors-and-materials.md) and [lighting and shadows](references/lighting-and-shadows.md). For edits, load these when changing the corresponding property.
3. Read [volume and finish](references/volume-and-finish.md) before drawing or reviewing an illustrated icon. For a set, complete and inspect one representative icon before propagating its construction. Establish the main mass as an unadorned shaded body first. Run the grayscale body study described in the finish reference before adding rims, symbols, screens, or cast shadows. Then add visible parts and identifying details. Read [SVG construction](references/svg-construction.md) before writing SVG. Read [construction examples](references/examples.md), then inspect the closest example source and its render. A geometry blockout is not a finished reference.
4. For React output, read [React and TypeScript](references/react-typescript.md). Deliver the standalone SVG alongside any component. Reuse the project's framework rather than introducing a dependency for an icon.
5. Read [visual validation](references/visual-validation.md), render the actual output, inspect it at intended sizes and backgrounds, and fix observed defects. Run its assembly check on detail placement, clearances, and foreground occlusion as well as its finish gate. Report any unavailable check explicitly. Source inspection alone does not establish visual quality.

## Default family

These are starting values, not overrides for an existing design system.

| Property | Default |
| --- | --- |
| Canvas | `viewBox="0 0 128 128"`, transparent |
| Projection | Equal world-axis scale, screen diagonals at ±30° |
| Light | Upper left of the screen |
| Material | Sculpted matte plastic with broad curvature shading on rounded bodies |
| Edges | Rounded silhouette and shaded bevels, with highlights limited to light-facing edges |
| Framing | About 12 units of padding including effects |
| Complexity | One primary object and only identifying details |
| Palette | One accent material plus neutral or supporting materials |

For this style, visual acceptance also requires the [volume and finish gate](references/volume-and-finish.md#acceptance-gate). A valid SVG or an angled silhouette alone is insufficient.

The family must share projection, light direction, corner treatment, and optical scale. Keep these decisions stable across the requested set. Use a simplified companion at small sizes when detail no longer survives rendering.

## Delivery gate

Before calling an icon complete, account for every applicable check:

1. Save the standalone SVG and run `python3 <skill-directory>/scripts/validate_svg.py <delivered-icon.svg>`. Fix every reported error. For sets, pass all delivered SVG paths. This checks vector structure, not visual correctness.
2. Render the saved file, complete the finish and assembly checks in [visual validation](references/visual-validation.md), and fix observed failures. Inspect a whole set together as well as each icon individually.
3. For React delivery, follow the integration checks in [React and TypeScript](references/react-typescript.md), including multiple instances and host type checks. The component must preserve the validated SVG geometry.
4. Report the SVG path, preview, checks actually performed, and any deviations or unavailable checks. Unavailable required checks leave validation incomplete; identify that status plainly.

## Delivery

Save the required SVG and any requested components in the project, use descriptive names, and show the rendered result. State which size and background checks actually ran. Completion requires valid local references, no embedded raster substitution, and a visual check of the delivered files. Do not claim automatic activation was tested merely because the description is present. Discovery requires installation in the host's skill search path; selection depends on that host and the task context.
