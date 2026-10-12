# Contributing

## Setup

Copy `.env.example` to `.env` for the hosted app, and `web/.env.example` to `web/.env` for the React app. Never commit `.env`.

The dev and test virtualenv is `.venv311`. Desktop installer builds use a separate `.venv-desktop*` environment. Do not mix them.

Python is 3.11 (3.10–3.12 only).

```bash
make install
make test
```

Windows:

```powershell
.\scripts\dev.ps1 install
.\scripts\dev.ps1 test
```

## Tests

Engine tests: `make test` or `.\scripts\dev.ps1 test`.

Lint the shared engine only:

```bash
ruff check src/audio_to_tab
```

Website tests: `cd web && npm test`. GitHub CI does not run them. CI also does not typecheck. Run `cd web && npx tsc --noEmit` yourself before calling TypeScript work done.

## Two products

Desktop is Streamlit in `ui/`. The website is FastAPI in `backend/` plus React in `web/`. They share `src/audio_to_tab/`. Do not treat them as one app.

Desktop Interface Lite is the Streamlit chrome that picks speed and device for this computer. Hosted processing mode `lite` is a different, quota-capped mode on the website. Desktop must not silently clamp audio length. The hosted `lite` mode does.

## Where to start

Read `PROJECT_TREE.md` before searching the tree. It maps a change to the file to open first.

## Committed frontends

Three desktop iframe components commit their Vite build so installer testers do not need Node. Edit `frontend/src/`, then rebuild. Never hand-edit `frontend/build/`.

| Component | Rebuild |
|---|---|
| `ui/stem_mixer_component/frontend/` | `make mixer-build` or `.\scripts\dev.ps1 mixer-build` |
| `ui/region_picker_component/frontend/` | `make region-picker-build` or `.\scripts\dev.ps1 region-picker-build` |
| `ui/mix_tabs_component/frontend/` | `make mix-tabs-build` or `.\scripts\dev.ps1 mix-tabs-build` |

## Never commit

Do not commit `.env`, model weights, user audio, `data/`, or `output/`.
