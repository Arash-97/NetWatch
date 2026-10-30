from netwatch.runner import run_target_check
from netwatch.diagnostics import diagnose
from netwatch.report import generate_report
from netwatch.storage import save_report


def run_network_diagnostic(host, port=443, timeout=3):
    # 1. Execute network checks
    results = run_target_check(
        host,
        port=port,
        timeout=timeout,
    )

    # 2. Analyze results
    diagnosis = diagnose(results)

    # 3. Generate report
    report = generate_report(
        host=host,
        results=results,
        diagnosis=diagnosis,
    )

    # 4. Save report
    save_report(report)

    return report