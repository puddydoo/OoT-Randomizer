I am new at this but this branch contains rewritten JSON files for logic. My files are put within the `scenes` folder.
Only the JSON files have been rewritten and they contain some problems. So if you tried to make the randomizer, it would definitely not actually work.

They pave way for such features as lock rando, door rando, hybridized Vanilla/MQ dungeons, and MM integration to be accounted for in logic, although these features are unlikely to be added and they do not completely account for them either. In general, it makes it simple to account for more requirements of traversing each room if you can look at each room individually. Also, if the randomizer ever eventually becomes a mod, then this would make it easier to add a logical component to the scene data itself.

* All regions, including overworld regions, have been split into rooms and numbered. For the sake of door rando, I treated each room as if it was in a vacuum and went through them both ways to provide conditions regardless of what is required to access the room in vanilla. And even regardless of whether the transition to that room consists of a door. In dungeons, I made it so that the original and Master Quest versions have the same regions with the same names. I gave the regions names that made sense for both versions (haven't done this yet in Dodongo's Cavern for some reason)
  * This also allows for separating boss doors from boss rooms and allowing backwards entrance into dungeons, although this would be a strange feature, and you can't fly across the river in Shadow Temple.
* I did not change the names of any item locations. I did add stones/medallions as locations although that doesn't mean they have to be shuffled.
* Most dungeon rooms with enemies that unlock something have been made into events which will make swordless easier to add. Did the same for silver rupees for convenience.
* Made logic for Gerudo's Fortress/Thieves' Hideout, Ganon's Tower collapse, and boss rooms so they can be included in ER.
  * There is a glitch heart piece at the top of Gerudo's Fortress as child which I added as a location but commented out since it would be ER only.

### Logic helpers

* I did not edit `LogicHelpers.json` but have used these in the files.
* `transition()`: Represents doors and other room transitions in dungeons. The first argument is the name of the door (so it can check for key requirements) and the second is the conditions required to unbar it. If lock rando were to place a lock on a barred door then the "unbars" for both sides of the door would be applied. The key requirements are listed in `Door Requirements (Manual).txt`.
* Unbars: There are many "Unbar" conditions listed in `Unbars.txt` for each barred door in the dungeons, that if set to true, would allow going through that door without completing the normal requirements to unbar it (if the flag on the door is edited)
* `barred_door`: I put this as an alternate condition on barred doors (meant to be false) before labeling the individual transitions. It remains on certain barred doors which turned out not to be actual transition actors such as in Ice Cavern. I might remove it.
* `can_break_icicles`: The ability to break icicles. I don't know exactly what it requires, though.
* `can_climb()`: For every ledge that I could think to add it I counted the change in Link's Y coordinate and put it as a condition. I even included ledges that are too high for Link to ever climb. Why do this instead of just `is_adult` for those ledges that child cannot climb? Because the forms of Link in MM have different heights. Deku Link is very short and Fierce Deity Link is very tall. But I do not even know the exact heights or maximum climbing heights of any of the forms in OoT or MM. Also, in Glitched, ground jumps can be calculated into this because they allow Link to climb higher than normal.
* `can_fall`: I put this for some instances in which the player is required to fall a distance that they cannot roll out of. I don't know if this is necessary to put it as its own term or just use the regular assortment of no OHKO or Fairy or Nayru's Love (if that prevents fall damage) or use another condition like can_live_dmg but I put that there and I couldn't be bothered to change it before forking.
* `can_press_floor_switch`: Every time that Link has to step on a floor switch I put this condition, which is always true. What is the point? Because Deku Link in MM is too light to do so.
* `can_swim`: I only thought to add this condition late on and did not put it in most of the places where it belongs. It is always true although it would not be for Deku and Goron Link, or if Link only had Iron Boots and no way to go back to floating.
* `can_wade()`: Uses the depth of the water to check whether Link can wade in it without swimming or using Iron Boots. Deku and Goron Link can wade across water that is shallow enough. This does not account for Deku Link's ability to skip across a given body of water. Used less than `can_swim` so far. Child Link's limit seems to be around 32.
* `can_sink`: Equivalent to can_use(Iron_Boots) though it could also be used for Zora.
* `can_crouch`: I don't know if this is required in any other place than Deku Tree MQ basement but Link can lower his hitbox by guarding with sticks, hammer, or Giant's Knife/Biggoron's Sword, or with Hylian Shield as child.
* `can_play_underwater`: This would make it possible to lower Water Temple's water from high to medium. This is always false although Zora Link can do this and it also happens to be an option in MM randomizer for human Link.
* `can_hold_down_switch`: This refers to the ability to hold down blue switches without anything that exists in the room including Ruto. Always false, but examples of situations where this could be true include shared-world multiplayer, Elegy of Emptiness in MM, and Cane of Somaria in other games.
* `mm_ice_arrows`: This is OoT, not MM, so this can always be false, but I still made logic for what if Ice Arrows could freeze water like in MM. There is not even a mod to allow this, but I reasoned it out. This would have an effect in various rooms of Water Temple, most notably allowing the player to access the boss without Longshot. Also in Zora's River for bypassing rocks as child or freezing the waterfall, and in one room of Jabu-Jabu which has a gold skulltula in MQ.
* `mm_light_arrows`: Similar to the above, always false. Note that this might be a greater violation of Vanilla by allowing you to give the Breath of the Wild treatment to a puzzle in Ganon's Castle where you would actually have Light Arrows.
* `can_jumpslash_except_kokiri`: I put this on one gold skulltula in Spirit Temple because I could jumpslash it with everything else but not Kokiri Sword. I'm not sure if this needs to be its own condition really.
* `can_autojump`: It wasn't until after I wrote all this logic that I found out that Goron Link in fact cannot autojump. This condition is currently included only in Gerudo's Fortress. Technically this condition wouldn't be entirely meaningless without MM because the Kokiri Boots could be shuffled, but who would want to start with Iron or Hover Boots?
* `autojump_climb()`: Similar to `can_climb` but only applies to ledges that Link can climb onto from an autojump. This also requires `can_autojump` to be true. This is separate from `can_climb` because the former instead allows other forms of "jumping" like ground jumps. But except in Gerudo's Fortress, no instances of `can_climb` have been replaced with this yet.
* `can_climb_with_flower()`: Similar to can_climb but there is a bomb flower that Link can use to do a ground jump without bombs. Not used anywhere yet.
* `shuffle_spirit_hands`: Condition that logically allows the hands of Spirit Temple to be shuffled in ER. This is (I think fully) covered in vanilla spirit temple logic including glitched, but MQ is incomplete.
* `is_past`, `is_future`: I had the idea to replace many instances of `is_child` and `is_adult` to distinguish age restrictions that are related to the scene setup, but have only done so in a few places so far.

