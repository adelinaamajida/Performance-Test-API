# Performance-Test-API
For Soar.inc

*Load Test on Register Case*
From the report: After running test with around 100 users, it can be concluded that API able to handle the request adequately. Hiccup on the graph possibly due to client latency, because it only happens for around 30 seconds.

Settings: 
- Total concurrent users = 100
- Ram up per second = 10

*Stress Test on Login Case*
From the report: At around 650 users, 95 percentile response time is above 1 second. And when it reaches around 750 users, 50 percentile response time is above 1 second which indicates that it's not ideal anymore.

Settings: 
- Total concurrent users = 1000
- Ram up per second = 10

For the BDD on performance test, since I don't have any experience on this and might spend too much time in doing some research, I decided to spend my time efficiently on another task.