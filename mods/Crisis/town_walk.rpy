## Town walk event
init -1 python:
    town_walk_mod_init = False
    town_walk_mod_weight = 5

init 2 python:
    def town_walk_mod_init_requirement():
        if town_walk_mod_init == False:
            return True
        return False

    def town_walk_crisis_requirement():
        if not mc.business.is_weekend(): # we only take a lunch break on weekdays
            if time_of_day == 2:
                return True
        return False

    town_walk_mod_init_event = Action("Town Walk Mod Initialization Event", town_walk_mod_init_requirement, "town_walk_mod_init_label")

    if not town_walk_mod_init_event in mod_list:
        mod_list.append(town_walk_mod_init_event)
        
label town_walk_mod_init_label:
    python:
        town_walk_crisis = Action("Town Walk Crisis",town_walk_crisis_requirement,"town_walk_action_description")

        if not town_walk_crisis in crisis_list[0]:
            crisis_list.append([town_walk_crisis,town_walk_mod_weight])
    
        town_walk_mod_init = True
    
    #if town_walk_mod_init:
    #    "Town Walk Mod Initialization is complete."
    return

label town_walk_action_description:
    call town_walk_crisis_action from _call_town_walk_crisis_action_1
    return
    
label town_walk_crisis_action:
    ## You spy on a neighbour during your town walk activities
    $ exclude_list = [mom, lily, mc] # exclude family and MC
    if mc.business.is_open_for_business() and not mc.business.is_weekend(): # exclude employees working on weekdays
        $ exclude_list.append(mc.business.get_employee_list())

    $ the_person = get_random_person_in_the_game(excluded_people=exclude_list)
    "While walking around the town, you see that the window in [the_person.name]'s house is open you get closer and peek inside."
    $ change_scene_display(bedroom)
    show screen person_info_ui(the_person)
    $ the_person.draw_person(position = "walking_away")
    "You see [the_person.name] is standing in front of a mirror, studing herself."
    "There is a glass of water right near the window. This is a good opportunity to test a serum for free."
    menu:
        "Add a dose of serum to [the_person.name]'s drink.":
            call give_serum(the_person) from _call_give_serum_P13N1
            "You quickly retreat away from the window."           
        "Keep watching.":
            "You decide not to risk being seen and stay away from her sight"
    the_person.char "I shoud get dresed for lunch. Don't have much time..."
    
    $ spy_clothing = the_person.outfit.get_copy()    
    $ the_clothing = spy_clothing.remove_random_any(top_layer_first = True, exclude_feet = True) #Remove something from our spy outfit.
    $ removed_clothing = False
    while the_clothing and the_person.judge_outfit(spy_clothing, temp_sluttiness_boost = 0): 
        #This will loop over and over until she is out of things to remove OR nolonger can strip something that is appropriate.
        #Note: there can be some variation in this event depending on if the upper or lower was randomly checked first.
        $ the_person.draw_animated_removal(the_clothing) #Draw the item being removed from our current outfit
        $ the_person.outfit = spy_clothing.get_copy() #Swap our current outfit out for the spy outfit.
        $ random_strip_descrip = renpy.random.randint(0,4)
        $ removed_clothing = True
        if random_strip_descrip == 0:
            "[the_person.name] takes off her [the_clothing.name] and throws it on the bed."
        elif random_strip_descrip == 1:
            "[the_person.name] keeps going and drops her [the_clothing.name]."
        elif random_strip_descrip == 2:
            "[the_person.name] strips off her [the_clothing.name] and tosses it to the side."
        elif random_strip_descrip == 3:
            "[the_person.name] removes her [the_clothing.name] and drops it to the floor."
        else: # random_strip_descrip == 4:
            "[the_person.name] quickly slides off her [the_clothing.name] and leaves it on the ground."
        $ the_clothing = spy_clothing.remove_random_any(top_layer_first = True, exclude_feet = True)
    
    if the_person.outfit.vagina_available():
        "You see that [the_person.name] also studies her pussy."
        if the_person.age <=30:
            the_person.char "Nicely shaven and clean, ready to go."
        else:
            the_person.char "Well, [the_person.name]. Even at [the_person.age] that pussy looks delicious."
        "She moves her hand between her legs, just teasing herself."
        $ arousal_plus = renpy.random.randint (20,50)
        $ the_person.change_arousal (arousal_plus)
    elif the_person.outfit.tits_available():
        "You see that [the_person.name] is looking at her breasts."
        if the_person.age <=30:
            the_person.char "Darn girl, these puppies look delightful :)"
        else:
            the_person.char "Good to know that even at [the_person.age] my chest is attractive."
        "She plays with her boobs a little, cuping them, and pinching the nipples so they get hard."
        $ arousal_plus = renpy.random.randint (10,40)
        $ the_person.change_arousal (arousal_plus)
    elif removed_clothing:
        "[the_person.name] only took off her top clothes, you just wonder why..."
    else:
        "[the_person.name] is just standing in front of the mirror."

    if the_person.sluttiness >=50 or the_person.get_opinion_score("masturbating") > 0 or the_person.arousal > 35:
        "[the_person.name] seems to get turned on by her own image in the mirror."
        $ the_person.draw_person(position = "missionary")
        "She lays down on the bed, spreads her legs and begins to slowly masturbate."
        if the_person.outfit.vagina_available():
            "You notice that she fingering herself with one hand, while the other is caressing the clit."
        else:
            "You notice that with one hand [the_person.name] squeezes her tits, while shoving the other between her legs."
        while the_person.arousal < 100:
            $ random_mast_descrip = renpy.random.randint(0,3)
            if random_mast_descrip == 0:
                "As she gets more and more turned on, her hand is moving faster and faster."
            elif random_mast_descrip == 1:
                if the_person.outfit.vagina_available():
                    "Her both hands move really fast around her wide-spread pussy."
                else:
                    "[the_person.name] pinches her nipples and squeezing the other vigorously between her legs."
                the_person.char "Ahh, yes. That's it. Just what I need."
            elif random_mast_descrip == 2:
                if the_person.outfit.vagina_available():
                    "She pushes 3 fingers inside, making a deep gutteral noice."
                    the_person.char "Ahh, yes. Fuck me hard and deep."
                else:
                    "[the_person.name] keeps rubbing and her moans grow louder."                   
            else:
                the_person.char "Mmm, yes. Keep going..."
            $ arousal_plus = renpy.random.randint (20,35)
            $ the_person.change_arousal (arousal_plus)
        the_person.char "Shit, I'm cumming!"
        $ the_person.draw_person(position = "missionary", emotion = "orgasm")
        "You see [the_person.name]'s body shiver as she reaches orgasm."
        the_person.char "Wow, that was intense. Need to be quieter or someone might just hear me - the window is still open... I would be so ashamed."
        $ slut_bonus = renpy.random.randint (5,10)
        $ the_person.sluttiness += slut_bonus
        $ the_person.reset_arousal()
        $ arousal_plus = renpy.random.randint (0,60)
        $ the_person.change_arousal (arousal_plus)
    else:
        pass
    menu:
        "Join her." if mc.current_stamina > 0:
            "You decide to use this opportunity and join her."
            mc.name "I was passing by, heard some noise  and decided to investigate. All this robberies, you know..."
            mc.name "And I see that that you indeed require some attention, [the_person.name]. Should I join?"
            if the_person.sluttiness <= 30 or the_person.arousal < 50:
                $ the_person.draw_person(position = "stand4", emotion = "angry")
                "[the_person.name] quickly turns around on hearing your voice. You see that she is not glad to see you."
                the_person.char "The fuck are you doing, Mr. [mc.last_name]? You can't just spy on people in their homes! Get out of here or I'll call the police!"
                "You quickly leave the area."
                $ the_person.happiness -= 5
            else:
                $ the_person.draw_person(position = "stand5", emotion = "happy")
                "[the_person.name] turns around on hearing your voice. You see her smile."
                if (the_person.love) > 30:
                    the_person.char "Come on in [mc.name]. I could use your help."
                else:
                    the_person.char "Well, that seems to be a good idea, Mr. [mc.last_name]. Come on, get inside."
                "You quickly climb inside through the window."
                call fuck_person(the_person) from _call_fuck_person_P13S2
        "Join her. (disabled)" if not mc.current_stamina > 0:
            pass
        "Walk away":
            "You decide not to disturb her and just walk away."

    hide screen person_info_ui
    $ the_person.reset_arousal()
    $ the_person.outfit = the_person.planned_outfit.get_copy() #Make sure to reset their outfits so they're dressed properly.
    $ renpy.scene()
    $ change_scene_display(mc.location)
    $ renpy.scene("Active")
    return