### Glitch conditions
As part of an effort to integrate glitched logic with the regular logic, there must be conditions that enable certain glitches.
* `glitch_hover`: Enables hovering. Usually used in a "not" context because can_hover can usually be used instead.
* `glitch_mega`
* `glitch_weirdshot`
* `glitch_unknown`: Used when I could not identify what the glitch was supposed to be. They will eventually be replaced with the type of glitch that they are.
 * `glitch_unk_spirit_block_adult_shield_skip`: Spirit Temple glitch that can bypass block as adult using shield.
 * `glitch_unk_spirit_crawl_hover_boots`: Use hover boots to go through first spirit temple crawlspace as adult
 * `glitch_unk_spirit_crawl_hover_boots_2`: Use hover boots to go through second spirit temple crawlspace as adult
* `glitch_spirit_block_hover_boots_skip`: Glitch taking advantage of collision to bypass block using hover boots
* `glitch_spirit_statue_climb`: Allows climbing from one side of the statue to the other.

### New Tricks

* `logic_gf_roof_jump`: In Gerudo's Fortress, the wall of the lower southeast roof is too high for to climb onto from the lower roof with two doors, but Adult Link can jump off the roof from an angle and climb up with the increased height of the jump. This would be important in ER.
* `logic_zf_fairy_without_bombs`: In Zora's Fountain, Silver Gauntlets plus Hammer allows you to reveal a hole that you can jump into and grab onto the other edge of the hole and climb into the Great Fairy Fountain without blowing up the wall.
* `logic_water_cracked_wall_bombchu`: In the Water Temple, the cracked wall can be blown up with bombchus from the third floor, at any water level.
* `logic_zd_gs_bombs`: The Gold Skulltula in Zora's Domain can be killed with a carefully aimed bomb or bombchu.
* `logic_zd_dins_fire`: The torches in Zora's Domain can be lit with Din's Fire by making the most of its range.

### Problems

