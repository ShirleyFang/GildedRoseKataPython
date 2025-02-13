# -*- coding: utf-8 -*-
import unittest


from gilded_rose import SulfurasItem, AgedBried, ConjuredItem, BackstagePassesItem, NormalItem, Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [SulfurasItem("Sulfuras", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(50, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [SulfurasItem("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEqual(items, all_items)

    # test syntax errors-calling a unexited attribute in the class of GildedRose
    def test_gilded_rose_list_all_items_syntax_error1(self):
        items = [SulfurasItem("Sulfuras", 2, 50)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items_name()
        self.assertEqual(["Sulfuras"], all_items)
    
     # test syntex errors-calling a unexited attribute in the class of GildedRose
    def test_gilded_rose_list_all_items_syntax_error(self):
        items = [SulfurasItem("Sulfuras", 2, 50)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.items
        self.assertTrue(
            all(item1.name == item2.name and
                item1.sell_in == item2.sell_in and
                item1.quality == item2.quality
                for item1, item2 in zip([SulfurasItem("Sulfuras", 2, 50)], all_items))
        )


    # tests that checks for logical errors
    # 1. Quality should never greater than 50
    def test_sulfuras_should_not_be_created(self):
        items = [SulfurasItem("Sulfuras", 5, 55)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]

        self.assertLessEqual(sulfuras_item.quality, 50) # the value should always less than 50

    # 2. Quality should never be negative
    def test_sulfuras_should_not_instantiated_negativce_quality(self):
        items = [SulfurasItem("Sulfuras", 3, -1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # self.assertEquals("fixme", items[0].name)
        sulfuras_item = items[0]
        print(sulfuras_item.quality)
        self.assertGreaterEqual(sulfuras_item.quality, 0) # the quality shoulg always greater than 0

    # 3. Based on the description("Conjured" items degrade in Quality twice as fast as normal items), it should not decrease 2
    def test_sulfuras_should_decrease_one(self):
        items = [NormalItem("Backstage passes", 0, 24)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(23, sulfuras_item.quality)


if __name__ == '__main__':
    unittest.main()
