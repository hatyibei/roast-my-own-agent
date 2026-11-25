"""Entry for Roast Your Own Agent: writes the roast line to /output/entry.txt."""

import os

TEXT = "My agent announced 'Done!' like a surgeon, cited three sources it invented, summarized a meeting that never happened, and asked if there was anything else it could hallucinate."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
