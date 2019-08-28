
init -1 python:
    def get_suggest_tier(the_person):   #Returns a value of 0-3 depending on the person's suggestability.
        if the_person.suggestibility < 15:
            return 0
        elif the_person.suggestibility < 35:
            return 1
        elif the_person.suggestibility < 55:
            return 2
        elif the_person.suggestibility < 75:
            return 3
        else:
            return 4 #Edge case, has suggestability not yet in game

    def get_slut_tier(the_person):   #returns the heart value of the person
        if the_person.core_sluttiness < 20:
            return 0
        elif the_person.core_sluttiness < 40:
            return 1
        elif the_person.core_sluttiness < 60:
            return 2
        elif the_person.core_sluttiness < 80:
            return 3
        elif the_person.core_sluttiness < 100:
            return 4
        else:
            return 5


    def pheremone_therapy_on_apply(the_person, add_to_log):
        the_person.change_slut_core(15, add_to_log, fire_event = False)
        the_person.change_slut_temp(15, add_to_log)

    def pheremone_therapy_on_remove(the_person, add_to_log):
        the_person.change_slut_core(-15, add_to_log, fire_event = False)
        the_person.change_slut_temp(-15, add_to_log)

    def ovulation_function_on_turn(the_person, add_to_log):
        if get_slut_tier(the_person) < 5:
            if renpy.random.randint(0,100) <50:  #chance to increase core sluttiness
                the_person.change_slut_core    (1, add_to_log)
            the_person.change_slut_temp(2, add_to_log)

    def constant_stimulation_on_turn(the_person, add_to_log, fire_event = True):
        if get_suggest_tier(the_person) > get_slut_tier(the_person):  #If the tier of sluttiness is less than the suggest tier
            the_person.change_slut_core(1, add_to_log)
            the_person.change_slut_temp(1, add_to_log)
        elif get_suggest_tier(the_person) == get_slut_tier(the_person): #If they are equal
            if renpy.random.randint(0,100) <50:
                the_person.change_slut_core(1, add_to_log)
                the_person.change_slut_temp(1, add_to_log)
        elif get_slut_tier(the_person) < 5:
            if renpy.random.randint(0,100) < (30 - (5 * get_slut_tier(the_person))):
                the_person.change_slut_core(1, add_to_log)
                the_person.change_slut_temp(1, add_to_log)


    def dopamine_therapy_on_turn(the_person, add_to_log, fire_event = True):
        if renpy.random.randint(0,100) < (the_person.suggestibility - (the_person.happiness - 100)) * 5:
            the_person.change_happiness(1, add_to_log)


    def behavior_adjustment_on_turn(the_person, add_to_log, fire_event = True):
        if renpy.random.randint(0,100) < (the_person.suggestibility - (the_person.obedience - 90)) * 5:
            the_person.change_obedience(1, add_to_log)

    def submission_function_on_apply(the_person, add_to_log):
        the_person.change_slut_core(-15, add_to_log, fire_event = False)
        the_person.change_slut_temp(-15, add_to_log)

    def submission_function_on_remove(the_person, add_to_log):
        the_person.change_slut_core(15, add_to_log, fire_event = False)
        the_person.change_slut_temp(15, add_to_log)

    def submission_function_on_turn(the_person, add_to_log):
        the_person.change_obedience(3, add_to_log)

    def fetish_basic_function_on_turn(the_person, add_to_log): #Developes basic sexual desires based on suggestability. At low tiers, turns hates to neutral.
        fetish_random_roll_1 = renpy.random.randint(0,100)
        fetish_random_roll_2 = renpy.random.randint(0,100)

        if get_suggest_tier(the_person) == 1:
            if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
                if the_person.sex_skills["Foreplay"] < (FETISH_SEX_SKILL_MAX - 2):
                    the_person.sex_skills["Foreplay"] += 1
            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_BASIC_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < (FETISH_OPINION_MAX - 2):
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

        elif get_suggest_tier(the_person) == 2:
            if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
                if the_person.sex_skills["Foreplay"] < (FETISH_SEX_SKILL_MAX - 1):
                    the_person.sex_skills["Foreplay"] += 1
            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_BASIC_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < (FETISH_OPINION_MAX - 1):
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]


        elif get_suggest_tier(the_person) == 3:
            if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
                if the_person.sex_skills["Foreplay"] < FETISH_SEX_SKILL_MAX:
                    the_person.sex_skills["Foreplay"] += 1

            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_BASIC_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < FETISH_OPINION_MAX:
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

    def fetish_exhibition_on_turn(the_person, add_to_log):
        fetish_random_roll_2 = renpy.random.randint(0,100)

        if get_suggest_tier(the_person) <= 1:
            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_EXHIBITION_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < (FETISH_OPINION_MAX - 2):
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

        elif get_suggest_tier(the_person) == 2:
            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_EXHIBITION_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < (FETISH_OPINION_MAX - 1):
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

        elif get_suggest_tier(the_person) >= 3:
            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_EXHIBITION_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < FETISH_OPINION_MAX:
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

    def fetish_oral_function_on_turn(the_person, add_to_log):
        fetish_random_roll_1 = renpy.random.randint(0,100)
        fetish_random_roll_2 = renpy.random.randint(0,100)

        if get_suggest_tier(the_person) <= 1:
            if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
                if the_person.sex_skills["Oral"] < (FETISH_SEX_SKILL_MAX - 2):
                    the_person.sex_skills["Oral"] += 1

            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_ORAL_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < (FETISH_OPINION_MAX - 2):
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

        elif get_suggest_tier(the_person) == 2:
            if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
                if the_person.sex_skills["Oral"] < (FETISH_SEX_SKILL_MAX - 1):
                    the_person.sex_skills["Oral"] += 1

            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_ORAL_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < (FETISH_OPINION_MAX - 1):
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

        elif get_suggest_tier(the_person) >= 3:
            if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
                if the_person.sex_skills["Oral"] < FETISH_SEX_SKILL_MAX:
                    the_person.sex_skills["Oral"] += 1

            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_ORAL_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < FETISH_OPINION_MAX:
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]


    def fetish_vaginal_function_on_turn(the_person, add_to_log):
        global FETISH_VAGINAL_EVENT_INUSE

        fetish_random_roll_1 = renpy.random.randint(0,100)
        fetish_random_roll_2 = renpy.random.randint(0,100)

        if get_suggest_tier(the_person) <= 1:
            if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
                if the_person.sex_skills["Vaginal"] < FETISH_SEX_SKILL_MAX - 2:
                    the_person.sex_skills["Vaginal"] += 1


            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_VAGINAL_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < FETISH_OPINION_MAX - 2:
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

        elif get_suggest_tier(the_person) == 2:
            if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
                if the_person.sex_skills["Vaginal"] < FETISH_SEX_SKILL_MAX - 1:
                    the_person.sex_skills["Vaginal"] += 1


            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_VAGINAL_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < FETISH_OPINION_MAX - 1:
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

        elif get_suggest_tier(the_person) >= 3:
            if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
                if the_person.sex_skills["Vaginal"] < FETISH_SEX_SKILL_MAX:
                    the_person.sex_skills["Vaginal"] += 1


            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_VAGINAL_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < FETISH_OPINION_MAX:
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]


            if the_person.sex_skills["Vaginal"] == 5:
                if the_person.get_opinion_score("vaginal sex") == 2:
                    if the_person.sluttiness >= 80:
                        if SB_get_fetish_count(the_person) < store.max_fetishes_per_person:
                            # renpy.say("", "Evaluate Vaginal Fetish (In Use: " + str(FETISH_VAGINAL_EVENT_INUSE) + ")")
                            if FETISH_VAGINAL_EVENT_INUSE:
                                return

                            FETISH_VAGINAL_EVENT_INUSE = True
                            SB_SET_RANDOM_EVENT_CHANCE(0)
                            # renpy.say("", "Trigger vaginal fetish " + the_person.name)

                            if the_person == mom:
                                mc.business.mandatory_crises_list.append(SB_fetish_mom_vaginal_crisis)
                            elif the_person == lily:
                                mc.business.mandatory_crises_list.append(SB_fetish_lily_vaginal_crisis)
                            else:
                                SB_fetish_vaginal_crisis.args = [the_person]    # set the current person as action argument
                                mc.business.mandatory_crises_list.append(SB_fetish_vaginal_crisis)
        return

    def fetish_anal_function_on_turn(the_person, add_to_log):
        global FETISH_ANAL_EVENT_INUSE

        fetish_random_roll_1 = renpy.random.randint(0,100)
        fetish_random_roll_2 = renpy.random.randint(0,100)

        if get_suggest_tier(the_person) <= 1:
            if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
                if the_person.sex_skills["Anal"] < FETISH_SEX_SKILL_MAX - 2:
                    the_person.sex_skills["Anal"] += 1

            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_ANAL_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < FETISH_OPINION_MAX - 2:
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

        elif get_suggest_tier(the_person) == 2:
            if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
                if the_person.sex_skills["Anal"] < FETISH_SEX_SKILL_MAX - 1:
                    the_person.sex_skills["Anal"] += 1

            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_ANAL_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < FETISH_OPINION_MAX - 1:
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

        elif get_suggest_tier(the_person) >= 3:
            if fetish_random_roll_1 < FETISH_SKILL_RAISE_CHANCE:
                if the_person.sex_skills["Anal"] < FETISH_SEX_SKILL_MAX:
                    the_person.sex_skills["Anal"] += 1

            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_ANAL_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < FETISH_OPINION_MAX:
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

            if the_person.sex_skills["Anal"] >= 5:
                if the_person.get_opinion_score("anal sex") == 2:
                    if the_person.sluttiness >= 90:
                        if SB_get_fetish_count(the_person) < store.max_fetishes_per_person:
                            # renpy.say("", "Evaluate Anal Fetish (In Use: " + str(FETISH_ANAL_EVENT_INUSE) + ")")
                            if FETISH_ANAL_EVENT_INUSE:
                                return

                            # renpy.say("", "Trigger anal fetish " + the_person.name)
                            if the_person == lily:
                                mc.business.mandatory_crises_list.append(SB_lily_anal_dp_fetish)
                                FETISH_ANAL_EVENT_INUSE = True
                                SB_SET_RANDOM_EVENT_CHANCE(0)
                            elif the_person == mom:
                                for mand_event in mc.business.mandatory_crises_list:
                                    if mand_event.name == "mom weekly pay":
                                        # renpy.say("","DEBUG: Succesfully located mom event, attempting removal and replacement.")
                                        mc.business.mandatory_crises_list.remove(mand_event)
                                        mc.business.mandatory_crises_list.append(SB_mom_anal_fetish)
                                        FETISH_ANAL_EVENT_INUSE = True
                                        SB_SET_RANDOM_EVENT_CHANCE(0)
                            elif the_person == starbuck:
                                if starbuck.shop_investment_rate == 6.0:
                                    mc.business.mandatory_crises_list.append(SB_starbuck_anal_intro_event)
                                    FETISH_ANAL_EVENT_INUSE = True
                                    SB_SET_RANDOM_EVENT_CHANCE(0)
                            else:
                                SB_fetish_anal_crisis.args = [the_person]    # set the current person as action argument
                                mc.business.mandatory_crises_list.append(SB_fetish_anal_crisis)
                                FETISH_ANAL_EVENT_INUSE = True
                                SB_SET_RANDOM_EVENT_CHANCE(0)
        return


    def fetish_cum_function_on_turn(the_person, add_to_log):
        global FETISH_CUM_EVENT_INUSE

        fetish_random_roll_1 = renpy.random.randint(0,100)
        fetish_random_roll_2 = renpy.random.randint(0,100)

        if get_suggest_tier(the_person) <= 1:
            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_CUM_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < FETISH_OPINION_MAX - 2:
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

        elif get_suggest_tier(the_person) == 2:
            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_CUM_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < FETISH_OPINION_MAX - 1:
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

        elif get_suggest_tier(the_person) >= 3:
            if fetish_random_roll_2 < FETISH_DEVELOPMENT_CHANCE:
                SB_random_fetish_key = get_random_from_list( FETISH_CUM_OPINION_LIST)
                SB_random_opinion = the_person.get_opinion_score(SB_random_fetish_key)
                if SB_random_opinion < 2:
                    SB_random_opinion += 1
                    the_person.sexy_opinions[SB_random_fetish_key] = [SB_random_opinion, True]

            if the_person.sex_skills["Oral"] >= 5:
                if SB_get_cum_score(the_person) >= 8:
                    if the_person.sluttiness >= 90:
                        # only allow one cum fetish either internal or external
                        if not (SB_check_fetish(the_person, cum_external_role) or SB_check_fetish(the_person, cum_internal_role)):
                            if SB_get_fetish_count(the_person) < store.max_fetishes_per_person:
                                #renpy.say("", "Evaluate Cum Fetish (In Use: " + str(FETISH_CUM_EVENT_INUSE) + ")")
                                if FETISH_CUM_EVENT_INUSE:
                                    return

                                FETISH_CUM_EVENT_INUSE = True
                                SB_SET_RANDOM_EVENT_CHANCE(0)
                                #renpy.say("", "Trigger cum fetish " + the_person.name)
                                if the_person == lily:
                                    mc.business.mandatory_morning_crises_list.append(SB_fetish_lily_cum)
                                elif the_person == mom:
                                    mc.business.mandatory_crises_list.append(SB_fetish_mom_cum)
                                else:
                                    SB_fetish_cum_crisis.args = [the_person]
                                    mc.business.mandatory_crises_list.append(SB_fetish_cum_crisis)
        return

