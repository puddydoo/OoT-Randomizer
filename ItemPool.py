from collections import namedtuple
import logging
import random
from itertools import chain
from Utils import random_choices
from Item import ItemFactory
from ItemList import item_table
from LocationList import location_groups
from decimal import Decimal, ROUND_HALF_UP


#This file sets the item pools for various modes. Timed modes and triforce hunt are enforced first, and then extra items are specified per mode to fill in the remaining space.
#Some basic items that various modes require are placed here, including pendants and crystals. Medallion requirements for the two relevant entrances are also decided.


alwaysitems = ([
    'Biggoron Sword',
    'Boomerang',
    'Lens of Truth',
    'Megaton Hammer',
    'Iron Boots',
    'Goron Tunic',
    'Zora Tunic',
    'Hover Boots',
    'Mirror Shield',
    'Stone of Agony',
    'Fire Arrows',
    'Ice Arrows',
    'Light Arrows',
    'Dins Fire',
    'Farores Wind',
    'Nayrus Love',
    'Rupee (1)']
    + ['Progressive Hookshot'] * 2
    + ['Deku Shield']
    + ['Hylian Shield']
    + ['Progressive Strength Upgrade'] * 3
    + ['Progressive Scale'] * 2
    + ['Recovery Heart'] * 6
    + ['Bow'] * 3
    + ['Slingshot'] * 3
    + ['Bomb Bag'] * 3
    + ['Bombs (5)'] * 2
    + ['Bombs (10)']
    + ['Bombs (20)']
    + ['Arrows (5)']
    + ['Arrows (10)'] * 5
    + ['Progressive Wallet'] * 2
    + ['Magic Meter'] * 2
    + ['Double Defense']
    + ['Deku Stick Capacity'] * 2
    + ['Deku Nut Capacity'] * 2
    + ['Piece of Heart (Treasure Chest Game)'])


easy_items = ([
    'Biggoron Sword',
    'Kokiri Sword',
    'Boomerang',
    'Lens of Truth',
    'Megaton Hammer',
    'Iron Boots',
    'Goron Tunic',
    'Zora Tunic',
    'Hover Boots',
    'Mirror Shield',
    'Fire Arrows',
    'Light Arrows',
    'Dins Fire',
    'Progressive Hookshot',
    'Progressive Strength Upgrade',
    'Progressive Scale',
    'Progressive Wallet',
    'Magic Meter',
    'Deku Stick Capacity', 
    'Deku Nut Capacity', 
    'Bow', 
    'Slingshot', 
    'Bomb Bag',
    'Double Defense'] +
    ['Heart Container'] * 16 +
    ['Piece of Heart'] * 3)

normal_items = (
    ['Heart Container'] * 8 +
    ['Piece of Heart'] * 35)


item_difficulty_max = {
    'plentiful': {},
    'balanced': {},
    'scarce': {
        'Bombchus': 3,
        'Bombchus (5)': 1,
        'Bombchus (10)': 2,
        'Bombchus (20)': 0,
        'Magic Meter': 1, 
        'Double Defense': 0, 
        'Deku Stick Capacity': 1, 
        'Deku Nut Capacity': 1, 
        'Bow': 2, 
        'Slingshot': 2, 
        'Bomb Bag': 2,
        'Heart Container': 0,
    },
    'minimal': {
        'Bombchus': 1,
        'Bombchus (5)': 1,
        'Bombchus (10)': 0,
        'Bombchus (20)': 0,
        'Nayrus Love': 0,
        'Magic Meter': 1, 
        'Double Defense': 0, 
        'Deku Stick Capacity': 0, 
        'Deku Nut Capacity': 0, 
        'Bow': 1, 
        'Slingshot': 1, 
        'Bomb Bag': 1,
        'Heart Container': 0,
        'Piece of Heart': 0,
    },
}

TriforceCounts = {
    'plentiful': Decimal(2.00),
    'balanced':  Decimal(1.50),
    'scarce':    Decimal(1.25),
    'minimal':   Decimal(1.00),
}

DT_vanilla = (
    ['Recovery Heart'] * 2)

DT_MQ = (
    ['Deku Shield'] * 2 +
    ['Rupees (50)'])

DC_vanilla = (
    ['Rupees (20)'])

DC_MQ = (
    ['Hylian Shield'] +
    ['Rupees (5)'])

JB_MQ = (
    ['Deku Nuts (5)'] * 4 +
    ['Recovery Heart'] +
    ['Deku Shield'] +
    ['Deku Stick (1)'])

FoT_vanilla = (
    ['Recovery Heart'] +
    ['Arrows (10)'] +
    ['Arrows (30)'])

FoT_MQ = (
    ['Arrows (5)'])

FiT_vanilla = (
    ['Rupees (200)'])

FiT_MQ = (
    ['Bombs (20)'] +
    ['Hylian Shield'])

SpT_vanilla = (
    ['Deku Shield'] * 2 +
    ['Recovery Heart'] +
    ['Bombs (20)'])

SpT_MQ = (
    ['Rupees (50)'] * 2 +
    ['Arrows (30)'])

ShT_vanilla = (
    ['Arrows (30)'])

ShT_MQ = (
    ['Arrows (5)'] * 2 +
    ['Rupees (20)'])

BW_vanilla = (
    ['Recovery Heart'] +
    ['Bombs (10)'] +
    ['Rupees (200)'] +
    ['Deku Nuts (5)'] +
    ['Deku Nuts (10)'] +
    ['Deku Shield'] +
    ['Hylian Shield'])

GTG_vanilla = (
    ['Arrows (30)'] * 3 +
    ['Rupees (200)'])

GTG_MQ = (
    ['Rupee (Treasure Chest Game)'] * 2 +
    ['Arrows (10)'] +
    ['Rupee (1)'] +
    ['Rupees (50)'])

GC_vanilla = (
    ['Rupees (5)'] * 3 +
    ['Arrows (30)'])

GC_MQ = (
    ['Arrows (10)'] * 2 +
    ['Bombs (5)'] +
    ['Rupees (20)'] +
    ['Recovery Heart'])


normal_bottles = [
    'Bottle',
    'Bottle with Milk',
    'Bottle with Red Potion',
    'Bottle with Green Potion',
    'Bottle with Blue Potion',
    'Bottle with Fairy',
    'Bottle with Fish',
    'Bottle with Bugs',
    'Bottle with Poe',
    'Bottle with Big Poe',
    'Bottle with Blue Fire']

bottle_count = 4


tokens = [
    'Gold Skulltula Token',
    'Gold Skulltula Token (Kokiri Forest)',
    'Gold Skulltula Token (Lost Woods)',
    'Gold Skulltula Token (Sacred Forest Meadow)',
    'Gold Skulltula Token (Market Guard House)',
    'Gold Skulltula Token (Hyrule Castle Grounds)',
    'Gold Skulltula Token (Grotto)',
    'Gold Skulltula Token (Ganons Castle Grounds)',
    'Gold Skulltula Token (Lon Lon Ranch)',
    'Gold Skulltula Token (Kakariko Village)',
    'Gold Skulltula Token (Graveyard)',
    'Gold Skulltula Token (Death Mountain Trail)',
    'Gold Skulltula Token (Goron City)',
    'Gold Skulltula Token (Death Mountain Crater)',
    'Gold Skulltula Token (Zoras River)',
    'Gold Skulltula Token (Zoras Domain)',
    'Gold Skulltula Token (Zoras Fountain)',
    'Gold Skulltula Token (Lake Hylia)',
    'Gold Skulltula Token (LH Lab)',
    'Gold Skulltula Token (Gerudo Valley)',
    'Gold Skulltula Token (Gerudo Fortress)',
    'Gold Skulltula Token (Haunted Wasteland)',
    'Gold Skulltula Token (Desert Colossus)',
    'Gold Skulltula Token (Deku Tree)',
    'Gold Skulltula Token (Dodongos Cavern)',
    'Gold Skulltula Token (Jabu Jabus Belly)',
    'Gold Skulltula Token (Forest Temple)',
    'Gold Skulltula Token (Fire Temple)',
    'Gold Skulltula Token (Water Temple)',
    'Gold Skulltula Token (Spirit Temple)',
    'Gold Skulltula Token (Shadow Temple)',
    'Gold Skulltula Token (Bottom of the Well)',
    'Gold Skulltula Token (Ice Cavern)']


dungeon_rewards = [
    'Kokiri Emerald',
    'Goron Ruby',
    'Zora Sapphire',
    'Forest Medallion',
    'Fire Medallion',
    'Water Medallion',
    'Shadow Medallion',
    'Spirit Medallion',
    'Light Medallion'
]


normal_rupees = (
    ['Rupees (5)'] * 13 +
    ['Rupees (20)'] * 5 +
    ['Rupees (50)'] * 7 +
    ['Rupees (200)'] * 3)

shopsanity_rupees = (
    ['Rupees (5)'] * 2 +
    ['Rupees (20)'] * 10 +
    ['Rupees (50)'] * 10 +
    ['Rupees (200)'] * 5 +
    ['Progressive Wallet'])


