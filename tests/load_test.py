import asyncio
import time
import statistics
import httpx

URL = "http://127.0.0.1:8000/predict"
TOTAL_REQUESTS = 200
CONCURRENCY = 50

SAMPLE_INPUT = {
    "Age": 45,
    "Gender": "M",
    "Fever": 1,
    "Cough": 1,
    "Fatigue": 1,
    "Breathlessness": 0,
    "Chest_Pain": 0,
    "Nausea": 0,
    "Headache": 1,
    "BMI": 24.5,
    "BP_Systolic": 120,
    "BP_Diastolic": 80,
    "SpO2": 98,
    "Glucose_mg_dL": 95,
    "HbA1c": 5.4
}

async def main():
    semaphore = asyncio.Semaphore(CONCURRENCY)
    latencies = []
    successes = 0
    failures = 0

    limits = httpx.Limits(
        max_connections=CONCURRENCY,
        max_keepalive_connections=CONCURRENCY
    )

    async with httpx.AsyncClient(
        limits=limits, timeout=30.0
    ) as client:

        async def send_request():
            nonlocal successes, failures

            async with semaphore:
                start = time.perf_counter()

                try:
                    response = await client.post(
                        URL, json=SAMPLE_INPUT
                    )
                    elapsed = time.perf_counter() - start
                    latencies.append(elapsed * 1000)

                    if response.status_code == 200:
                        successes += 1
                    else:
                        failures += 1

                except Exception as error:
                    failures += 1
                    print("Request error:", error)

        start_all = time.perf_counter()

        await asyncio.gather(
            *(send_request() for _ in range(TOTAL_REQUESTS))
        )

        total_time = time.perf_counter() - start_all

    print("\n=== CAREBOT LOAD TEST RESULTS ===")
    print("Total requests:", TOTAL_REQUESTS)
    print("Maximum concurrent requests:", CONCURRENCY)
    print("Successful requests:", successes)
    print("Failed requests:", failures)
    print("Total test time:", round(total_time, 3), "seconds")

    if latencies:
        print("Average latency:", round(statistics.mean(latencies), 2), "ms")
        print("Median latency:", round(statistics.median(latencies), 2), "ms")
        print("95th percentile latency:", round(
            sorted(latencies)[int(0.95 * (len(latencies) - 1))], 2
        ), "ms")
        print("Maximum latency:", round(max(latencies), 2), "ms")
        print("Throughput:", round(successes / total_time, 2), "requests/second")

asyncio.run(main())
