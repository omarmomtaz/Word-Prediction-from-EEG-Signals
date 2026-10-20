"""Aligns EEG representations with sentence representations."""


class EEGTextAligner:
    def fit(self, eeg_features, text_embeddings):
        raise NotImplementedError  # TODO

    def transform(self, eeg_features):
        raise NotImplementedError  # TODO
