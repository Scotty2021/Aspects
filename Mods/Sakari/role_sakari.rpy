# SAKARI OUTLINE
# Sakari is Kaya's mother, who is in failing health due to a bloodborn disease. She doesn't actually meet MC until later in the game (EG pacing with Candace)
# Sakari's intro event is paced based on having Ellie doing IT projects, since that means the business is somewhere in tier 2. Sakari's story is the first that is TIME SENSITIVE
# Sakari starts at 100 max energy, and it drops by 5 every week. Upon reaching <50, MC gets a notification that Sakari has gone to the hospital, then hospice, then passes away.
# Sakari's love events will give MC the opportunity to research a cure for her, but it will be very expensive. Alternatively, MC can try and make her remaining days "as pleasurable as possible"
# We introduce Sakari at the clothes store, which we discover she owns. Her 20 love event involves MC discovering the nature of her affliction, at 40 she offers to sell MC her business
# At 60 love she wants to be with MC for what is left of her time if she hasn't been cured yet. If MC cures sakari before she gets to 60 love, she bypasses the 60 love event and goes to 80 love event
# 80 love event only activates if Sakari has been cured, and she basically offers to be MC's personal MILF, even if MC is also dating Kaya.
# At 100 love if Kaya is also at 100 love they offer to move in with MC. Kaya's love quests involve MC talking with Lily and Jennifer about their relationship, so it is not a surprise to them.
# Sakari's sluttiness events basically revolve around doing slutty things she never got to do during her life.
# At 20 she skinny dips with MC at night
# at 40 she blows MC at the movie theatre
# at 60 she fucks MC in a dressing room at her clothing store
# at 80 she asks MC if she can dance at his strip club for one night (must own strip club)
# at 100 she offers to join MC's harem if he has one, if not and 100 sluttiness with Kaya she has a threesome with her and MC.



