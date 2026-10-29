import os
import unittest

os.environ["NOTES_DB"] = ":memory:"
import notes  # noqa: E402
import server  # noqa: E402


class NotesTest(unittest.TestCase):
    def setUp(self):
        self.db = notes.connect()

    def test_owner_sees_only_their_notes(self):
        notes.add_note(self.db, "ana", "mine")
        notes.add_note(self.db, "ben", "his")
        self.assertEqual([n["body"] for n in notes.list_notes(self.db, "ana")], ["mine"])

    def test_cannot_delete_another_users_note(self):
        note_id = notes.add_note(self.db, "ana", "mine")
        self.assertFalse(notes.delete_note(self.db, "ben", note_id))

    def test_limit_caps_the_list(self):
        for i in range(3):
            notes.add_note(self.db, "ana", f"note {i}")
        self.assertEqual(len(notes.list_notes(self.db, "ana", limit=2)), 2)
        with self.assertRaises(ValueError):
            notes.list_notes(self.db, "ana", limit=0)

    def test_rejects_empty_body(self):
        with self.assertRaises(ValueError):
            notes.add_note(self.db, "ana", "")


class AdminTest(unittest.TestCase):
    def test_stats_need_the_token(self):
        os.environ["ADMIN_TOKEN"] = "test-token"
        status, _ = server.route("GET", "/admin/stats", {}, {}, {})
        self.assertEqual(status, 401)
        status, _ = server.route("GET", "/admin/stats", {}, {"Authorization": "Bearer test-token"}, {})
        self.assertEqual(status, 200)


if __name__ == "__main__":
    unittest.main()
