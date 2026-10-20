"""Unseen-subject and cross-dataset (ZuCo 1.0 <-> 2.0) evaluation."""
import argparse


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config", default="configs/generalization.yaml")
    p.parse_args()
    raise NotImplementedError  # TODO


if __name__ == "__main__":
    main()
