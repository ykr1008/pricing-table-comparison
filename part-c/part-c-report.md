# Part C — Refactoring for Reuse

## 1. Jinja Partial vs. Tailwind `@apply`

**Jinja Partial:** The Jinja partial approach extracts the repeated pricing card HTML into `_pricing-card.html`. The main template uses `{% include "_pricing-card.html" %}` inside a loop to render the Starter, Pro, and Business plans using shared data. This reduces duplicated markup and makes the structure easier to maintain. If the card layout needs to change, I can update the partial once, and the change applies to all three plans.

**Tailwind `@apply`:** The `@apply` approach extracts repeated utility styles into reusable CSS classes such as `.pricing-card`, `.pricing-price`, and `.pricing-button`. This reduces repeated utility-class lists in the HTML and keeps common styling in one place. However, the HTML structure is still repeated unless a separate component or template partial is also used.

## 2. Comparison

Jinja partials improve reuse at the template and markup level, while `@apply` improves reuse at the styling level. They solve different problems and can also be combined.

## 3. Recommendation

I would ship the Jinja partial approach as the primary solution because it removes duplicated markup, separates presentation structure from page data, and makes future changes easier. I would use `@apply` selectively when a repeated group of styles genuinely benefits from a named CSS class. For this pricing page, the Jinja partial provides the more complete solution to markup duplication.