label serum_mod_starbuck_traits(stack):
    python:
        pher_ther = SerumTraitMod(name = "Pheremone Therapy",
                desc = "By mimicing pheremones found in closely related animals, this serum can recreate feelings of going into heat in women.",
                positive_slug = "+$40 Value, +15 Sluttiness",
                negative_slug = "+200 Serum Research",
                value_added = 40,
                research_added = 200,
        #     slots_added = a_number,
        #     production_added = a_number,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
                on_apply = pheremone_therapy_on_apply,
                on_remove = pheremone_therapy_on_remove,
        #     on_turn = a_function,
        #     on_day = a_function,
        #     requires = [list_of_other_traits],
                tier = 2,
                start_researched =  False,
                research_needed = 800,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        sub_ther = SerumTraitMod(name = "Submission Therapy",
                desc = "Introduces substances that naturally incline females to obey males, found in many mammals. Reduces feeling in the skin, including erogenous zones.",
                positive_slug = "+3 Obedience/Turn, +$20 Value",
                negative_slug = "-15 Sluttiness, +80 Serum Research",
                value_added = 20,
                research_added = 80,
        #     slots_added = a_number,
        #     production_added = a_number,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
                on_apply = submission_function_on_apply,
                on_remove = submission_function_on_remove,
                on_turn = submission_function_on_turn,
        #     on_day = a_function,
        #     requires = [list_of_other_traits],
                tier = 2,
                start_researched =  False,
                research_needed = 800,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        ovulation_ther = SerumTraitMod(name = "Hormonal Ovulation",
                desc = "Reproduces hormones naturally occuring during ovulation to make females more receptive to sex. Increases sluttiness over time.",
                positive_slug = "+(0-2) Sluttiness/Turn, +$40 Value",
                negative_slug = "+200 Serum Research",
                value_added = 40,
                research_added = 200,
        #     slots_added = a_number,
        #     production_added = a_number,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = ovulation_function_on_turn,
        #     on_day = a_function,
        #     requires = [list_of_other_traits],
                tier = 3,
                start_researched =  False,
                research_needed = 1500,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        fetish_basic_ther = SerumTraitMod(name = "Initial Fetish Therapy",
                desc = "Over time, increases general positivity towards basic sexual acts. Increases effectiveness with greater suggestability.",
                positive_slug = "Slowly increases sexual opinions, Slowly increases Foreplay skill, +$20 Value",
                negative_slug = "+100 Serum Research, +20 Production Cost",
                value_added = 20,
                research_added = 100 * FETISH_RESEARCH_PERCENT,
        #     slots_added = a_number,
                production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 25,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = fetish_basic_function_on_turn,
        #     on_day = a_function,
        #     requires = [list_of_other_traits],
                tier = FETISH_RESEARCH_BASE_TIER,
                start_researched =  False,
                research_needed = 400 * FETISH_RESEARCH_PERCENT,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        fetish_exhibition_ther = SerumTraitMod(name = "Exhibitionism Fetish Therapy",
                desc = "Over time, increases the need to behave in an extravagant way in order to attract attention. Increases effectiveness with greater suggestability",
                positive_slug = "Slowly increases exhibionistic behaviour, +$20 Value",
                negative_slug = "+100 Serum Research, +20 Production Cost",
                value_added = 20,
                research_added = 100 * FETISH_RESEARCH_PERCENT,
        #     slots_added = a_number,
                production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 25,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = fetish_exhibition_on_turn,
        #     on_day = a_function,
                requires = [fetish_basic_ther],
                tier = FETISH_RESEARCH_BASE_TIER,
                start_researched =  False,
                research_needed = 400 * FETISH_RESEARCH_PERCENT,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        fetish_oral_ther = SerumTraitMod(name = "Oral Fetish Therapy",
                desc = "Over time, increases general positivity towards Oral Sex. Increases effectiveness with greater suggestability",
                positive_slug = "Slowly increases oral sexual opinions, Slowly increases Oral skill, +$20 Value",
                negative_slug = "+200 Serum Research, +20 Production Cost",
                value_added = 20,
                research_added = 200 * FETISH_RESEARCH_PERCENT,
        #     slots_added = a_number,
                production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 50,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = fetish_oral_function_on_turn,
        #     on_day = a_function,
                requires = [fetish_basic_ther],
                tier = FETISH_RESEARCH_MID_TIER,
                start_researched =  False,
                research_needed = 500 * FETISH_RESEARCH_PERCENT,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        fetish_vaginal_ther = SerumTraitMod(name = "Vaginal Fetish Therapy",
                desc = "Over time, increases general positivity towards Vaginal Sex. Increases effectiveness with greater suggestability. Warning: At high suggestability it may induce a fetish.",
                positive_slug = "Slowly increases Vaginal sexual opinions, Slowly increases Vaginal skill, +$20 Value",
                negative_slug = "+200 Serum Research, +20 Production Cost",
                value_added = 20,
                research_added = 200 * FETISH_RESEARCH_PERCENT,
        #     slots_added = a_number,
                production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 50,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = fetish_vaginal_function_on_turn,
        #     on_day = a_function,
                requires = [fetish_basic_ther],
                tier = FETISH_RESEARCH_MID_TIER,
                start_researched =  False,
                research_needed = 500 * FETISH_RESEARCH_PERCENT,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        fetish_anal_ther = SerumTraitMod(name = "Anal Fetish Therapy",
                desc = "Over time, increases general positivity towards Anal Sex. Increases effectiveness with greater suggestability. Warning: At high suggestability it may induce a fetish.",
                positive_slug = "Slowly increases Anal sexual opinions, Slowly increases Anal skill, +$25 Value",
                negative_slug = "+200 Serum Research, +20 Production Cost",
                value_added = 25,
                research_added = 200 * FETISH_RESEARCH_PERCENT,
        #     slots_added = a_number,
                production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 75,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = fetish_anal_function_on_turn,
        #     on_day = a_function,
                requires = [fetish_vaginal_ther],
                tier = FETISH_RESEARCH_FINAL_TIER,
                start_researched =  False,
                research_needed = 800 * FETISH_RESEARCH_PERCENT,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        fetish_cum_ther = SerumTraitMod(name = "Cum Fetish Therapy",
                desc = "Over time, increases general positivity towards Cum. Increases effectiveness with greater suggestability. Warning: At high suggestability it may induce a fetish.",
                positive_slug = "Slowly increases Cum sexual opinions, +$25 Value",
                negative_slug = "+200 Serum Research, +20 Production Cost",
                value_added = 25,
                research_added = 200 * FETISH_RESEARCH_PERCENT,
        #     slots_added = a_number,
                production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 75,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = fetish_cum_function_on_turn,
        #     on_day = a_function,
                requires = [fetish_oral_ther],
                tier = FETISH_RESEARCH_FINAL_TIER,
                start_researched =  False,
                research_needed = 800 * FETISH_RESEARCH_PERCENT,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        constant_stimulation_ther = SerumTraitMod(name = "Constant Stimulation",
                desc = "Slowly increases sluttiness. Strong wills can resist it, but it increases effect based on suggestability.",
                positive_slug = "Slowly increases sluttiness based on suggestability, +$15 Value",
                negative_slug = "+100 Serum Research",
                value_added = 15,
                research_added = 100,
        #     slots_added = a_number,
        #     production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 50,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = constant_stimulation_on_turn,
        #     on_day = a_function,
        #     requires = [fetish_oral_ther],
                tier = 1,
                start_researched =  False,
                research_needed = 500,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        dopamine_therapy_ther = SerumTraitMod(name = "Dopamine Therapy",
                desc = "Slowly increases happiness. Increases effect based on suggestability.",
                positive_slug = "Slowly increases happiness based on suggestability, +$10 Value",
                negative_slug = "+100 Serum Research",
                value_added = 10,
                research_added = 100,
        #     slots_added = a_number,
        #     production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = dopamine_therapy_on_turn,
        #     on_day = a_function,
        #     requires = [fetish_oral_ther],
                tier = 1,
                start_researched =  False,
                research_needed = 500,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        behavior_adjustment_ther = SerumTraitMod(name = "Behavior Adjustment",
                desc = "Slowly increases obedience. Increases effect based on suggestability.",
                positive_slug = "Slowly increases obedience based on suggestability, +$10 Value",
                negative_slug = "+100 Serum Research",
                value_added = 10,
                research_added = 100,
        #     slots_added = a_number,
        #     production_added = FETISH_PRODUCTION_COST,
        #     duration_added = a_number,
                base_side_effect_chance = 20,
        #     on_apply = submission_function_on_apply,
        #     on_remove = submission_function_on_remove,
                on_turn = behavior_adjustment_on_turn,
        #     on_day = a_function,
        #     requires = [fetish_oral_ther],
                tier = 1,
                start_researched =  False,
                research_needed = 500,
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
