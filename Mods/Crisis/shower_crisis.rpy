## Morning Shower Crisis Mod by Tristimdorion
# Based on the Pilotus13 Vanilla extension
init -1 python:
    shower_mod_weight = 5

init 2 python:
    def shower_crisis_requirement():
        if mc_at_home() and time_of_day == 0:
            return True
        return False

    def shower_mod_initialization(self):
        # add home shower to active places
        list_of_places.append(home_shower)
        home_shower.link_locations(hall)
        return

    shower_crisis_action = ActionMod("Morning Shower", shower_crisis_requirement,"shower_crisis_action_label", initialization = shower_mod_initialization,
        menu_tooltip = "In the morning you notice the door to shower is open and someone is in there.", category="Home", is_crisis = True, is_morning_crisis = True, crisis_weight = shower_mod_weight)

label shower_crisis_action_label:
    ## Someone is taking a shower
    $ the_person = get_random_from_list(people_in_mc_home()) #Checks all the rooms in player's home

    "While walking around the house, you hear the shower running and notice that the bathroom door is not fully closed."
    menu:
        "Take a peek?":
            pass
        "Ignore it.":
            return
    "You decide to take a peek."
    $ change_scene_display(home_shower)
    $ the_person.draw_person(position = "walking_away")
    "You see [the_person.possessive_title] is standing in front of a mirror, getting ready for a shower."
    $ shower_clothing = the_person.outfit.remove_random_any(top_layer_first = True)
    while shower_clothing is not None:
        "You see [the_person.possessive_title] undressing, taking off her [shower_clothing.name]"
        $ the_person.draw_animated_removal(shower_clothing, position = "walking_away")
        $ shower_clothing = the_person.outfit.remove_random_any(top_layer_first = True)
    "Now completely nude, she gets into the shower."
    "You see the water running down her chest."
    $ the_person.draw_person(position = "stand3", emotion = "happy")
    "[the_person.possessive_title] turns around, with the water now going on her back and firm ass."
    if the_person.has_large_tits():
        "You can't help but admire [the_person.possessive_title]'s great body and tits."
        "Just as this thought flashes through your mind, she starts rubbing her boobs."
    else:
        "You can't help but admire [the_person.possessive_title]'s slim body and perky tits."
        "Just as this thought flashes through your mind, she starts rubbing her breasts, pinching her small nipples."
    $ the_person.change_arousal(renpy.random.randint(10,50))
    if the_person.sluttiness >=50 or the_person.get_opinion_score("masturbating") > 0 or the_person.arousal > 35:
        "The warmth of the water and her caresses seem to turn [the_person.possessive_title] on."
        $ the_person.draw_person(position = "missionary")
        "She sits on the shower floor, spreads her legs and begins to masturbate with her hand."
        while the_person.arousal < 100:
            $ rand_chance = renpy.random.randint(0,4)
            if rand_chance == 0:
                "[the_person.possessive_title] rubs her clit and her moans grow louder."
            elif rand_chance == 1:
                "As she gets more and more turned on, her hand is moving faster and faster."
            elif rand_chance == 2:
                "She pushes 3 fingers inside, making a deep guttural noise."
                the_person.char "Ahh, yes. Fuck me hard and deep."
            elif rand_chance == 3:
                if the_person.get_opinion_score("anal sex") > 0:
                    "She slow pushes a finger in her rectum..."
                    the_person.char "Mmmm, yes, make me your little anal slut."
                else:
                    "[the_person.possessive_title] moves two fingers along her labia, quietly moaning with pleasure."
            else:
                if the_person.get_opinion_score("being submissive") > 0:
                    "[the_person.possessive_title] pinches her nipples hard, wincing from excitement and pain."
                else:
                    if the_person.has_large_tits():
                        "With one hand she softly squeezes her large breast."
                    else:
                        "With one hand she squeezes het perky little breast."
            $ the_person.change_arousal(renpy.random.randint(20,35))
        the_person.char "Shit, I'm cumming!"
        $ the_person.draw_person(position = "missionary", emotion = "orgasm")
        "You see [the_person.possessive_title]'s body shiver as she reaches orgasm."
        the_person.char "Wow, that was intense. Need to be quieter or someone might just hear me."
        $ the_person.draw_person(position = "walking_away")
        "She gets up and returns to washing her body."
        "You see her love juices mixing with the water dripping on the floor."
        $ the_person.reset_arousal()
        $ the_person.change_stats(arousal = renpy.random.randint(10,50), slut_temp = renpy.random.randint(2,5))
    else:
        pass
    menu:
        "Join her." if mc.current_stamina > 0:
            "You decide to use this opportunity and join her."
            mc.name "The door was not closed, how about we shower together, [the_person.title]?"
            if the_person.sluttiness > 70 or the_person.arousal > 35:
                $ the_person.draw_person(position = "back_peek", emotion = "happy")
                "[the_person.possessive_title] turns her head when she hears your voice. You see her smile."
                the_person.char "Well, that sounds like a plan, [the_person.mc_title]. Come on, get in here."
                "You quickly take off your clothes and step into the shower."
                "[the_person.possessive_title] stands still as you hug her from behind. Your erect dick pushing against her bottom."
                the_person.char "Ow, I feel that someone is happy to see me. Why don't you slide it in?"
                # move to shower for fucking, then go back to original location
                $ current_location = mc.location
                $ mc.location = home_shower
                call fuck_person(the_person) from _call_fuck_person_shower
                $ mc.location = current_location
            else:
                $ the_person.draw_person(position = "back_peek", emotion = "angry")
                "[the_person.possessive_title] quickly turns her head, you see the rage on her face."
                the_person.char "What the fuck, [the_person.mc_title]? Can't you see I'm naked here? Get lost, you perv!"
                "You quickly leave the bathroom."
                $ the_person.happiness -= 5
        "Join her. (disabled)" if not mc.current_stamina > 0:
            pass
        "Walk away":
            "You decide not to disturb her and just walk away."

    python:
        the_person.reset_arousal()
        the_person.review_outfit(show_review_message = False) #Make sure to reset her outfit so she is dressed properly.
        change_scene_display(mc.location)
        # Release variables
        del shower_clothing
        renpy.scene("Active")
    return
