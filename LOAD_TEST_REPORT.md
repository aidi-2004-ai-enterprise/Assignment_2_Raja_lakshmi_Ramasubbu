## Load Testing Summary

To evaluate the performance of my deployed machine learning application (`penguin-predictor`), I performed a series of load tests using Locust. My objective was to understand how the app handles different traffic conditions and whether it can scale efficiently under pressure.

I conducted the following three test scenarios:

1. **Baseline Test** – Steady traffic from 10 users.
2. **Stress Test** – Gradual ramp-up to 100 users.
3. **Spike Test** – Sudden ramp from 1 to 100 users in less than a minute.

---

## Test Results Overview

| Test Type   | Users | Requests | Avg Response Time (ms) | Max Time (ms) | Requests/sec | Failures |
|-------------|-------|----------|-------------------------|----------------|---------------|----------|
| Baseline    | 10    | 949      | 193.28                  | 16055          | 3.9           | 0        |
| Stress      | 100   | 1574     | 77.51                   | 975            | 15.9          | 0        |
| Spike       | 100   | 1046     | 84.79                   | 711            | 30.6          | 0        |

All tests ran successfully without any failed requests.

---

## What I Observed

- During the **baseline test**, one request had a very high response time (over 16 seconds), which I suspect was due to the model being loaded for the first time or a cold start issue in Cloud Run.
- In both the **stress** and **spike tests**, the response times were more stable and consistently low, which shows the app performs better once it's warmed up.
- Overall, the app scaled well and managed the traffic without errors.

---

## My Key Takeaways

- The application is reliable under both slow and sudden traffic increases.
- Cloud Run auto-scaling worked smoothly after the initial warm-up.
- The average response time stayed below 200 milliseconds, which is acceptable for a real-time prediction service like this.

---

## Recommendations (Based on My Experience)

1. **Preload the Model at Startup**  
   To avoid delays on the first request, I suggest initializing the model when the app starts instead of loading it during the first API call.

2. **Tweak Cloud Run Settings**  
   Setting a minimum number of instances or adjusting concurrency could help reduce cold start delays.

3. **Add Monitoring Tools**  
   I plan to integrate basic monitoring (e.g., Google Cloud Monitoring) to track performance and detect slowdowns in production.

4. **Use Load Testing in Future Updates**  
   I'll consider including light load tests in the CI/CD process to make sure performance remains stable with new changes.

---

## Final Thoughts

I'm happy with how the application performed under different traffic scenarios. The zero failure rate and low response times prove that the deployment is stable. With just a few minor improvements (like reducing the cold start time), the app can be even more efficient and responsive.