"""Download ZuCo 1.0 / 2.0 from OSF into data/raw/."""
import argparse

ZUCO1 = "https://osf.io/q3zws/overview"
ZUCO2 = "https://osf.io/2urht/overview"


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--dataset", choices=["zuco1", "zuco2", "all"], default="all")
    p.add_argument("--out", default="data/raw")
    p.parse_args()
    raise NotImplementedError  # TODO


if __name__ == "__main__":
    main()
