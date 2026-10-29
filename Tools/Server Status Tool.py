services = [
    "nginx",
    "postgres",
    "redis",
    "rabbitmq"
]

while True:
    print("=== Service Status Tool ===")
    print("1. Visa alla tjänster")

    choice = int(input("> "))

    if choice == 1:
        for service in services:
            print(f"{service}")
    elif choice == 2:
        print("To be implemented")
    elif choice == 3:
        print("To be implemented")
    else:
        print("To be implemented")
    input()