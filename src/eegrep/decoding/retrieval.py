"""Sentence retrieval and the noise-input control."""


def retrieval_scores(pred_embeddings, text_embeddings, top_k=(1, 5, 10)):
    raise NotImplementedError  # TODO


def noise_control(aligner, shape, n_repeats=5):
    """Decode from random noise to check decoding relies on real EEG."""
    raise NotImplementedError  # TODO
