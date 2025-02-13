# -*- coding: utf-8 -*-

MAX_QUALITY = 50
MIN_QUALITY = 0
TWO = 2
FOUR = 4
ONE = 1


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class SubItem(Item):
    def __init__(self, name, sell_in, quality):
        quality = max(MIN_QUALITY, min(quality, MAX_QUALITY))
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        pass


class NormalItem(SubItem):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def validate_quality(self):
        return self.quality > MIN_QUALITY and self.quality <= MAX_QUALITY

    def update_quality(self):
        if self.sell_in >= MIN_QUALITY and self.quality > ONE:
            self.quality -= ONE
        elif self.sell_in < MIN_QUALITY and self.quality > TWO: 
            self.quality -= TWO
        else:
            self.quality = MIN_QUALITY
        self.sell_in -= ONE


class AgedBried(SubItem):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        self.sell_in -= ONE
        if (self.quality < MAX_QUALITY):
            self.quality += ONE


class SulfurasItem(SubItem):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        self.sell_in -= ONE


class BackstagePassesItem(SubItem):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        FIVE_DAYS = 5
        TEN_DAYS = 10
        THREE = 3

        if self.sell_in == MIN_QUALITY:
            self.quality = MIN_QUALITY
        elif self.sell_in <= FIVE_DAYS:
            self.quality = min(MAX_QUALITY, self.quality + THREE)
        elif self.sell_in <= TEN_DAYS:
            self.quality = min(MAX_QUALITY, self.quality + TWO)

        self.sell_in -= ONE


class ConjuredItem(SubItem):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):

        if self.sell_in >= MIN_QUALITY and self.quality > TWO:
            self.quality -= TWO
        elif self.sell_in < MIN_QUALITY and self.quality > FOUR:
            self.quality -= FOUR
        else:
            self.quality = MIN_QUALITY
        self.sell_in -= ONE


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def get_items_name(self):
        item_names = [item.name for item in self.items]
        return item_names

    def get_items(self):
        return self.items

    def update_quality(self):
        for item in self.items:
            item.update_quality()
