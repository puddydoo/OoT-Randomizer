I am new at this but this branch contains rewritten JSON files for logic. My files are put within the `data/scenes` folder.
Only the JSON files have been rewritten and they contain some problems. So if you tried to make the randomizer, it would definitely not actually work.

They pave way for such features as lock rando, door rando, hybridized Vanilla/MQ dungeons, and MM integration to be accounted for in logic, although these features are unlikely to be added and they do not completely account for them either. In general, it makes it simple to account for more requirements of traversing each room if you can look at each room individually. It makes requirements for complex dungeons like Spirit Temple less confusing. Also, if the randomizer ever eventually becomes a mod, then this would make it easier to add a logical component to the scene data itself.

* All regions, including overworld regions, have been split into rooms and numbered. For the sake of door rando, I treated each room as if it was in a vacuum and went through them both ways to provide conditions regardless of what is required to access the room in vanilla. And even regardless of whether the transition to that room consists of a door. In dungeons, every region has the same name for both the original and Master Quest and I gave them names that made sense for both versions (haven't done the latter yet in Dodongo's Cavern or Bottom of the Well for some reason)
  * This also allows for separating boss doors from boss rooms and allowing backwards entrance into dungeons, although this would be a strange feature, and you can't fly across the river in Shadow Temple.
* Most dungeon rooms with enemies that unlock something have been made into events which will make swordless easier to add. Did the same for silver rupees for convenience.
* Made logic for Gerudo's Fortress/Thieves' Hideout, Ganon's Tower collapse, and boss rooms so they can be included in ER.

### Logic helpers

* I did not edit `LogicHelpers.json` but have used these in the files.
* `barred_door`: When a door can be barred for any reason, I put this as an alternate condition on that exit. This is meant to be false. Perhaps this would make it possible to have all barred doors open automatically or split it up for each barred door in the game. The ones in Ice Cavern and Jabu-Jabu are different from the standard barred doors and might need to be separate things but I didn't.
* `can_climb()`: For every ledge that I could think to add it I counted the change in Link's Y coordinate and put it as a condition. Why do this instead of just is_adult for those ledges that child cannot climb? Because the forms of Link in MM have different heights. Deku Link is very short and Fierce Deity Link is very tall. But I do not even know the exact heights or maximum climbing heights of any of the forms in OoT or MM.
* `can_fall`: I put this for some instances in which the player is required to fall a distance that they cannot roll out of. I don't know if this is necessary to put it as its own term or just use the regular assortment of no OHKO or Fairy or Nayru's Love (if that prevents fall damage) but I put that there and I couldn't be bothered to change it before forking.
* `can_press_floor_switch`: Every time that Link has to step on a floor switch I put this condition, which is always true. What is the point? Because Deku Link in MM is too light to do so.
* `can_swim`: I only thought to add this condition late on and did not put it in most of the places where it belongs. It is always true although it would not be for Deku and Goron Link. I also did not account for the heights that Goron Link can stand in without drowning or the distances that Deku Link can skip across, or for Zora's ability to survive underwater, but I don't really care about those now.
* `can_crouch`: I don't know if this is required in any other place than Deku Tree MQ basement but Link can lower his hitbox by guarding with sticks, hammer, or Giant's Knife/Biggoron's Sword, or with Hylian Shield as child.
* `can_play_underwater`: This would make it possible to lower Water Temple's water from high to medium. This is always false although Zora Link can do this and it also happens to be an option in MM randomizer for human Link.
* `can_hold_down_switch`: This refers to the ability to hold down blue switches without anything that exists in the room including Ruto. Always false, but examples of situations where this could be true include shared-world multiplayer, Elegy of Emptiness in MM, and Cane of Somaria in other games.
* `mm_ice_arrows`: This is OoT, not MM, so this can always be false, but I still made logic for what if Ice Arrows could freeze water like in MM. This would have an effect in various rooms of Water Temple most notably allowing the player to access the boss without Longshot. Also in Zora's River for bypassing rocks as child or freezing the waterfall, and in one room of Jabu-Jabu which has a gold skulltula in MQ.
* `mm_light_arrows`: Similar to the above, always false. Note that this might be a greater violation of Vanilla by allowing you to give the BotW treatment to a puzzle in Ganon's Castle where you would actually have Light Arrows.
* `can_jumpslash_except_kokiri`: I put this on one gold skulltula in Spirit Temple because I could jumpslash it with everything else but not Kokiri Sword. I'm not sure if this needs to be its own condition really.

### New Tricks

* Trick to climb Gerudo Fortress: The wall of the lower southeast roof is too high for Adult Link to climb onto from the lower roof with two doors, but it is possible to jump off the roof from an angle and climb up with the increased height of the jump.
* `logic_zf_fairy_without_bombs`: In Zora's Fountain, Silver Gauntlets plus Hammer allows you to reveal a hole that you can jump into and grab onto the other edge of the hole and climb into the Great Fairy Fountain without blowing up the wall.
* `logic_water_cracked_wall_bombchu`: In the Water Temple, the cracked wall can be blown up with bombchus from the third floor, at any water level.

### Problems

* In general, many things that I didn't bother to figure out all the conditions for I went bleh.
* All these conditions will slow down generation.
* I put a single key as a requirement for each locked door and the logic doesn't currently tally them. In general, it will be necessary for lock rando to introduce some representation for doors into these JSON files but since I couldn't decide on how to do that I just used the exits for now. Whenever I got to the other side of a key door I put "Still_a_key" or some such there.
* Deku Tree MQ has requirements of using torch from outside the room. Though this might not matter without Door Rando.
* Jabu-Jabu has Ruto and I couldn't decide how to handle this as a condition since she goes away so that would be technically NRA. Not as much of a problem without door rando though.
* Forest Temple twisting rooms hurt me especially when they both turned out to be a permanent flag in MQ only.
* Fire Temple has those hot rooms and if you go from one into another with Door Rando you absolutely need Goron Tunic but I didn't know how to represent this in a way that could work in door rando.
* Water Temple has the water levels which I split into 3 different regions for my sanity... This needs a lot of work to even work. Though maybe randomizing the starting water level might become a possibility?
* Spirit Temple top floor mirrors wouldn't work in Door Rando.
* Though even if we did have door rando some of those things that would be problems there could be worked around simply by not rando-ing those specific adjacent rooms.
* Did not yet integrate Glitched logic.