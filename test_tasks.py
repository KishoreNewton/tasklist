import os
import tempfile
import unittest

import tasks


class TasksTest(unittest.TestCase):
    def setUp(self):
        os.chdir(tempfile.mkdtemp())

    def test_add(self):
        tasks.add("Buy milk")
        self.assertEqual(tasks.load(), [{"title": "Buy milk", "done": False}])

    def test_done(self):
        tasks.add("Buy milk")
        tasks.add("Call the bank")
        tasks.done(2)
        self.assertEqual([t["done"] for t in tasks.load()], [False, True])


if __name__ == "__main__":
    unittest.main()
