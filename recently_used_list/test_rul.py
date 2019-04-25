import unittest
from rul import RecentlyUsedList

class RecentlyUsedListTests(unittest.TestCase):
    def setUp(self):
        self.rul = RecentlyUsedList()

    def test_a_new_list_has_length_0(self):
        got = len(self.rul)
        self.assertEqual(got, 0)

    def test_a_list_with_one_element_has_length_1(self):
        self.rul.insert('item')
        got = len(self.rul)
        self.assertEqual(got, 1)

    def test_if_a_list_contains_the_added_element(self):
        self.rul.insert('item')
        got = self.rul[0]
        self.assertEqual(got, item)

    def test_new_item_is_inserted_at_the_beginning(self):
        self.rul.insert('first')
        most_recent_item = 'second'
        self.rul.insert(most_recent_item)
        self.assertEqual(self.rul[0], most_recent_item)
        
    def test_inserting_existing_element_moves_it_to_the_beginning(self):
        duplicate = 'b'
        for item in 'a', duplicate, 'c', duplicate:
            self.rul.insert(item)
        self.assertEqual(len(self.rul), 3)
        self.assertEqual(self.rul[0], duplicate)