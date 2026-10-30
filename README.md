# NetWatch

**A lightweight network diagnostics tool for understanding connectivity issues.**

NetWatch is an open-source network diagnostics project designed to inspect connectivity across multiple layers of a network connection.

Instead of simply reporting whether a website is reachable, NetWatch performs a sequence of checks to help identify where a connection may be failing — from DNS resolution to TCP connectivity, TLS negotiation, and HTTP communication.

The project currently provides a Python-based diagnostic engine, a Django API, and a web dashboard.

---

## Features

- **DNS Resolution:** Resolves a hostname into IP addresses and measures lookup duration.
- **TCP Connectivity:** Checks whether a TCP connection can be established with the target.
- **TLS Handshake:** Tests secure connection establishment and certificate validation.
- **HTTP Request:** Checks whether the target responds to an HTTP request and records its status code.
- **Automated Diagnostics:** Combines individual check results into a structured diagnostic report.
- **JSON Reports:** Stores diagnostic reports locally in JSON Lines format.
- **Web Dashboard:** Provides a browser-based interface for running and viewing diagnostics.
- **Django API:** Exposes a backend endpoint for submitting diagnostic requests.

## How It Works

NetWatch currently follows this diagnostic sequence:

```text
          Target Domain
                |
                v
        DNS Resolution
                |
                v
        TCP Connectivity
                |
                v
         TLS Handshake
                |
                v
         HTTP Request
                |
                v
       Diagnostic Analysis
                |
                v
         JSON Report
```

Each stage provides evidence about a different part of the connection process.

If a stage fails, subsequent dependent checks are skipped. The results are then passed to the diagnostic engine to generate a preliminary assessment.

## Tech Stack

| Component | Technology |
|---|---|
| Core Engine | Python |
| Web Framework | Django |
| Backend API | Django Views |
| Frontend | HTML, CSS, JavaScript |
| Network Operations | Python Standard Library |
| Data Storage | JSON Lines |
| Development Database | SQLite |

## Project Structure

```text
NetWatch/
│
├── api/
│   ├── migrations/
│   ├── templates/
│   │   └── api/
│   │       └── dashboard.html
│   ├── views.py
│   └── urls.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── netwatch/
│   ├── measurement.py
│   ├── runner.py
│   ├── diagnostics.py
│   ├── report.py
│   ├── service.py
│   ├── statistics.py
│   ├── storage.py
│   └── network_info.py
│
├── tests/
├── data/
├── main.py
├── manage.py
└── requirements.txt
```

### Architecture Overview

The project separates network measurements, diagnostic logic, reporting, and application interfaces.

- `measurement.py`: Performs individual network measurements.
- `runner.py`: Coordinates the diagnostic sequence.
- `diagnostics.py`: Analyzes measurement results and identifies potential issues.
- `report.py`: Generates structured diagnostic reports.
- `storage.py`: Persists reports locally.
- `service.py`: Provides a central entry point for running diagnostics.
- `api/`: Connects the diagnostic engine to the Django web application.

This separation allows the diagnostic engine to be reused by different interfaces without tying its core functionality to Django.

## Getting Started

### Requirements

- Python 3.14 or a compatible Python version.
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Arash-97/NetWatch.git
cd NetWatch
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the diagnostic engine

```bash
python main.py
```

The command runs diagnostics against the configured target domains and prints structured JSON reports.

### 5. Start the web application

Apply database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open the dashboard:

```text
http://127.0.0.1:8000/
```

## API Usage

NetWatch provides an endpoint for running network diagnostics.

**Endpoint**

```http
POST /diagnostics/
```

**Request Body**

```json
{
    "host": "google.com"
}
```

**Example using cURL**

```bash
curl -X POST http://127.0.0.1:8000/diagnostics/ \
  -H "Content-Type: application/json" \
  -d "{\"host\":\"google.com\"}"
```

The endpoint returns a JSON report containing the measurement results and diagnostic assessment.

## Diagnostic Report

A report contains:

- Target hostname
- Timestamp
- Overall diagnostic status
- DNS measurement results
- TCP connection results
- TLS handshake results
- HTTP response information
- Diagnostic assessment and confidence level

Example structure:

```json
{
    "target": "google.com",
    "status": "healthy",
    "checks": {
        "dns": {},
        "tcp": {},
        "tls": {},
        "http": {}
    },
    "diagnosis": {
        "cause": "no_detected_issue",
        "confidence": "high"
    }
}
```

*The example above illustrates the report structure; individual measurement values depend on the actual network environment.*

## Current Limitations

NetWatch is an early-stage project. Its current diagnostic engine has some limitations:

- It tests the first IP address returned by the system resolver.
- DNS measurements use the operating system's hostname resolution mechanism.
- Diagnostic conclusions are preliminary and do not establish the exact root cause of every failure.
- HTTP requests perform their own connection process and are not guaranteed to use the same IP address tested by the preceding TCP and TLS checks.
- The current implementation does not directly inspect a user's local Wi-Fi, gateway, or complete network routing path.

These limitations will be addressed as the project evolves.

## Roadmap

Planned improvements include:

- [ ] Improve diagnostic accuracy and confidence evaluation.
- [ ] Add multiple DNS resolver comparisons.
- [ ] Support testing multiple resolved IP addresses.
- [ ] Add gateway and local network connectivity checks.
- [ ] Introduce network interface and protocol inspection.
- [ ] Improve historical measurement analysis.
- [ ] Build a more detailed diagnostic dashboard.
- [ ] Develop a local monitoring agent.
- [ ] Introduce a mobile application.
- [ ] Expand the API for external clients.

## Project Goals

The long-term goal of NetWatch is to build a cross-platform network diagnostics platform that helps users understand why their internet connection is unavailable or unstable.

By combining multiple measurements and analyzing their results, NetWatch aims to provide more useful information than a simple online/offline indicator.

## Contributing

Contributions, bug reports, and suggestions are welcome.

If you find a problem or have an idea for improving NetWatch, feel free to open an issue or submit a pull request.

## License

No license has been added to this repository yet.
