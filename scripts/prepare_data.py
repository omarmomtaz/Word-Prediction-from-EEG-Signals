"""Load ZuCo, align EEG with sentences, build subject-wise splits."""
import argparse


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config", default="configs/data.yaml")
    p.parse_args()
    raise NotImplementedError  # TODO


if __name__ == "__main__":
    main()
