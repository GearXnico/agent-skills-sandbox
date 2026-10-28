# worker

Loop:

1. Pop `{order_id}` from the `orders` queue.
2. Charge the order total through the payment provider.
3. Set the order status to `paid` and send the receipt by email.

If any step fails, the job is pushed back to the queue and retried immediately, with no limit.
