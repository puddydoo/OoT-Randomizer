import random

#   Abbreviations
#       DMC     Death Mountain Crater
#       DMT     Death Mountain Trail
#       GC      Goron City
#       GF      Gerudo Fortress
#       GS      Gold Skulltula
#       GV      Gerudo Valley
#       HC      Hyrule Castle
#       HF      Hyrule Field
#       KF      Kokiri Forest
#       LH      Lake Hylia
#       LLR     Lon Lon Ranch
#       LW      Lost Woods
#       OGC     Outside Ganon's Castle
#       SFM     Sacred Forest Meadow
#       ZD      Zora's Domain
#       ZF      Zora's Fountain
#       ZR      Zora's River

class Hint(object):
    name = ""
    text = ""
    type = []

    def __init__(self, name, text, type, choice=None):
        self.name = name
        self.type = [type] if not isinstance(type, list) else type

        if isinstance(text, str):
            self.text = text
        else:
            if choice == None:
                self.text = random.choice(text)
            else:
                self.text = text[choice]


def getHint(name, clearer_hint=False):
    textOptions, clearText, type = hintTable[name]
    if clearer_hint:
        if clearText == None:
            return Hint(name, textOptions, type, 0)
        return Hint(name, clearText, type)
    else:
        return Hint(name, textOptions, type)


def getHintGroup(group, world):
    ret = []
    for name in hintTable:

        hint = getHint(name, world.clearer_hints)

        if hint.name in world.always_hints:
            hint.type = 'always'

        if group in hint.type and not (name in hintExclusions(world)):
            ret.append(hint)
    return ret


def getRequiredHints(world):
    ret = []
    for name in hintTable:
        hint = getHint(name)
        if 'always' in hint.type or hint.name in conditional_always and conditional_always[hint.name](world):
            ret.append(hint)
    return ret


# Hints required under certain settings
conditional_always = {
    'Market 10 Big Poes':           lambda world: world.big_poe_count > 3,
    'Deku Theater Skull Mask':      lambda world: world.hint_dist == 'tournament' and world.open_kakariko == 'closed',
    'Deku Theater Mask of Truth':   lambda world: not world.complete_mask_quest,
    'Song from Ocarina of Time':    lambda world: world.bridge not in ('stones', 'dungeons') and world.shuffle_ganon_bosskey not in ('lacs_stones', 'lacs_dungeons'),
    'HF Ocarina of Time Item':      lambda world: world.bridge not in ('stones', 'dungeons') and world.shuffle_ganon_bosskey not in ('lacs_stones', 'lacs_dungeons'),
    'Sheik in Kakariko':            lambda world: world.bridge not in ('medallions', 'dungeons') and world.shuffle_ganon_bosskey not in ('lacs_medallions', 'lacs_dungeons'),
    'DMT Biggoron':                 lambda world: world.logic_earliest_adult_trade != 'claim_check' or world.logic_latest_adult_trade != 'claim_check',
    'Kak 50 Gold Skulltula Reward': lambda world: world.bridge != 'tokens' or world.bridge_tokens < 50,
    'Kak 40 Gold Skulltula Reward': lambda world: world.bridge != 'tokens' or world.bridge_tokens < 40,
    'Kak 30 Gold Skulltula Reward': lambda world: world.bridge != 'tokens' or world.bridge_tokens < 30,
}


