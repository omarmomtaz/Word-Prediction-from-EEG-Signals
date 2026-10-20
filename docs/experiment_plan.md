# Experiment plan

## Required components
- Subject-wise splits (evaluation on unseen subjects)
- At least two representation approaches, one trained/fine-tuned self-supervised on ZuCo, plus baselines
- Noise-input control for EEG-to-language decoding
- Signal-quality / robustness analysis, including quality-aware representations
- Unseen-subject generalization and ZuCo 1.0 <-> 2.0 transfer
- Comparison under normal and degraded EEG, with findings and limitations

## Open decisions
- Which pretrained EEG model(s) to use
- Self-supervised objective
- Decoding target / alignment loss
- Quality metric and degradation settings
