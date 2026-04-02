# AI Basics Workshop — Content Site

A fast, fully-static content site that delivers 17 sessions of the **AI Basics** workshop curriculum — a five-week program teaching developers how to work effectively with large language models. The site is built with Astro 5, Tailwind CSS v4, and MDX, and deploys to Netlify in seconds.

---

## Who is this for?

| Role | How you use this repo |
|------|-----------------------|
| **Workshop facilitator** | Run the site locally during class; share the Netlify URL with participants |
| **Content author** | Add or edit Markdown sessions in `src/content/sessions/` |
| **Developer / maintainer** | Extend components, adjust design tokens, or add new pages |

---

## Quick Start

> **Requirements:** Node.js 20 LTS · npm 10 · Git

```bash
# 1. Clone the repository
git clone https://github.com/your-org/ai-basics.git

# 2. Enter the site directory
cd ai-basics/site

# 3. Copy the environment variable template
cp .env.example .env

# 4. Install dependencies
npm install

# 5. Start the development server
npm run dev
```

Open **http://localhost:4321** — the full site is live with hot-module replacement.

---

## Common Tasks

```bash
# Development server (HMR enabled)
npm run dev

# Full production build → site/dist/
npm run build

# Preview the production build locally
npm run preview

# Type-check all Astro + TypeScript files
npm run check

# Full CI pass (type-check + build)
npm test
```

---

## Project Structure

```
site/
├── astro.config.mjs         # Astro + Vite + MDX config
├── tailwind.config.mjs      # Tailwind CSS v4 config
├── tsconfig.json            # TypeScript config
├── netlify.toml             # Netlify build settings + security headers
├── .env.example             # Environment variable template
│
├── public/                  # Static assets (fonts, favicon)
│
└── src/
    ├── components/
    │   ├── layout/          # Sidebar, BaseHead, MobileMenuToggle
    │   ├── session/         # SessionHeader, KeyConcept, Takeaway, …
    │   └── ui/              # Badge, Callout, CodeBlock, ProgressBar
    ├── content/
    │   ├── config.ts        # Zod schema for session frontmatter
    │   └── sessions/        # 01-*.md … 17-*.md — one file per session
    ├── layouts/
    │   ├── BaseLayout.astro
    │   ├── SessionLayout.astro
    │   └── RetroLayout.astro
    ├── lib/
    │   ├── constants.ts     # Week themes / labels
    │   └── sessions.ts      # getAllSessions(), getAdjacentSessions()
    ├── pages/
    │   ├── index.astro      # Home page — curriculum grid
    │   └── sessions/[slug].astro  # Dynamic session route
    └── styles/
        ├── tokens.css       # CSS custom properties (design system)
        └── global.css       # Base reset + Tailwind imports
```

→ Full directory breakdown: [`SITE_STRUCTURE.md`](SITE_STRUCTURE.md)

---

## Key Features

| Feature | Details |
|---------|---------|
| **Static-first** | Every route pre-rendered at build time; zero server-side code |
| **MDX components** | `<KeyConcept>`, `<Callout>`, `<CodeBlock>`, `<TeachingMoment>`, `<Takeaway>` usable inside Markdown |
| **Dark sidebar** | Fixed left navigation grouped by week; collapses on mobile |
| **Design tokens** | All colours, spacing, and typography defined in `tokens.css` — one file to re-brand |
| **Responsive** | Full-width on mobile (hamburger menu), sidebar layout on desktop |
| **Type-safe content** | Zod schema validates all session frontmatter at build time |
| **Prev / Next navigation** | Auto-generated from session `order` field |
| **Self-hosted fonts** | Inter (body) and JetBrains Mono (code) — no Google Fonts request |
| **Security headers** | `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy` via `netlify.toml` |

---

## Curriculum Overview

The site covers 17 sessions across five weeks:

| Week | Theme | Sessions |
|------|-------|---------|
| 1 | **Foundations** — How LLMs Actually Work | 1–3 |
| 2 | **Evaluation & Guidance** — Tell the Model What It Can and Cannot Do | 4–6 |
| 3 | **Thinking in Agents** — Making Behavior Persistent | 7–10 |
| 4 | **Harness Engineering** — Constraining the Agent Makes It Perform Better | 11–14 |
| 5 | **Spec-Driven Development** — The Capstone Skill | 15–17 |

---

## Development Workflow

### Adding a new session

1. Create `src/content/sessions/18-your-topic.md` with required frontmatter:
   ```yaml
   ---
   title: "Your Topic"
   order: 18
   week: 5
   duration: "45 min"
   type: "lecture"     # lecture | workshop | project | retrospective
   objectives:
     - "Understand X"
   ---
   ```
2. Write the session body — MDX components are available automatically.
3. Run `npm run dev` and visit `/sessions/18-your-topic`.

### Changing the visual design

All design values live in [`src/styles/tokens.css`](src/styles/tokens.css).
To change the primary accent colour everywhere: edit `--color-primary`.
Tailwind utility classes (`text-primary`, `bg-surface`, etc.) update automatically.

### Adding an MDX component

1. Create the component in `src/components/session/` or `src/components/ui/`.
2. Import and register it in [`src/pages/sessions/[slug].astro`](src/pages/sessions/%5Bslug%5D.astro).
3. Use `<YourComponent />` in any session `.md` file.

---

## Deployment

Full deployment instructions — local preview, Netlify (automatic + CLI), environment variables, and troubleshooting — are in [`DEPLOYMENT.md`](DEPLOYMENT.md).

**TL;DR — deploy to Netlify:**

```bash
# Push to main; Netlify auto-deploys via netlify.toml
git push origin main

# — or manually —
npm run build
netlify deploy --dir dist --prod
```

---

## Contributing

Code style, naming conventions, frontmatter requirements, and the pre-commit checklist are documented in [`CONTRIBUTING.md`](CONTRIBUTING.md).

**Quick pre-commit check:**

```bash
cd site
npm run check   # type-check
npm run build   # production build
```

Both steps must pass before opening a pull request.

---

## Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| Framework | [Astro](https://astro.build) | 5.x |
| MDX | [@astrojs/mdx](https://docs.astro.build/en/guides/mdx/) | 4.x |
| CSS framework | [Tailwind CSS](https://tailwindcss.com) | 4.x |
| Language | TypeScript | 5.x |
| Content validation | [Zod](https://zod.dev) (via Astro content collections) | bundled |
| Fonts | Inter Variable · JetBrains Mono Variable | self-hosted |
| Hosting | [Netlify](https://netlify.com) | — |
| CI/CD | GitHub Actions | — |

---

## Documentation Index

| Document | Purpose |
|----------|---------|
| [`README.md`](README.md) | ← you are here |
| [`SITE_STRUCTURE.md`](SITE_STRUCTURE.md) | Component hierarchy, conventions, how-to guides |
| [`DEPLOYMENT.md`](DEPLOYMENT.md) | Local setup, production builds, Netlify deploy |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Code style, naming conventions, PR checklist |
