# Iron Horse Precision Agriculture Experiments

This repository is the local experimentation workspace for vineyard imagery analysis at Iron
Horse. The immediate goal is to develop a practical computer-vision workflow that can identify
visual regions worth human inspection, especially possible vine-health issues such as brown
foliage, missing foliage, unusual coloration, irrigation irregularities, or other visible
abnormalities.

The project is currently exploratory. We are not trying to diagnose disease automatically.
The near-term target is decision support: propose inspection regions, let a human review them,
and use that feedback to improve future annotation and model training.

## Two Layers In This Workspace

There are two important layers in this working directory.

### 1. This Repo: Local CV Experimentation

The root repository contains the files we own for this investigation:

- `notebooks/` - exploratory notebooks for region definition, dataset creation, and YOLO model
  evaluation.
- `scripts/` - small reusable scripts for YOLO setup, training, prediction, and evaluation.
- `docs/` - team-facing notes that should become stable enough for another person to use.
- `data/` - local image datasets and annotation exports. This is ignored by Git.
- `models/` - pretrained and trained model weights. Model weights are ignored by Git.
- `runs/` - YOLO output artifacts. This is ignored by Git.
- `smart_vine_monitoring/` - inherited local reference assets from earlier vine-monitoring
  work. This is ignored by Git.

This layer should contain the reproducible experiment scaffolding: annotation rules, dataset
schemas, training commands, evaluation notes, and lightweight code that explains how results
were produced.

### 2. `ihv/`: Partner Repository Reference Clone

The `ihv/` directory is a separate cloned Git repository from a project partner. It is present
locally so we can inspect the broader Iron Horse operational platform, but it is not owned by
this repository and should not be committed here.

Use `ihv/` as read-only context for understanding:

- vineyard block boundaries and GIS assets
- field media sorting and metadata extraction
- S3, CephFS, and cluster data movement
- map ingestion, STAC/PostGIS cataloging, and review queues
- telemetry dashboards from ThingsBoard and InfluxDB
- 3D reconstruction and Gaussian splatting workflows

The partner repo is useful because it shows where a future inspection-region workflow could
eventually connect: sorted field media, block assignments, spatial catalog records, map layers,
and human review workflows. For this repo, however, `ihv/` is only a local reference checkout.

## Current Investigation Areas

- Define what an "inspection region" means in vineyard imagery.
- Decide how regions should be annotated and reviewed.
- Compare annotation workflow options such as CVAT and Roboflow.
- Evaluate whether an inherited YOLO model can provide useful baseline detections.
- Build a small trial dataset for YOLO training and evaluation.
- Design a human-in-the-loop path from model detections to reviewed annotations.

## Current Pipeline Shape

The current root-level pipeline is intentionally small:

1. Collect or select imagery from local vineyard frames.
2. Define region labels and annotation rules.
3. Annotate a small trial dataset.
4. Export annotations in YOLO format.
5. Train or fine-tune a YOLO model.
6. Run predictions on held-out images.
7. Review false positives, missed regions, and confidence thresholds.
8. Feed human review back into the next dataset version.

The existing inherited `smart_vine_monitoring/models/best.pt` model has been loaded and tested
in `notebooks/evaluate_existing_yolo.ipynb`. Initial results suggest it should be treated as a
baseline only, not as a reliable production detector.

## Documentation Map

- `docs/onboarding/YOLO_setup_guide.md` - local YOLO setup and smoke-test notes.
- `docs/git_rules.md` - what belongs in Git versus private or draft notes.
- `docs/datasets/` - dataset and region-definition documentation.
- `docs/experiments/` - experiment decisions, including annotation tooling.
- `notebooks/region_definition.ipynb` - early inspection-region framing.
- `notebooks/region_trial_001_dataset_creation.ipynb` - first trial dataset plan.
- `notebooks/evaluate_existing_yolo.ipynb` - inherited YOLO model evaluation.

## Git Hygiene

Large, local, generated, or partner-owned assets should stay out of this repository. In
particular:

- Do not commit `ihv/`; it is a separate partner repository clone.
- Do not commit `data/`, `runs/`, model weights, virtual environments, or local caches.
- Promote only stable, team-useful notes into `docs/`.
- Keep reusable experiment code in `scripts/`.

Before committing, ask whether another team member would understand why the file exists and
how to use it.

## Recommended Next Steps

1. Turn the region-definition notes into a stable dataset document.
2. Finish the CVAT vs Roboflow annotation-tool decision.
3. Create `region_trial_001` with a real YOLO `data.yaml`, train/val split, and labels.
4. Add a reproducible YOLO training script.
5. Add a repeatable evaluation report for confidence thresholds, false positives, missed
   inspection regions, and qualitative review notes.
6. Later, map reviewed inspection regions back into the broader `ihv/` spatial/catalog model.
