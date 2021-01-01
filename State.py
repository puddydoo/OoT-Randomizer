from collections import Counter
import copy

from Item import ItemInfo
from Region import Region, TimeOfDay



class State(object):

    def __init__(self, parent):
        self.prog_items = Counter()
        self.world = parent
        self.search = None
        self._won = self.won_triforce_hunt if self.world.triforce_hunt else self.won_normal


    ## Ensure that this will always have a value
    @property
    def is_glitched(self):
        return self.world.logic_rules != 'glitchless'


    def copy(self, new_world=None):
        if not new_world:
            new_world = self.world
        new_state = State(new_world)
        new_state.prog_items = copy.copy(self.prog_items)
        return new_state


    def item_name(self, location):
        location = self.world.get_location(location)
        if location.item is None:
            return None
        return location.item.name


    def won(self):
        return self._won()


    def won_triforce_hunt(self):
        return self.has('Triforce Piece', self.world.triforce_count)


    def won_normal(self):
        return self.has('Triforce')


    def has(self, item, count=1):
        return self.prog_items[item] >= count


    def has_any_of(self, items):
        return any(map(self.prog_items.__contains__, items))


    def has_all_of(self, items):
        return all(map(self.prog_items.__contains__, items))


    def count_of(self, items):
        return len(list(filter(self.prog_items.__contains__, items)))


    def item_count(self, item):
        return self.prog_items[item]


    def has_bottle(self, **kwargs):
        # Extra Ruto's Letter are automatically emptied
        return self.has_any_of(ItemInfo.bottles) or self.has('Rutos Letter', 2)


    def has_hearts(self, count):
        # Warning: This only considers items that are marked as advancement items
        return self.heart_count() >= count


    def heart_count(self):
        # Warning: This only considers items that are marked as advancement items
        containers = self.world.starting_hearts
        if self.world.logic_heart_containers:
            containers += self.item_count('Heart Container')
        if self.world.logic_heart_pieces:
            containers += ((self.item_count('Piece of Heart') + self.item_count('Piece of Heart (Treasure Chest Game)')) // 4)
        # Much logic still assumes 3 hearts (the number of hearts required for all checks is not known) so make 3 hearts obtainable
        if containers < 3:
            containers = min(3, (self.world.starting_hearts + self.item_count('Heart Container') + ((self.item_count('Piece of Heart') + self.item_count('Piece of Heart (Treasure Chest Game)')) // 4)))
        return containers

    def has_medallions(self, count):
        return self.count_of(ItemInfo.medallions) >= count


    def has_stones(self, count):
        return self.count_of(ItemInfo.stones) >= count


    def has_dungeon_rewards(self, count):
        return (self.count_of(ItemInfo.medallions) + self.count_of(ItemInfo.stones)) >= count


    def had_night_start(self):
        stod = self.world.starting_tod
        # These are all not between 6:30 and 18:00
        if (stod == 'sunset' or         # 18
            stod == 'evening' or        # 21
            stod == 'midnight' or       # 00
            stod == 'witching-hour'):   # 03
            return True
        else:
            return False


    # Used for fall damage and other situations where damage is unavoidable
    def can_live_dmg(self, damage):
        damage = damage * self.world.damage
        health = self.heart_count()
        return self.world.damage_multiplier != 'ohko' and (damage < health or (damage / 2 < health and self.has('Double Defense')))


    # Use the guarantee_hint rule defined in json.
    def guarantee_hint(self):
        return self.world.parser.parse_rule('guarantee_hint')(self)


    # Be careful using this function. It will not collect any
    # items that may be locked behind the item, only the item itself.
    def collect(self, item):
        if item.advancement:
            self.prog_items[item.name] += 1


    # Be careful using this function. It will not uncollect any
    # items that may be locked behind the item, only the item itself.
    def remove(self, item):
        if self.prog_items[item.name] > 0:
            self.prog_items[item.name] -= 1
            if self.prog_items[item.name] <= 0:
                del self.prog_items[item.name]


    def __getstate__(self):
        return self.__dict__.copy()


    def __setstate__(self, state):
        self.__dict__.update(state)


