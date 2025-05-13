# 🎨 HTML & CSS Mastery

> *"Where structure meets style - documenting my frontend fundamentals journey."*

## 🧩 HTML: The Web's Skeleton
```html
<!-- Semantic HTML5 example -->
<section aria-labelledby="projects-heading">
  <h2 id="projects-heading">My Projects</h2>
  <article class="card">
    <h3>Accessible Form</h3>
    <p>Built with proper ARIA labels</p>
  </article>
</section>

# Key Concepts
    Semantic markup (<header>, <main>, <footer>)

    Accessibility fundamentals (alt text, ARIA)

    Form validation patterns

## 🎨 CSS: The Visual Language
/* Modern CSS example */
.card {
  --primary-color: #3a86ff;
  display: grid;
  gap: 1rem;
  padding: clamp(1rem, 2vw, 2rem);
  box-shadow: 0 0.25rem 1rem hsl(0 0% 0% / 0.1);
}

.card:hover {
  transform: translateY(-0.5rem);
  transition: transform 200ms ease;
}

# Core Skills
    Layout systems (Flexbox/Grid)

    Responsive units (rem, vw, clamp())

    CSS variables (--primary-color)

    Pseudo-classes (:hover, :focus)
