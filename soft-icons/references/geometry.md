# Isometric geometry

## Projection

Use world coordinates `x, y, z`, with `z` pointing up. A useful projection into SVG's downward-positive canvas is:

```text
sx = ox + s * 0.8660254 * (x - y)
sy = oy + s * (0.5 * (x + y) - z)
```

`ox, oy` place the object, and `s` is the common scale for all world axes. This is an orthographic isometric projection. Parallel world edges remain parallel on screen. Avoid perspective vanishing points and independent face skewing. Rotate the object in world space only when the family needs that orientation.

For a box spanning `0..w`, `0..d`, `0..h`, project these faces:

- Top: `(0,0,h)`, `(w,0,h)`, `(w,d,h)`, `(0,d,h)`.
- Screen-left side: `(0,0,0)`, `(0,d,0)`, `(0,d,h)`, `(0,0,h)`.
- Screen-right side: `(0,0,0)`, `(w,0,0)`, `(w,0,h)`, `(0,0,h)`.

Draw shadows, rear objects, visible sides, top, then details, adjusting order for actual overlap. Share identical vertices across adjacent faces. Thin light seams often mean adjacent paths do not meet or use different rounding.

## Soft edges

Use a radius around 2–4 canvas units on a medium object. Construct tangency points and quadratic or cubic curves in the path. Match the treatment at shared corners. A `stroke-linejoin` only rounds strokes; it does not round a filled polygon. Avoid blur on the whole object, which erases silhouette and face boundaries.

For circles on a face, draw them in the face's local plane and apply the same projection. A circle on a horizontal plane becomes an ellipse whose vertical-to-horizontal radius ratio is approximately 0.577. Arbitrary world planes need their own projected basis. Cylinder caps and sides must meet at the same ellipse endpoints.

## Composition

Choose a recognizable silhouette before adding detail. Start around 88–104 units wide, then fit height and shadow inside the canvas. Center the visible mass optically, including protrusions. Objects of equal bounding-box size may need different scale to look balanced.

At 24–32 px, simplify labels, grooves, and tiny secondary objects. When a defining feature would be less than one rendered pixel, enlarge it or omit it. Keep the original geometry for larger illustrated use.
