# Workshop Site — Orchestration Overview

This document provides a high-level summary of **what was built**, **why each decision was made**, and **how to navigate the codebase** for anyone taking over development or deployment of the AI Basics Workshop content site.

---

## What Was Built

A **fully-static, content-driven website** that serves as the curriculum hub for the *AI Basics* workshop — a five-week, $899/person program teaching developers how to work effectively with large language models.

### At a glance

| Attribute | Value |
|-----------|-------|
| Total sessions | 17 |
| Weeks covered | 5 |
| Pages generated | 18 (home + 17 session pages) |
| Framework | Astro 5 (static output) |
| Styling | Tailwind CSS v4 + CSS custom properties |
| Content format | Markdown with MDX component support |
| Hosting target | Netlify (zero-config via `netlify.toml`) |
| Build time | ~3–5 seconds |
| Runtime JS | Minimal (sidebar mobile toggle only) |

---

## Architecture Decisions & Rationale

### 1. Astro (static output mode)

**Decision:** Use Astro with full static pre-rendering rather than a Next.js / Remix SSR approach.

**Rationale:**
- Workshop content changes infrequently; there is no need for server-side rendering.
- Static HTML is faster, cheaper to host, and has no cold-start latency.
- Astro's content collections give us type-safe frontmatter validation (via Zod) without a CMS.
- Astro's island architecture means we can add interactive components later without rewriting the stack.

### 2. Tailwind CSS v4 + Design Tokens

**Decision:** Use Tailwind v4 utility classes built on top of CSS custom properties defined in `tokens.css`.

**Rationale:**
- Design tokens (`--color-primary`, `--color-surface`, etc.) allow a complete visual rebrand by editing one file.
- Tailwind utility classes keep per-component CSS minimal and co-located with markup.
- v4's Vite-native plugin avoids the PostCSS configuration overhead of v3.

### 3. MDX Components for Rich Content

**Decision:** Register a set of purpose-built MDX components (`KeyConcept`, `Callout`, `CodeBlock`, `TeachingMoment`, `Takeaway`) that content authors can drop into Markdown.

**Rationale:**
- Content authors write in plain Markdown but need occasional rich formatting (callout boxes, highlighted concepts, code blocks with labels).
- MDX provides this without forcing authors into raw HTML or a visual editor.
- Components enforce consistent visual treatment across all 17 sessions.

### 4. Dark Sidebar Navigation

**Decision:** Fixed-position dark sidebar on desktop; hamburger-triggered overlay on mobile.

**Rationale:**
- Workshop participants navigate non-linearly (jumping between sessions for reference).
- A persistent sidebar makes the full curriculum visible at all times on desktop.
- Sessions are grouped by week, matching the physical workshop schedule.
- The dark sidebar contrasts with the light content area, creating clear visual hierarchy.

### 5. Zod-Validated Content Collections

**Decision:** Use Astro's content collections with a strict Zod schema for all session frontmatter.

**Rationale:**
- Missing or malformed frontmatter causes a build-time error, not a runtime surprise.
- The schema doubles as documentation — authors can see exactly which fields are required.
- TypeScript types for session data are inferred automatically from the Zod schema.

### 6. Self-Hosted Fonts

**Decision:** Bundle Inter Variable and JetBrains Mono Variable in `public/fonts/` rather than loading from Google Fonts.

**Rationale:**
- Eliminates an external network request during initial page load.
- No GDPR concerns about third-party font service requests.
- Variable fonts mean a single file covers all font weights.

---

## Five-Week Curriculum Structure

```
Week 1 — Foundations: How LLMs Actually Work
  Session 01 · Tokens & the Context Window
  Session 02 · Prompt Engineering
  Session 03 · Modes & System Prompts

Week 2 — Evaluation & Guidance: Tell the Model What It Can/Cannot Do
  Session 04 · Model Selection & Assignment
  Session 05 · Output Evaluation
  Session 06 · Basic Rules

Week 3 — Thinking in Agents: Making Behavior Persistent
  Session 07 · Scoped Rules
  Session 08 · Skills
  Session 09 · Agents (Claude)
  Session 10 · Tool Use & MCP

Week 4 — Harness Engineering: Constraining the Agent Makes It Perform Better
  Session 11 · The Paradigm Shift
  Session 12 · Context Engineering
  Session 13 · Architectural Constraints
  Session 14 · Garbage Collection & Audit

Week 5 — Spec-Driven Development: The Capstone Skill
  Session 15 · Writing Specs
  Session 16 · Project Demo
  Session 17 · Retrospective
```

---

## File Structure at a Glance

