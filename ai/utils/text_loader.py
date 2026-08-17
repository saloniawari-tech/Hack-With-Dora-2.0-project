from pathlib import Path


def load_lease():

    file_path = (
        Path(__file__)
        .parent
        .parent
        .parent
        / "sample_data"
        / "sample_lease.txt"
    )

    return file_path.read_text(
        encoding="utf-8"
    )