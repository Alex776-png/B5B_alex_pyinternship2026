subscribers = {
    "alice123@example.com",
    "david456@example.com",
    "charlie789@example.com",
    "bob012@example.com"
}

customers = {
    "bob123@example.com",
    "david456@example.com",
    "eve789@example.com",
    "frank012@example.com"
}

subscribers_never_purchased = subscribers - customers
customers_never_subscribed = customers - subscribers

print("Subscribers who never purchased:",subscribers_never_purchased)

print("Customers who never subscribed:",customers_never_subscribed)
