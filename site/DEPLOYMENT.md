# Deployment Guide

This document covers everything needed to run the AI Basics Workshop site locally, build it for production, and deploy it to Netlify.

---

## Prerequisites

| Tool | Minimum version | Check |
|------|-----------------|-------|
| Node.js | 20.x LTS | `node --version` |
| npm | 10.x | `npm --version` |
| Git | any recent | `git --version` |

> **Tip:** Use [nvm](https://github.com/nvm-sh/nvm) or [fnm](https://github.com/Schniz/fnm) to manage Node versions.
> A `.nvmrc` / `.node-version` file pinned to `20` lives at the repo root.

---

## Local Development Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-org/ai-basics.git
cd ai-basics/site

# 2. Copy environment variables template
cp .env.example .env
# (edit .env if needed — defaults work for local dev)

# 3. Install dependencies
npm install

# 4. Generate Astro content-collection types and start the dev server
npm run dev
```

The site will be available at **http://localhost:4321**.

Hot-module replacement (HMR) is enabled — saving any source file immediately
updates the browser without a full reload.

---

## Building for Production

```bash
cd site
npm run build
```

Output is written to `site/dist/`. The build is fully static (no server-side
rendering): every route is pre-rendered to an HTML file at build time.

### Verifying the build locally

```bash
npm run preview
```

Serves `dist/` at **http://localhost:4321** using Astro's built-in preview
server — identical to what Netlify will serve.

### Full test pass (type-check + build)

```bash
npm test
# equivalent to: npm run check && npm run build
```

---

## Deploying to Netlify

### Option A — Automatic (recommended)

1. Push the repository to GitHub.
2. In the [Netlify dashboard](https://app.netlify.com/) click **Add new site → Import an existing project**.
3. Connect to your GitHub repo.
4. Netlify auto-detects `netlify.toml`; no manual configuration required.
5. Click **Deploy site**.

Every push to `main` triggers a new deploy automatically via GitHub Actions
(`.github/workflows/build-deploy.yml`).

### Option B — Manual CLI deploy

```bash
# Install Netlify CLI globally (once)
npm install -g netlify-cli

# Authenticate
netlify login

# Deploy a preview
netlify deploy --dir site/dist

# Deploy to production
netlify deploy --dir site/dist --prod
```

---

## Environment Variables

| Variable | Where to set | Purpose |
|----------|--------------|---------|
| `SITE_URL` | Netlify UI → Site settings → Environment variables | Canonical URL used in `<link rel="canonical">` and the sitemap |
| `NETLIFY_AUTH_TOKEN` | GitHub repo → Settings → Secrets | Netlify personal access token for CI deployments |
| `NETLIFY_SITE_ID` | GitHub repo → Settings → Secrets | UUID of the Netlify site (found in Site settings → General) |

### Getting `NETLIFY_SITE_ID`

```bash
netlify sites:list
# or open: Site settings → General → Site details → Site ID
```

### Getting `NETLIFY_AUTH_TOKEN`

Netlify dashboard → User settings → Applications → **New access token**.

---

## Netlify Configuration (`netlify.toml`)

Key settings in [`netlify.toml`](netlify.toml):

| Setting | Value | Notes |
|---------|-------|-------|
| `build.base` | `site` | Subdirectory containing the Astro project |
| `build.command` | `npm run build` | |
| `build.publish` | `dist` | Output directory (relative to `base`) |
| `NODE_VERSION` | `20` | Matches our CI environment |

Security headers (`X-Frame-Options`, `X-Content-Type-Options`, etc.) and
aggressive cache headers for static assets are also configured in `netlify.toml`.

---

## Troubleshooting

### `Cannot find module 'astro:content'`

These are IDE-only TypeScript errors that disappear after Astro generates its
types. Run:

```bash
npm run dev   # or: npx astro sync
```

Then restart your editor's TypeScript language server.

### Build fails with `astro check` errors

Run `npm run check` locally and fix all TypeScript / Astro type errors before
pushing. The CI workflow runs `astro check` and will fail the build if errors
are present.

### Netlify deploy shows old content

Force a cache-busted redeploy:

```bash
netlify deploy --dir site/dist --prod --message "force rebuild"
```

Or trigger via the Netlify dashboard: **Deploys → Trigger deploy → Clear cache and deploy**.

### `npm ci` fails on Netlify

Ensure `package-lock.json` is committed. The `netlify.toml` sets
`NPM_FLAGS=--legacy-peer-deps`; remove that line if your dependency tree is
clean (no peer-dependency conflicts).

### Port 4321 already in use

```bash
npm run dev -- --port 4322
```
