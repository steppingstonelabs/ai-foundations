# Contributing Guide

Thank you for helping maintain the AI Basics Workshop site. This document outlines code style, naming conventions, session content requirements, and the pre-commit checklist.

---

## Code Style

### General

- **TypeScript everywhere** — all `.ts` / `.astro` files use TypeScript.
- **No `any`** — avoid implicit `any`; add explicit types or use the Zod-inferred types from the content collection.
- **Consistent formatting** — the project uses default Prettier settings. Run `npx prettier --write .` before committing if you don't have a format-on-save hook.
- **No trailing whitespace**, no mixed tabs/spaces (spaces only, 2-space indent).

### Astro components

- Keep component props typed via the `interface Props` pattern:
  ```astro
  ---
  interface Props {
    title: string;
    variant?: 'info' | 'warning' | 'tip';
  }
  const { title, variant = 'info' } = Astro.props;
  ---
  ```
- Import styles and scripts only where needed — avoid polluting `BaseHead`.
- Prefer semantic HTML elements (`<nav>`, `<main>`, `<article>`, `<section>`) over generic `<div>` soup.

### CSS / Tailwind

- Use **design-token utility classes** (`text-primary`, `bg-surface`, etc.) before reaching for raw colour values.
- Raw hex values in component styles are a code smell — add a token to `tokens.css` instead.
- Keep Tailwind class lists readable by grouping: layout → spacing → typography → colours → states.

---

## Component Naming Conventions

| Category | Pattern | Example |
|----------|---------|---------|
| Layout shell | `PascalCase.astro` in `components/layout/` | `Sidebar.astro` |
| Session content | `PascalCase.astro` in `components/session/` | `KeyConcept.astro` |
| Reusable UI | `PascalCase.astro` in `components/ui/` | `Callout.astro` |
| Page layouts | `PascalCase.astro` in `layouts/` | `SessionLayout.astro` |
| Utility functions | `camelCase.ts` in `lib/` | `sessions.ts` |

Rules:
- One component per file.
- File name matches the exported component name exactly.
- No generic names like `Component.astro` or `Helper.ts`.

---

## Session Frontmatter Requirements

Every file in `src/content/sessions/` **must** include all required fields
(validated by Zod at build time — missing fields cause a build error).

```yaml
---
title: "Human-readable session title"   # required, string
order: 1                                 # required, integer 1–99 (controls sort order)
week: 1                                  # required, integer 1–5 (controls sidebar grouping)
duration: "45 min"                       # required, string (free-form, e.g. "1 hr 30 min")
type: "lecture"                          # required, enum: lecture | workshop | project | retrospective
objectives:                              # required, array of strings (minimum 1)
  - "Understand X"
  - "Be able to do Y"
---
```

### Optional frontmatter fields

```yaml
description: "Short summary for the home-page card"   # optional, string
prereqs:                                               # optional, array of session slugs
  - "01-tokens-context-window"
```

### File naming

`{two-digit-order}-{kebab-case-title}.md`

Examples: `01-tokens-context-window.md`, `17-retrospective.md`

---

## Testing Before Commit

Run these checks **before every commit** (the CI pipeline runs the same steps):

```bash
cd site

# 1. Type-check all Astro + TypeScript files
npm run check

# 2. Production build (catches rendering errors, missing frontmatter, broken imports)
npm run build

# 3. Smoke-test the built site
npm run preview
# Open http://localhost:4321 and verify:
#   ✓ Home page loads with all session cards
#   ✓ Sidebar shows all 5 week groups
#   ✓ Click a session — content renders correctly
#   ✓ Prev / Next navigation works
#   ✓ Mobile menu toggle works (resize browser to < 768 px)
```

### What the CI pipeline checks

| Step | Command | Fails on |
|------|---------|---------|
| Type check | `astro check` | Any TS / Astro type error |
| Build | `astro build` | Rendering errors, bad frontmatter, broken imports |
| Page count | shell `find` | Fewer than 17 session HTML files in `dist/` |

---

## Pull Request Checklist

Before opening a PR, confirm:

- [ ] `npm run check` passes with zero errors
- [ ] `npm run build` completes with zero errors/warnings
- [ ] All 17 session pages render correctly in `npm run preview`
- [ ] New session files follow the frontmatter schema exactly
- [ ] New components are placed in the correct `components/` subdirectory
- [ ] Design tokens are used for colours and spacing (no raw hex values)
- [ ] Semantic HTML is used (no unnecessary `<div>` wrappers)
- [ ] PR description explains *what* changed and *why*

---

## Questions & Issues

Open a GitHub Issue or start a Discussion in the repo. Please include:
- Node.js version (`node --version`)
- npm version (`npm --version`)
- The full error output from `npm run build` or `npm run check`
