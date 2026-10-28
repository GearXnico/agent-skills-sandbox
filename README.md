# Orders

Customers place orders on the web app. The API stores them in Postgres and puts a job on a Redis queue; the worker takes the job, charges the card through the payment provider and emails a receipt.

| Service | Does | Talks to |
| --- | --- | --- |
| `web` | Static storefront | `api` |
| `api` | REST API for products and orders | `db`, `redis` |
| `worker` | Charges orders and sends receipts | `redis`, `db`, payment provider, SMTP |
| `db` | Postgres | |
| `redis` | Job queue | |

Run it with `docker compose up`.

Expected load: 50 orders a day today, 5,000 a day after the marketing launch in three months.
