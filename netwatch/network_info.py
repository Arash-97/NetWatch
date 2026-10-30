
import subprocess


def get_network_info():
    result = subprocess.run(
        ["ipconfig", "/all"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )

    if result.returncode != 0:
        return {
            "success": False,
            "error": result.stderr.strip() or "Failed to read network configuration.",
        }

    return {
        "success": True,
        "output": result.stdout,
        "error": None,
    }
