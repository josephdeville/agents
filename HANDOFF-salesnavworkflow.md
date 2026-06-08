# Handoff: `salesnavworkflow.vercel.app` returning 403

**Date:** 2026-06-08
**Prepared by:** Claude Code (web session) → for handoff to **Claude Code running locally**
**Why handoff:** The web session's Vercel connector is scoped to only the `cortex`
project and cannot see/manage `salesnavworkflow`. A local Claude Code session with the
Vercel CLI (`vercel login` as a user with full CortexBuilds team access) can act directly.

---

## TL;DR

- `https://salesnavworkflow.vercel.app` returns **HTTP 403 Forbidden** to anonymous visitors.
- Most likely cause: **Deployment Protection → Vercel Authentication** is enabled for
  **All Deployments**, so the production URL sits behind a login wall.
- The owner wants this to be **restricted / internal** (not fully public, not requiring
  every viewer to have a Vercel account) → target solution is **Password Protection**.
- This was diagnosed remotely without project access; **a local session must verify the
  actual settings and logs before changing anything.**

---

## Key identifiers

| Thing | Value |
|---|---|
| Vercel team (name / slug / id) | CortexBuilds / `gtmengcortexio` / `team_o5pJhVvADZInKFwjWscEfQNE` |
| Affected project | `salesnavworkflow` — dashboard: `https://vercel.com/gtmengcortexio/salesnavworkflow` |
| Public URL (symptom) | `https://salesnavworkflow.vercel.app` → 403 |
| Other project in team (accessible to web session) | `cortex` (`prj_YykEIieORgYF8qZHwxiGJSOlPL2g`) |

---

## What was verified (web session)

1. `list_teams` → one team: **CortexBuilds** (`gtmengcortexio`).
2. `list_projects` for that team → returns **only `cortex`**. `salesnavworkflow` is NOT
   visible to the connector.
3. `get_project("salesnavworkflow")` → **404** (connector not authorized for it).
4. `get_project("cortex")` → ✅ full data (proves the token works and targets the right
   team — the limitation is project scope, not team).
5. `get_deployment("salesnavworkflow.vercel.app")` → **404 not_found** (out of scope).
6. Plain web fetch of the URL → **403 Forbidden**.
7. Vercel MCP `web_fetch_vercel_url` → "Unable to create shareable URL" (consistent with
   no access to that project's deployments).

**Conclusion:** team is correct; the connector simply lacks access to the
`salesnavworkflow` project. The 403 is a *project setting*, not a team-level issue.

---

## Root-cause reasoning

- **403 (not 404)** on a live `*.vercel.app` URL almost always = the deployment exists and
  is being **gated by Deployment Protection (Vercel Authentication)**, not a failed build
  (which usually shows a different error page) and not a missing project (which 404s).
- Owner confirmed intended audience = **restricted / internal**.

---

## Owner's decision

Audience = **Restricted / internal**. They do NOT want it fully public, but also raised the
concern that full public exposure is undesirable. They have not yet changed any setting.
Target: keep an access gate, but ideally one that doesn't require each viewer to have a
Vercel account → **Password Protection**.

> Note: **Password Protection is a paid feature** (Pro plan / Enterprise add-on). If the
> team is on Hobby/free, this option will be unavailable in the dashboard. Fallbacks below.

---

## Action plan for the local session

> Prereq: `vercel login` (or `VERCEL_TOKEN`) as a user with full access to the
> **CortexBuilds** team. Then `vercel switch gtmengcortexio` / link the project.

1. **Confirm the project + deployment state**
   ```bash
   vercel projects ls                 # confirm salesnavworkflow exists
   vercel ls salesnavworkflow         # list deployments; confirm latest prod is READY
   vercel inspect <prod-deployment-url>
   ```
2. **Confirm the cause of the 403** — check Deployment Protection in
   Settings → Deployment Protection (dashboard) OR via API/CLI. Verify whether
   *Vercel Authentication* is set to **All Deployments**.
3. **If build/runtime is actually failing instead** (i.e. not a protection gate), pull logs:
   ```bash
   vercel inspect --logs <deployment-url>
   vercel logs <deployment-url>
   ```
4. **Apply the chosen protection (owner wants restricted/internal):**
   - **Preferred:** Settings → Deployment Protection →
     - Turn **OFF** *Vercel Authentication*.
     - Turn **ON** *Password Protection*, set a shared password, scope = **All Deployments**.
   - **If on Hobby (Password Protection unavailable):** keep *Vercel Authentication →
     All Deployments* (secure, but each viewer needs Vercel team access), or upgrade to Pro,
     or use *Vercel Authentication → Only Preview Deployments* only if production is allowed
     to be public (it is NOT, per owner — so don't do this for prod).
5. **Verify the fix:**
   - With password protection: hitting the URL should show a **password prompt**, then load
     after entering the password (no hard 403).
   - Re-fetch `https://salesnavworkflow.vercel.app` and confirm expected behavior.

---

## Open items / questions for the owner

- Confirm the team's **Vercel plan** (determines whether Password Protection is available).
- Decide the shared password and who receives it.
- (Optional) Widen the web Vercel connector's project scope to include
  `salesnavworkflow` (or "All Projects") so future remote sessions can manage it directly.

---

## Notes

- This handoff doc lives in the `agents` repo only because that was the repo attached to the
  web session; it is unrelated to the `salesnavworkflow` codebase. Move/copy it into the
  actual `salesnavworkflow` project repo if useful.
