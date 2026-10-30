
import ssl
import socket
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def measure_latency(host, port=443, timeout=3):
    start_time = time.perf_counter()

    try:
        with socket.create_connection(
            (host, port),
            timeout=timeout,
        ):
            end_time = time.perf_counter()
            latency = (end_time - start_time) * 1000

            return {
                "success": True,
                "latency": latency,
                "error": None,
            }

    except OSError as exception:
        return {
            "success": False,
            "latency": None,
            "error": str(exception),
        }

def resolve_host(host):
    start_time = time.perf_counter()

    try:
        results = socket.getaddrinfo(
            host,
            None,
            type=socket.SOCK_STREAM,
        )

        elapsed = (time.perf_counter() - start_time) * 1000

        ips = list(dict.fromkeys(
            result[4][0] for result in results
        ))

        return {
            "success": True,
            "ips": ips,
            "dns_time_ms": elapsed,
            "error": None,
        }

    except socket.gaierror as error:
        elapsed = (time.perf_counter() - start_time) * 1000

        return {
            "success": False,
            "ips": [],
            "dns_time_ms": elapsed,
            "error": str(error),
        }
        
        
        
        
        
def measure_tcp_connection(ip, port=443, timeout=3):
    start_time = time.perf_counter()

    try:
        with socket.create_connection(
            (ip, port),
            timeout=timeout,
        ):
            elapsed = (time.perf_counter() - start_time) * 1000

            return {
                "success": True,
                "tcp_time_ms": elapsed,
                "error": None,
            }

    except OSError as error:
        elapsed = (time.perf_counter() - start_time) * 1000

        return {
            "success": False,
            "tcp_time_ms": elapsed,
            "error": str(error),
        }
        
        
        
        
        
        
        
def measure_tls_connection(host, ip, port=443, timeout=3):
    start_time = time.perf_counter()

    try:
        context = ssl.create_default_context()

        with socket.create_connection(
            (ip, port),
            timeout=timeout,
        ) as connection:
            with context.wrap_socket(
                connection,
                server_hostname=host,
            ):
                elapsed = (time.perf_counter() - start_time) * 1000

                return {
                    "success": True,
                    "tls_time_ms": elapsed,
                    "error": None,
                }

    except (OSError, ssl.SSLError) as error:
        elapsed = (time.perf_counter() - start_time) * 1000

        return {
            "success": False,
            "tls_time_ms": elapsed,
            "error": str(error),
        }


def measure_http_request(url, timeout=5):
    start_time = time.perf_counter()

    request = Request(
        url,
        headers={"User-Agent": "NetWatch/0.1"},
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            elapsed = (time.perf_counter() - start_time) * 1000

            return {
                "success": True,
                "status_code": response.status,
                "http_time_ms": elapsed,
                "error": None,
            }

    except HTTPError as error:
        # حتی پاسخ‌هایی مثل 404 و 500 نشان می‌دهند
        # که سرور به درخواست HTTP پاسخ داده است.
        elapsed = (time.perf_counter() - start_time) * 1000

        return {
            "success": True,
            "status_code": error.code,
            "http_time_ms": elapsed,
            "error": None,
        }

    except (URLError, OSError, TimeoutError) as error:
        elapsed = (time.perf_counter() - start_time) * 1000

        return {
            "success": False,
            "status_code": None,
            "http_time_ms": elapsed,
            "error": str(error),
        }