vanilla_shop_items = {
    'KF Shop Item 1': 'Buy Deku Shield',
    'KF Shop Item 2': 'Buy Deku Nut (5)',
    'KF Shop Item 3': 'Buy Deku Nut (10)',
    'KF Shop Item 4': 'Buy Deku Stick (1)',
    'KF Shop Item 5': 'Buy Deku Seeds (30)',
    'KF Shop Item 6': 'Buy Arrows (10)',
    'KF Shop Item 7': 'Buy Arrows (30)',
    'KF Shop Item 8': 'Buy Heart',
    'Kak Potion Shop Item 1': 'Buy Deku Nut (5)',
    'Kak Potion Shop Item 2': 'Buy Fish',
    'Kak Potion Shop Item 3': 'Buy Red Potion [30]',
    'Kak Potion Shop Item 4': 'Buy Green Potion',
    'Kak Potion Shop Item 5': 'Buy Blue Fire',
    'Kak Potion Shop Item 6': 'Buy Bottle Bug',
    'Kak Potion Shop Item 7': 'Buy Poe',
    'Kak Potion Shop Item 8': 'Buy Fairy\'s Spirit',
    'Market Bombchu Shop Item 1': 'Buy Bombchu (5)',
    'Market Bombchu Shop Item 2': 'Buy Bombchu (10)',
    'Market Bombchu Shop Item 3': 'Buy Bombchu (10)',
    'Market Bombchu Shop Item 4': 'Buy Bombchu (10)',
    'Market Bombchu Shop Item 5': 'Buy Bombchu (20)',
    'Market Bombchu Shop Item 6': 'Buy Bombchu (20)',
    'Market Bombchu Shop Item 7': 'Buy Bombchu (20)',
    'Market Bombchu Shop Item 8': 'Buy Bombchu (20)',
    'Market Potion Shop Item 1': 'Buy Green Potion',
    'Market Potion Shop Item 2': 'Buy Blue Fire',
    'Market Potion Shop Item 3': 'Buy Red Potion [30]',
    'Market Potion Shop Item 4': 'Buy Fairy\'s Spirit',
    'Market Potion Shop Item 5': 'Buy Deku Nut (5)',
    'Market Potion Shop Item 6': 'Buy Bottle Bug',
    'Market Potion Shop Item 7': 'Buy Poe',
    'Market Potion Shop Item 8': 'Buy Fish',
    'Market Bazaar Item 1': 'Buy Hylian Shield',
    'Market Bazaar Item 2': 'Buy Bombs (5) [35]',
    'Market Bazaar Item 3': 'Buy Deku Nut (5)',
    'Market Bazaar Item 4': 'Buy Heart',
    'Market Bazaar Item 5': 'Buy Arrows (10)',
    'Market Bazaar Item 6': 'Buy Arrows (50)',
    'Market Bazaar Item 7': 'Buy Deku Stick (1)',
    'Market Bazaar Item 8': 'Buy Arrows (30)',
    'Kak Bazaar Item 1': 'Buy Hylian Shield',
    'Kak Bazaar Item 2': 'Buy Bombs (5) [35]',
    'Kak Bazaar Item 3': 'Buy Deku Nut (5)',
    'Kak Bazaar Item 4': 'Buy Heart',
    'Kak Bazaar Item 5': 'Buy Arrows (10)',
    'Kak Bazaar Item 6': 'Buy Arrows (50)',
    'Kak Bazaar Item 7': 'Buy Deku Stick (1)',
    'Kak Bazaar Item 8': 'Buy Arrows (30)',
    'ZD Shop Item 1': 'Buy Zora Tunic',
    'ZD Shop Item 2': 'Buy Arrows (10)',
    'ZD Shop Item 3': 'Buy Heart',
    'ZD Shop Item 4': 'Buy Arrows (30)',
    'ZD Shop Item 5': 'Buy Deku Nut (5)',
    'ZD Shop Item 6': 'Buy Arrows (50)',
    'ZD Shop Item 7': 'Buy Fish',
    'ZD Shop Item 8': 'Buy Red Potion [50]',
    'GC Shop Item 1': 'Buy Bombs (5) [25]',
    'GC Shop Item 2': 'Buy Bombs (10)',
    'GC Shop Item 3': 'Buy Bombs (20)',
    'GC Shop Item 4': 'Buy Bombs (30)',
    'GC Shop Item 5': 'Buy Goron Tunic',
    'GC Shop Item 6': 'Buy Heart',
    'GC Shop Item 7': 'Buy Red Potion [40]',
    'GC Shop Item 8': 'Buy Heart',
}


min_shop_items = (
    ['Buy Deku Shield'] +
    ['Buy Hylian Shield'] +
    ['Buy Goron Tunic'] +
    ['Buy Zora Tunic'] +
    ['Buy Deku Nut (5)'] * 2 + ['Buy Deku Nut (10)'] +
    ['Buy Deku Stick (1)'] * 2 +
    ['Buy Deku Seeds (30)'] +
    ['Buy Arrows (10)'] * 2 + ['Buy Arrows (30)'] + ['Buy Arrows (50)'] +
    ['Buy Bombchu (5)'] + ['Buy Bombchu (10)'] * 2 + ['Buy Bombchu (20)'] +
    ['Buy Bombs (5) [25]'] + ['Buy Bombs (5) [35]'] + ['Buy Bombs (10)'] + ['Buy Bombs (20)'] +
    ['Buy Green Potion'] +
    ['Buy Red Potion [30]'] +
    ['Buy Blue Fire'] +
    ['Buy Fairy\'s Spirit'] +
    ['Buy Bottle Bug'] +
    ['Buy Fish'])


vanilla_deku_scrubs = {
    'ZR Deku Scrub Grotto Rear': 'Buy Red Potion [30]',
    'ZR Deku Scrub Grotto Front': 'Buy Green Potion',
    'SFM Deku Scrub Grotto Rear': 'Buy Red Potion [30]',
    'SFM Deku Scrub Grotto Front': 'Buy Green Potion',
    'LH Deku Scrub Grotto Left': 'Buy Deku Nut (5)',
    'LH Deku Scrub Grotto Right': 'Buy Bombs (5) [35]',
    'LH Deku Scrub Grotto Center': 'Buy Arrows (30)',
    'GV Deku Scrub Grotto Rear': 'Buy Red Potion [30]',
    'GV Deku Scrub Grotto Front': 'Buy Green Potion',
    'LW Deku Scrub Near Deku Theater Right': 'Buy Deku Nut (5)',
    'LW Deku Scrub Near Deku Theater Left': 'Buy Deku Stick (1)',
    'LW Deku Scrub Grotto Rear': 'Buy Arrows (30)',
    'Colossus Deku Scrub Grotto Rear': 'Buy Red Potion [30]',
    'Colossus Deku Scrub Grotto Front': 'Buy Green Potion',
    'DMC Deku Scrub': 'Buy Bombs (5) [35]',
    'DMC Deku Scrub Grotto Left': 'Buy Deku Nut (5)',
    'DMC Deku Scrub Grotto Right': 'Buy Bombs (5) [35]',
    'DMC Deku Scrub Grotto Center': 'Buy Arrows (30)',
    'GC Deku Scrub Grotto Left': 'Buy Deku Nut (5)',
    'GC Deku Scrub Grotto Right': 'Buy Bombs (5) [35]',
    'GC Deku Scrub Grotto Center': 'Buy Arrows (30)',
    'LLR Deku Scrub Grotto Left': 'Buy Deku Nut (5)',
    'LLR Deku Scrub Grotto Right': 'Buy Bombs (5) [35]',
    'LLR Deku Scrub Grotto Center': 'Buy Arrows (30)',
}


deku_scrubs_items = (
    ['Deku Nuts (5)'] * 5 +
    ['Deku Stick (1)'] +
    ['Bombs (5)'] * 5 +
    ['Recovery Heart'] * 4 +
    ['Rupees (5)'] * 4) # ['Green Potion']


songlist = [
    'Zeldas Lullaby',
    'Eponas Song',
    'Suns Song',
    'Sarias Song',
    'Song of Time',
    'Song of Storms',
    'Minuet of Forest',
    'Prelude of Light',
    'Bolero of Fire',
    'Serenade of Water',
    'Nocturne of Shadow',
    'Requiem of Spirit']

tradeitems = (
    'Pocket Egg',
    'Pocket Cucco',
    'Cojiro',
    'Odd Mushroom',
    'Poachers Saw',
    'Broken Sword',
    'Prescription',
    'Eyeball Frog',
    'Eyedrops',
    'Claim Check')

tradeitemoptions = (
    'pocket_egg',
    'pocket_cucco',
    'cojiro',
    'odd_mushroom',
    'poachers_saw',
    'broken_sword',
    'prescription',
    'eyeball_frog',
    'eyedrops',
    'claim_check')


fixedlocations = {
    'Ganon': 'Triforce',
    'Pierre': 'Scarecrow Song',
    'Deliver Rutos Letter': 'Deliver Letter',
    'Master Sword Pedestal': 'Time Travel',
    'Market Bombchu Bowling Bombchus': 'Bombchu Drop',
}

