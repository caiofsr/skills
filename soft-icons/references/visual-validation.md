# Visual validation

## Render and inspect

Use an available browser or vector renderer. No specific renderer is required. Make a temporary contact sheet from the delivered assets, not a separate recreation. Keep temporary previews out of source control unless requested as deliverables.

Show each icon at its intended size plus 32, 64, and 128 px for illustrated use. If intended for 16–24 px, inspect those sizes and create a simpler variant when the subject loses recognition. Include a white background, a neutral gray background to reveal halos, and the application's background. Add the actual dark theme when relevant.

Inspect these properties at normal display scale:

| Check | Pass condition | Typical correction |
| --- | --- | --- |
| Recognition | Subject readable without its filename | Simplify silhouette or enlarge identifying feature |
| Projection | Shared edges align; parallel edges stay parallel | Recompute projected vertices |
| Lighting | Top and sides agree on the light | Adjust face roles and gradient direction |
| Material | Soft shading preserves clear face boundaries | Reduce highlight contrast or remove blur on faces |
| Shadow | Contact and direction match object placement | Move footprint and expand effect bounds |
| Framing | Geometry and effects remain inside canvas | Reposition or scale the complete composition |
| Small sizes | Details remain legible without muddy clusters | Remove details or make a dedicated small variant |
| Family | Similar apparent mass, depth, and edge softness | Compare adjacent icons and adjust optical scale |

Zoom in to investigate seams and clipping, then return to intended size before deciding. Judge a set together, not only one icon at a time.

## Finish gate

For a new family or a reported flatness problem, render the unadorned main body in grayscale at 64 and 128 px. Hide the ground shadow, trim, and emblem so the study tests surface shape. Keep this study in the temporary preview, not in the delivered icon.

Apply every condition in the [volume and finish acceptance gate](volume-and-finish.md#acceptance-gate) to each delivered icon. Inspect the body with its ground shadow hidden when depth is uncertain. Include one representative icon in the preview before building the rest of a new family. Fix a failed finish check in the geometry or shading, then rerender; adding a larger shadow does not repair flat construction.

## Code and integration

Parse each SVG and check all local references. Open the actual output after any optimizer or conversion. For React, render multiple instances, verify the accessible name or decorative state, and use the project's existing type/build checks. Confirm custom CSS does not override fills or aspect ratio unexpectedly.

## Completion report

Name the files delivered and the sizes/backgrounds actually inspected. Show a preview when the host supports it. Record unavailable rendering or integration checks as limitations; never substitute a source-only check for a claimed visual pass.

## Skill selection scenarios

Evaluate the description against realistic tasks when changing its scope:

- "Create a soft isometric cloud upload icon in SVG" should select this skill.
- "Add a custom illustrated icon to this screen using the existing soft isometric family" should select it without an explicit skill name.
- "Make our isometric SVG icon a reusable TypeScript component" should select it.
- "Use the existing Lucide search icon" should preserve that library.
- "Fix the dimensions of this flat logo SVG" should preserve its style.
- "Generate a photorealistic 3D PNG" belongs to raster generation.

These are routing expectations. Actual automatic selection needs a fresh host session with the skill installed and visible in its catalog. Manual invocation validates execution, not implicit selection.
