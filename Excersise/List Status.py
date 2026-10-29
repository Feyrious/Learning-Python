services = [
    {"name": "nginx", "status": "running"},
    {"name": "prostgres", "status": "stopped"},
    {"name": "redis", "status": "stopped"},
    {"name": "rabbitmq", "status": "running"},
]

for service in services:
    if service["status"] == "stopped":
        print("Service " + service["name"] + " is Stopped")
