"""Aggregate results into comparison tables and figures."""
import argparse


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config", default="configs/evaluation.yaml")
    p.parse_args()
    raise NotImplementedError  # TODO


if __name__ == "__main__":
    main()
