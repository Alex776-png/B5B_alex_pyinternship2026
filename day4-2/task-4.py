def update_status():
    status = "pending"

    def change_status():
        nonlocal status
        status = "completed"

    change_status()

    print("Final status:", status)


update_status()