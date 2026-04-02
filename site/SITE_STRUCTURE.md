# Site Structure

This document describes the directory layout, component hierarchy, and conventions used in the AI Basics Workshop site.

---

## Directory Layout

```
site/
├── astro.config.mjs          # Astro + Vite + MDX configuration
├── tailwind.config.mjs       # Tailwind CSS v4 configuration
├── tsconfig.json             # TypeScript configuration
├── package.json              # NPM scripts and dependencies
├── netlify.toml              # Netlify build & headers configuration
├── .env.example              # Environment variable template
│
├── public/                   # Static assets (copied verbatim to dist/)
│   ├── favicon.svg
│   └── fonts/                # Self-hosted web fonts
│
└── src/
    ├── components/
    │   ├── layout/           # Shell / chrome components
    │   │   ├── BaseHead.astro          # <head> meta, fonts, global CSS
    │   │   ├── Sidebar.astro           # Full sidebar (week groups + links)
    │   │   ├── SidebarWeekGroup.astro  # Collapsible week heading
    │   │   ├── SidebarLink.astro       # Individual session nav link
    │   │   └── MobileMenuToggle.astro  # Hamburger button (mobile)
    │   │
    │   ├── session/          # Per-session content components
    │   │   ├── SessionHeader.astro     # Title, badge, meta row
    │   │   ├── ObjectivesList.astro    # Learning objectives list
    │   │   ├── KeyConcept.astro        # Highlighted concept block
    │   │   ├── Takeaway.astro          # Summary takeaway block
    │   │   └── TeachingMoment.astro    # Inline instructor note
    │   │
    │   └── ui/               # Generic, reusable UI primitives
    │       ├── Badge.astro             # Pill / label badge
    │       ├── Callout.astro           # Info / warning / tip callout
    │       ├── CodeBlock.astro         # Syntax-highlighted code block
    │       └── ProgressBar.astro       # Visual progress indicator
    │
    ├── content/
    │   ├── config.ts          # Zod schema for the "sessions" collection
    │   └── sessions/          # One Markdown file per session (01–17)
    │       ├── 01-tokens-context-window.md
    │       ├── 02-prompt-engineering.md
    │       └── ... (17 total)
    │
    ├── layouts/
    │   ├── BaseLayout.astro   # Outer shell (BaseHead + Sidebar + slot)
    │   ├── SessionLayout.astro# Standard session page wrapper
    │   └── RetroLayout.astro  # Retrospective session (session 17)
    │
    ├── lib/
    │   ├── constants.ts       # WEEK_MAP, site-wide constants
    │   └── sessions.ts        # getAllSessions(), getAdjacentSessions()
    │
    ├── pages/
    │   ├── index.astro        # Home page — curriculum grid
    │   └── sessions/
    │       └── [slug].astro   # Dynamic route for each session
    │
    └── styles/
        ├── tokens.css         # CSS custom properties (design tokens)
        └── global.css         # Base reset + Tailwind @layer imports
```

---

## Component Hierarchy

```
BaseLayout
└── BaseHead         (injected into <head>)
└── Sidebar
    ├── SidebarWeekGroup  (×5 weeks)
    │   └── SidebarLink   (×3–4 sessions per week)
    └── MobileMenuToggle  (shown on small screens)
└── <slot />         (page content goes here)
    └── SessionLayout  (or RetroLayout for session 17)
        ├── SessionHeader
        ├── ObjectivesList
        └── MDX body
            ├── KeyConcept
            ├── Callout
            ├── CodeBlock
            ├── TeachingMoment
            └── Takeaway
```

---

## How to Add a New Session

1. **Create the content file**
   ```
   site/src/content/sessions/18-new-topic.md
   ```

2. **Add required frontmatter** (all fields validated by Zod in `config.ts`):
   ```md
   ---
   title: "New Topic"
   order: 18
   week: 5
   duration: "45 min"
   type: "lecture"          # lecture | workshop | project | retrospective
   objectives:
     - "Understand X"
     - "Apply Y"
   ---
   ```

3. **Write the session body** — use MDX components freely:
   ```mdx
   import KeyConcept from '../../components/session/KeyConcept.astro';

   <KeyConcept title="Core Idea">
     Explanation here...
   </KeyConcept>
   ```

4. **Update `WEEK_MAP`** in [`src/lib/constants.ts`](src/lib/constants.ts) if the session
   belongs to a new week grouping.

5. **Run `npm run dev`** and navigate to `/sessions/18-new-topic` to verify.

---

## How to Modify Styling (Design Tokens)

All visual design values are defined as CSS custom properties in
[`src/styles/tokens.css`](src/styles/tokens.css):

| Token group      | Examples                                          |
|------------------|---------------------------------------------------|
| Colors           | `--color-primary`, `--color-surface`, `--color-text` |
| Typography       | `--font-sans`, `--font-mono`, `--text-base`       |
| Spacing          | `--space-1` … `--space-16`                        |
| Border radius    | `--radius-sm`, `--radius-md`, `--radius-lg`       |
| Shadows          | `--shadow-sm`, `--shadow-md`                      |

To change the primary accent colour site-wide, edit `--color-primary` in
`tokens.css`. Tailwind's theme in [`tailwind.config.mjs`](tailwind.config.mjs)
references these variables, so Tailwind utility classes (`text-primary`,
`bg-surface`, etc.) update automatically.

---

## How to Extend MDX Components

MDX components are registered in [`src/pages/sessions/[slug].astro`](src/pages/sessions/[slug].astro)
via the `components` prop passed to `<Content />`:

```astro
<Content
  components={{
    KeyConcept,
    Callout,
    CodeBlock,
    TeachingMoment,
    Takeaway,
    // Add your new component here:
    MyComponent,
  }}
/>
```

1. Create your component in `src/components/session/` or `src/components/ui/`.
2. Import it in `[slug].astro`.
3. Add it to the `components` map.
4. Use it in any session's `.md` file with `<MyComponent ... />`.
