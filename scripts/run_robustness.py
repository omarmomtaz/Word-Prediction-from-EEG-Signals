"""Evaluate decoding under degraded EEG signal quality."""
import argparse


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config", default="configs/robustness.yaml")
    p.parse_args()
    raise NotImplementedError  # TODO


if __name__ == "__main__":
    main()
