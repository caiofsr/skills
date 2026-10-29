# Colors and materials

## Establish a material palette

Choose colors from the depicted object and its materials. An explicit user request for a palette, monochrome treatment, brand colors, or tonal range takes precedence. Apply that request within its stated scope. A reference supplied as the desired appearance also guides the object's colors.

Without that direction, use familiar real-world colors. Cardboard is kraft brown, wood uses its natural brown tones, leaves are green, and paper is white or cream. For subjects with many plausible colors, choose a recognizable real-world variant. For abstract subjects, use familiar semantic colors or a restrained palette suited to the concept.

Assign each material its own base, light, and shade colors. Derive highlights and shadows from that base so the material keeps its recognizable hue. Use neutral gray where the actual material calls for it, such as steel; keep warm materials warm under the default lighting. A set shares geometry, lighting, and finish while retaining each subject's colors.

Project tokens may implement these choices when they match the material. Adopting a site's brand palette for the whole illustration requires the user's explicit direction. Construction examples demonstrate geometry and shading; their colors are not defaults for unrelated objects.

Keep errors, success, and warnings aligned with the application when an icon communicates state. Use shape or labels as well as color.

## Matte appearance

Choose stops from the surface cross-section. A planar face may need two; a rounded body often needs a broad light region, midtone, and darker turning region. Inspect their visible distribution rather than limiting every face to the same recipe. Keep hue shifts restrained and the top lighter than the sides under the default light. A lighter screen-left face and darker screen-right face communicate the light direction.

Use broad shading with enough lightness separation to reveal the intended curvature at delivery size. Low contrast is a starting point, not a reason to accept a visually flat face. Small white specular dots suggest glossy material. Metallic reflections, glass transparency, and heavy texture belong only to a user-requested material variation. Preserve the family's geometry and light when changing material.

For multiple materials, assign each its own base/light/shade roles. Keep neighboring faces distinguishable at delivery size. Avoid using opacity on the whole icon to create a pale palette because overlapping shapes and backgrounds then change its appearance.

## Backgrounds and themes

Test on white and the actual application background. Check a dark background when the destination supports dark mode. Prefer explicit theme palette roles or CSS variables with fallbacks to whole-icon inversion. A standalone SVG loaded with `<img>` does not inherit the page's CSS variables or `currentColor`; inline SVG can.

Do not force an illustration to satisfy text contrast ratios. If the icon alone conveys a functional control or state, evaluate its contrast in the actual UI and provide an accessible name through the component or control.
