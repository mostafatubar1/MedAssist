"""Nour-owned evaluation harness entrypoint.

Expected future comparison: plain RAG vs agentic RAG on the same versioned dataset.
This scaffold intentionally contains no medical evaluation logic.
"""

from pathlib import Path

RESULTS_DIR = Path(__file__).parent / "results"


def main() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)
    print("Evaluation harness scaffold only. Add versioned datasets/metrics on feature/swe-lead.")


if __name__ == "__main__":
    main()
