# React and TypeScript

Deliver a standalone `.svg` alongside the component. Render native SVG elements in React; preserve the same paths, viewBox, and effects in both outputs. Use the project's React and TypeScript conventions. The following wrapper illustrates instance IDs and accessibility. Copy the geometry and definitions of the actual icon into it; the body comment is an insertion point, not a completed icon.

```tsx
import { useId, type SVGProps } from "react";

type IconProps = Omit<
  SVGProps<SVGSVGElement>,
  "children" | "dangerouslySetInnerHTML" | "role" | "aria-hidden" |
  "aria-label" | "aria-labelledby" | "viewBox" | "title"
> & {
  title?: string;
};

export function BoxIcon({ title, width = 48, height = 48, ...props }: IconProps) {
  const prefix = `box-${useId()}`;
  const titleId = `${prefix}-title`;
  const topId = `${prefix}-top`;
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 128 128"
      width={width}
      height={height}
      focusable="false"
      role={title ? "img" : undefined}
      aria-hidden={title ? undefined : true}
      aria-labelledby={title ? titleId : undefined}
    >
      {title ? <title id={titleId}>{title}</title> : null}
      <defs>
        <linearGradient id={topId} x1="35" y1="30" x2="90" y2="65"
          gradientUnits="userSpaceOnUse">
          <stop stopColor="#B8D9FF" />
          <stop offset="1" stopColor="#8DBBFA" />
        </linearGradient>
      </defs>
      {/* Insert the complete geometry; reference topId with fill={`url(#${topId})`}. */}
    </svg>
  );
}
```

Convert SVG attributes to JSX names, including `className`, `stopColor`, `strokeWidth`, `clipPath`, and `colorInterpolationFilters`. Rewrite every ID and reference together, including filter, clip, mask, gradient inheritance, and title IDs. React IDs may contain colons; fragment references accept them. Use attribute lookup or escape IDs when querying with CSS selectors.

`useId` keeps instances distinct and supports matching server/client trees. Multiple React roots need distinct `identifierPrefix` configuration when they share a document. Use the project's existing setup. Avoid random values, timestamps, or module counters for SSR IDs. Hooks require a compatible React component context; respect framework server/client boundaries rather than adding a client boundary to the entire page.

Without `title`, the component is decorative. For an icon-only button, label the button and keep the icon decorative. With `title`, it is informative. Use the user's language for that title. If the project exposes another accessibility API, preserve it with equivalent behavior.

Render at least two instances together to check gradient/filter isolation. Run the host's type check and inspect SSR/hydration when that path exists. Do not claim React validation for a standalone SVG-only delivery.
