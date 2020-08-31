I am new at this but this branch contains rewritten JSON files for logic. My files are put within the `scenes` folder.
Only the JSON files have been rewritten and they contain some problems. So if you tried to make the randomizer, it would definitely not actually work.

They pave way for such features as lock rando, door rando, hybridized Vanilla/MQ dungeons, and MM integration to be accounted for in logic, although these features are unlikely to be added and they do not completely account for them either. In general, it makes it simple to account for more requirements of traversing each room if you can look at each room individually. It makes requirements for complex dungeons like Spirit Temple less confusing. Also, if the randomizer ever eventually becomes a mod, then this would make it easier to add a logical component to the scene data itself.

* All regions, including overworld regions, have been split into rooms and numbered. For the sake of door rando, I treated each room as if it was in a vacuum and went through them both ways to provide conditions regardless of what is required to access the room in vanilla. And even regardless of whether the transition to that room consists of a door. In dungeons, I made it so that the original and Master Quest versions have the same regions with the same names. I gave the regions names that made sense for both versions (haven't done this yet in Dodongo's Cavern for some reason)
  * This also allows for separating boss doors from boss rooms and allowing backwards entrance into dungeons, although this would be a strange feature, and you can't fly across the river in Shadow Temple.
* I did not change the names of any item locations. I did add stones/medallions as locations although that doesn't mean they have to be shuffled.
* Most dungeon rooms with enemies that unlock something have been made into events which will make swordless easier to add. Did the same for silver rupees for convenience.
* Made logic for Gerudo's Fortress/Thieves' Hideout, Ganon's Tower collapse, and boss rooms so they can be included in ER.
  * There is a glitch heart piece at the top of Gerudo's Fortress as child which I added as a location but commented out since it would be ER only.

### Logic helpers

* I did not edit `LogicHelpers.json` but have used these in the files.
* `transition()`: Represents doors and other room transitions in dungeons. The intent is that it should first check whether that door needs to be unlocked with a key. If not, the condition after the comma is required to go through the door (to unbar it). The key is checked first because a lock placed by door rando would replace the bars on both sides of the door.
* `barred_door`: I put this as an alternate condition on barred doors (meant to be false) before labeling the individual transitions. It remains on certain barred doors which turned out not to be actual transition actors such as in Ice Cavern. I might remove it.
* `can_climb()`: For every ledge that I could think to add it I counted the change in Link's Y coordinate and put it as a condition. I even included ledges that are too high for Link to ever climb. Why do this instead of just `is_adult` for those ledges that child cannot climb? Because the forms of Link in MM have different heights. Deku Link is very short and Fierce Deity Link is very tall. But I do not even know the exact heights or maximum climbing heights of any of the forms in OoT or MM. Also, in Glitched, ground jumps can be calculated into this because they allow Link to climb higher than normal.
* `can_fall`: I put this for some instances in which the player is required to fall a distance that they cannot roll out of. I don't know if this is necessary to put it as its own term or just use the regular assortment of no OHKO or Fairy or Nayru's Love (if that prevents fall damage) or use another condition like can_live_dmg but I put that there and I couldn't be bothered to change it before forking.
* `can_press_floor_switch`: Every time that Link has to step on a floor switch I put this condition, which is always true. What is the point? Because Deku Link in MM is too light to do so.
* `can_swim`: I only thought to add this condition late on and did not put it in most of the places where it belongs. It is always true although it would not be for Deku and Goron Link. I also did not account for the distances that Deku Link can skip across, or for Zora's ability to survive underwater, but I don't really care about those now.
* `can_wade()`: Not used anywhere but would be used for the height Link would have to be to walk in the water without swimming, which would be important for Goron Link who cannot swim. Or maybe this could be handled with parentheses after `can_swim`.
* `can_crouch`: I don't know if this is required in any other place than Deku Tree MQ basement but Link can lower his hitbox by guarding with sticks, hammer, or Giant's Knife/Biggoron's Sword, or with Hylian Shield as child.
* `can_play_underwater`: This would make it possible to lower Water Temple's water from high to medium. This is always false although Zora Link can do this and it also happens to be an option in MM randomizer for human Link.
* `can_hold_down_switch`: This refers to the ability to hold down blue switches without anything that exists in the room including Ruto. Always false, but examples of situations where this could be true include shared-world multiplayer, Elegy of Emptiness in MM, and Cane of Somaria in other games.
* `mm_ice_arrows`: This is OoT, not MM, so this can always be false, but I still made logic for what if Ice Arrows could freeze water like in MM. There is not even a mod to allow this, but I reasoned it out. This would have an effect in various rooms of Water Temple, most notably allowing the player to access the boss without Longshot. Also in Zora's River for bypassing rocks as child or freezing the waterfall, and in one room of Jabu-Jabu which has a gold skulltula in MQ.
* `mm_light_arrows`: Similar to the above, always false. Note that this might be a greater violation of Vanilla by allowing you to give the Breath of the Wild treatment to a puzzle in Ganon's Castle where you would actually have Light Arrows.
* `can_jumpslash_except_kokiri`: I put this on one gold skulltula in Spirit Temple because I could jumpslash it with everything else but not Kokiri Sword. I'm not sure if this needs to be its own condition really.
* `can_autojump`: It wasn't until after I wrote all this logic that I found out that Goron Link in fact cannot autojump. This condition is currently included only in Gerudo's Fortress. Technically this condition wouldn't be entirely meaningless without MM because the Kokiri Boots could be shuffled, but who would want to start with Iron or Hover Boots?
* `autojump_climb`: Similar to can_climb but only applies to ledges that Link can climb onto from an autojump. This also requires `can_autojump` to be true. This is separate from `can_climb` because the former instead allows other forms of "jumping" like ground jumps. But except in Gerudo's Fortress, no instances of `can_climb` have been replaced with this yet.

