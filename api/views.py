
import json
import re

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from netwatch.service import run_network_diagnostic


def dashboard(request):
    return render(request, "api/dashboard.html")


@csrf_exempt
@require_POST
def run_diagnostic(request):
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse(
            {"error": "Invalid JSON request."},
            status=400
        )

    if not isinstance(data, dict):
        return JsonResponse(
            {"error": "Invalid request structure."},
            status=400
        )

    host = data.get("host")

    if not isinstance(host, str):
        return JsonResponse(
            {"error": "The host field is required."},
            status=400
        )

    host = host.strip().lower()

    if not host or len(host) > 253:
        return JsonResponse(
            {"error": "Invalid domain name."},
            status=400
        )

    hostname_pattern = (
        r"^(?=.{1,253}$)"
        r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+"
        r"[a-z]{2,63}$"
    )

    if not re.fullmatch(hostname_pattern, host):
        return JsonResponse(
            {"error": "Invalid domain format."},
            status=400
        )

    try:
        report = run_network_diagnostic(host)
        return JsonResponse(report)

    except Exception:
        return JsonResponse(
            {"error": "An error occurred during network diagnostics."},
            status=500
        )