droplocations = {
    'Deku Baba Sticks': 'Deku Stick Drop',
    'Deku Baba Nuts': 'Deku Nut Drop',
    'Stick Pot': 'Deku Stick Drop',
    'Nut Pot': 'Deku Nut Drop',
    'Nut Crate': 'Deku Nut Drop',
    'Blue Fire': 'Blue Fire',
    'Lone Fish': 'Fish',
    'Fish Group': 'Fish',
    'Bug Rock': 'Bugs',
    'Bug Shrub': 'Bugs',
    'Wandering Bugs': 'Bugs',
    'Fairy Pot': 'Fairy',
    'Free Fairies': 'Fairy',
    'Wall Fairy': 'Fairy',
    'Butterfly Fairy': 'Fairy',
    'Gossip Stone Fairy': 'Fairy',
    'Bean Plant Fairy': 'Fairy',
    'Fairy Pond': 'Fairy',
    'Big Poe Kill': 'Big Poe',
}

vanillaBK = {
    'Fire Temple Boss Key Chest': 'Boss Key (Fire Temple)',
    'Shadow Temple Boss Key Chest': 'Boss Key (Shadow Temple)',
    'Spirit Temple Boss Key Chest': 'Boss Key (Spirit Temple)',
    'Water Temple Boss Key Chest': 'Boss Key (Water Temple)',
    'Forest Temple Boss Key Chest': 'Boss Key (Forest Temple)',

    'Fire Temple MQ Boss Key Chest': 'Boss Key (Fire Temple)',
    'Shadow Temple MQ Boss Key Chest': 'Boss Key (Shadow Temple)',
    'Spirit Temple MQ Boss Key Chest': 'Boss Key (Spirit Temple)',
    'Water Temple MQ Boss Key Chest': 'Boss Key (Water Temple)',
    'Forest Temple MQ Boss Key Chest': 'Boss Key (Forest Temple)',    
}

vanillaMC = {
    'Bottom of the Well Compass Chest': 'Compass (Bottom of the Well)',
    'Deku Tree Compass Chest': 'Compass (Deku Tree)',
    'Dodongos Cavern Compass Chest': 'Compass (Dodongos Cavern)',
    'Fire Temple Compass Chest': 'Compass (Fire Temple)',
    'Forest Temple Blue Poe Chest': 'Compass (Forest Temple)',
    'Ice Cavern Compass Chest': 'Compass (Ice Cavern)',
    'Jabu Jabus Belly Compass Chest': 'Compass (Jabu Jabus Belly)',
    'Shadow Temple Compass Chest': 'Compass (Shadow Temple)',
    'Spirit Temple Compass Chest': 'Compass (Spirit Temple)',
    'Water Temple Compass Chest': 'Compass (Water Temple)',

    'Bottom of the Well Map Chest': 'Map (Bottom of the Well)',
    'Deku Tree Map Chest': 'Map (Deku Tree)',
    'Dodongos Cavern Map Chest': 'Map (Dodongos Cavern)',
    'Fire Temple Map Chest': 'Map (Fire Temple)',
    'Forest Temple Map Chest': 'Map (Forest Temple)',
    'Ice Cavern Map Chest': 'Map (Ice Cavern)',
    'Jabu Jabus Belly Map Chest': 'Map (Jabu Jabus Belly)',
    'Shadow Temple Map Chest': 'Map (Shadow Temple)',
    'Spirit Temple Map Chest': 'Map (Spirit Temple)',
    'Water Temple Map Chest': 'Map (Water Temple)',

    'Bottom of the Well MQ Compass Chest': 'Compass (Bottom of the Well)',
    'Deku Tree MQ Compass Chest': 'Compass (Deku Tree)',
    'Dodongos Cavern MQ Compass Chest': 'Compass (Dodongos Cavern)',
    'Fire Temple MQ Compass Chest': 'Compass (Fire Temple)',
    'Forest Temple MQ Compass Chest': 'Compass (Forest Temple)',
    'Ice Cavern MQ Compass Chest': 'Compass (Ice Cavern)',
    'Jabu Jabus Belly MQ Compass Chest': 'Compass (Jabu Jabus Belly)',
    'Shadow Temple MQ Compass Chest': 'Compass (Shadow Temple)',
    'Spirit Temple MQ Compass Chest': 'Compass (Spirit Temple)',
    'Water Temple MQ Compass Chest': 'Compass (Water Temple)',

    'Bottom of the Well MQ Map Chest': 'Map (Bottom of the Well)',
    'Deku Tree MQ Map Chest': 'Map (Deku Tree)',
    'Dodongos Cavern MQ Map Chest': 'Map (Dodongos Cavern)',
    'Fire Temple MQ Map Chest': 'Map (Fire Temple)',
    'Forest Temple MQ Map Chest': 'Map (Forest Temple)',
    'Ice Cavern MQ Map Chest': 'Map (Ice Cavern)',
    'Jabu Jabus Belly MQ Map Chest': 'Map (Jabu Jabus Belly)',
    'Shadow Temple MQ Map Chest': 'Map (Shadow Temple)',
    'Spirit Temple MQ Map Chest': 'Map (Spirit Temple)',
    'Water Temple MQ Map Chest': 'Map (Water Temple)',
}

vanillaSK = {
    'Bottom of the Well Front Left Fake Wall Chest': 'Small Key (Bottom of the Well)',
    'Bottom of the Well Right Bottom Fake Wall Chest': 'Small Key (Bottom of the Well)',
    'Bottom of the Well Freestanding Key': 'Small Key (Bottom of the Well)',
    'Fire Temple Big Lava Room Blocked Door Chest': 'Small Key (Fire Temple)',
    'Fire Temple Big Lava Room Lower Open Door Chest': 'Small Key (Fire Temple)',
    'Fire Temple Boulder Maze Shortcut Chest': 'Small Key (Fire Temple)',
    'Fire Temple Boulder Maze Lower Chest': 'Small Key (Fire Temple)',
    'Fire Temple Boulder Maze Side Room Chest': 'Small Key (Fire Temple)',
    'Fire Temple Boulder Maze Upper Chest': 'Small Key (Fire Temple)',
    'Fire Temple Near Boss Chest': 'Small Key (Fire Temple)',
    'Fire Temple Highest Goron Chest': 'Small Key (Fire Temple)',
    'Forest Temple First Stalfos Chest': 'Small Key (Forest Temple)',
    'Forest Temple First Room Chest': 'Small Key (Forest Temple)',
    'Forest Temple Floormaster Chest': 'Small Key (Forest Temple)',
    'Forest Temple Red Poe Chest': 'Small Key (Forest Temple)',
    'Forest Temple Well Chest': 'Small Key (Forest Temple)',
    'Ganons Castle Light Trial Invisible Enemies Chest': 'Small Key (Ganons Castle)',
    'Ganons Castle Light Trial Lullaby Chest': 'Small Key (Ganons Castle)',
    'Gerudo Training Grounds Beamos Chest': 'Small Key (Gerudo Training Grounds)',
    'Gerudo Training Grounds Eye Statue Chest': 'Small Key (Gerudo Training Grounds)',
    'Gerudo Training Grounds Hammer Room Switch Chest': 'Small Key (Gerudo Training Grounds)',
    'Gerudo Training Grounds Heavy Block Third Chest': 'Small Key (Gerudo Training Grounds)',
    'Gerudo Training Grounds Hidden Ceiling Chest': 'Small Key (Gerudo Training Grounds)',
    'Gerudo Training Grounds Near Scarecrow Chest': 'Small Key (Gerudo Training Grounds)',
    'Gerudo Training Grounds Stalfos Chest': 'Small Key (Gerudo Training Grounds)',
    'Gerudo Training Grounds Underwater Silver Rupee Chest': 'Small Key (Gerudo Training Grounds)',
    'Gerudo Training Grounds Freestanding Key': 'Small Key (Gerudo Training Grounds)',
    'Shadow Temple After Wind Hidden Chest': 'Small Key (Shadow Temple)',
    'Shadow Temple Early Silver Rupee Chest': 'Small Key (Shadow Temple)',
    'Shadow Temple Falling Spikes Switch Chest': 'Small Key (Shadow Temple)',
    'Shadow Temple Invisible Floormaster Chest': 'Small Key (Shadow Temple)',
    'Shadow Temple Freestanding Key': 'Small Key (Shadow Temple)',
    'Spirit Temple Child Early Torches Chest': 'Small Key (Spirit Temple)',
    'Spirit Temple Early Adult Right Chest': 'Small Key (Spirit Temple)',
    'Spirit Temple Near Four Armos Chest': 'Small Key (Spirit Temple)',
    'Spirit Temple Statue Room Hand Chest': 'Small Key (Spirit Temple)',
    'Spirit Temple Sun Block Room Chest': 'Small Key (Spirit Temple)',
    'Water Temple Central Bow Target Chest': 'Small Key (Water Temple)',
    'Water Temple Central Pillar Chest': 'Small Key (Water Temple)',
    'Water Temple Cracked Wall Chest': 'Small Key (Water Temple)',
    'Water Temple Dragon Chest': 'Small Key (Water Temple)',
    'Water Temple River Chest': 'Small Key (Water Temple)',
    'Water Temple Torches Chest': 'Small Key (Water Temple)',

    'Bottom of the Well MQ Dead Hand Freestanding Key': 'Small Key (Bottom of the Well)',
    'Bottom of the Well MQ East Inner Room Freestanding Key': 'Small Key (Bottom of the Well)',
    'Fire Temple MQ Big Lava Room Blocked Door Chest': 'Small Key (Fire Temple)',
    'Fire Temple MQ Near Boss Chest': 'Small Key (Fire Temple)',
    'Fire Temple MQ Lizalfos Maze Side Room Chest': 'Small Key (Fire Temple)',
    'Fire Temple MQ Chest On Fire': 'Small Key (Fire Temple)',
    'Fire Temple MQ Freestanding Key': 'Small Key (Fire Temple)',
    'Forest Temple MQ Wolfos Chest': 'Small Key (Forest Temple)',
    'Forest Temple MQ First Room Chest': 'Small Key (Forest Temple)',
    'Forest Temple MQ Raised Island Courtyard Lower Chest': 'Small Key (Forest Temple)',
    'Forest Temple MQ Raised Island Courtyard Upper Chest': 'Small Key (Forest Temple)',
    'Forest Temple MQ Redead Chest': 'Small Key (Forest Temple)',
    'Forest Temple MQ Well Chest': 'Small Key (Forest Temple)',
    'Ganons Castle MQ Shadow Trial Eye Switch Chest': 'Small Key (Ganons Castle)',
    'Ganons Castle MQ Spirit Trial Sun Back Left Chest': 'Small Key (Ganons Castle)',
    'Ganons Castle MQ Forest Trial Freestanding Key': 'Small Key (Ganons Castle)',
    'Gerudo Training Grounds MQ Dinolfos Chest': 'Small Key (Gerudo Training Grounds)',
    'Gerudo Training Grounds MQ Flame Circle Chest': 'Small Key (Gerudo Training Grounds)',
    'Gerudo Training Grounds MQ Underwater Silver Rupee Chest': 'Small Key (Gerudo Training Grounds)',
    'Shadow Temple MQ Falling Spikes Switch Chest': 'Small Key (Shadow Temple)',
    'Shadow Temple MQ Invisible Blades Invisible Chest': 'Small Key (Shadow Temple)',
    'Shadow Temple MQ Early Gibdos Chest': 'Small Key (Shadow Temple)',
    'Shadow Temple MQ Near Ship Invisible Chest': 'Small Key (Shadow Temple)',
    'Shadow Temple MQ Wind Hint Chest': 'Small Key (Shadow Temple)',
    'Shadow Temple MQ Freestanding Key': 'Small Key (Shadow Temple)',
    'Spirit Temple MQ Child Hammer Switch Chest': 'Small Key (Spirit Temple)',
    'Spirit Temple MQ Child Climb South Chest': 'Small Key (Spirit Temple)',
    'Spirit Temple MQ Map Room Enemy Chest': 'Small Key (Spirit Temple)',
    'Spirit Temple MQ Entrance Back Left Chest': 'Small Key (Spirit Temple)',
    'Spirit Temple MQ Entrance Front Right Chest': 'Small Key (Spirit Temple)',
    'Spirit Temple MQ Mirror Puzzle Invisible Chest': 'Small Key (Spirit Temple)',
    'Spirit Temple MQ Silver Block Hallway Chest': 'Small Key (Spirit Temple)',
    'Water Temple MQ Central Pillar Chest': 'Small Key (Water Temple)',
    'Water Temple MQ Freestanding Key': 'Small Key (Water Temple)',    
}