### New Tricks

* `logic_gf_roof_jump`: In Gerudo's Fortress, the wall of the lower southeast roof is too high for to climb onto from the lower roof with two doors, but Adult Link can jump off the roof from an angle and climb up with the increased height of the jump. This would be important in ER.
* `logic_zf_fairy_without_bombs`: In Zora's Fountain, Silver Gauntlets plus Hammer allows you to reveal a hole that you can jump into and grab onto the other edge of the hole and climb into the Great Fairy Fountain without blowing up the wall.
* `logic_water_cracked_wall_bombchu`: In the Water Temple, the cracked wall can be blown up with bombchus from the third floor, at any water level.

### Problems

* In general, many things that I didn't bother to figure out all the conditions for I went bleh. See "Missing Conditions" below.
* All these conditions will slow down generation.
* The `transition()` condition is meant to check the key status of each door on a separate json but I have written no such json, much less provided a way to handle lock rando logic without softlocks.
* Deku Tree MQ has requirements of using torch from outside the room. Though this might not matter without Door Rando.
* Jabu-Jabu non-MQ requires bringing Ruto to the branching hallways room to open some doors, although this is not NRA because the randomizer uses a patch to keep her from going away after the boss.
* Forest Temple twisting rooms hurt me especially when they both turned out to be a permanent flag in MQ only.
* Fire Temple has those hot rooms and if you go from one into another with Door Rando you absolutely need Goron Tunic but I didn't know how to represent this in a way that could work in door rando.
* Water Temple has the water levels which I split into 3 different regions for my sanity... This needs a lot of work to even work. Though maybe randomizing the starting water level might become a possibility?
  * If it is possible to keep track of the water level in a similar way to Link's age, then the 3 regions for each water level can be combined.
* Spirit Temple top floor mirrors wouldn't work in Door Rando since they would just reset.
* In the collapsing Ganon's Tower escape sequence, room 3 is the stairway that leads to the castle and room 0 is the room before it, but normally the bars in room 3 can only be opened when room 0 is entered the "proper" way. If room 3 was entered through cross-scene door rando then there would be no Zelda to open the bars. (Not a problem for non-cross-scene door rando because there are no other doors within the scene)
* Though even if we did have door rando some of those things that would be problems there could be worked around simply by not rando-ing those specific adjacent rooms and keeping them together always. And some may work in non-cross-scene door rando if it doesn't reload the scene and keeps flags.
* Did not yet integrate Glitched logic.

### Missing Conditions
* Deku Tree: None
* Deku Tree MQ
  * Room 4: Kill enemies
  * Room 6: Kill enemies
  * Room 10: Kill enemies
* Dodongo's Cavern
  * Room 3: Kill Lizalfos
  * Room 15: Kill Armos without Goron's Bracelet
