---
name: soft-icons
description: >-
  Create, edit, and review custom Soft Isometric 3D icons as editable SVG or React/TypeScript code. Use when a task requests isometric or soft 3D SVG icons, an illustrated icon set, or new custom UI icons where this visual style is requested or already established, including icons needed while building a screen. Preserve existing icon libraries and other visual styles unless the user asks to replace them. Raster image generation and unrelated SVG fixes are outside this skill.
---

# Soft isometric icons

Produce editable vector icons with consistent projection, matte materials, and soft lighting. Use SVG geometry and native effects. Respect the project's icon conventions and the user's visual direction.

## Workflow

1. Inspect the destination's icons, tokens, framework, and expected display sizes. Identify the subject and its distinguishing silhouette. Reuse an established palette and projection. When none exists, use the defaults below. Ask only when an unresolved choice materially changes the requested result.
2. Before drawing new geometry, read [geometry](references/geometry.md). For a new visual family, also read [colors and materials](references/colors-and-materials.md) and [lighting and shadows](references/lighting-and-shadows.md). For edits, load these when changing the corresponding property.
3. Read [volume and finish](references/volume-and-finish.md) before drawing or reviewing an illustrated icon. For a set, complete and inspect one representative icon before propagating its construction. Establish the main mass as an unadorned shaded body first. Run the grayscale body study described in the finish reference before adding rims, symbols, screens, or cast shadows. Then add visible parts and identifying details. Read [SVG construction](references/svg-construction.md) before writing SVG. Use [the shield example](assets/examples/shield.svg) to inspect the separation between body, bevel, and face shading. The [box example](assets/examples/box.svg) demonstrates projection only and is not a finish reference.
4. For React output, read [React and TypeScript](references/react-typescript.md). Keep standalone SVG available when requested. Reuse the project's framework rather than introducing a dependency for an icon.
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

## Delivery

Save the requested SVG/components in the project, use descriptive names, and show the rendered result. State which size and background checks actually ran. Completion requires valid local references, no embedded raster substitution, and a visual check of the delivered files. Do not claim automatic activation was tested merely because the description is present. Discovery requires installation in the host's skill search path; selection depends on that host and the task context.
