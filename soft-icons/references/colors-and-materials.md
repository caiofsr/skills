# Colors and materials

## Establish a material palette

Use project tokens when available. Otherwise this blue family is a starting point:

| Role | Example |
| --- | --- |
| Top light | `#B8D9FF` |
| Top base | `#8DBBFA` |
| Left face | `#78A7EA` |
| Right face | `#527BC5` |
| Neutral light | `#EDF2F8` |
| Neutral shade | `#BECBDD` |
| Shadow | `#263653`, low opacity |

These values are material roles, not semantic status colors. Keep errors, success, and warnings aligned with the application. Use shape or labels as well as color when an icon communicates state.

## Matte appearance

Use two stops per face by default, with a third only when it improves curvature. Keep hue shifts restrained and the top lighter than the sides under the default light. A lighter screen-left face and darker screen-right face communicate the light direction.

Use broad shading with enough lightness separation to reveal the intended curvature at delivery size. Low contrast is a starting point, not a reason to accept a visually flat face. Small white specular dots suggest glossy material. Metallic reflections, glass transparency, and heavy texture belong only to a user-requested material variation. Preserve the family's geometry and light when changing material.

For multiple materials, assign each its own base/light/shade roles. Keep neighboring faces distinguishable at delivery size. Avoid using opacity on the whole icon to create a pale palette because overlapping shapes and backgrounds then change its appearance.

## Backgrounds and themes

Test on white and the actual application background. Check a dark background when the destination supports dark mode. Prefer explicit theme palette roles or CSS variables with fallbacks to whole-icon inversion. A standalone SVG loaded with `<img>` does not inherit the page's CSS variables or `currentColor`; inline SVG can.

Do not force an illustration to satisfy text contrast ratios. If the icon alone conveys a functional control or state, evaluate its contrast in the actual UI and provide an accessible name through the component or control.
