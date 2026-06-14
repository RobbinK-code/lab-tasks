import os
import tempfile
import unittest

import sys
import os

# Ensure project root is importable when running tests directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import task_utils as u
import validation as v


class TaskUtilsTests(unittest.TestCase):
    def test_add_and_list_pending_and_progress(self):
        tasks = []
        u.add_task(tasks, "Task 1", "desc")
        u.add_task(tasks, "Task 2")
        pending = u.list_pending(tasks)
        self.assertEqual(len(pending), 2)
        u.mark_complete(tasks, 0)
        pending = u.list_pending(tasks)
        self.assertEqual(len(pending), 1)
        self.assertEqual(u.progress(tasks), 50)

    def test_validation_helpers(self):
        self.assertTrue(v.is_non_empty_string("a"))
        self.assertFalse(v.is_non_empty_string("  "))
        tasks = [{}, {}]
        self.assertTrue(v.is_valid_index(0, tasks))
        self.assertTrue(v.is_valid_index("1", tasks))
        self.assertFalse(v.is_valid_index(2, tasks))

    def test_persistence_save_and_load(self):
        tasks = []
        u.add_task(tasks, "Persist", "file")
        fd, path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        try:
            u.save_tasks(tasks, path)
            loaded = u.load_tasks(path)
            self.assertEqual(len(loaded), 1)
            self.assertEqual(loaded[0]["title"], "Persist")
        finally:
            os.remove(path)


if __name__ == "__main__":
    unittest.main()
