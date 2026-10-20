"""PyTorch Dataset wrapping preprocessed EEG epochs and their sentences."""


class EEGSentenceDataset:
    """Yields (eeg_epoch, sentence, subject_id, metadata)."""

    def __init__(self, processed_dir, subjects):
        raise NotImplementedError  # TODO