# table of hints, format is (name, hint text, clear hint text, type of hint) there are special characters that are read for certain in game commands:
# ^ is a box break
# & is a new line
# @ will print the player name
# # sets color to white (currently only used for dungeon reward hints).
hintTable = {
    'Triforce Piece':                                           (["a triumph fork", "cheese", "a gold fragment"], "a Piece of the Triforce", "item"),
    'Magic Meter':                                              (["mystic training", "pixie dust", "a green rectangle"], "a Magic Meter", 'item'),
    'Double Defense':                                           (["a white outline", "damage decrease", "strengthened love"], "Double Defense", 'item'),
    'Slingshot':                                                (["a seed shooter", "a rubberband", "a child's catapult"], "a Slingshot", 'item'),
    'Boomerang':                                                (["a banana", "a stun stick"], "the Boomerang", 'item'),
    'Bow':                                                      (["an archery enabler", "a danger dart launcher"], "a Bow", 'item'),
    'Bomb Bag':                                                 (["an explosive container", "a blast bag"], "a Bomb Bag", 'item'),
    'Progressive Hookshot':                                     (["Dampe's keepsake", "the Grapple Beam", "the BOING! chain"], "a Hookshot", 'item'),
    'Progressive Strength Upgrade':                             (["power gloves", "metal mittens", "the heavy lifty"], "a Strength Upgrade", 'item'),
    'Progressive Scale':                                        (["a deeper dive", "a piece of Zora"], "a Zora Scale", 'item'),
    'Megaton Hammer':                                           (["the dragon smasher", "the metal mallet", "the heavy hitter"], "the Megaton Hammer", 'item'),
    'Iron Boots':                                               (["sink shoes", "clank cleats"], "the Iron Boots", 'item'),
    'Hover Boots':                                              (["butter boots", "sacred slippers", "spacewalkers"], "the Hover Boots", 'item'),
    'Kokiri Sword':                                             (["a butter knife", "a starter slasher", "a switchblade"], "the Kokiri Sword", 'item'),
    'Giants Knife':                                             (["a fragile blade", "a breakable cleaver"], "the Giant's Knife", 'item'),
    'Biggoron Sword':                                           (["the biggest blade", "a colossal cleaver"], "the Biggoron Sword", 'item'),
    'Master Sword':                                             (["evil's bane"], "the Master Sword", 'item'),
    'Deku Shield':                                              (["a wooden ward", "a burnable barrier"], "a Deku Shield", 'item'),
    'Hylian Shield':                                            (["a steel safeguard", "Like Like's metal meal"], "a Hylian Shield", 'item'),
    'Mirror Shield':                                            (["the reflective rampart", "Medusa's weakness", "a silvered surface"], "the Mirror Shield", 'item'),
    'Farores Wind':                                             (["teleportation", "a relocation rune", "a green ball", "a green gust"], "Farore's Wind", 'item'),
    'Nayrus Love':                                              (["a safe space", "an impregnable aura", "a blue barrier", "a blue crystal"], "Nayru's Love", 'item'),
    'Dins Fire':                                                (["an inferno", "a heat wave", "a red ball"], "Din's Fire", 'item'),
    'Fire Arrows':                                              (["the furnace firearm", "the burning bolts", "a magma missile"], "the Fire Arrows", 'item'),
    'Ice Arrows':                                               (["the refrigerator rocket", "the frostbite bolts", "an iceberg maker"], "the Ice Arrows", 'item'),
    'Light Arrows':                                             (["the shining shot", "the luminous launcher", "Ganondorf's bane", "the lighting bolts"], "the Light Arrows", 'item'),
    'Lens of Truth':                                            (["a lie detector", "a ghost tracker", "true sight", "a detective's tool"], "the Lens of Truth", 'item'),
    'Ocarina':                                                  (["a flute", "a music maker"], "an Ocarina", 'item'),
    'Goron Tunic':                                              (["ruby robes", "fireproof fabric", "cooking clothes"], "a Goron Tunic", 'item'),
    'Zora Tunic':                                               (["a sapphire suit", "scuba gear", "a swimsuit"], "a Zora Tunic", 'item'),
    'Epona':                                                    (["a horse", "a four legged friend"], "Epona", 'item'),
    'Zeldas Lullaby':                                           (["a song of royal slumber", "a triforce tune"], "Zelda's Lullaby", 'item'),
    'Eponas Song':                                              (["an equestrian etude", "Malon's melody", "a ranch song"], "Epona's Song", 'item'),
    'Sarias Song':                                              (["a song of dancing Gorons", "Saria's phone number"], "Saria's Song", 'item'),
    'Suns Song':                                                (["Sunny Day", "the ReDead's bane", "the Gibdo's bane"], "the Sun's Song", 'item'),
    'Song of Time':                                             (["a song 7 years long", "the tune of ages"], "the Song of Time", 'item'),
    'Song of Storms':                                           (["Rain Dance", "a thunderstorm tune", "windmill acceleration"], "the Song of Storms", 'item'),
    'Minuet of Forest':                                         (["the song of tall trees", "an arboreal anthem", "a green spark trail"], "the Minuet of Forest", 'item'),
    'Bolero of Fire':                                           (["a song of lethal lava", "a red spark trail", "a volcanic verse"], "the Bolero of Fire", 'item'),
    'Serenade of Water':                                        (["a song of a damp ditch", "a blue spark trail", "the lake's lyric"], "the Serenade of Water", 'item'),
    'Requiem of Spirit':                                        (["a song of sandy statues", "an orange spark trail", "the desert ditty"], "the Requiem of Spirit", 'item'),
    'Nocturne of Shadow':                                       (["a song of spooky spirits", "a graveyard boogie", "a haunted hymn", "a purple spark trail"], "the Nocturne of Shadow", 'item'),
    'Prelude of Light':                                         (["a luminous prologue melody", "a yellow spark trail", "the temple traveler"], "the Prelude of Light", 'item'),
    'Bottle':                                                   (["a glass container", "an empty jar", "encased air"], "a Bottle", 'item'),
    'Rutos Letter':                                             (["a call for help", "the note that Mweeps", "an SOS call", "a fishy stationery"], "Ruto's Letter", 'item'),
    'Bottle with Milk':                                         (["cow juice", "a white liquid", "a baby's breakfast"], "a Milk Bottle", 'item'),
    'Bottle with Red Potion':                                   (["a vitality vial", "a red liquid"], "a Red Potion Bottle", 'item'),
    'Bottle with Green Potion':                                 (["a magic mixture", "a green liquid"], "a Green Potion Bottle", 'item'),
    'Bottle with Blue Potion':                                  (["an ailment antidote", "a blue liquid"], "a Blue Potion Bottle", 'item'),
    'Bottle with Fairy':                                        (["an imprisoned fairy", "an extra life", "Navi's cousin"], "a Fairy Bottle", 'item'),
    'Bottle with Fish':                                         (["an aquarium", "a deity's snack"], "a Fish Bottle", 'item'),
    'Bottle with Blue Fire':                                    (["a conflagration canteen", "an icemelt jar"], "a Blue Fire Bottle", 'item'),
    'Bottle with Bugs':                                         (["an insectarium", "Skulltula finders"], "a Bug Bottle", 'item'),
    'Bottle with Poe':                                          (["a spooky ghost", "a face in the jar"], "a Poe Bottle", 'item'),
    'Bottle with Big Poe':                                      (["the spookiest ghost", "a sidequest spirit"], "a Big Poe Bottle", 'item'),
    'Stone of Agony':                                           (["the shake stone", "the Rumble Pak (TM)"], "the Stone of Agony", 'item'),
    'Gerudo Membership Card':                                   (["a girl club membership", "a desert tribe's pass"], "the Gerudo Card", 'item'),
    'Progressive Wallet':                                       (["a mo' money holder", "a gem purse", "a portable bank"], "a Wallet", 'item'),
    'Deku Stick Capacity':                                      (["a lumber rack", "more flammable twigs"], "Deku Stick Capacity", 'item'),
    'Deku Nut Capacity':                                        (["more nuts", "flashbang storage"], "Deku Nut Capacity", 'item'),
    'Heart Container':                                          (["a lot of love", "a Valentine's gift", "a boss's organ"], "a Heart Container", 'item'),
    'Piece of Heart':                                           (["a little love", "a broken heart"], "a Piece of Heart", 'item'),
    'Piece of Heart (Treasure Chest Game)':                     ("a victory valentine", "a Piece of Heart", 'item'),
    'Recovery Heart':                                           (["a free heal", "a hearty meal", "a Band-Aid"], "a Recovery Heart", 'item'),
    'Rupee (Treasure Chest Game)':                              ("the dollar of defeat", 'a Green Rupee', 'item'),
    'Deku Stick (1)':                                           ("a breakable branch", 'a Deku Stick', 'item'),
    'Rupee (1)':                                                (["a unique coin", "a penny", "a green gem"], "a Green Rupee", 'item'),
    'Rupees (5)':                                               (["a common coin", "a blue gem"], "a Blue Rupee", 'item'),
    'Rupees (20)':                                              (["couch cash", "a red gem"], "a Red Rupee", 'item'),
    'Rupees (50)':                                              (["big bucks", "a purple gem", "wealth"], "a Purple Rupee", 'item'),
    'Rupees (200)':                                             (["a juicy jackpot", "a yellow gem", "a giant gem", "great wealth"], "a Huge Rupee", 'item'),
    'Weird Egg':                                                (["a chicken dilemma"], "the Weird Egg", 'item'),
    'Zeldas Letter':                                            (["an autograph", "royal stationery", "royal snail mail"], "Zelda's Letter", 'item'),
    'Pocket Egg':                                               (["a Cucco container", "a Cucco, eventually", "a fowl youth"], "the Pocket Egg", 'item'),
    'Pocket Cucco':                                             (["a little clucker"], "the Pocket Cucco", 'item'),
    'Cojiro':                                                   (["a cerulean capon"], "Cojiro", 'item'),
    'Odd Mushroom':                                             (["a powder ingredient"], "an Odd Mushroom", 'item'),
    'Odd Potion':                                               (["Granny's goodies"], "an Odd Potion", 'item'),
    'Poachers Saw':                                             (["a tree killer"], "the Poacher's Saw", 'item'),
    'Broken Sword':                                             (["a shattered slicer"], "the Broken Sword", 'item'),
    'Prescription':                                             (["a pill pamphlet", "a doctor's note"], "the Prescription", 'item'),
    'Eyeball Frog':                                             (["a perceiving polliwog"], "the Eyeball Frog", 'item'),
    'Eyedrops':                                                 (["a vision vial"], "the Eyedrops", 'item'),
    'Claim Check':                                              (["a three day wait"], "the Claim Check", 'item'),
    'Map':                                                      (["a dungeon atlas", "blueprints"], "a Map", 'item'),
    'Compass':                                                  (["a treasure tracker", "a magnetic needle"], "a Compass", 'item'),
    'BossKey':                                                  (["a master of unlocking", "a dungeon's master pass"], "a Boss Key", 'item'),
    'SmallKey':                                                 (["a tool for unlocking", "a dungeon pass", "a lock remover", "a lockpick"], "a Small Key", 'item'),
    'HideoutSmallKey':                                          (["a get out of jail free card"], "a Jail Key", 'item'),
    'KeyError':                                                 (["something mysterious", "an unknown treasure"], "An Error (Please Report This)", 'item'),
    'Arrows (5)':                                               (["a few danger darts", "a few sharp shafts"], "Arrows (5 pieces)", 'item'),
    'Arrows (10)':                                              (["some danger darts", "some sharp shafts"], "Arrows (10 pieces)", 'item'),
    'Arrows (30)':                                              (["plenty of danger darts", "plenty of sharp shafts"], "Arrows (30 pieces)", 'item'),
    'Bombs (5)':                                                (["a few explosives", "a few blast balls"], "Bombs (5 pieces)", 'item'),
    'Bombs (10)':                                               (["some explosives", "some blast balls"], "Bombs (10 pieces)", 'item'),
    'Bombs (20)':                                               (["lots-o-explosives", "plenty of blast balls"], "Bombs (20 pieces)", 'item'),
    'Ice Trap':                                                 (["a gift from Ganon", "a chilling discovery", "frosty fun"], "an Ice Trap", 'item'),
    'Magic Bean':                                               (["a wizardly legume"], "a Magic Bean", 'item'),
    'Magic Bean Pack':                                          (["wizardly legumes"], "Magic Beans", 'item'),
    'Bombchus':                                                 (["mice bombs", "proximity mice", "wall crawlers", "trail blazers"], "Bombchus", 'item'),
    'Bombchus (5)':                                             (["a few mice bombs", "a few proximity mice", "a few wall crawlers", "a few trail blazers"], "Bombchus (5 pieces)", 'item'),
    'Bombchus (10)':                                            (["some mice bombs", "some proximity mice", "some wall crawlers", "some trail blazers"], "Bombchus (10 pieces)", 'item'),
    'Bombchus (20)':                                            (["plenty of mice bombs", "plenty of proximity mice", "plenty of wall crawlers", "plenty of trail blazers"], "Bombchus (20 pieces)", 'item'),
    'Deku Nuts (5)':                                            (["some nuts", "some flashbangs", "some scrub spit"], "Deku Nuts (5 pieces)", 'item'),
    'Deku Nuts (10)':                                           (["lots-o-nuts", "plenty of flashbangs", "plenty of scrub spit"], "Deku Nuts (10 pieces)", 'item'),
    'Deku Seeds (30)':                                          (["catapult ammo", "lots-o-seeds"], "Deku Seeds (30 pieces)", 'item'),
    'Gold Skulltula Token':                                     (["proof of destruction", "an arachnid chip", "spider remains", "one percent of a curse"], "a Gold Skulltula Token", 'item'),

    'Deku Theater Mask of Truth':                               ("the #Mask of Truth# yields", None, ['overworld', 'sometimes']),
    'ZR Frogs Ocarina Game':                                    (["an #amphibian feast# yields", "the #croaking choir's magnum opus# awards", "the #froggy finale# yields"], "the final reward from the #Frogs of Zora's River# is", 'always'),
    'KF Links House Cow':                                       ("the #bovine bounty of a horseback hustle# gifts", "#Malon's obstacle course# leads to", 'always'),

    'Song from Ocarina of Time':                                ("the #Ocarina of Time# teaches", None, ['song', 'sometimes']),
    'Song from Composers Grave':                                (["#ReDead in the Composers' Grave# guard", "the #Composer Brothers wrote#"], None, ['song', 'sometimes']),
    'Sheik in Forest':                                          ("#in a meadow# Sheik teaches", None, ['song', 'sometimes']),
    'Sheik at Temple':                                          ("Sheik waits at a #monument to time# to teach", None, ['song', 'sometimes']),
    'Sheik in Crater':                                          ("the #crater's melody# is", None, ['song', 'sometimes']),
    'Sheik in Ice Cavern':                                      ("the #frozen cavern# echoes with", None, ['song', 'sometimes']),
    'Sheik in Kakariko':                                        ("a #ravaged village# mourns with", None, ['song', 'sometimes']),
    'Sheik at Colossus':                                        ("a hero ventures #beyond the wasteland# to learn", None, ['song', 'sometimes']),

    'Market 10 Big Poes':                                       ("#ghost hunters# will be rewarded with", "catching #Big Poes# leads to", ['overworld', 'sometimes']),
    'Deku Theater Skull Mask':                                  ("the #Skull Mask# yields", None, ['overworld', 'sometimes']),
    'HF Ocarina of Time Item':                                  ("the #treasure thrown by Princess Zelda# is", None, ['overworld', 'sometimes']),
    'DMT Biggoron':                                             ("#Biggoron# crafts", None, ['overworld', 'sometimes']),
    'Kak 50 Gold Skulltula Reward':                             ("slaying #50 Gold Skulltulas# reveals", None, ['overworld', 'sometimes']),
    'Kak 40 Gold Skulltula Reward':                             ("slaying #40 Gold Skulltulas# reveals", None, ['overworld', 'sometimes']),
    'Kak 30 Gold Skulltula Reward':                             ("slaying #30 Gold Skulltulas# reveals", None, ['overworld', 'sometimes']),
    'Kak 20 Gold Skulltula Reward':                             ("slaying #20 Gold Skulltulas# reveals", None, ['overworld', 'sometimes']),
    'Kak Anju as Child':                                        ("#collecting cuccos# rewards", None, ['overworld', 'sometimes']),
    'GC Darunias Joy':                                          ("#Darunia's dance# leads to", None, ['overworld', 'sometimes']),
    'LW Skull Kid':                                             ("the #Skull Kid# grants", None, ['overworld', 'sometimes']),
    'LH Sun':                                                   ("staring into #the sun# grants", "shooting #the sun# grants", ['overworld', 'sometimes']),
    'Market Treasure Chest Game':                               (["#gambling# grants", "there is a #1/32 chance# to win"], "the #treasure chest game# grants", ['overworld', 'sometimes']),
    'GF HBA 1500 Points':                                       ("mastery of #horseback archery# grants", "scoring 1500 in #horseback archery# grants", ['overworld', 'sometimes']),
    'Graveyard Heart Piece Grave Chest':                        ("playing #Sun's Song# in a grave spawns", None, ['overworld', 'sometimes']),
    'GC Maze Left Chest':                                       ("in #Goron City# the hammer unlocks", None, ['overworld', 'sometimes']),
    'GV Chest':                                                 ("in #Gerudo Valley# the hammer unlocks", None, ['overworld', 'sometimes']),
    'GV Cow':                                                   ("a #cow in Gerudo Valley# gifts", None, ['overworld', 'sometimes']),
    'HC GS Storms Grotto':                                      ("a #spider behind a muddy wall# in a grotto holds", None, ['overworld', 'sometimes']),
    'HF GS Cow Grotto':                                         ("a #spider behind webs# in a grotto holds", None, ['overworld', 'sometimes']),
    'HF Cow Grotto Cow':                                        ("a #cow behind webs# in a grotto gifts", None, ['overworld', 'sometimes']),
    'GS Zora\'s Fountain Hidden Cave':                          ("a spider high #above the icy waters# holds", None, ['overworld', 'sometimes']),
    'Wasteland Chest':                                          (["#deep in the wasteland# is", "beneath #the sands#, flames reveal"], None, ['overworld', 'sometimes']),
    'Colossus GS Bean Patch':                                   ("a #spider in the wasteland# holds", None, ['overworld', 'sometimes']),
    'Graveyard Composers Grave Chest':                          (["#flames in the Composers' Grave# reveal", "the #Composer Brothers hid#"], None, ['overworld', 'sometimes']),
    'ZF Bottom Freestanding PoH':                               ("#under the icy waters# lies", None, ['overworld', 'sometimes']),
    'GC Pot Freestanding PoH':                                  ("spinning #Goron pottery# contains", None, ['overworld', 'sometimes']),
    'ZD King Zora Thawed':                                      ("unfreezing #King Zora# grants", None, ['overworld', 'sometimes']),
    'DMC Deku Scrub':                                           ("a single #scrub in the crater# sells", None, ['overworld', 'sometimes']),
    'GC GS Boulder Maze':                                       ("a spider under a #crate in the crater# holds", None, ['overworld', 'sometimes']),

    'Deku Tree MQ After Spinning Log Chest':                    ("a #temporal stone within a tree# contains", "a #temporal stone within the Deku Tree# contains", ['dungeon', 'sometimes']),
    'Deku Tree MQ GS Basement Graves Room':                     ("a #spider on a ceiling in a tree# holds", "a #spider on a ceiling in the Deku Tree# holds", ['dungeon', 'sometimes']),
    'GS Dodongo\'s Cavern MQ Song of Time Block Room':          ("a spider under #temporal stones in a cavern# holds", "a spider under #temporal stones in Dodongo's Cavern# holds", ['dungeon', 'sometimes']),
    'Jabu Jabus Belly Boomerang Chest':                         ("a school of #stingers swallowed by a deity# guard", "a school of #stingers swallowed by Jabu Jabu# guard", ['dungeon', 'sometimes']),
    'Jabu Jabus Belly MQ GS Invisible Enemies Room':            ("a spider surrounded by #shadows in the belly of a deity# holds", "a spider surrounded by #shadows in Jabu Jabu's Belly# holds", ['dungeon', 'sometimes']),
    'Jabu Jabus Belly MQ Cow':                                  ("a #cow swallowed by a deity# gifts", "a #cow swallowed by Jabu Jabu# gifts", ['dungeon', 'sometimes']),
    'Fire Temple Scarecrow Chest':                              ("a #scarecrow atop the volcano# hides", "#Pierre atop the Fire Temple# hides", ['dungeon', 'sometimes']),
    'Fire Temple Megaton Hammer Chest':                         ("the #Flare Dancer atop the volcano# guards a chest containing", "the #Flare Dancer atop the Fire Temple# guards a chest containing", ['dungeon', 'sometimes']),
    'Fire Temple MQ Chest On Fire':                             ("the #Flare Dancer atop the volcano# guards a chest containing", "the #Flare Dancer atop the Fire Temple# guards a chest containing", ['dungeon', 'sometimes']),
    'Fire Temple MQ GS Skull On Fire':                          ("a #spider under a block in the volcano# holds", "a #spider under a block in the Fire Temple# holds", ['dungeon', 'sometimes']),
    'Water Temple River Chest':                                 ("beyond the #river under the lake# waits", "beyond the #river in the Water Temple# waits", ['dungeon', 'sometimes']),
    'Water Temple Boss Key Chest':                              ("dodging #rolling boulders under the lake# leads to", "dodging #rolling boulders in the Water Temple# leads to", ['dungeon', 'sometimes']),
    'Water Temple GS Behind Gate':                              ("a spider behind a #gate under the lake# holds", "a spider behind a #gate in the Water Temple# holds", ['dungeon', 'sometimes']),
    'Water Temple MQ Freestanding Key':                         ("hidden in a #box under the lake# lies", "hidden in a #box in the Water Temple# lies", ['dungeon', 'sometimes']),
    'Water Temple MQ GS Freestanding Key Area':                 ("the #locked spider under the lake# holds", "the #locked spider in the Water Temple# holds", ['dungeon', 'sometimes']),
    'Water Temple MQ GS Triple Wall Torch':                     ("a spider behind a #gate under the lake# holds", "a spider behind a #gate in the Water Temple# holds", ['dungeon', 'sometimes']),
    'Gerudo Training Grounds Underwater Silver Rupee Chest':    ("those who seek #sunken silver rupees# will find", None, ['dungeon', 'sometimes']),
    'Gerudo Training Grounds MQ Underwater Silver Rupee Chest': ("those who seek #sunken silver rupees# will find", None, ['dungeon', 'sometimes']),
    'Gerudo Training Grounds Maze Path Final Chest':            ("the final prize of #the thieves\' training# is", None, ['dungeon', 'sometimes']),
    'Gerudo Training Grounds MQ Ice Arrows Chest':              ("the final prize of #the thieves\' training# is", None, ['dungeon', 'sometimes']),
    'Bottom of the Well Lens of Truth Chest':                   ("#Dead Hand in the well# holds", None, ['dungeon', 'sometimes']),
    'Bottom of the Well MQ Compass Chest':                      ("#Dead Hand in the well# holds", None, ['dungeon', 'sometimes']),
    'Spirit Temple Silver Gauntlets Chest':                     ("upon the #Colossus's right hand# is", None, ['dungeon', 'sometimes']),
    'Spirit Temple Mirror Shield Chest':                        ("upon the #Colossus's left hand# is", None, ['dungeon', 'sometimes']),
    'Spirit Temple MQ Child Hammer Switch Chest':               ("a #temporal paradox in the Colossus# yields", "a #temporal paradox in the Spirit Temple# yields", ['dungeon', 'sometimes']),
    'Spirit Temple MQ Symphony Room Chest':                     ("a #symphony in the Colossus# yields", "a #symphony in the Spirit Temple# yields", ['dungeon', 'sometimes']),
    'Spirit Temple MQ GS Symphony Room':                        ("a #spider's symphony in the Colossus# yields", "a #spider's symphony in the Spirit Temple# yields", ['dungeon', 'sometimes']),
    'Shadow Temple Invisible Floormaster Chest':                ("shadows in an #invisible maze# guard", None, ['dungeon', 'sometimes']),
    'Shadow Temple MQ Bomb Flower Chest':                       ("shadows in an #invisible maze# guard", None, ['dungeon', 'sometimes']),

    'Desert Colossus -> Colossus Grotto':                       ("lifting a #rock in the desert# reveals", None, 'entrance'),
    'GV Grotto Ledge -> GV Octorok Grotto':                     ("a rock on #a ledge in the valley# hides", None, 'entrance'),
    'GC Grotto Platform -> GC Grotto':                          ("a #pool of lava# in Goron City blocks the way to", None, 'entrance'),
    'GF Entrances Behind Crates -> GF Storms Grotto':           ("a #storm within Gerudo's Fortress# reveals", None, 'entrance'),
    'Zoras Domain -> ZD Storms Grotto':                         ("a #storm within Zora's Domain# reveals", None, 'entrance'),
    'Hyrule Castle Grounds -> HC Storms Grotto':                ("a #storm near the castle# reveals", None, 'entrance'),
    'GV Fortress Side -> GV Storms Grotto':                     ("a #storm in the valley# reveals", None, 'entrance'),
    'Desert Colossus -> Colossus Great Fairy Fountain':         ("a #fractured desert wall# hides", None, 'entrance'),
    'Ganons Castle Grounds -> OGC Great Fairy Fountain':        ("a #heavy pillar# outside the castle obstructs", None, 'entrance'),
    'Zoras Fountain -> ZF Great Fairy Fountain':                ("a #fountain wall# hides", None, 'entrance'),
    'GV Fortress Side -> GV Carpenter Tent':                    ("a #tent in the valley# covers", None, 'entrance'),
    'Graveyard Warp Pad Region -> Shadow Temple Entryway':      ("at the #back of the Graveyard#, there is", None, 'entrance'),
    'Lake Hylia -> Water Temple Lobby':                         ("deep #under a vast lake#, one can find", None, 'entrance'),
    'Gerudo Fortress -> Gerudo Training Grounds Lobby':         ("paying a #fee to the Gerudos# grants access to", None, 'entrance'),
    'Zoras Fountain -> Jabu Jabus Belly Beginning':             ("inside #Jabu Jabu#, one can find", None, 'entrance'),
    'Kakariko Village -> Bottom of the Well':                   ("a #village well# leads to", None, 'entrance'),

    'KF Links House':                                           ("Link's House", None, 'region'),
    'Temple of Time':                                           ("the #Temple of Time#", None, 'region'),
    'KF Midos House':                                           ("Mido's house", None, 'region'),
    'KF Sarias House':                                          ("Saria's House", None, 'region'),
    'KF House of Twins':                                        ("the #House of Twins#", None, 'region'),
    'KF Know It All House':                                     ("Know-It-All Brothers' House", None, 'region'),
    'KF Kokiri Shop':                                           ("the #Kokiri Shop#", None, 'region'),
    'LH Lab':                                                   ("the #Lakeside Laboratory#", None, 'region'),
    'LH Fishing Hole':                                          ("the #Fishing Pond#", None, 'region'),
    'GV Carpenter Tent':                                        ("the #Carpenters' tent#", None, 'region'),
    'Market Guard House':                                       ("the #Guard House#", None, 'region'),
    'Market Mask Shop':                                         ("the #Happy Mask Shop#", None, 'region'),
    'Market Bombchu Bowling':                                   ("the #Bombchu Bowling Alley#", None, 'region'),
    'Market Potion Shop':                                       ("the #Market Potion Shop#", None, 'region'),
    'Market Treasure Chest Game':                               ("the #Treasure Chest Game#", None, 'region'),
    'Market Bombchu Shop':                                      ("the #Bombchu Shop#", None, 'region'),
    'Market Man in Green House':                                ("Man in Green's House", None, 'region'),
    'Kak Windmill':                                             ("the #Windmill#", None, 'region'),
    'Kak Carpenter Boss House':                                 ("the #Carpenters' Boss House#", None, 'region'),
    'Kak House of Skulltula':                                   ("the #House of Skulltula#", None, 'region'),
    'Kak Impas House':                                          ("Impa's House", None, 'region'),
    'Kak Impas House Back':                                     ("Impa's cow cage", None, 'region'),
    'Kak Odd Medicine Building':                                ("Granny's Potion Shop", None, 'region'),
    'Graveyard Dampes House':                                   ("Dampe's Hut", None, 'region'),
    'GC Shop':                                                  ("the #Goron Shop#", None, 'region'),
    'ZD Shop':                                                  ("the #Zora Shop#", None, 'region'),
    'LLR Talons House':                                         ("Talon's House", None, 'region'),
    'LLR Stables':                                              ("a #stable#", None, 'region'),
    'LLR Tower':                                                ("the #Lon Lon Tower#", None, 'region'),
    'Market Bazaar':                                            ("the #Market Bazaar#", None, 'region'),
    'Market Shooting Gallery':                                  ("a #Slingshot Shooting Gallery#", None, 'region'),
    'Kak Bazaar':                                               ("the #Kakariko Bazaar#", None, 'region'),
    'Kak Potion Shop Front':                                    ("the #Kakariko Potion Shop#", None, 'region'),
    'Kak Potion Shop Back':                                     ("the #Kakariko Potion Shop#", None, 'region'),
    'Kak Shooting Gallery':                                     ("a #Bow Shooting Gallery#", None, 'region'),
    'Colossus Great Fairy Fountain':                            ("a #Great Fairy Fountain#", None, 'region'),
    'HC Great Fairy Fountain':                                  ("a #Great Fairy Fountain#", None, 'region'),
    'OGC Great Fairy Fountain':                                 ("a #Great Fairy Fountain#", None, 'region'),
    'DMC Great Fairy Fountain':                                 ("a #Great Fairy Fountain#", None, 'region'),
    'DMT Great Fairy Fountain':                                 ("a #Great Fairy Fountain#", None, 'region'),
    'ZF Great Fairy Fountain':                                  ("a #Great Fairy Fountain#", None, 'region'),
    'Graveyard Shield Grave':                                   ("a #grave with a free chest#", None, 'region'),
    'Graveyard Heart Piece Grave':                              ("a chest spawned by #Sun's Song#", None, 'region'),
    'Graveyard Composers Grave':                                ("the #Composers' Grave#", None, 'region'),
    'Graveyard Dampes Grave':                                   ("Dampe's Grave", None, 'region'),
    'DMT Cow Grotto':                                           ("a solitary #Cow#", None, 'region'),
    'HC Storms Grotto':                                         ("a sandy grotto with #fragile walls#", None, 'region'),
    'HF Tektite Grotto':                                        ("a pool guarded by a #Tektite#", None, 'region'),
    'HF Near Kak Grotto':                                       ("a #Big Skulltula# guarding a Gold one", None, 'region'),
    'HF Cow Grotto':                                            ("a grotto full of #spider webs#", None, 'region'),
    'Kak Redead Grotto':                                        ("#ReDeads# guarding a chest", None, 'region'),
    'SFM Wolfos Grotto':                                        ("#Wolfos# guarding a chest", None, 'region'),
    'GV Octorok Grotto':                                        ("an #Octorok# guarding a rich pool", None, 'region'),
    'Deku Theater':                                             ("the #Lost Woods Stage#", None, 'region'),
    'ZR Open Grotto':                                           ("a #generic grotto#", None, 'region'),
    'DMC Upper Grotto':                                         ("a #generic grotto#", None, 'region'),
    'DMT Storms Grotto':                                        ("a #generic grotto#", None, 'region'),
    'Kak Open Grotto':                                          ("a #generic grotto#", None, 'region'),
    'HF Near Market Grotto':                                    ("a #generic grotto#", None, 'region'),
    'HF Open Grotto':                                           ("a #generic grotto#", None, 'region'),
    'HF Southeast Grotto':                                      ("a #generic grotto#", None, 'region'),
    'KF Storms Grotto':                                         ("a #generic grotto#", None, 'region'),
    'LW Near Shortcuts Grotto':                                 ("a #generic grotto#", None, 'region'),
    'HF Inside Fence Grotto':                                   ("a #single Upgrade Deku Scrub#", None, 'region'),
    'LW Scrubs Grotto':                                         ("#2 Deku Scrubs# including an Upgrade one", None, 'region'),
    'Colossus Grotto':                                          ("2 Deku Scrubs", None, 'region'),
    'ZR Storms Grotto':                                         ("2 Deku Scrubs", None, 'region'),
    'SFM Storms Grotto':                                        ("2 Deku Scrubs", None, 'region'),
    'GV Storms Grotto':                                         ("2 Deku Scrubs", None, 'region'),
    'LH Grotto':                                                ("3 Deku Scrubs", None, 'region'),
    'DMC Hammer Grotto':                                        ("3 Deku Scrubs", None, 'region'),
    'GC Grotto':                                                ("3 Deku Scrubs", None, 'region'),
    'LLR Grotto':                                               ("3 Deku Scrubs", None, 'region'),
    'ZR Fairy Grotto':                                          ("a small #Fairy Fountain#", None, 'region'),
    'HF Fairy Grotto':                                          ("a small #Fairy Fountain#", None, 'region'),
    'SFM Fairy Grotto':                                         ("a small #Fairy Fountain#", None, 'region'),
    'ZD Storms Grotto':                                         ("a small #Fairy Fountain#", None, 'region'),
    'GF Storms Grotto':                                         ("a small #Fairy Fountain#", None, 'region'),

    '1001':                                                     ("Ganondorf 2020!", None, 'junk'),
    '1002':                                                     ("They say that monarchy is a terrible system of governance.", None, 'junk'),
    '1003':                                                     ("They say that Zelda is a poor leader.", None, 'junk'),
    '1004':                                                     ("These hints can be quite useful. This is an exception.", None, 'junk'),
    '1006':                                                     ("They say that all the Zora drowned in Wind Waker.", None, 'junk'),
    '1008':                                                     ("'Member when Ganon was a blue pig?^I 'member.", None, 'junk'),
    '1009':                                                     ("One who does not have Triforce can't go in.", None, 'junk'),
    '1010':                                                     ("Save your future, end the Happy Mask Salesman.", None, 'junk'),
    '1012':                                                     ("I'm stoned. Get it?", None, 'junk'),
    '1013':                                                     ("Hoot! Hoot! Would you like me to repeat that?", None, 'junk'),
    '1014':                                                     ("Gorons are stupid. They eat rocks.", None, 'junk'),
    '1015':                                                     ("They say that Lon Lon Ranch prospered under Ingo.", None, 'junk'),
    '1016':                                                     ("The single rupee is a unique item.", None, 'junk'),
    '1017':                                                     ("Without the Lens of Truth, the Treasure Chest Mini-Game is a 1 out of 32 chance.^Good luck!", None, 'junk'),
    '1018':                                                     ("Use bombs wisely.", None, 'junk'),
    '1021':                                                     ("I found you, faker!", None, 'junk'),
    '1022':                                                     ("You're comparing yourself to me?^Ha! You're not even good enough to be my fake.", None, 'junk'),
    '1023':                                                     ("I'll make you eat those words.", None, 'junk'),
    '1024':                                                     ("What happened to Sheik?", None, 'junk'),
    '1025':                                                     ("L2P @.", None, 'junk'),
    '1026':                                                     ("I heard @ isn't very good at Zelda.", None, 'junk'),
    '1027':                                                     ("I'm Lonk from Pennsylvania.", None, 'junk'),
    '1028':                                                     ("I bet you'd like to have more bombs.", None, 'junk'),
    '1029':                                                     ("When all else fails, use Fire.", None, 'junk'),
    '1030':                                                     ("Here's a hint, @. Don't be bad.", None, 'junk'),
    '1031':                                                     ("Game Over. Return of Ganon.", None, 'junk'),
    '1032':                                                     ("May the way of the Hero lead to the Triforce.", None, 'junk'),
    '1033':                                                     ("Can't find an item? Scan an Amiibo.", None, 'junk'),
    '1034':                                                     ("They say this game has just a few glitches.", None, 'junk'),
    '1035':                                                     ("BRRING BRRING This is Ulrira. Wrong number?", None, 'junk'),
    '1036':                                                     ("Tingle Tingle Kooloo Limpah", None, 'junk'),
    '1037':                                                     ("L is real 2041", None, 'junk'),
    '1038':                                                     ("They say that Ganondorf will appear in the next Mario Tennis.", None, 'junk'),
    '1039':                                                     ("Medigoron sells the earliest Breath of the Wild demo.", None, 'junk'),
    '1040':                                                     ("There's a reason why I am special inquisitor!", None, 'junk'),
    '1041':                                                     ("You were almost a @ sandwich.", None, 'junk'),
    '1042':                                                     ("I'm a helpful hint Gossip Stone!^See, I'm helping.", None, 'junk'),
    '1043':                                                     ("Dear @, please come to the castle. I've baked a cake for you.&Yours truly, princess Zelda.", None, 'junk'),
    '1044':                                                     ("They say all toasters toast toast.", None, 'junk'),
    '1045':                                                     ("They say that Okami is the best Zelda game.", None, 'junk'),
    '1046':                                                     ("They say that quest guidance can be found at a talking rock.", None, 'junk'),
    '1047':                                                     ("They say that the final item you're looking for can be found somewhere in Hyrule.", None, 'junk'),
    '1048':                                                     ("Mweep.^Mweep.^Mweep.^Mweep.^Mweep.^Mweep.^Mweep.^Mweep.^Mweep.^Mweep.^Mweep.^Mweep.", None, 'junk'),
    '1049':                                                     ("They say that Barinade fears Deku Nuts.", None, 'junk'),
    '1050':                                                     ("They say that Flare Dancers do not fear Goron-crafted blades.", None, 'junk'),
    '1051':                                                     ("They say that Morpha is easily trapped in a corner.", None, 'junk'),
    '1052':                                                     ("They say that Bongo Bongo really hates the cold.", None, 'junk'),
    '1053':                                                     ("They say that crouch stabs mimic the effects of your last attack.", None, 'junk'),
    '1054':                                                     ("They say that bombing the hole Volvagia last flew into can be rewarding.", None, 'junk'),
    '1055':                                                     ("They say that invisible ghosts can be exposed with Deku Nuts.", None, 'junk'),
    '1056':                                                     ("They say that the real Phantom Ganon is bright and loud.", None, 'junk'),
    '1057':                                                     ("They say that walking backwards is very fast.", None, 'junk'),
    '1058':                                                     ("They say that leaping above the Market entrance enriches most children.", None, 'junk'),
    '1059':                                                     ("They say that looking into darkness may find darkness looking back into you.", None, 'junk'),
    '1060':                                                     ("You found a spiritual Stone! By which I mean, I worship Nayru.", None, 'junk'),
    '1061':                                                     ("They say that the stick is mightier than the sword.", None, 'junk'),
    '1062':                                                     ("Open your eyes.^Open your eyes.^Wake up, @.", None, 'junk'),
    '1063':                                                     ("They say that arbitrary code execution leads to the credits sequence.", None, 'junk'),
    '1064':                                                     ("They say that Twinrova always casts the same spell the first three times.", None, 'junk'),
    '1065':                                                     ("They say that the Development branch may be unstable.", None, 'junk'),
    '1066':                                                     ("You're playing a Randomizer. I'm randomized!^Here's a random number:  #4#.&Enjoy your Randomizer!", None, 'junk'),
    '1067':                                                     ("They say Ganondorf's bolts can be reflected with glass or steel.", None, 'junk'),
    '1068':                                                     ("They say Ganon's tail is vulnerable to nuts, arrows, swords, explosives, hammers...^...sticks, seeds, boomerangs...^...rods, shovels, iron balls, angry bees...", None, 'junk'),
    '1069':                                                     ("They say that you're wasting time reading this hint, but I disagree. Talk to me again!", None, 'junk'),
    '1070':                                                     ("They say Ganondorf knows where to find the instrument of his doom.", None, 'junk'),

    'Deku Tree':                                                ("an ancient tree", "Deku Tree", 'dungeonName'),
    'Dodongos Cavern':                                          ("an immense cavern", "Dodongo's Cavern", 'dungeonName'),
    'Jabu Jabus Belly':                                         ("the belly of a deity", "Jabu Jabu's Belly", 'dungeonName'),
    'Forest Temple':                                            ("a deep forest", "Forest Temple", 'dungeonName'),
    'Fire Temple':                                              ("a high mountain", "Fire Temple", 'dungeonName'),
    'Water Temple':                                             ("a vast lake", "Water Temple", 'dungeonName'),
    'Shadow Temple':                                            ("the house of the dead", "Shadow Temple", 'dungeonName'),
    'Spirit Temple':                                            ("the goddess of the sand", "Spirit Temple", 'dungeonName'),
    'Ice Cavern':                                               ("a frozen maze", "Ice Cavern", 'dungeonName'),
    'Bottom of the Well':                                       ("a shadow\'s prison", "Bottom of the Well", 'dungeonName'),
    'Gerudo Training Grounds':                                  ("the test of thieves", "Gerudo Training Grounds", 'dungeonName'),
    'Ganons Castle':                                            ("a conquered citadel", "Ganon's Castle", 'dungeonName'),
    
    'Queen Gohma':                                              ("One inside an #ancient tree#...", "One in the #Deku Tree#...", 'boss'),
    'King Dodongo':                                             ("One within an #immense cavern#...", "One in #Dodongo's Cavern#...", 'boss'),
    'Barinade':                                                 ("One in the #belly of a deity#...", "One in #Jabu Jabu's Belly#...", 'boss'),
    'Phantom Ganon':                                            ("One in a #deep forest#...", "One in the #Forest Temple#...", 'boss'),
    'Volvagia':                                                 ("One on a #high mountain#...", "One in the #Fire Temple#...", 'boss'),
    'Morpha':                                                   ("One under a #vast lake#...", "One in the #Water Temple#...", 'boss'),
    'Bongo Bongo':                                              ("One within the #house of the dead#...", "One in the #Shadow Temple#...", 'boss'),
    'Twinrova':                                                 ("One inside a #goddess of the sand#...", "One in the #Spirit Temple#...", 'boss'),
    'Links Pocket':                                             ("One in #@'s pocket#...", "One #@ already has#...", 'boss'),

    'bridge_vanilla':                                           ("the #Shadow and Spirit Medallions# as well as the #Light Arrows#", None, 'bridge'),
    'bridge_stones':                                            ("all Spiritual Stones", None, 'bridge'),
    'bridge_medallions':                                        ("all Medallions", None, 'bridge'),
    'bridge_dungeons':                                          ("all Spiritual Stones and Medallions", None, 'bridge'),
    'bridge_tokens':                                            ("Gold Skulltula Tokens", None, 'bridge'),

    'ganonBK_dungeon':                                          ("hidden somewhere #inside its castle#", None, 'ganonBossKey'),
    'ganonBK_vanilla':                                          ("kept in a big chest #inside its tower#", None, 'ganonBossKey'),
    'ganonBK_keysanity':                                        ("hidden somewhere #in Hyrule#", None, 'ganonBossKey'),
    'ganonBK_triforce':                                         ("given to the Hero once the #Triforce# is completed", None, 'ganonBossKey'),

    'lacs_vanilla':                                             ("the #Shadow and Spirit Medallions#", None, 'lacs'),
    'lacs_medallions':                                          ("all Medallions", None, 'lacs'),
    'lacs_stones':                                              ("all Spiritual Stones", None, 'lacs'),
    'lacs_dungeons':                                            ("all Spiritual Stones and Medallions", None, 'lacs'),

    'Spiritual Stone Text Start':                               ("3 Spiritual Stones found in Hyrule...", None, 'altar'),
    'Child Altar Text End':                                     ("\x13\x08Ye who may become a Hero...&Stand with the Ocarina and&play the Song of Time.", None, 'altar'),
    'Adult Altar Text Start':                                   ("When evil rules all, an awakening&voice from the Sacred Realm will&call those destined to be Sages,&who dwell in the \x05\x41five temples\x05\x40.", None, 'altar'),

    'Validation Line':                                          ("Hmph... Since you made it this far,&I'll let you know what glorious&prize of Ganon's you likely&missed out on in my tower.^Behold...^", None, 'validation line'),
    'Light Arrow Location':                                     ("Ha ha ha... You'll never beat me by&reflecting my lightning bolts&and unleashing the arrows from&", None, 'Light Arrow Location'),
    '2001':                                                     ("Oh! It's @.&I was expecting someone called&Sheik. Do you know what&happened to them?", None, 'ganonLine'),
    '2002':                                                     ("I knew I shouldn't have put the key&on the other side of my door.", None, 'ganonLine'),
    '2003':                                                     ("Looks like it's time for a&round of tennis.", None, 'ganonLine'),
    '2004':                                                     ("You'll never deflect my bolts of&energy with your sword,&then shoot me with those Light&Arrows you happen to have.", None, 'ganonLine'),
    '2005':                                                     ("Why did I leave my trident&back in the desert?", None, 'ganonLine'),
    '2006':                                                     ("Zelda is probably going to do&something stupid, like send you&back to your own timeline.^So this is quite meaningless.&Do you really want&to save this moron?", None, 'ganonLine'),
    '2007':                                                     ("What about Zelda makes you think&she'd be a better ruler than I?^I saved Lon Lon Ranch,&fed the hungry,&and my castle floats.", None, 'ganonLine'),
    '2008':                                                     ("I've learned this spell,&it's really neat,&I'll keep it later&for your treat!", None, 'ganonLine'),
    '2009':                                                     ("Many tricks are up my sleeve,&to save yourself&you'd better leave!", None, 'ganonLine'),
    '2010':                                                     ("After what you did to&Koholint Island, how can&you call me the bad guy?", None, 'ganonLine'),
    '2011':                                                     ("Today, let's begin down&'The Hero is Defeated' timeline.", None, 'ganonLine'),
}


# This specifies which hints will never appear due to either having known or known useless contents or due to the locations not existing.
def hintExclusions(world, clear_cache=False):
    if not clear_cache and hintExclusions.exclusions is not None:
        return hintExclusions.exclusions

    hintExclusions.exclusions = []
    hintExclusions.exclusions.extend(world.disabled_locations)

    for location in world.get_locations():
        if location.locked:
            hintExclusions.exclusions.append(location.name)

    world_location_names = [
        location.name for location in world.get_locations()]

    location_hints = []
    for name in hintTable:
        hint = getHint(name, world.clearer_hints)
        if any(item in hint.type for item in 
                ['always',
                 'sometimes',
                 'overworld',
                 'dungeon',
                 'song']):
            location_hints.append(hint)

    for hint in location_hints:
        if hint.name not in world_location_names and hint.name not in hintExclusions.exclusions:
            hintExclusions.exclusions.append(hint.name)

    return hintExclusions.exclusions


hintExclusions.exclusions = None
