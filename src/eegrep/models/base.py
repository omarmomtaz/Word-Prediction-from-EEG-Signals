"""Common interface for all representation approaches."""


class EEGEncoder:
    """Maps an EEG epoch to a feature vector."""

    def encode(self, batch):
        raise NotImplementedError  # TODO