```
ai-basics/                          ← repository root
├── README.md                       ← (empty / placeholder)
├── WORKSHOP_SITE_OVERVIEW.md       ← this document
├── SUMMARY.md                      ← project summary / build log
├── plans/
│   └── site-architecture.md        ← original architecture plan
└── site/                           ← Astro project root
    ├── README.md                   ← site-specific quick-start ★
    ├── SITE_STRUCTURE.md           ← component hierarchy + how-to guides ★
    ├── DEPLOYMENT.md               ← local dev, build, Netlify deploy ★
    ├── CONTRIBUTING.md             ← code style, naming, PR checklist ★
    ├── astro.config.mjs
    ├── tailwind.config.mjs
    ├── tsconfig.json
    ├── netlify.toml
    ├── package.json
    ├── .env.example
    │
    ├── public/
    │   ├── favicon.svg
    │   └── fonts/
    │       ├── Inter-Variable.woff2
    │       └── JetBrainsMono-Variable.woff2
    │
    └── src/
        ├── components/
        │   ├── layout/             ← site chrome
        │   │   ├── BaseHead.astro
        │   │   ├── Sidebar.astro
        │   │   ├── SidebarWeekGroup.astro
        │   │   ├── SidebarLink.astro
        │   │   └── MobileMenuToggle.astro
        │   ├── session/            ← per-session MDX components
        │   │   ├── SessionHeader.astro
        │   │   ├── ObjectivesList.astro
        │   │   ├── KeyConcept.astro
        │   │   ├── Takeaway.astro
        │   │   └── TeachingMoment.astro
        │   └── ui/                 ← generic reusable primitives
        │       ├── Badge.astro
        │       ├── Callout.astro
        │       ├── CodeBlock.astro
        │       └── ProgressBar.astro
        ├── content/
        │   ├── config.ts           ← Zod schema
        │   └── sessions/           ← 01-*.md … 17-*.md
        ├── layouts/
        │   ├── BaseLayout.astro
        │   ├── SessionLayout.astro
        │   └── RetroLayout.astro
        ├── lib/
        │   ├── constants.ts        ← WEEKS array
        │   └── sessions.ts         ← getAllSessions(), getAdjacentSessions()
        ├── pages/
        │   ├── index.astro         ← home page
        │   └── sessions/[slug].astro
        └── styles/
            ├── tokens.css          ← design system (CSS custom properties)
            └── global.css
```

---

## How to Navigate the Codebase

### "I want to edit session content"

→ Edit `.md` files in [`site/src/content/sessions/`](site/src/content/sessions/)

### "I want to change how a session page looks"

→ Edit [`site/src/layouts/SessionLayout.astro`](site/src/layouts/SessionLayout.astro) (layout) or component files in [`site/src/components/session/`](site/src/components/session/)

### "I want to change the sidebar"

→ Edit [`site/src/components/layout/Sidebar.astro`](site/src/components/layout/Sidebar.astro), [`SidebarWeekGroup.astro`](site/src/components/layout/SidebarWeekGroup.astro), or [`SidebarLink.astro`](site/src/components/layout/SidebarLink.astro)

### "I want to change colours / spacing / fonts"

→ Edit CSS custom properties in [`site/src/styles/tokens.css`](site/src/styles/tokens.css)

### "I want to add a new MDX component"

→ Create in `site/src/components/session/` or `site/src/components/ui/`, then register in [`site/src/pages/sessions/[slug].astro`](site/src/pages/sessions/%5Bslug%5D.astro)

### "I want to add a new page (not a session)"

→ Create an `.astro` file in `site/src/pages/` — Astro's file-based router picks it up automatically

### "I want to change the home page grid"

→ Edit [`site/src/pages/index.astro`](site/src/pages/index.astro)

### "I want to change week labels or themes"

→ Edit the `WEEKS` array in [`site/src/lib/constants.ts`](site/src/lib/constants.ts)

---

## Detailed Documentation Links

| Document | Location | Contents |
|----------|----------|---------|
| **Site README** | [`site/README.md`](site/README.md) | Quick start, commands, project structure, tech stack |
| **Site Structure** | [`site/SITE_STRUCTURE.md`](site/SITE_STRUCTURE.md) | Full directory layout, component hierarchy, how-to guides |
| **Deployment Guide** | [`site/DEPLOYMENT.md`](site/DEPLOYMENT.md) | Local dev, production build, Netlify, environment variables |
| **Contributing Guide** | [`site/CONTRIBUTING.md`](site/CONTRIBUTING.md) | Code style, naming conventions, frontmatter schema, PR checklist |
| **Architecture Plan** | [`plans/site-architecture.md`](plans/site-architecture.md) | Original design decisions and technical specification |

---

## Key Design Principles

1. **Content over infrastructure** — content authors should need only Markdown knowledge; no framework expertise required.
2. **Static by default** — no server, no database, no runtime dependencies in production.
3. **Type safety at the edges** — all content is validated by Zod at build time; TypeScript covers all component props.
4. **Design tokens own the look** — `tokens.css` is the single source of truth for visual design; no magic numbers elsewhere.
5. **Zero external requests** — fonts, icons, and scripts are self-hosted or inlined.

---

## Next Steps for Customization

### Short-term

- [ ] Replace the placeholder `<SITE_URL>` in `.env.example` and Netlify with the real production URL
- [ ] Add your GitHub repository URL to the deploy badges in `site/README.md`
- [ ] Populate the empty root `README.md` (currently blank) with a repo-level overview linking to `WORKSHOP_SITE_OVERVIEW.md`

### Medium-term

- [ ] Add a **search** page — Astro's [Pagefind integration](https://pagefind.app/) is a lightweight option
- [ ] Add **session progress tracking** — a localStorage-backed `useProgress` hook to mark sessions complete
- [ ] Add **print / PDF styles** — useful for participants who want offline handouts
- [ ] Add **OpenGraph / Twitter card** meta images — one per session using Astro's `@astrojs/og` integration

### Long-term

- [ ] Internationalization (i18n) via Astro's built-in i18n routing
- [ ] A CMS integration (Notion, Sanity, Contentful) if non-developer content editors are needed
- [ ] Analytics (Plausible or Fathom) — privacy-friendly options that work with Netlify

---

## Build & Deploy Summary

```bash
# Local development
cd site && npm install && npm run dev
# → http://localhost:4321

# Production build
cd site && npm run build
# → site/dist/ (static HTML/CSS/JS)

# Deploy to Netlify
# Option A: push to main — CI/CD handles it automatically
# Option B: netlify deploy --dir site/dist --prod
```

The site passes CI when:
- `astro check` exits with 0 errors
- `astro build` completes without errors
- All 17 session HTML files are present in `dist/sessions/`
