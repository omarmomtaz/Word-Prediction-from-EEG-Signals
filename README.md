# EEG Representation Learning for Brain Signal Decoding

Investigates whether modern pretrained EEG representation models can learn language-related
information from EEG recorded while subjects read sentences (ZuCo 1.0 and ZuCo 2.0), and whether
those representations stay useful on unseen subjects and under degraded signal quality.

> **Status:** project skeleton only. Modules contain stubs and TODOs.

## Pipeline

1. **Data** - download and prepare ZuCo 1.0 / 2.0, build subject-wise train/val/test splits
2. **Preprocessing** - filtering, artifact handling, normalization, consistent epoch format
3. **Representation learning** - pretrained EEG encoders, a self-supervised model trained/fine-tuned on ZuCo, baselines
4. **EEG-to-language decoding** - align EEG features with sentence embeddings, retrieval / semantic evaluation, noise-input control
5. **Signal quality and robustness** - noise/artifact degradation, quality-aware representations
6. **Generalization** - unseen subjects, cross-dataset transfer (ZuCo 1.0 <-> ZuCo 2.0)
7. **Evaluation and analysis** - comparison, degraded vs. normal conditions, findings and limitations

## Datasets

- ZuCo 1.0: https://osf.io/q3zws/overview
- ZuCo 2.0: https://osf.io/2urht/overview

Raw data is not committed. Place it under `data/raw/zuco1/` and `data/raw/zuco2/` (see `scripts/download_data.py`).

## Repository layout

```
configs/        experiment configs (YAML)
data/           raw / interim / processed data (git-ignored)
docs/           project notes and experiment plan
notebooks/      exploration notebooks
scripts/        command-line entry points for each pipeline stage
src/eegrep/     main package (data, preprocessing, models, decoding, robustness, evaluation)
tests/          unit tests
results/        outputs: figures, tables, checkpoints (git-ignored)
```

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
python scripts/download_data.py --help
```

## Experiments (planned)

| Step | Script | Config |
|------|--------|--------|
| Prepare data | `scripts/prepare_data.py` | `configs/data.yaml` |
| Preprocess | `scripts/preprocess.py` | `configs/preprocessing.yaml` |
| Extract / train representations | `scripts/train_representation.py` | `configs/representation.yaml` |
| Decode EEG to language | `scripts/run_decoding.py` | `configs/decoding.yaml` |
| Robustness analysis | `scripts/run_robustness.py` | `configs/robustness.yaml` |
| Generalization | `scripts/run_generalization.py` | `configs/generalization.yaml` |
| Evaluate / report | `scripts/evaluate.py` | `configs/evaluation.yaml` |

## License

TODO
