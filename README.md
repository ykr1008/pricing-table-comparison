# Pricing Table: Plain CSS vs Tailwind CSS

A hands-on comparison of building the same responsive pricing table using plain CSS and Tailwind CSS.

## Project Overview

This project compares two approaches to styling a pricing table with three tiers: Starter, Pro, and Business.

Both versions will include:
- Responsive layouts
- A highlighted middle pricing tier with a badge
- Hover effects
- Dark mode
- Custom brand colours and typography

## Project Structure

```text
pricing-table-comparison/
├── plain-css/
│   ├── index.html
│   └── style.css
├── tailwind/
│   ├── index.html
│   └── input.css
├── .gitignore
└── README.md
```

## Assignment Tasks

### Part A — Build It Twice
Build the pricing table using plain CSS and Tailwind CSS. Compare handwritten CSS lines, final minified CSS bundle size, build time, and the time needed to change the brand colour and add a badge.

### Part B — Dynamic Class Bug
Demonstrate a dynamically generated Tailwind class that is missing from the production build, explain why it happens, and implement two fixes.

### Part C — Refactor for Reuse
Compare reusable template/component markup with Tailwind's `@apply` directive.

### Part D — Theme Configuration
Extend the Tailwind theme with a brand colour palette, a custom font, and an additional spacing value.

### Part E — Written Evaluation
Evaluate the strongest arguments for and against Tailwind CSS and decide which approach suits a five-person team building a product over two years.

## Technologies

- HTML5
- CSS3
- Tailwind CSS
- Node.js and npm for the Tailwind build process

React is not required for this project.

## Measurements

Results will be recorded after both implementations are completed and tested.