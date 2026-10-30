def diagnose(results):
    dns = results["dns"]
    tcp = results["tcp"]
    tls = results["tls"]
    http = results["http"]

    if not dns["success"]:
        return {
            "cause": "dns_failure",
            "confidence": "high",
            "message": "Domain name resolution failed.",
        }

    if tcp is None or not tcp["success"]:
        return {
            "cause": "tcp_connection_failure",
            "confidence": "medium",
            "message": "DNS succeeded, but TCP connection failed.",
        }

    if tls is None or not tls["success"]:
        return {
            "cause": "tls_failure",
            "confidence": "medium",
            "message": "TCP succeeded, but TLS handshake failed.",
        }

    if http is None or not http["success"]:
        return {
            "cause": "http_failure",
            "confidence": "medium",
            "message": "TLS succeeded, but HTTP request failed.",
        }

    return {
        "cause": "no_detected_issue",
        "confidence": "high",
        "message": "All tested network stages succeeded.",
    }