* Many locations are in multiple regions.
* Spitit Temple logic with shuffled hands should be changed due to the fact that savewarping takes you to the normal entrance.
* Dungeons have missing conditions that aren't completely filled out, mainly enemies. See "Missing Conditions" below.
* All these conditions will slow down generation.
* Every once in a while I find a formatting error or something from vanilla accidentally copied in MQ and there are probably some left in the ones I haven't revisited in a while.
* Door rando, lock rando, and hybrid dungeons are not logically possible without either removing keys or rewriting key logic to be automatic. But until that ever happens, I am making a list of manual door requirements in `Door Requirements (Manual).txt` so that the `transition()` condition might work without those features.
* Deku Tree MQ has requirements of using torch from outside the room. Though this might not matter without Door Rando.
* Jabu-Jabu non-MQ requires bringing Ruto to the branching hallways room to open some doors, although this is not NRA because the randomizer uses a patch to keep her from going away after the boss.
* Forest Temple twisting rooms hurt me especially when they both turned out to be a permanent flag in MQ only.
* Fire Temple has those hot rooms and if you go from one into another with Door Rando you absolutely need Goron Tunic but I didn't know how to represent this in a way that could work in door rando.
* Water Temple requires the water level to be kept track of in a similar way to Link's age. If so, the starting water level can also be shuffled. I first split each region into 3 separate regions for each water level but later merged them together and added conditions for water level. Many of the locations and events need to require the current water level to be repeatable.
* In the collapsing Ganon's Tower escape sequence, room 3 is the stairway that leads to the castle and room 0 is the room before it, but normally the bars in room 3 can only be opened when room 0 is entered the "proper" way. If room 3 was entered through cross-scene door rando then there would be no Zelda to open the bars. (Not a problem for non-cross-scene door rando because there are no other doors within the scene)
* Though even if we did have door rando some of those things that would be problems there could be worked around simply by not rando-ing those specific adjacent rooms and keeping them together always. And some may work in non-cross-scene door rando if it doesn't reload the scene and keeps flags.
* Did not yet integrate Glitched logic, except in vanilla Spirit Temple

### Missing Conditions
* Deku Tree: None
* Deku Tree MQ: None
* Dodongo's Cavern
  * Room 3: Kill Lizalfos
  * Room 15: Kill Armos without Goron's Bracelet
* Dodongo's Cavern MQ
  * Room 3: Kill Lizalfos
  * Room 5: Kill Dodongos
  * Room 6: Kill Gohma Larvae
  * Room 8: Kill Armos as child to blow up wall bombs
  * Room 13: Kill Mad Scrubs and Keese
  * Room 14: Kill Poe
* Jabu-Jabu
  * Room 6: Ruto and Big Octo
  * Room 9: Kill Stingers
  * Room 12: Kill Shaboms
* Jabu-Jabu MQ
  * Room 6: Ruto and Big Octo
  * Room 14: Kill Like Like and Stingers
* Forest Temple
  * Room 18: Kill Floormaster
  * Room 21: Kill Blue Bubbles
* Forest Temple MQ
  * Room 18: Kill ReDeads
  * Room 19: Straightening room
  * Room 20: Twisting room
  * Room 21: Kill Floormaster
* Fire Temple
  * Room 3: Kill Flare Dancer
  * Room 15: Kill Torch SLugs and Fire Keese
  * Room 24: Kill Flare Dancer
* Fire Temple MQ
  * Room 3: Kill Flare Dancer
  * Room 18: Kill Iron Knuckle
  * Room 24: Kill Flare Dancer
* Water Temple
  * Room 13: Kill Dark Link
  * Room 18: Kill Shell Blades
  * Room 19: Kill Spikes
* Water Temple MQ
  * Room 13: Kill Dark Link
  * Room 14: Kill Dodongos
  * Room 18: Kill Spike and Lizalfos
* Spirit Temple
  * Room 1: Kill Keese, Fire Keese, and Armos
  * Room 10: Kill Iron Knuckle
  * Room 20: Kill Iron Knuckle
* Spirit Temple MQ
  * Room 2: Kill Gibdos
  * Room 3: Kill Keese
  * Room 4: Kill Like like, Baby Dodongos, and Beamos
  * Room 10: Kill Iron Knuckle
  * Room 14: Kill Leevers
  * Room 19: Kill invisible Floormaster
  * Room 20: Kill Iron Knuckle
* Shadow Temple
  * Room 1: Kill Keese and ReDead
  * Room 7: Kill Gibdos
  * Room 11: Kill ReDeads
  * Room 14: Kill Keese and Gold Skulltula
  * Room 16: Kill Like Like and Keese
  * Room 17: Kill invisible Floormasters
  * Room 19: Kill ReDeads
  * Room 20: Kill Gibdos
* Shadow Temple MQ
  * Room 1: Kill ReDead
  * Room 6: Kill Skulltulas
  * Room 7: Kill Gibdos
  * Room 11: Kill ReDeads
  * Room 20: Kill Gibdos
* Ice Cavern: None
* Ice Cavern MQ: None
* Bottom of the Well: None
* Bottom of the Well MQ: None
* Gerudo Training Ground
  * Room 3: Kill Wolfos and White Wolfos
  * Room 5: Kill Torch Slugs and Keese
  * Room 10: Kill Like Likes
* Gerudo Training Ground MQ
  * Room 5: Kill Torch Slugs and Iron Knuckle
  * Room 10: Kill Freezards and Spikes
* Ganon's Castle
  * Room 5: Kill Wolfos
* Ganon's Castle MQ
  * Room 0: Kill Green Bubbles, Armos, and Iron Knuckle
  * Room 9: Kill Dinolfos and Torch Slugs
* Ganon's Tower
  * Room 0: Kill Dinolfos
  * Room 4: Kill Iron Knuckles