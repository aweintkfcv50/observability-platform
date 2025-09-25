from prometheus_client import start_http_server, Counter
import random
import time

API_REQUESTS = Counter('my_api_requests_total', 'Total API requests', ['endpoint'])

if __name__ == '__main__':
    start_http_server(8000)
    print("Exporter started on port 8000")
    
    while True:
        API_REQUESTS.labels(endpoint='/user/register').inc(random.randint(1, 5))
        API_REQUESTS.labels(endpoint='/api/order').inc(random.randint(1, 3))
        time.sleep(10)

