# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Application to manage [Open Vet Sim](https://openvetsim.org/) scenario archives: a Django REST backend that stores
scenario data relationally and can import/export it as an OVS Scenario Archive (a zip of `main.xml` plus
`images`/`vocals`/`media` directories, per OVS Scenario Specification §2.2-2.5), plus a Vue/Quasar frontend for
browsing, creating, importing, and exporting scenarios.

## Running the stack

```shell
docker compose build
docker compose up -d --wait     # or: make build run
```
- Backend served at `http://localhost:8000` (Django admin at `/admin/`, default creds `test`/`test` in dev fixtures).
- Requires `backend/.env` copied from `backend/example.env` before first run.
- `make clean` / `make cleanv` tear the stack down (`cleanv` also drops volumes).

For frontend-only iteration outside Docker: `cd frontend && npm install && npm run dev` (Quasar dev server, reads
`BACKEND_URL` env var for the API base URL used by the axios boot file).

## Backend (`backend/`)

Django 4.2 LTS + Django REST Framework, Python >=3.12, SQLite at `backend/data/db.sqlite3` in local dev (cloud deploys use
`DATABASE_URL`/Postgres instead — see the cloud-deploy config note below).

- Test: `python manage.py test` (run from `backend/`). Single test: `python manage.py test app.tests.test_scenario`.
- Coverage: `coverage run --source='.' manage.py test && coverage html`.
- Lint: `ruff check ./backend` (from repo root).
- Regenerate OpenAPI schema after changing serializers/views:
  `./manage.py spectacular --file ./schema.json --format openapi-json --api-version v1`.

### Structure

- `backend/backend/` — Django project package (`settings.py`, root `urls.py`, wsgi/asgi).
- `backend/app/` — the single Django app containing everything:
  - `models/` — one file per OVS XML entity (`Scenario`, `Profile`, `Header`, `EventGroup`, `Event`, `Scene`,
    `Trigger`, `Control`, `Cardiac`, `Respiration`, `Avatar`, `File`, etc). `Scenario` is the root aggregate; other
    models hang off it via FK/O2O. Saving/deleting a `Scenario` has signal handlers (`models/Scenario.py`) that
    create/remove its per-scenario file directories (`files/<pk>/{images,media,vocals}`) under `MEDIA_ROOT`.
  - `serializers/` — one DRF serializer per model, mirroring the `models/` split.
  - `urls/api.py` — versioned REST API routes (mounted at `/api/v1/`, namespace `v1`): scenario CRUD, plus
    dedicated endpoints for vocals/media/images since those are file uploads (`multipart/form-data`) handled
    outside the main JSON/XML serializer flow.
  - `urls/auth.py` — session-based auth routes (mounted at `/auth/`, namespace `auth`): `login/`, `auth-check`,
    session expiry.
  - `views.py` — all API views live here (not split further). Views commonly stack
    `@renderer_classes`/`@parser_classes` decorators per-view to opt in/out of XML support.
  - `renderers.py` / `parsers.py` — **the core domain logic of this app**. Two custom XML codecs:
    - `ScenarioXMLRenderer`/`ScenarioXMLParser` — round-trips the *internal* serializer shape (used by
      `/api/v1/scenarios`), so the DB-backed JSON and XML representations stay 1:1.
    - `OvsXMLRenderer`/`OvsXMLParser` — convert to/from the actual OVS scenario XML format consumed by OpenVetSim.
      See the field-mapping notes in `README.md` for the differences (e.g. `<vocalfiles>/<mediafiles>` → `<file>`,
      `<eventgroups>` → `<events>/<category>`, flattened `<scenes>`, file paths truncated to basename).
      `OvsXMLParser`'s generic "same tag ⇒ list" inference breaks on two real shapes — unwrapped repeated `<scene>`
      siblings, and `<controls>`/`<category>` mixing metadata with repeated children — which is why `archive.py`
      (below) does its own targeted parsing for those instead of delegating to it wholesale.
  - `archive.py` — Scenario Archive (zip) ⇄ internal shape, per OVS Scenario Specification §2.2-2.5: a zip of one
    `main.xml` manifest plus `images/`/`vocals/`/`media/` directories. `read_archive()` unpacks and validates a
    zip; `manifest_to_internal()` reshapes a parsed manifest into the `ScenarioSerializer` payload (stripping file
    bytes, which get attached separately — see `ScenarioImport`/`ScenarioExport` in `views.py`, and ADR-0002/0003
    in `docs/adr/` for why). `/api/v1/import` (POST, multipart, one `.zip` field named `archive`) creates a
    `Scenario` from an archive; `/api/v1/export/<pk>` now returns a zip archive (not bare XML).
  - `admin/` — Django admin customizations built on `grappelli` + `django-nested-admin`, so nested OVS structures
    (events, scenes, triggers, inline files) can be edited as one nested form in `/admin/`.
  - `storage.py` — custom file storage (per-scenario subdirectories under `MEDIA_ROOT`).
  - `validators.py` — shared field validators used across serializers.
  - `fixtures/`, `migrations/`, `tests/` — standard Django layout. Tests use `APITestCase` with reversed URL names
    (e.g. `reverse('v1:scenario_list')`); `test.json`/`test.xml`/`updated.json`/`updated.xml` are fixture payloads
    exercised against both representations.

