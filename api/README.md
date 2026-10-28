# api

- `GET /products`: lists products.
- `POST /orders`: validates the cart, inserts the order with status `pending` and pushes `{order_id}` to the `orders` queue. Returns `201` with the order.
- `GET /orders/{id}`: returns an order and its status.

No authentication: the order id is the only thing a customer needs to see their order.