#Init
init 2 python:
    def sakari_mod_initialization():
        #sakari_wardrobe = wardrobe_from_xml("ashley_Wardrobe")
        sakari_base_outfit = Outfit("sakari's base accessories")
        the_glasses = modern_glasses.get_copy()
        the_glasses.colour = [.15, .15, .15, 1.0]
        the_lipstick = lipstick.get_copy()
        the_lipstick.colour = [.15, .15, .15, 0.5]
        the_rings = garnet_ring.get_copy()   #Change this
        the_rings.colour = [.82,.15,.15,1.0]
        sakari_base_outfit.add_accessory(the_lipstick)
        sakari_base_outfit.add_accessory(the_rings)
        sakari_base_outfit.add_accessory(the_glasses)

        # init sakari role
        sakari_role = Role(role_name ="sakari", actions =[], hidden = True)

        #global sakari_role
        global sakari
        sakari = make_person(name = "Sakari", last_name ="Greene", age = 42, body_type = "thin_body", face_style = "Face_14",  tits="C", height = 0.92, hair_colour=["bald", [0.414, 0.305, 0.258,0]], hair_style = short_hair, skin="tan" , \
            eyes = "brown", personality = sakari_personality, name_color = "#228b22", dial_color = "228b22" , \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_array = [4,2,2,2], start_sluttiness = 7, start_obedience = 18, start_happiness = 88, start_love = 0, \
            relationship = "Single", kids = 1, force_random = True, base_outfit = sakari_base_outfit,
            forced_opinions = [["production work", 2, True], ["work uniforms", -1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["the colour blue", -2, False], ["classical", 1, False]],
            forced_sexy_opinions = [["being submissive", 2, False], ["getting head", 1, False], ["drinking cum", -2, False], ["giving blowjobs", -1, False], ["creampies", 2, False]])

        sakari.generate_home()
        sakari.set_schedule(sakari.home, times = [0,1,2,3,4])   #Hide Sakari at home until we are ready to use her
        sakari.home.add_person(sakari)
        sakari.hair_colour = ["bald", [0.414, 0.305, 0.258,0]]
        sakari.hair_style.colour = [0.414, 0.305, 0.258,0]

        sakari.event_triggers_dict["intro_complete"] = False    # True after first talk
        sakari.event_triggers_dict["is_sick"] = False           # True after intro. This triggers her energy degeneration
        sakari.event_triggers_dict["mc_knows_sick"] = False
        sakari.event_triggers_dict["mc_offered_partner"] = False
        sakari.event_triggers_dict["mc_is_partner"] = False
        sakari.event_triggers_dict["mc_is_booty_call"] = False
        sakari.event_triggers_dict["is_mc_personal_milf"] = False
        sakari.event_triggers_dict["is_jealous"] = True
        sakari.event_triggers_dict["has_skinny_dipped"] = False
        sakari.event_triggers_dict["has_given_movie_bj"] = False
        sakari.event_triggers_dict["has_fucked_at_store"] = False
        sakari.event_triggers_dict["has_stripped_at_club"] = False
        sakari.event_triggers_dict["had_kaya_threesome"] = False
        sakari.event_triggers_dict["ophelia_teamup_started"] = False
        sakari.event_triggers_dict["opehlia_teamup"] = False
        sakari.event_triggers_dict["rebecca_teamup_started"] = False
        sakari.event_triggers_dict["rebecca_teamup"] = False

        # In Kaya's event, we keep the variable for whether or not Sakari has died, since

        # add appoint
        #office.add_action(HR_director_appointment_action)

        # sakari_intro = Action("sakari_intro",sakari_intro_requirement,"sakari_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        # mc.business.add_mandatory_crisis(sakari_intro) #Add the event here so that it pops when the requirements are met.

        # set relationships
        town_relationships.update_relationship(sakari, kaya, "Daughter", "Mother")
        # town_relationships.update_relationship(nora, sakari, "Friend")
        # town_relationships.update_relationship(lily, sakari, "Rival")

        sakari.add_role(sakari_role)
        return

#Requirement Functions
init -2 python:
    def sakari_intro_requirement(the_person):
        return False


# Actions
init 3 python:
    sakari_intro = Action("See Sakari at Clothing Store",sakari_intro_requirement,"sakari_intro_label")

#Story Labels
label sakari_intro_label(the_person):
    pass    #Written on mobile, TODO import to repo
    return


label sakari_coffee_break_label(the_person):
    pass    #written on mobile. TODO import to repo "Myeloma"
    return

label sakari_business_proposition_label():    #mandatory event
    pass
    return

label sakari_business_partner_start_label():
    pass
    return

label sakari_mc_booty_call_intro_label():     #Mandatory event
    pass
    return

label sakari_mc_booty_call_crisis_label():      #After the mandatory event, we add it to possible nighttime crisis events.
    pass
    return

label sakari_invites_mc_for_sleepover_label():  #mandatory event
    pass
    return

label sakari_kaya_move_in_label():          #Live in girlfriends still a WIP. come back to this later.
    pass
    return


#Sluttiness Labels

label sakari_goes_skinny_dipping_label():   #mandatory event
    pass
    return

label sakari_goes_to_the_movies_label():
    pass
    return

label sakari_fuck_at_clothing_store_label(the_person):  #room enter event
    pass
    return

label sakari_dances_at_strip_club_intro_label(the_person):  #room_enter_event
    pass
    return

label sakari_dances_at_strip_club_label():      #mandatory event.
    pass
    return

label sakari_share_mc_during_sleepover_label(): #Mandatory event
    pass
    return


#Sakari cure storyline  - Eventually pull these labels out of this file and into a new one, but adding a new file named "sakari cure" would be spoiler, so for now leave it buried here
#Starts with MC talking to Ellie about Nanobots. during a nighttime mandatory crisis MC realizes nanobots could be used to target Sakari's sickness.
#First prototype kills lab rats because bots are either too effective and flood the system with dead cells, or not effective enough and the illness comes back
#Second phase create a new serum type to combat the effects of the necrosis of the nanobot tech
#Put both together into a serum and it will cure sakari if she is given sufficient doses.

#Start race for the cure storyline###
label nanobot_cure_ellie_inspiration_label(the_person):  #On room enter event.
    pass
    return

label nanobot_cure_mc_nighttime_plans_label():  #Mandatory night crisis
    pass
    return

label nanobot_cure_plan_stage_one_label(the_person):    #ellie on talk event
    pass
    return

label nanobot_cure_ask_sakari_for_blood_label(the_person):  #Sakari on talk event
    pass
    return

label nanobot_cure_start_IT_project_label(the_person):  #Ellie on room enter event.
    pass
    return

label nanobot_cure_setup_stage_one_test_label():    #Mandatory event
    pass
    return

label nanobot_cure_plan_stage_two_label():     #Mandatory event
    pass
    return

label nanobot_cure_start_serum_research_label(the_person): #room enter event with head researcher.
    pass
    return

label nanobot_cure_kaya_stays_late_label(the_person):   #Room enter. if Kaya is in research she stays late to keep researching cure for her mother.
    pass
    return

label nanobot_cure_serum_complete_label(): #mandatory event
    pass
    return

label nanobot_cure_setup_stage_two_test_label():    #mandatory event
    pass
    return

label nanobot_cure_give_serum_to_sakari_label():
    pass
    return

label nanobot_cure_sakari_recurring_treatment_label():
    pass
    return

label nanobot_cure_complete_label():
    pass
    return

#End race for the cure storyline###

#Race for the cure failure labels

label sakari_is_in_hospital_label():
    pass
    return

label sakari_is_in_hospice_label():
    pass
    return

label sakari_has_passed_label():
    pass
    return

#Story wrappers
init 3 python:
    def sakari_is_sick():
        return sakari.event_triggers_dict.get("is_sick", False)

    def sakari_intro_complete():
        return sakari.event_triggers_dict.get("intro_complete", False)

    def sakari_mc_knows_sick():
        return sakari.event_triggers_dict.get("mc_knows_sick", False)

    def sakari_offered_mc_partner():
        return sakari.event_triggers_dict.get("mc_offered_partner", False)

    def sakari_mc_are_partners():
        return sakari.event_triggers_dict.get("mc_is_partner", False)

    def sakari_mc_is_booty_call():
        return sakari.event_triggers_dict.get("mc_is_booty_call", False)

    def sakari_is_mc_personal_milf():
        return sakari.event_triggers_dict.get("is_mc_personal_milf", False)

    def sakari_is_jealous():
        return sakari.event_triggers_dict.get("is_jealous", True)

    def sakari_has_skinny_dipped():
        return sakari.event_triggers_dict.get("has_skinny_dipped", False)

    def sakari_has_given_movie_bj():
        return sakari.event_triggers_dict.get("has_given_movie_bj", False)

    def sakari_has_fucked_at_store():
        return sakari.event_triggers_dict.get("has_fucked_at_store", False)

    def sakari_has_stripped_at_club():
        return sakari.event_triggers_dict.get("has_stripped_at_club", False)

    def sakari_has_had_kaya_threesome():
        return sakari.event_triggers_dict.get("had_kaya_threesome", False)

    def sakari_has_died():
        return kaya.event_triggers_dict.get("sakari_has_died", False)

#Sakari other functions
