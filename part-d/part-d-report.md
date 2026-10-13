# Part D — Tailwind Theme Configuration

## Objective

Extend the default Tailwind CSS theme with a custom brand colour palette, a custom font family, and an additional spacing value without replacing existing theme values.

## Configuration

The configuration uses `theme.extend` in `tailwind.config.js` to add:

- **Brand colours:** `brand-500` (`#6366f1`) and `brand-700` (`#4338ca`).
- **Custom font:** `font-brand`, configured with the Arial font stack.
- **Custom spacing:** `18`, equivalent to `4.5rem`, which enables utilities such as `p-18` and `mt-18`.

Because this project uses Tailwind CSS v4, the JavaScript configuration is explicitly loaded using the `@config` directive in `input.css`.

## Difference Between `theme` and `theme.extend`

Defining values directly under `theme` replaces the corresponding default theme configuration rather than extending it. For example, defining only custom colours under `theme.colors` can remove the default colour palette.

Using `theme.extend` adds custom values while preserving the existing defaults. This allows custom design tokens and standard Tailwind utilities to work together.

## Verification

The test page successfully displays the custom brand colours, uses the configured font utility and applies the additional spacing. Existing gray colours and default spacing utilities remain available.

## Conclusion

Using `theme.extend` provides a maintainable way to customize a project's design system while retaining Tailwind's built-in utility classes.