vanillaoverworldGS = {
    'KF GS Know It All House': 'Gold Skulltula Token (Kokiri Forest)',
    'KF GS Bean Patch': 'Gold Skulltula Token (Kokiri Forest)',
    'KF GS House of Twins': 'Gold Skulltula Token (Kokiri Forest)',
    'LW GS Bean Patch Near Bridge': 'Gold Skulltula Token (Lost Woods)',
    'LW GS Bean Patch Near Theater': 'Gold Skulltula Token (Lost Woods)',
    'LW GS Above Theater': 'Gold Skulltula Token (Lost Woods)',
    'SFM GS': 'Gold Skulltula Token (Sacred Forest Meadow)',
    'HF GS Near Kak Grotto': 'Gold Skulltula Token (Grotto)',
    'HF GS Cow Grotto': 'Gold Skulltula Token (Grotto)',
    'Market GS Guard House': 'Gold Skulltula Token (Market Guard House)',
    'HC GS Tree': 'Gold Skulltula Token (Hyrule Castle Grounds)',
    'HC GS Storms Grotto': 'Gold Skulltula Token (Grotto)',
    'OGC GS': 'Gold Skulltula Token (Ganons Castle Grounds)',
    'LLR GS Tree': 'Gold Skulltula Token (Lon Lon Ranch)',
    'LLR GS Rain Shed': 'Gold Skulltula Token (Lon Lon Ranch)',
    'LLR GS House Window': 'Gold Skulltula Token (Lon Lon Ranch)',
    'LLR GS Back Wall': 'Gold Skulltula Token (Lon Lon Ranch)',
    'Kak GS House Under Construction': 'Gold Skulltula Token (Kakariko Village)',
    'Kak GS Skulltula House': 'Gold Skulltula Token (Kakariko Village)',
    'Kak GS Guards House': 'Gold Skulltula Token (Kakariko Village)',
    'Kak GS Tree': 'Gold Skulltula Token (Kakariko Village)',
    'Kak GS Watchtower': 'Gold Skulltula Token (Kakariko Village)',
    'Kak GS Above Impas House': 'Gold Skulltula Token (Kakariko Village)',
    'Graveyard GS Wall': 'Gold Skulltula Token (Graveyard)',
    'Graveyard GS Bean Patch': 'Gold Skulltula Token (Graveyard)',
    'DMT GS Bean Patch': 'Gold Skulltula Token (Death Mountain Trail)',
    'DMT GS Near Kak': 'Gold Skulltula Token (Death Mountain Trail)',
    'DMT GS Falling Rocks Path': 'Gold Skulltula Token (Death Mountain Trail)',
    'DMT GS Above Dodongos Cavern': 'Gold Skulltula Token (Death Mountain Trail)',
    'GC GS Boulder Maze': 'Gold Skulltula Token (Goron City)',
    'GC GS Center Platform': 'Gold Skulltula Token (Goron City)',
    'DMC GS Crate': 'Gold Skulltula Token (Death Mountain Crater)',
    'DMC GS Bean Patch': 'Gold Skulltula Token (Death Mountain Crater)',
    'ZR GS Ladder': 'Gold Skulltula Token (Zoras River)',
    'ZR GS Tree': 'Gold Skulltula Token (Zoras River)',
    'ZR GS Near Raised Grottos': 'Gold Skulltula Token (Zoras River)',
    'ZR GS Above Bridge': 'Gold Skulltula Token (Zoras River)',
    'ZD GS Frozen Waterfall': 'Gold Skulltula Token (Zoras Domain)',
    'ZF GS Tree': 'Gold Skulltula Token (Zoras Fountain)',
    'ZF GS Above the Log': 'Gold Skulltula Token (Zoras Fountain)',
    'ZF GS Hidden Cave': 'Gold Skulltula Token (Zoras Fountain)',
    'LH GS Bean Patch': 'Gold Skulltula Token (Lake Hylia)',
    'LH GS Lab Wall': 'Gold Skulltula Token (Lake Hylia)',
    'LH GS Small Island': 'Gold Skulltula Token (Lake Hylia)',
    'LH GS Tree': 'Gold Skulltula Token (Lake Hylia)',
    'LH GS Lab Crate': 'Gold Skulltula Token (LH Lab)',
    'GV GS Small Bridge': 'Gold Skulltula Token (Gerudo Valley)',
    'GV GS Bean Patch': 'Gold Skulltula Token (Gerudo Valley)',
    'GV GS Behind Tent': 'Gold Skulltula Token (Gerudo Valley)',
    'GV GS Pillar': 'Gold Skulltula Token (Gerudo Valley)',
    'GF GS Archery Range': 'Gold Skulltula Token (Gerudo Fortress)',
    'GF GS Top Floor': 'Gold Skulltula Token (Gerudo Fortress)',
    'Wasteland GS': 'Gold Skulltula Token (Haunted Wasteland)',
    'Colossus GS Bean Patch': 'Gold Skulltula Token (Desert Colossus)',
    'Colossus GS Tree': 'Gold Skulltula Token (Desert Colossus)',
    'Colossus GS Hill': 'Gold Skulltula Token (Desert Colossus)',
}

