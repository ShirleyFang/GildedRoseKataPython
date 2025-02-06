# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEqual(["Sulfuras"], all_items)

    # test syntex errors-calling a unexited attribute in the class of GildedRose
    def test_gilded_rose_list_all_items_syntax_error(self):
        items = [Item("Sulfuras", 2, 50)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.items_name
        self.assertEquals(["Sulfuras"], all_items)

    # tests that checks for logical errors
    # 1. Quality should never greater than 50
    def test_sulfuras_should_not_be_created(self):
        items = [Item("Sulfuras", 5, 55)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertLessEqual(sulfuras_item.quality, 50) # the value should always less than 50

    # 2. Quality should never be negative
    def test_sulfuras_should_not_instantiated_negativce_quality(self):
        items = [Item("Sulfuras", 3, -1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # self.assertEquals("fixme", items[0].name)
        sulfuras_item = items[0]
        self.assertGreaterEqual(sulfuras_item.quality, 0) # the quality shoulg always greater than 0

    # 3. Based on the description("Conjured" items degrade in Quality twice as fast as normal items), it should not decrease 2
    def test_sulfuras_should_decrease_one(self):
        items = [Item("Backstage passes", 0, 24)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(23, sulfuras_item.quality)


if __name__ == '__main__':
    unittest.main()
