# Part A — Plain CSS vs Tailwind CSS: Pricing Table Comparison

## Measurements and Results

| Measurement | Plain CSS | Tailwind CSS |
|---|---:|---:|
| Handwritten CSS lines | 208 | 2 lines of input directives |
| Original CSS size | 3,728 bytes | Not directly comparable |
| Minified CSS size | 2,718 bytes | 11,978 bytes |
| Reported build time | No separate build step | 72 ms |
| Time to change brand colour to purple and add the middle-tier badge | 43.42 seconds | 1 minute 28.73 seconds |

**Note on handwritten CSS:** The Tailwind count refers only to the two lines in `tailwind/input.css`. It does not count utility classes written in HTML or any custom theme CSS added later.