vanilladungeonGS = {
    'Deku Tree GS Compass Room': 'Gold Skulltula Token (Deku Tree)',
    'Deku Tree GS Basement Vines': 'Gold Skulltula Token (Deku Tree)',
    'Deku Tree GS Basement Gate': 'Gold Skulltula Token (Deku Tree)',
    'Deku Tree GS Basement Back Room': 'Gold Skulltula Token (Deku Tree)',
    'Dodongos Cavern GS Side Room Near Lower Lizalfos': 'Gold Skulltula Token (Dodongos Cavern)',
    'Dodongos Cavern GS Vines Above Stairs': 'Gold Skulltula Token (Dodongos Cavern)',
    'Dodongos Cavern GS Back Room': 'Gold Skulltula Token (Dodongos Cavern)',
    'Dodongos Cavern GS Alcove Above Stairs': 'Gold Skulltula Token (Dodongos Cavern)',
    'Dodongos Cavern GS Scarecrow': 'Gold Skulltula Token (Dodongos Cavern)',
    'Jabu Jabus Belly GS Water Switch Room': 'Gold Skulltula Token (Jabu Jabus Belly)',
    'Jabu Jabus Belly GS Lobby Basement Lower': 'Gold Skulltula Token (Jabu Jabus Belly)',
    'Jabu Jabus Belly GS Lobby Basement Upper': 'Gold Skulltula Token (Jabu Jabus Belly)',
    'Jabu Jabus Belly GS Near Boss': 'Gold Skulltula Token (Jabu Jabus Belly)',
    'Forest Temple GS First Room': 'Gold Skulltula Token (Forest Temple)',
    'Forest Temple GS Lobby': 'Gold Skulltula Token (Forest Temple)',
    'Forest Temple GS Raised Island Courtyard': 'Gold Skulltula Token (Forest Temple)',
    'Forest Temple GS Level Island Courtyard': 'Gold Skulltula Token (Forest Temple)',
    'Forest Temple GS Basement': 'Gold Skulltula Token (Forest Temple)',
    'Fire Temple GS Song of Time Room': 'Gold Skulltula Token (Fire Temple)',
    'Fire Temple GS Boulder Maze': 'Gold Skulltula Token (Fire Temple)',
    'Fire Temple GS Scarecrow Climb': 'Gold Skulltula Token (Fire Temple)',
    'Fire Temple GS Scarecrow Top': 'Gold Skulltula Token (Fire Temple)',
    'Fire Temple GS Boss Key Loop': 'Gold Skulltula Token (Fire Temple)',
    'Water Temple GS Behind Gate': 'Gold Skulltula Token (Water Temple)',
    'Water Temple GS River': 'Gold Skulltula Token (Water Temple)',
    'Water Temple GS Falling Platform Room': 'Gold Skulltula Token (Water Temple)',
    'Water Temple GS Central Pillar': 'Gold Skulltula Token (Water Temple)',
    'Water Temple GS Near Boss Key Chest': 'Gold Skulltula Token (Water Temple)',
    'Spirit Temple GS Metal Fence': 'Gold Skulltula Token (Spirit Temple)',
    'Spirit Temple GS Sun on Floor Room': 'Gold Skulltula Token (Spirit Temple)',
    'Spirit Temple GS Hall After Sun Block Room': 'Gold Skulltula Token (Spirit Temple)',
    'Spirit Temple GS Boulder Room': 'Gold Skulltula Token (Spirit Temple)',
    'Spirit Temple GS Lobby': 'Gold Skulltula Token (Spirit Temple)',
    'Shadow Temple GS Like Like Room': 'Gold Skulltula Token (Shadow Temple)',
    'Shadow Temple GS Falling Spikes Room': 'Gold Skulltula Token (Shadow Temple)',
    'Shadow Temple GS Single Giant Pot': 'Gold Skulltula Token (Shadow Temple)',
    'Shadow Temple GS Near Ship': 'Gold Skulltula Token (Shadow Temple)',
    'Shadow Temple GS Triple Giant Pot': 'Gold Skulltula Token (Shadow Temple)',
    'Bottom of the Well GS West Inner Room': 'Gold Skulltula Token (Bottom of the Well)',
    'Bottom of the Well GS East Inner Room': 'Gold Skulltula Token (Bottom of the Well)',
    'Bottom of the Well GS Like Like Cage': 'Gold Skulltula Token (Bottom of the Well)',
    'Ice Cavern GS Spinning Scythe Room': 'Gold Skulltula Token (Ice Cavern)',
    'Ice Cavern GS Heart Piece Room': 'Gold Skulltula Token (Ice Cavern)',
    'Ice Cavern GS Push Block Room': 'Gold Skulltula Token (Ice Cavern)',
    
    'Deku Tree MQ GS Lobby': 'Gold Skulltula Token (Deku Tree)',
    'Deku Tree MQ GS Compass Room': 'Gold Skulltula Token (Deku Tree)',
    'Deku Tree MQ GS Basement Graves Room': 'Gold Skulltula Token (Deku Tree)',
    'Deku Tree MQ GS Basement Back Room': 'Gold Skulltula Token (Deku Tree)',
    'Dodongos Cavern MQ GS Scrub Room': 'Gold Skulltula Token (Dodongos Cavern)',
    'Dodongos Cavern MQ GS Song of Time Block Room': 'Gold Skulltula Token (Dodongos Cavern)',
    'Dodongos Cavern MQ GS Lizalfos Room': 'Gold Skulltula Token (Dodongos Cavern)',
    'Dodongos Cavern MQ GS Larvae Room': 'Gold Skulltula Token (Dodongos Cavern)',
    'Dodongos Cavern MQ GS Back Area': 'Gold Skulltula Token (Dodongos Cavern)',
    'Jabu Jabus Belly MQ GS Tailpasaran Room': 'Gold Skulltula Token (Jabu Jabus Belly)',
    'Jabu Jabus Belly MQ GS Invisible Enemies Room': 'Gold Skulltula Token (Jabu Jabus Belly)',
    'Jabu Jabus Belly MQ GS Boomerang Chest Room': 'Gold Skulltula Token (Jabu Jabus Belly)',
    'Jabu Jabus Belly MQ GS Near Boss': 'Gold Skulltula Token (Jabu Jabus Belly)',
    'Forest Temple MQ GS First Hallway': 'Gold Skulltula Token (Forest Temple)',
    'Forest Temple MQ GS Block Push Room': 'Gold Skulltula Token (Forest Temple)',
    'Forest Temple MQ GS Raised Island Courtyard': 'Gold Skulltula Token (Forest Temple)',
    'Forest Temple MQ GS Level Island Courtyard': 'Gold Skulltula Token (Forest Temple)',
    'Forest Temple MQ GS Well': 'Gold Skulltula Token (Forest Temple)',
    'Fire Temple MQ GS Above Fire Wall Maze': 'Gold Skulltula Token (Fire Temple)',
    'Fire Temple MQ GS Fire Wall Maze Center': 'Gold Skulltula Token (Fire Temple)',
    'Fire Temple MQ GS Big Lava Room Open Door': 'Gold Skulltula Token (Fire Temple)',
    'Fire Temple MQ GS Fire Wall Maze Side Room': 'Gold Skulltula Token (Fire Temple)',
    'Fire Temple MQ GS Skull On Fire': 'Gold Skulltula Token (Fire Temple)',
    'Water Temple MQ GS Before Upper Water Switch': 'Gold Skulltula Token (Water Temple)',
    'Water Temple MQ GS Freestanding Key Area': 'Gold Skulltula Token (Water Temple)',
    'Water Temple MQ GS Lizalfos Hallway': 'Gold Skulltula Token (Water Temple)',
    'Water Temple MQ GS River': 'Gold Skulltula Token (Water Temple)',
    'Water Temple MQ GS Triple Wall Torch': 'Gold Skulltula Token (Water Temple)',
    'Spirit Temple MQ GS Symphony Room': 'Gold Skulltula Token (Spirit Temple)',
    'Spirit Temple MQ GS Leever Room': 'Gold Skulltula Token (Spirit Temple)',
    'Spirit Temple MQ GS Nine Thrones Room West': 'Gold Skulltula Token (Spirit Temple)',
    'Spirit Temple MQ GS Nine Thrones Room North': 'Gold Skulltula Token (Spirit Temple)',
    'Spirit Temple MQ GS Sun Block Room': 'Gold Skulltula Token (Spirit Temple)',
    'Shadow Temple MQ GS Falling Spikes Room': 'Gold Skulltula Token (Shadow Temple)',
    'Shadow Temple MQ GS Wind Hint Room': 'Gold Skulltula Token (Shadow Temple)',
    'Shadow Temple MQ GS After Wind': 'Gold Skulltula Token (Shadow Temple)',
    'Shadow Temple MQ GS After Ship': 'Gold Skulltula Token (Shadow Temple)',
    'Shadow Temple MQ GS Near Boss': 'Gold Skulltula Token (Shadow Temple)',
    'Bottom of the Well MQ GS Basement': 'Gold Skulltula Token (Bottom of the Well)',
    'Bottom of the Well MQ GS Coffin Room': 'Gold Skulltula Token (Bottom of the Well)',
    'Bottom of the Well MQ GS West Inner Room': 'Gold Skulltula Token (Bottom of the Well)',
    'Ice Cavern MQ GS Scarecrow': 'Gold Skulltula Token (Ice Cavern)',
    'Ice Cavern MQ GS Ice Block': 'Gold Skulltula Token (Ice Cavern)',
    'Ice Cavern MQ GS Red Ice': 'Gold Skulltula Token (Ice Cavern)',
}

