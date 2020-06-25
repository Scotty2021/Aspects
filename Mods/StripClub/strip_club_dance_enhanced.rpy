# override standard strip club dance to remove randomness of performer on stage

init 5 python:
    config.label_overrides["stripclub_dance"] = "stripclub_dance_enhanced_label"

    def update_strip_club_rotation():
        rotation = [x.identifier for x in stripclub_strippers]
        renpy.random.shuffle(rotation)
        mc.business.event_triggers_dict["stripper_rotation_changed"] = day
        mc.business.event_triggers_dict["stripper_rotation"] = rotation
        mc.business.event_triggers_dict["stripper_number"] = 0
        return rotation

    def get_next_stripper():
        if mc.business.event_triggers_dict.get("stripper_rotation_changed", 0) != day:
            update_strip_club_rotation()    # rotation changes daily

        rotation = mc.business.event_triggers_dict.get("stripper_rotation", None)
        if not rotation:
            rotation = update_strip_club_rotation()

        stripper = None
        while not stripper:
            current = mc.business.event_triggers_dict.get("stripper_number", 0) + 1
            if current > len(stripclub_strippers):
                current = 1

            mc.business.event_triggers_dict["stripper_number"] = current
            # select stripper from girls working right now
            stripper = find_in_list(lambda x: x.identifier == rotation[current-1], [x for x in stripclub_strippers if x in mc.location.people])

        return stripper


label stripclub_dance_enhanced_label():
    #Watch a dance at the strip club.
    #-> You sit down and watch. A girl (generate a list of girls at the club) comes out wearing one of several special outfits.
    #-> She poses a few times. Each time you can tip her or just watch.
    #-> If you tip enough she strips off her bra and/or panties.
    #-> When she ends her dance, if you've paid enough she may ask if you want to come back for a private lap dance.
    #-> Lap dance scene may just turn into sex.

    "You take a seat near the edge of the stage and wait for the next performer."

    $ the_person = get_next_stripper()
    $ the_person.apply_outfit(stripclub_wardrobe.pick_random_outfit())

    $ title = the_person.title
    $ the_person.draw_person()
    "A new song starts playing over the speakers and a girl steps out onto the stage."
    if title is not None:
        if cousin_role in the_person.special_role:
            if the_person.event_triggers_dict.get("blackmail_level",-1) < 2 and not the_person.event_triggers_dict.get("seen_cousin_stripping",False):
                $ add_cousin_blackmail_2_confront_action()

                "It takes you a moment to recognize your cousin, [the_person.title], as she struts out onto the stage."
                if not the_person.event_triggers_dict.get("found_stripping_clue", False):
                    "[the_person.possessive_title]'s late nights and secret keeping suddenly make a lot more sense."

                "With the glare of the stage lights it's likely she won't be able to see who you are, but you can talk to her later and use this as leverage to blackmail her."

            else:
                "You recognize your cousin almost as soon as she steps onto the stage."

        elif sister_role in the_person.special_role:
            "You recognize your little sister almost as soon as she steps onto the stage."

        elif aunt_role in the_person.special_role:
            "You recognize your aunt as she steps into the stage spotlights."

        elif mother_role in the_person.special_role:
            "You recognize your mother as soon as she steps into the stage spotlight."

        elif employee_role in the_person.special_role:
            "You recognize [title] as one of your employees."

        else:
            "You recognize her as [title]."

        $ title = the_person.possessive_title #Change to their possessive title, because that sounds better in the following dialogue

    else:
        $ title = the_person.create_formatted_title("The stripper")
    "She poses for a moment, and the crowd cheers around you. Then she starts to strut down the walkway."
    "She stops at the end of the stage, surrounded on three sides by eagerly watching men."
    "[title] starts to dance to the music, swinging her hips and turning slowly to show herself off to all members of the crowd."
    call stripshow_strip(the_person) from _call_stripshow_strip_dance_enhanced
    $ the_person.draw_person(position = "back_peek")
    "She spins and poses for her audience, who respond with whoops and cheers."
    call stripshow_strip(the_person) from _call_stripshow_strip_dance_enhanced_1
    if the_person.has_large_tits():
        if the_person.outfit.tits_available():
            "As the music builds, [title]'s dance becomes more energetic. Her big tits bounce and jiggle in rhythm with her movements."
        else:
            "As the music builds, [title]'s dance becomes more energetic. Her big tits bounce and jiggle, looking almost desperate to escape."
    else:
        "As the music builds, [title]'s dance becomes more energetic. She runs her hands over her tight body, accentuating her curves."
    call stripshow_strip(the_person) from _call_stripshow_strip_dance_enhanced_2
    $ the_person.draw_person(position = get_random_from_list(cousin_strip_pose_list), the_animation = blowjob_bob, animation_effect_strength = 0.7)
    "Her music hits its crescendo and her dancing does the same. [title] holds onto the pole in the middle of the stage and spins herself around it."
    call stripshow_strip(the_person) from _call_stripshow_strip_dance_enhanced_3
    $ the_person.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 0.8)
    if the_person.outfit.vagina_visible():
        "As the song comes to an end, the dancer lowers herself to all fours, showing off her ass and pussy to the crowd."
    else:
        "As the song comes to an end, the dancer lowers herself to all fours. She spreads her legs and works her hips, jiggling her ass for the crowd's amusement."

    $ the_person.draw_person()
    "She stands up and waves to her audience."
    the_person.char "Thank you everyone, you've been wonderful!"
    $ the_person.draw_person(position = "walking_away")
    "[title] blows a kiss and struts off stage."

    $ the_person.apply_planned_outfit()
    $ renpy.scene("Active")
    return
