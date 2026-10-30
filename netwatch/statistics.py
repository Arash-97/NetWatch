def calculate_statistics(results):
    if not results:
        return {
            "successful_count": 0,
            "failed_count": 0,
            "average": None,
            "minimum": None,
            "maximum": None,
        }

    successful_count = 0
    failed_count = 0
    latencies = []

    for result in results:
        if result["success"]:
            successful_count += 1
            latencies.append(result["tcp_time_ms"])
        else:
            failed_count += 1

    statistics = {
        "successful_count": successful_count,
        "failed_count": failed_count,
        "average": None,
        "minimum": None,
        "maximum": None,
    }

    if latencies:
        statistics["average"] = sum(latencies) / len(latencies)
        statistics["minimum"] = min(latencies)
        statistics["maximum"] = max(latencies)

    return statistics