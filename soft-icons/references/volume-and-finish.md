# Volume and finish

## Target

Create small matte objects whose curvature and construction remain visible at the intended size. Projection establishes orientation; shaped edges and local shading establish softness. Treat a flat symbol extruded sideways as a blockout, not a finished illustrated icon.

Read the supplied reference image as evidence of the user's desired or rejected appearance. A verbal label such as "3D" is less specific than that reference. Keep geometry editable in SVG.

## Construct the object

Identify the body's thickness, the visible side, the rounded transition into the front, and any recessed or raised parts before writing paths. Let these parts follow the same projection.

Use subject-specific volume:

| Subject | Useful construction |
| --- | --- |
| Shield | Rounded perimeter, broad curved face, recessed or raised emblem |
| Key | Rounded bow and shaft, a real hole with an inner wall, distinct teeth |
| Book | Separate covers and page block, a curved spine, pages that follow the fold |
| Laptop | Separate lid, inset display, hinge and base; believable thickness for each |
| Monitor | Recessed display, rounded frame, stem and foot with coherent joins |
| Phone | Rounded body, inset display and a consistent rim |

These are construction options, not mandatory ornament. Preserve physically thin subjects. A phone gains volume from its rim and recess, not by inflating it into a toy block.

## Shape the edges

Draw the silhouette's corner curves explicitly. Build a narrow bevel region between the outer body and inset face, with highlights toward the upper-left light and darker transitions away from it. Scale that region with the object. At 128 units, start around 2–5 units for a medium body, then judge the render.

A pale line of uniform width around the whole object reads as an outline. Replace it with a shaped transition that varies with light direction. Keep the light-facing edge brightest, soften the transition into the front, and reduce or omit highlights on shadow-facing edges. Avoid tracing every seam with white.

## Shade surfaces locally

Use broad front-face or curved-surface shading in addition to separate side colors. A restrained radial gradient can model a gently domed shield; a directional gradient can describe a rounded cover or rim. Clip highlights to their surface. Darken actual recesses and contact joins rather than all edges equally.

A gradient earns its place only when the rendered surface reads as rounded or recessed. Merely assigning gradients with nearly identical stops does not establish volume. Increase the useful lightness separation or change the highlight's extent if the result still reads as a flat polygon. Keep broad matte highlights rather than hard white reflections.

Use material roles, not a universal two-color fill rule. A screen, a page block, and a plastic housing can share the family palette while having different local contrast and surface treatment.

## Acceptance gate

Inspect the actual render at the intended size and at 128 px. Revise before delivery when any of these conditions holds:

- The main body reads as a flat symbol with a narrow offset copy behind it. Rebuild its rim, curvature, recess, or joints according to the subject.
- A uniform pale outline supplies most of the apparent depth. Replace it with directional bevel shading.
- Front surfaces remain visually uniform despite intended rounded material. Adjust local shading until the curvature is visible without blurring the silhouette.
- The shadow is the only cue separating the object from a flat illustration. Temporarily hide the ground shadow and inspect the body alone.
- A set mixes incompatible viewing directions, thickness conventions, or apparent object scales. Compare a contact sheet before completing the set.
- Details merge at the intended size. Simplify the model while retaining its silhouette and useful depth cues.

After each revision, rerender and recheck the failed condition. If the available renderer or target size prevents a convincing result, report the limitation and show the remaining issue. Do not describe an uninspected result as passing this gate.

The shield example demonstrates curved-face shading and a bevel. It is one editable construction, not a universal template or a guarantee of quality for other subjects. Use the user's reference and target size to judge each output.