### Auth & API conventions

- DRF default permission is `IsAuthenticatedOrReadOnly`; reads are open, writes require a logged-in session.
- Auth is Django session-based (not tokens): `POST /auth/login/`, `GET /auth/auth-check` to check session state,
  `/api-auth/logout/` (DRF browsable API logout) to log out.
- CSRF is enforced; the frontend must send `X-CSRFToken` from the `csrftoken` cookie on POST/PUT (see
  `frontend/src/boot/axios.ts`).
- CORS/CSRF trusted origins are restricted by regex to `localhost`/`127.0.0.1`/`nginx` — update
  `backend/backend/settings.py` (`CORS_ALLOWED_ORIGIN_REGEXES`, `CSRF_TRUSTED_ORIGINS`) if adding new hosts.

### Cloud deploy config

`docker-compose.yml` (SQLite, local disk) is dev/POC-only (see `docs/adr/0004-cloud-deployment-target.md`) — the
intended target is Postgres + object storage. `SECRET_KEY`/`DEBUG`/`DJANGO_ALLOWED_HOSTS` and `DATABASE_URL`
(via `dj_database_url`) are env-driven with the current dev values as fallback defaults; setting `GS_BUCKET_NAME`
switches file storage to GCS via `django-storages`. **Known gap:** `models/Scenario.py`'s post-save signal and the
zip-building code in `ScenarioExport` both walk `MEDIA_ROOT` with raw `os.path`/`os.listdir` rather than the
Django Storage API, and `storage.py`'s `OverwriteStorage` assumes a local path — all three need porting to
Storage-API calls before GCS mode actually works end-to-end.

## Frontend (`frontend/`)

Vue 3 + Quasar (app-vite) + Pinia + TypeScript.

- Dev server: `npm run dev`.
- Build: `npm run build`.
- Lint: `npm run lint` (ESLint, auto-fixes). Format: `npm run format` (Prettier: single quotes, semicolons,
  trailing commas, printWidth 120 — see `.prettierrc`).
- E2E tests: `npm run test:ui` (Playwright; CI runs `npx playwright test` directly). There is no unit test setup
  (`npm test` is a no-op placeholder).
- Regenerating API types from the backend OpenAPI schema (after backend serializer changes):
  ```shell
  cd backend && ./manage.py spectacular --file ./schema.json --format openapi-json --api-version v1
  cd frontend && npx openapi-typescript-codegen --input ~/tmp/schema.json --output ./src/types
  ```

### Structure

- `src/boot/axios.ts` — shared `api` axios instance (`withCredentials: true`, CSRF cookie wiring). Import `api`
  from here rather than instantiating axios elsewhere.
- `src/stores/app-auth-store.ts` — session auth state (login/logout/auth-check), polls `auth-check` every 21
  minutes while logged in to keep the session alive (backend session age is 20 min).
- `src/stores/` — one Pinia store per step of the multi-step "create scenario" wizard (`create-new-*-store.ts` for
  header/profile/vocals/media/scenario-init/eventgroups/scenes), plus `new-scenario-store.ts` (aggregates all 7 and
  drives the submit sequence) and `scenario-store.ts` (existing scenario list/detail).
- `src/components/CreateScenarioStepper.vue` + `Create*Step.vue` — the scenario creation flow is a 7-step Quasar
  stepper, one component per step, each backed by its matching store above.
  `CardiacRespirationGeneralFields.vue` is shared by the ScenarioInit and Scenes steps (cardiac/respiration/general
  are the same field set in both `ScenarioInit` and per-scene `init`).
  Submission is a single POST at the final step, not progressive (see `docs/adr/0002-single-submit-scenario-creation.md`):
  vocal/media files and the avatar/summary images are picked via `QUploader` in `auto-upload="false"` mode (used
  purely as a file picker — files are held in the Pinia store as plain `File` objects, not uploaded via the
  uploader's own mechanism) and attached via separate `PUT`/`PATCH` calls once the scenario id exists.
- `src/pages/` — top-level routed pages (`IndexPage` = scenario list, `CreatePage`, `ExportPage` = pick a scenario
  and download its archive, `ImportPage` = upload a `.zip` archive).
- `src/router/routes.ts` — route table; all real pages nest under `MainLayout.vue`.
- `src/types/` — TypeScript types, including codegen output from the backend OpenAPI schema (`types/models`) —
  regenerate rather than hand-edit when backend serializers change.

## CI

- `.github/workflows/django.yml` — backend: `python manage.py test` on push to `main`/`feature/**`/`bug/**`.
- `.github/workflows/playwright.yml` — frontend: Playwright e2e suite on the same branches.
- `.github/workflows/bump-version.yml` — auto-bumps `pyproject.toml` version + changelog via conventional commits
  when a PR merges to `main`. Commit messages should follow conventional-commit style accordingly.
