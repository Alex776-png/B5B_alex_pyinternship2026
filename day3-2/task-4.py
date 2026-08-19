subscribers = {
    "alice@example.com",
    "bob@example.com",
    "charlie@example.com",
    "david@example.com"
}

customers = {
    "bob@example.com",
    "david@example.com",
    "eve@example.com",
    "frank@example.com"
}

subscribers_never_purchased = subscribers - customers
customers_never_subscribed = customers - subscribers

print("Subscribers who never purchased:",
      subscribers_never_purchased)

print("Customers who never subscribed:",
      customers_never_subscribed)
