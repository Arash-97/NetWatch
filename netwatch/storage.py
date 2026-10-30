import json
from pathlib import Path


def get_data_directory():
    project_root = Path(__file__).parent.parent
    data_directory = project_root / "data"

    data_directory.mkdir(parents=True, exist_ok=True)

    return data_directory


def save_report(report):
    if not report:
        return False

    data_directory = get_data_directory()
    file_path = data_directory / "reports.jsonl"

    with file_path.open(
        mode="a",
        encoding="utf-8",
    ) as file:
        file.write(json.dumps(report, ensure_ascii=False) + "\n")

    return True