junk_pool_base = [
    ('Bombs (5)',       8),
    ('Bombs (10)',      2),
    ('Arrows (5)',      8),
    ('Arrows (10)',     2),
    ('Deku Stick (1)',  5),
    ('Deku Nuts (5)',   5),
    ('Deku Seeds (30)', 5),
    ('Rupees (5)',      10),
    ('Rupees (20)',     4),
    ('Rupees (50)',     1),
]

pending_junk_pool = []
junk_pool = []


remove_junk_items = [
    'Bombs (5)',
    'Deku Nuts (5)',
    'Deku Stick (1)',
    'Recovery Heart',
    'Arrows (5)',
    'Arrows (10)',
    'Arrows (30)',
    'Rupees (5)',
    'Rupees (20)',
    'Rupees (50)',
    'Rupees (200)',
    'Deku Nuts (10)',
    'Bombs (10)',
    'Bombs (20)',
    'Deku Seeds (30)',
    'Ice Trap',
]


item_groups = {
    'Junk': remove_junk_items,
    'JunkSong': ('Prelude of Light', 'Serenade of Water'),
    'AdultTrade': tradeitems,
    'Bottle': normal_bottles,
    'Token': tokens,
    'Spell': ('Dins Fire', 'Farores Wind', 'Nayrus Love'),
    'Shield': ('Deku Shield', 'Hylian Shield'),
    'Song': songlist,
    'NonWarpSong': songlist[0:6],
    'WarpSong': songlist[6:],
    'HealthUpgrade': ('Heart Container', 'Piece of Heart'),
    'ProgressItem': [name for (name, data) in item_table.items() if data[0] == 'Item' and data[1]],
    'DungeonReward': dungeon_rewards,

    'ForestFireWater': ('Forest Medallion', 'Fire Medallion', 'Water Medallion'),
    'FireWater': ('Fire Medallion', 'Water Medallion'),
}


def get_junk_item(count=1, pool=None, plando_pool=None):
    if count < 1:
        raise ValueError("get_junk_item argument 'count' must be greater than 0.")

    return_pool = []
    if pending_junk_pool:
        pending_count = min(len(pending_junk_pool), count)
        return_pool = [pending_junk_pool.pop() for _ in range(pending_count)]
        count -= pending_count

    if pool and plando_pool:
        jw_list = [(junk, weight) for (junk, weight) in junk_pool
                   if junk not in plando_pool or pool.count(junk) < plando_pool[junk].count]
        try:
            junk_items, junk_weights = zip(*jw_list)
        except ValueError:
            raise RuntimeError("Not enough junk is available in the item pool to replace removed items.")
    else:
        junk_items, junk_weights = zip(*junk_pool)
    return_pool.extend(random_choices(junk_items, weights=junk_weights, k=count))

    return return_pool


def replace_max_item(items, item, max):
    count = 0
    for i,val in enumerate(items):
        if val == item:
            if count >= max:
                items[i] = get_junk_item()[0]
            count += 1


def generate_itempool(world):
    junk_pool[:] = list(junk_pool_base)
    if world.junk_ice_traps == 'on': 
        junk_pool.append(('Ice Trap', 10))
    elif world.junk_ice_traps in ['mayhem', 'onslaught']:
        junk_pool[:] = [('Ice Trap', 1)]

    fixed_locations = list(filter(lambda loc: loc.name in fixedlocations, world.get_locations()))
    for location in fixed_locations:
        item = fixedlocations[location.name]
        world.push_item(location, ItemFactory(item, world))
        location.locked = True

    drop_locations = list(filter(lambda loc: loc.type == 'Drop', world.get_locations()))
    for drop_location in drop_locations:
        item = droplocations[drop_location.name]
        world.push_item(drop_location, ItemFactory(item, world))
        drop_location.locked = True

    # set up item pool
    (pool, placed_items) = get_pool_core(world)
    world.itempool = ItemFactory(pool, world)
    for (location, item) in placed_items.items():
        world.push_item(location, ItemFactory(item, world))
        world.get_location(location).locked = True

    world.initialize_items()
    world.distribution.set_complete_itempool(world.itempool)


def try_collect_heart_container(world, pool):
    if 'Heart Container' in pool:
        pool.remove('Heart Container')
        pool.extend(get_junk_item())
        world.state.collect(ItemFactory('Heart Container'))
        return True
    return False


def try_collect_pieces_of_heart(world, pool):
    n = pool.count('Piece of Heart') + pool.count('Piece of Heart (Treasure Chest Game)')
    if n >= 4:
        for i in range(4):
            if 'Piece of Heart' in pool:
                pool.remove('Piece of Heart')
                world.state.collect(ItemFactory('Piece of Heart'))
            else:
                pool.remove('Piece of Heart (Treasure Chest Game)')
                world.state.collect(ItemFactory('Piece of Heart (Treasure Chest Game)'))
            pool.extend(get_junk_item())
        return True
    return False


def collect_pieces_of_heart(world, pool):
    success = try_collect_pieces_of_heart(world, pool)
    if not success:
        try_collect_heart_container(world, pool)


def collect_heart_container(world, pool):
    success = try_collect_heart_container(world, pool)
    if not success:
        try_collect_pieces_of_heart(world, pool)


