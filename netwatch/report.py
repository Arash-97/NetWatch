from datetime import datetime, timezone


def generate_report(host, results, diagnosis):
    return {
        "target": host,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": (
            "healthy"
            if diagnosis["cause"] == "no_detected_issue"
            else "issue_detected"
        ),
        "checks": {
            "dns": results["dns"],
            "tcp": results["tcp"],
            "tls": results["tls"],
            "http": results["http"],
        },
        "diagnosis": diagnosis,
    }