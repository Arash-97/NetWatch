import json

from netwatch.service import run_network_diagnostic


targets = [
    "google.com",
    "cloudflare.com",
]

for host in targets:
    print(f"\n--- Checking {host} ---")

    report = run_network_diagnostic(host)

    print(json.dumps(
        report,
        indent=4,
        ensure_ascii=False,
    ))