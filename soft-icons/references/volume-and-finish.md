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

## Model the main mass before the trim

Start with the largest continuous surface and identify its curved cross-section. A domed shield has a broad convex center that rolls into its perimeter; a book page block arches toward the spine; a key bow has a rounded section around its hole. Sketch the light-facing region, midtone, turning region, and occlusion before adding a border or emblem.

The turning region is where the surface bends away from the light. Give it visible area inside the silhouette. If all darkening fits in a narrow rim, the result still reads as a flat inset panel. For an organic or padded body, a useful first study lets the light-to-shadow transition span roughly a quarter of the visible face. Adjust it to the actual cross-section rather than applying that proportion to every object.

Build one shaded body with no symbol, screen content, outline, or ground shadow. Inspect it in grayscale at 64 and 128 px. Its shape should remain readable from the distribution of light, not just an offset side face. If it reads as a flat cutout, change the shape and the shading together before adding detail.

Keep truly planar surfaces planar. On devices, concentrate curvature on the housing, corners, hinge, and stand. A screen can stay flat; a dark gradient inside a screen does not demonstrate a rounded housing. Avoid using a large inset screen as the only example when establishing the family's volume.

## Shape the edges

Draw the silhouette's corner curves explicitly. Build a narrow bevel region between the outer body and inset face, with highlights toward the upper-left light and darker transitions away from it. Scale that region with the object. At 128 units, start around 2–5 units for a medium body, then judge the render.

A pale line of uniform width around the whole object reads as an outline. Replace it with a shaped transition that varies with light direction. Keep the light-facing edge brightest, soften the transition into the front, and reduce or omit highlights on shadow-facing edges. Avoid tracing every seam with white.

## Shade surfaces locally

Use broad front-face or curved-surface shading in addition to separate side colors. A radial gradient with a broad off-center light region and a substantial darker turning region can model a domed shield; a directional gradient can describe a rounded cover or rim. Clip highlights to their surface. Darken actual recesses and contact joins rather than all edges equally.

A gradient earns its place only when the rendered surface reads as rounded or recessed. Merely assigning gradients with nearly identical stops does not establish volume. Increase the useful lightness separation or change the highlight's extent if the result still reads as a flat polygon. Keep broad matte highlights rather than hard white reflections.

Use material roles, not a universal two-color fill rule. A screen, a page block, and a plastic housing can share the family palette while having different local contrast and surface treatment.

## Diagnose the second flatness failure

A bevel and a gradient can still produce a flat result. The characteristic failure is a large uniformly lit panel, a bright perimeter, and a darker offset slab. More trim, a deeper extrusion, and a stronger ground shadow preserve that construction.

Correct the main face first: broaden its curved transition, reshape the perimeter where the material turns, and place local occlusion only where parts meet. Avoid a bright concentric inner border that visually separates the front into another flat plate. Use overlapping clipped gradients when one gradient cannot describe the surface, but keep each layer tied to a specific change in curvature or contact.

Compare the unadorned body with the complete icon. If its apparent volume appears only after the trim, symbol, or cast shadow is restored, return to the body study. A set of seven icons should not reproduce the same slab construction seven times.

## Acceptance gate

Inspect the actual render at the intended size and at 128 px. Revise before delivery when any of these conditions holds:

- The main body reads as a flat symbol with a narrow offset copy behind it. Rebuild its rim, curvature, recess, or joints according to the subject.
- A uniform pale outline supplies most of the apparent depth. Replace it with directional bevel shading.
- The unadorned main body reads as a flat panel in the grayscale study. Rebuild its cross-section and broad turning region before adding details.
- Front surfaces remain visually uniform despite intended rounded material. Adjust local shading until the curvature is visible without blurring the silhouette.
- The shadow is the only cue separating the object from a flat illustration. Temporarily hide the ground shadow and inspect the body alone.
- A set mixes incompatible viewing directions, thickness conventions, or apparent object scales. Compare a contact sheet before completing the set.
- Details merge at the intended size. Simplify the model while retaining its silhouette and useful depth cues.

After each revision, rerender and recheck the failed condition. If the available renderer or target size prevents a convincing result, report the limitation and show the remaining issue. Do not describe an uninspected result as passing this gate.

The shield example demonstrates curved-face shading and a bevel. It is one editable construction, not a universal template or a guarantee of quality for other subjects. Use the user's reference and target size to judge each output.
