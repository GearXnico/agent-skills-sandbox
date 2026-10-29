import hmac
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

import notes

DB = notes.connect(os.environ.get("NOTES_DB", "notes.db"))


def require_admin(headers):
    token = os.environ.get("ADMIN_TOKEN", "")
    given = headers.get("Authorization", "").removeprefix("Bearer ")
    return bool(token) and hmac.compare_digest(given, token)


def route(method, path, query, headers, body):
    user = headers.get("X-User")
    if method == "GET" and path == "/notes" and user:
        return 200, notes.list_notes(DB, user)
    if method == "POST" and path == "/notes" and user:
        return 201, {"id": notes.add_note(DB, user, body.get("body", ""))}
    if method == "DELETE" and path == "/notes" and user:
        ok = notes.delete_note(DB, user, int(query.get("id", ["0"])[0]))
        return (204, None) if ok else (404, {"error": "not found"})
    if method == "GET" and path == "/admin/stats":
        if not require_admin(headers):
            return 401, {"error": "unauthorized"}
        return 200, {"notes": notes.count_notes(DB)}
    return 404, {"error": "not found"}


class Handler(BaseHTTPRequestHandler):
    def handle_any(self, method):
        url = urlparse(self.path)
        length = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(length) or b"{}")
            status, data = route(method, url.path, parse_qs(url.query), self.headers, body)
        except (ValueError, json.JSONDecodeError):
            status, data = 400, {"error": "bad request"}
        except Exception:
            status, data = 500, {"error": "internal error"}
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if data is not None:
            self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        self.handle_any("GET")

    def do_POST(self):
        self.handle_any("POST")

    def do_DELETE(self):
        self.handle_any("DELETE")


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8080), Handler).serve_forever()
