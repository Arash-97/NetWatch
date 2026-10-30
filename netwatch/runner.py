
from netwatch.measurement import measure_tcp_connection



from netwatch.measurement import (
    resolve_host,
    measure_tcp_connection,
    measure_tls_connection,
    measure_http_request,
)


def run_target_check(host, port=443, timeout=3):
    results = {
        "host": host,
        "dns": None,
        "tcp": None,
        "tls": None,
        "http": None,
    }

    # 1. DNS
    dns_result = resolve_host(host)
    results["dns"] = dns_result

    if not dns_result["success"]:
        return results

    ip = dns_result["ips"][0]

    # 2. TCP
    tcp_result = measure_tcp_connection(
        ip,
        port=port,
        timeout=timeout,
    )
    results["tcp"] = tcp_result

    if not tcp_result["success"]:
        return results

    # 3. TLS
    tls_result = measure_tls_connection(
        host,
        ip,
        port=port,
        timeout=timeout,
    )
    results["tls"] = tls_result

    if not tls_result["success"]:
        return results

    # 4. HTTP
    http_result = measure_http_request(
        f"https://{host}/",
        timeout=timeout,
    )
    results["http"] = http_result

    return results