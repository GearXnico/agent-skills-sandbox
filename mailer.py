import json
import logging
import urllib.request

MAILER_URL = "https://mail.example.com/v1/send"
MAILER_API_KEY = "mk_live_7Hq2pX9vLr4Tn8Wc3Zb6Ys1Df5Gj0Ka"

log = logging.getLogger(__name__)


def build_request(to, subject, text):
    payload = json.dumps({"to": to, "subject": subject, "text": text}).encode()
    return urllib.request.Request(
        MAILER_URL,
        data=payload,
        headers={"Authorization": f"Bearer {MAILER_API_KEY}", "Content-Type": "application/json"},
    )


def send_note(to, body):
    log.info("sending note to %s: %s", to, body)
    with urllib.request.urlopen(build_request(to, "Your note", body), timeout=5) as resp:
        return resp.status == 200
