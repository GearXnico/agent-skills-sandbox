# Notes from the on-call channel, 2026-10-21 (UTC)

- 14:31 Support: a customer says order 9812 was charged twice.
- 14:50 On-call starts looking. The payment provider's status page shows "elevated latency" since 14:00.
- 15:18 Timeout set back to 30 s; deployed as v1.3.1 at 15:25.
- 15:40 No new duplicate charges after this time.
- Finance count the next day: 37 orders charged two or more times, 41,370 CLP refunded in total.