def get_pool_core(world):
    pool = []
    placed_items = {
        'HC Zeldas Letter': 'Zeldas Letter',
    }

    if world.shuffle_kokiri_sword:
        pool.append('Kokiri Sword')
    else:
        placed_items['KF Kokiri Sword Chest'] = 'Kokiri Sword'

    ruto_bottles = 1
    if world.zora_fountain == 'open':
        ruto_bottles = 0
    elif world.item_pool_value == 'plentiful':
        ruto_bottles += 1

    if world.shuffle_weird_egg:
        pool.append('Weird Egg')
    else:
        placed_items['HC Malon Egg'] = 'Weird Egg'

    if world.shuffle_ocarinas:
        pool.extend(['Ocarina'] * 2)
        if world.item_pool_value == 'plentiful':
            pending_junk_pool.append('Ocarina')
    else:
        placed_items['LW Gift from Saria'] = 'Ocarina'
        placed_items['HF Ocarina of Time Item'] = 'Ocarina'

    if world.shuffle_cows:
        pool.extend(get_junk_item(10 if world.dungeon_mq['Jabu Jabus Belly'] else 9))
    else:
        placed_items['LLR Stables Left Cow'] = 'Milk'
        placed_items['LLR Stables Right Cow'] = 'Milk'
        placed_items['LLR Tower Left Cow'] = 'Milk'
        placed_items['LLR Tower Right Cow'] = 'Milk'
        placed_items['KF Links House Cow'] = 'Milk'
        placed_items['Kak Impas House Cow'] = 'Milk'
        placed_items['GV Cow'] = 'Milk'
        placed_items['DMT Cow Grotto Cow'] = 'Milk'
        placed_items['HF Cow Grotto Cow'] = 'Milk'
        if world.dungeon_mq['Jabu Jabus Belly']:
            placed_items['Jabu Jabus Belly MQ Cow'] = 'Milk'

    if world.shuffle_beans:
        if world.distribution.get_starting_item('Magic Bean') < 10:
            pool.append('Magic Bean Pack')
            if world.item_pool_value == 'plentiful':
                pending_junk_pool.append('Magic Bean Pack')
        else:
            pool.extend(get_junk_item())
    else:
        placed_items['ZR Magic Bean Salesman'] = 'Magic Bean'

    if world.shuffle_medigoron_carpet_salesman:
        pool.append('Giants Knife')
    else:
        placed_items['GC Medigoron'] = 'Giants Knife'

    if world.bombchus_in_logic:
        pool.extend(['Bombchus'] * 4)
        if world.dungeon_mq['Jabu Jabus Belly']:
            pool.extend(['Bombchus'])
        if world.dungeon_mq['Spirit Temple']:
            pool.extend(['Bombchus'] * 2)
        if not world.dungeon_mq['Bottom of the Well']:
            pool.extend(['Bombchus'])
        if world.dungeon_mq['Gerudo Training Grounds']:
            pool.extend(['Bombchus'])
        if world.shuffle_medigoron_carpet_salesman:
            pool.append('Bombchus')

    else:
        pool.extend(['Bombchus (5)'] + ['Bombchus (10)'] * 2)
        if world.dungeon_mq['Jabu Jabus Belly']:
                pool.extend(['Bombchus (10)'])
        if world.dungeon_mq['Spirit Temple']:
                pool.extend(['Bombchus (10)'] * 2)
        if not world.dungeon_mq['Bottom of the Well']:
                pool.extend(['Bombchus (10)'])
        if world.dungeon_mq['Gerudo Training Grounds']:
                pool.extend(['Bombchus (10)'])
        if world.dungeon_mq['Ganons Castle']:
            pool.extend(['Bombchus (10)'])
        else:
            pool.extend(['Bombchus (20)'])
        if world.shuffle_medigoron_carpet_salesman:
            pool.append('Bombchus (10)')

    if not world.shuffle_medigoron_carpet_salesman:
        placed_items['Wasteland Bombchu Salesman'] = 'Bombchus (10)'

    pool.extend(['Ice Trap'])
    if not world.dungeon_mq['Gerudo Training Grounds']:
        pool.extend(['Ice Trap'])
    if not world.dungeon_mq['Ganons Castle']:
        pool.extend(['Ice Trap'] * 4)

    if world.gerudo_fortress == 'open':
        placed_items['GF North F1 Carpenter'] = 'Recovery Heart'
        placed_items['GF North F2 Carpenter'] = 'Recovery Heart'
        placed_items['GF South F1 Carpenter'] = 'Recovery Heart'
        placed_items['GF South F2 Carpenter'] = 'Recovery Heart'
    elif world.shuffle_fortresskeys in ['any_dungeon', 'overworld', 'keysanity']:
        if world.gerudo_fortress == 'fast':
            pool.append('Small Key (Gerudo Fortress)')
            placed_items['GF North F2 Carpenter'] = 'Recovery Heart'
            placed_items['GF South F1 Carpenter'] = 'Recovery Heart'
            placed_items['GF South F2 Carpenter'] = 'Recovery Heart'
        else:
            pool.extend(['Small Key (Gerudo Fortress)'] * 4)
        if world.item_pool_value == 'plentiful':
            pending_junk_pool.append('Small Key (Gerudo Fortress)')
    else:
        if world.gerudo_fortress == 'fast':
            placed_items['GF North F1 Carpenter'] = 'Small Key (Gerudo Fortress)'
            placed_items['GF North F2 Carpenter'] = 'Recovery Heart'
            placed_items['GF South F1 Carpenter'] = 'Recovery Heart'
            placed_items['GF South F2 Carpenter'] = 'Recovery Heart'
        else:
            placed_items['GF North F1 Carpenter'] = 'Small Key (Gerudo Fortress)'
            placed_items['GF North F2 Carpenter'] = 'Small Key (Gerudo Fortress)'
            placed_items['GF South F1 Carpenter'] = 'Small Key (Gerudo Fortress)'
            placed_items['GF South F2 Carpenter'] = 'Small Key (Gerudo Fortress)'

    if world.shuffle_gerudo_card and world.gerudo_fortress != 'open':
        pool.append('Gerudo Membership Card')
    elif world.shuffle_gerudo_card:
        pending_junk_pool.append('Gerudo Membership Card')
        placed_items['GF Gerudo Membership Card'] = 'Ice Trap'
    else:
        placed_items['GF Gerudo Membership Card'] = 'Gerudo Membership Card'
    if world.shuffle_gerudo_card and world.item_pool_value == 'plentiful':
        pending_junk_pool.append('Gerudo Membership Card')

    if world.item_pool_value == 'plentiful' and world.shuffle_smallkeys in ['any_dungeon', 'overworld', 'keysanity']:
        pending_junk_pool.append('Small Key (Bottom of the Well)')
        pending_junk_pool.append('Small Key (Forest Temple)')
        pending_junk_pool.append('Small Key (Fire Temple)')
        pending_junk_pool.append('Small Key (Water Temple)')
        pending_junk_pool.append('Small Key (Shadow Temple)')
        pending_junk_pool.append('Small Key (Spirit Temple)')
        pending_junk_pool.append('Small Key (Gerudo Training Grounds)')
        pending_junk_pool.append('Small Key (Ganons Castle)')

    if world.item_pool_value == 'plentiful' and world.shuffle_bosskeys in ['any_dungeon', 'overworld', 'keysanity']:
        pending_junk_pool.append('Boss Key (Forest Temple)')
        pending_junk_pool.append('Boss Key (Fire Temple)')
        pending_junk_pool.append('Boss Key (Water Temple)')
        pending_junk_pool.append('Boss Key (Shadow Temple)')
        pending_junk_pool.append('Boss Key (Spirit Temple)')

    if world.item_pool_value == 'plentiful' and world.shuffle_ganon_bosskey in ['any_dungeon', 'overworld', 'keysanity']:
        pending_junk_pool.append('Boss Key (Ganons Castle)')

    if world.shopsanity == 'off':
        placed_items.update(vanilla_shop_items)
        if world.bombchus_in_logic:
            placed_items['KF Shop Item 8'] = 'Buy Bombchu (5)'
            placed_items['Market Bazaar Item 4'] = 'Buy Bombchu (5)'
            placed_items['Kak Bazaar Item 4'] = 'Buy Bombchu (5)'
        pool.extend(normal_rupees)

    else:
        remain_shop_items = list(vanilla_shop_items.values())
        pool.extend(min_shop_items)
        for item in min_shop_items:
            remain_shop_items.remove(item)

        shop_slots_count = len(remain_shop_items)
        shop_nonitem_count = len(world.shop_prices)
        shop_item_count = shop_slots_count - shop_nonitem_count

        pool.extend(random.sample(remain_shop_items, shop_item_count))
        if shop_nonitem_count:
            pool.extend(get_junk_item(shop_nonitem_count))
        if world.shopsanity == '0':
            pool.extend(normal_rupees)
        else:
            pool.extend(shopsanity_rupees)

    if world.shuffle_scrubs != 'off':
        if world.dungeon_mq['Deku Tree']:
            pool.append('Deku Shield')
        if world.dungeon_mq['Dodongos Cavern']:
            pool.extend(['Deku Stick (1)', 'Deku Shield', 'Recovery Heart'])
        else:
            pool.extend(['Deku Nuts (5)', 'Deku Stick (1)', 'Deku Shield'])
        if not world.dungeon_mq['Jabu Jabus Belly']:
            pool.append('Deku Nuts (5)')
        if world.dungeon_mq['Ganons Castle']:
            pool.extend(['Bombs (5)', 'Recovery Heart', 'Rupees (5)', 'Deku Nuts (5)'])
        else:
            pool.extend(['Bombs (5)', 'Recovery Heart', 'Rupees (5)'])
        pool.extend(deku_scrubs_items)
        for _ in range(7):
            pool.append('Arrows (30)' if random.randint(0,3) > 0 else 'Deku Seeds (30)')

    else:
        if world.dungeon_mq['Deku Tree']:
            placed_items['Deku Tree MQ Deku Scrub'] = 'Buy Deku Shield'
        if world.dungeon_mq['Dodongos Cavern']:
            placed_items['Dodongos Cavern MQ Deku Scrub Lobby Rear'] = 'Buy Deku Stick (1)'
            placed_items['Dodongos Cavern MQ Deku Scrub Lobby Front'] = 'Buy Deku Seeds (30)'
            placed_items['Dodongos Cavern MQ Deku Scrub Staircase'] = 'Buy Deku Shield'
            placed_items['Dodongos Cavern MQ Deku Scrub Side Room Near Lower Lizalfos'] = 'Buy Red Potion [30]'
        else:
            placed_items['Dodongos Cavern Deku Scrub Near Bomb Bag Left'] = 'Buy Deku Nut (5)'
            placed_items['Dodongos Cavern Deku Scrub Side Room Near Dodongos'] = 'Buy Deku Stick (1)'
            placed_items['Dodongos Cavern Deku Scrub Near Bomb Bag Right'] = 'Buy Deku Seeds (30)'
            placed_items['Dodongos Cavern Deku Scrub Lobby'] = 'Buy Deku Shield'
        if not world.dungeon_mq['Jabu Jabus Belly']:
            placed_items['Jabu Jabus Belly Deku Scrub'] = 'Buy Deku Nut (5)'
        if world.dungeon_mq['Ganons Castle']:
            placed_items['Ganons Castle MQ Deku Scrub Right'] = 'Buy Deku Nut (5)'
            placed_items['Ganons Castle MQ Deku Scrub Center-Left'] = 'Buy Bombs (5) [35]'
            placed_items['Ganons Castle MQ Deku Scrub Center'] = 'Buy Arrows (30)'
            placed_items['Ganons Castle MQ Deku Scrub Center-Right'] = 'Buy Red Potion [30]'
            placed_items['Ganons Castle MQ Deku Scrub Left'] = 'Buy Green Potion'
        else:
            placed_items['Ganons Castle Deku Scrub Center-Left'] = 'Buy Bombs (5) [35]'
            placed_items['Ganons Castle Deku Scrub Center-Right'] = 'Buy Arrows (30)'
            placed_items['Ganons Castle Deku Scrub Right'] = 'Buy Red Potion [30]'
            placed_items['Ganons Castle Deku Scrub Left'] = 'Buy Green Potion'
        placed_items.update(vanilla_deku_scrubs)

    pool.extend(alwaysitems)
    
    if world.dungeon_mq['Deku Tree']:
        pool.extend(DT_MQ)
    else:
        pool.extend(DT_vanilla)
    if world.dungeon_mq['Dodongos Cavern']:
        pool.extend(DC_MQ)
    else:
        pool.extend(DC_vanilla)
    if world.dungeon_mq['Jabu Jabus Belly']:
        pool.extend(JB_MQ)
    if world.dungeon_mq['Forest Temple']:
        pool.extend(FoT_MQ)
    else:
        pool.extend(FoT_vanilla)
    if world.dungeon_mq['Fire Temple']:
        pool.extend(FiT_MQ)
    else:
        pool.extend(FiT_vanilla)
    if world.dungeon_mq['Spirit Temple']:
        pool.extend(SpT_MQ)
    else:
        pool.extend(SpT_vanilla)
    if world.dungeon_mq['Shadow Temple']:
        pool.extend(ShT_MQ)
    else:
        pool.extend(ShT_vanilla)
    if not world.dungeon_mq['Bottom of the Well']:
        pool.extend(BW_vanilla)
    if world.dungeon_mq['Gerudo Training Grounds']:
        pool.extend(GTG_MQ)
    else:
        pool.extend(GTG_vanilla)
    if world.dungeon_mq['Ganons Castle']:
        pool.extend(GC_MQ)
    else:
        pool.extend(GC_vanilla)

    for i in range(bottle_count):
        if i >= ruto_bottles:
            bottle = random.choice(normal_bottles)
            pool.append(bottle)
        else:
            pool.append('Rutos Letter')

    earliest_trade = tradeitemoptions.index(world.logic_earliest_adult_trade)
    latest_trade = tradeitemoptions.index(world.logic_latest_adult_trade)
    if earliest_trade > latest_trade:
        earliest_trade, latest_trade = latest_trade, earliest_trade
    tradeitem = random.choice(tradeitems[earliest_trade:latest_trade+1])
    world.selected_adult_trade_item = tradeitem
    pool.append(tradeitem)

    pool.extend(songlist)
    if world.shuffle_song_items == 'any' and world.item_pool_value == 'plentiful':
        pending_junk_pool.extend(songlist)

    if world.free_scarecrow:
        world.state.collect(ItemFactory('Scarecrow Song'))
    
    if world.no_epona_race:
        world.state.collect(ItemFactory('Epona', event=True))

    if world.shuffle_mapcompass == 'remove' or world.shuffle_mapcompass == 'startwith':
        for item in [item for dungeon in world.dungeons for item in dungeon.dungeon_items]:
            world.state.collect(item)
            pool.extend(get_junk_item())
    if world.shuffle_smallkeys == 'remove':
        for item in [item for dungeon in world.dungeons for item in dungeon.small_keys]:
            world.state.collect(item)
            pool.extend(get_junk_item())
    if world.shuffle_bosskeys == 'remove':
        for item in [item for dungeon in world.dungeons if dungeon.name != 'Ganons Castle' for item in dungeon.boss_key]:
            world.state.collect(item)
            pool.extend(get_junk_item())
    if world.shuffle_ganon_bosskey in ['remove', 'triforce']:
        for item in [item for dungeon in world.dungeons if dungeon.name == 'Ganons Castle' for item in dungeon.boss_key]:
            world.state.collect(item)
            pool.extend(get_junk_item())

    if world.overworld_tokens == 'vanilla':
        for location, item in vanillaoverworldGS.items():
            try:
                world.get_location(location)
                placed_items[location] = item
            except KeyError:
                continue
    else:
        pool.extend(['Gold Skulltula Token (Kokiri Forest)'] * 3)
        pool.extend(['Gold Skulltula Token (Lost Woods)'] * 3)
        pool.extend(['Gold Skulltula Token (Sacred Forest Meadow)'] * 1)
        pool.extend(['Gold Skulltula Token (Market Guard House)'] * 1)
        pool.extend(['Gold Skulltula Token (Hyrule Castle Grounds)'] * 1)
        pool.extend(['Gold Skulltula Token (Grotto)'] * 3)
        pool.extend(['Gold Skulltula Token (Ganons Castle Grounds)'] * 1)
        pool.extend(['Gold Skulltula Token (Lon Lon Ranch)'] * 4)
        pool.extend(['Gold Skulltula Token (Kakariko Village)'] * 6)
        pool.extend(['Gold Skulltula Token (Graveyard)'] * 2)
        pool.extend(['Gold Skulltula Token (Death Mountain Trail)'] * 4)
        pool.extend(['Gold Skulltula Token (Goron City)'] * 2)
        pool.extend(['Gold Skulltula Token (Death Mountain Crater)'] * 2)
        pool.extend(['Gold Skulltula Token (Zoras River)'] * 4)
        pool.extend(['Gold Skulltula Token (Zoras Domain)'] * 1)
        pool.extend(['Gold Skulltula Token (Zoras Fountain)'] * 3)
        pool.extend(['Gold Skulltula Token (Lake Hylia)'] * 4)
        pool.extend(['Gold Skulltula Token (LH Lab)'] * 1)
        pool.extend(['Gold Skulltula Token (Gerudo Valley)'] * 4)
        pool.extend(['Gold Skulltula Token (Gerudo Fortress)'] * 2)
        pool.extend(['Gold Skulltula Token (Haunted Wasteland)'] * 1)
        pool.extend(['Gold Skulltula Token (Desert Colossus)'] * 3)
    if world.dungeon_tokens == 'vanilla':
        for location, item in vanilladungeonGS.items():
            try:
                world.get_location(location)
                placed_items[location] = item
            except KeyError:
                continue
    if world.shuffle_mapcompass == 'vanilla':
        for location, item in vanillaMC.items():
            try:
                world.get_location(location)
                placed_items[location] = item
            except KeyError:
                continue
    if world.shuffle_smallkeys == 'vanilla':
        for location, item in vanillaSK.items():
            try:
                world.get_location(location)
                placed_items[location] = item
            except KeyError:
                continue
        # Logic cannot handle vanilla key layout in some dungeons
        # this is because vanilla expects the dungeon major item to be
        # locked behind the keys, which is not always true in rando.
        # We can resolve this by starting with some extra keys
        if world.dungeon_mq['Spirit Temple']:
            # Yes somehow you need 3 keys. This dungeon is bonkers
            world.state.collect(ItemFactory('Small Key (Spirit Temple)'))
            world.state.collect(ItemFactory('Small Key (Spirit Temple)'))
            world.state.collect(ItemFactory('Small Key (Spirit Temple)'))
        #if not world.dungeon_mq['Fire Temple']:
        #    world.state.collect(ItemFactory('Small Key (Fire Temple)'))
    if world.shuffle_bosskeys == 'vanilla':
        for location, item in vanillaBK.items():
            try:
                world.get_location(location)
                placed_items[location] = item
            except KeyError:
                continue


    if not world.keysanity and not world.dungeon_mq['Fire Temple']:
        world.state.collect(ItemFactory('Small Key (Fire Temple)'))
    if not world.dungeon_mq['Water Temple']:
        world.state.collect(ItemFactory('Small Key (Water Temple)'))

    if world.triforce_hunt:
        triforce_count = int((TriforceCounts[world.item_pool_value] * world.triforce_goal_per_world).to_integral_value(rounding=ROUND_HALF_UP))
        pending_junk_pool.extend(['Triforce Piece'] * triforce_count)

    if world.shuffle_ganon_bosskey in ['lacs_vanilla', 'lacs_medallions', 'lacs_stones', 'lacs_dungeons', 'lacs_tokens']:
        placed_items['ToT Light Arrows Cutscene'] = 'Boss Key (Ganons Castle)'
    elif world.shuffle_ganon_bosskey == 'vanilla':
        placed_items['Ganons Tower Boss Key Chest'] = 'Boss Key (Ganons Castle)'

    if world.item_pool_value == 'plentiful':
        pool.extend(easy_items)
    else:
        pool.extend(normal_items)

    if not world.shuffle_kokiri_sword:
        replace_max_item(pool, 'Kokiri Sword', 0)

    if world.junk_ice_traps == 'off': 
        replace_max_item(pool, 'Ice Trap', 0)
    elif world.junk_ice_traps == 'onslaught':
        for item in [item for item, weight in junk_pool_base] + ['Recovery Heart', 'Bombs (20)', 'Arrows (30)']:
            replace_max_item(pool, item, 0)

    for item,max in item_difficulty_max[world.item_pool_value].items():
        replace_max_item(pool, item, max)

    world.distribution.alter_pool(world, pool)

    # Make sure our pending_junk_pool is empty. If not, remove some random junk here.
    if pending_junk_pool:
        for item in set(pending_junk_pool):
            # Ensure pending_junk_pool contents don't exceed values given by distribution file
            if item in world.distribution.item_pool:
                while pending_junk_pool.count(item) > world.distribution.item_pool[item].count:
                    pending_junk_pool.remove(item)
                # Remove pending junk already added to the pool by alter_pool from the pending_junk_pool
                if item in pool:
                    count = pool.count(item)
                    for _ in range(count):
                        pending_junk_pool.remove(item)

        remove_junk_pool, _ = zip(*junk_pool_base)
        remove_junk_pool = list(remove_junk_pool) + ['Recovery Heart', 'Bombs (20)', 'Arrows (30)', 'Ice Trap']

        junk_candidates = [item for item in pool if item in remove_junk_pool]
        while pending_junk_pool:
            pending_item = pending_junk_pool.pop()
            if not junk_candidates:
                raise RuntimeError("Not enough junk exists in item pool for %s to be added." % pending_item)
            junk_item = random.choice(junk_candidates)
            junk_candidates.remove(junk_item)
            pool.remove(junk_item)
            pool.append(pending_item)

    world.distribution.configure_starting_items_settings(world)
    world.distribution.collect_starters(world.state)

    return (pool, placed_items)