* Dodongo's Cavern MQ
  * Room 3: Kill Lizalfos
  * Room 5: Kill Dodongos
  * Room 6: Kill Gohma Larvae
  * Room 8: Hit crystal switches
  * Room 12: Hit crystal switch
  * Room 13: Kill enemies
  * Room 14: Kill Poe
* Jabu-Jabu
  * Room 5: Kill Gold Skulltula
  * Room 6: Ruto and Big Octo
  * Room 7: Ruto
  * Room 9: Kill enemies
  * Room 12: Kill Shaboms
* Jabu-Jabu MQ
  * Room 6: Ruto and Big Octo
  * Room 14: Kill enemies
* Forest Temple
  * Room 18: Kill enemies
  * Room 21: Kill enemies
* Forest Temple MQ
  * Room 11: Hit crystal switch
  * Room 17: Hit crystal switch
  * Room 18: Kill ReDeads
  * Room 19: Straightening room
  * Room 20: Twisting room
  * Room 21: Kill enemies
* Fire Temple
  * Room 3: Kill Flare Dancer
  * Room 7: Kill Gold Skulltula
  * Room 15: Kill enemies
  * Room 18: Kill Gold Skulltula
  * Room 24: Kill Flare Dancer
* Fire Temple MQ
  * Room 3: Kill Flare Dancer
  * Room 15: Kill enemies
  * Room 18: Kill Iron Knuckle
  * Room 24: Kill Flare Dancer
* Water Temple
  * Room 8: Hit crystal switch
  * Room 9: Hit crystal switch
  * Room 13: Kill Dark Link
  * Room 18: Kill Shell Blades
  * Room 19: Kill enemies
* Water Temple MQ
  * Room 9: Hit crystal switch
  * Room 13: Kill Dark Link
  * Room 14: Kill Dodongos
  * Room 15: Hit crystal switch
  * Room 18: Kill enemies
* Spirit Temple
  * Room 1: Kill enemies
  * Room 5: Kill Gold Skulltula
  * Room 10: Kill Iron Knuckle
  * Room 20: Kill Iron Knuckle
  * Room 25: Hit crystal switch
* Spirit Temple MQ
  * Room 2: Kill Gibdos
  * Room 3: Kill Keese
  * Room 4: Hit crystal switch and kill enemies
  * Room 5: Kill Gold Skulltula
  * Room 10: Kill Iron Knuckle
  * Room 14: Kill Leevers
  * Room 18: Chest switch
  * Room 19: Kill invisible Floormaster
  * Room 20: Kill Iron Knuckle
* Shadow Temple
  * Room 1: Kill Keese and ReDead
  * Room 7: Kill Gibdos
  * Room 11: Kill ReDeads
  * Room 12: Get Gold Skulltula of this room
  * Room 14: Kill Keese and Gold Skulltula
  * Room 16: Kill enemies
  * Room 17: Kill invisible Floormasters
  * Room 19: Kill ReDeads
  * Room 20: Kill Gibdos
* Shadow Temple MQ
  * Room 1: Kill ReDead
  * Room 6: Kill Skulltulas
  * Room 7: Kill Gibdos
  * Room 9: Hit crystal switch
  * Room 11: Kill ReDeads
  * Room 20: Kill Gibdos
* Ice Cavern
  * Room 3: Break icicles
* Ice Cavern MQ
  * Room 3: Break icicles
  * Room 9: Kill Gold Skulltula
* Bottom of the Well: None
* Bottom of the Well MQ: None
* Gerudo Training Ground
  * Room 3: Kill Wolfos and White Wolfos
  * Room 5: Kill Torch Slugs and Keese
  * Room 10: Kill Like Likes
* Gerudo Training Ground MQ
  * Room 4: Hit crystal switch
  * Room 5: Kill Torch Slugs and Iron Knuckle
  * Room 10: Kill Freezards and Spikes
* Ganon's Castle
  * Room 2: Break icicles
  * Room 5: Kill Wolfos
  * Room 18: Hit crystal switches
* Ganon's Castle MQ
  * Room 0: Kill enemies
  * Room 2: Hit switch
  * Room 9: Kill enemies
  * Room 18: Hit crystal switch
* Ganon's Tower
  * Room 0: Kill Dinolfos
  * Room 4: Kill Iron Knuckles