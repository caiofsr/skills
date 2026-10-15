# Construction examples

Before drawing, open the SVG source and render of the example closest to the requested construction. Inspect where its faces meet and how its details attach. Adapt its construction principle, not its complete silhouette or palette.

| Example | Study | Limits |
| --- | --- | --- |
| [House](../assets/examples/house.svg) | Multiple planes, roof overhang, door and window on their supporting walls, roof painted after wall details | Architectural planes are intentionally flat; they are not a reference for curved organic bodies |
| [Parcel](../assets/examples/parcel.svg) | Rounded box, projected packing band crossing top and side, label attached to the front | Planar faces need less curvature than a padded body |
| [Cloud](../assets/examples/cloud.svg) | Continuous curved silhouette and broad body shading without a bright perimeter | Organic form, not a template for planar housings |
| [Shield](../assets/examples/shield.svg) | Broad near-frontal face, rounded bevel, visible right-side thickness, and raised check with local contact shadow | Follow this silhouette for shields; do not squeeze it into a narrow diagonal plate |
| [Box](../assets/examples/box.svg) | Shared projected vertices and face order | Geometry blockout only; insufficient finish for delivery |

The house is the established style reference from this skill's development. The other examples demonstrate particular constructions; still apply all delivery checks to the generated output. An example does not override an instruction or waive visual validation.

Validate sources with `python3 scripts/validate_svg.py assets/examples/*.svg` from the skill directory. To render without project tooling, use an available SVG renderer. PNG exports are inspection previews; the SVG remains the required source and deliverable.
