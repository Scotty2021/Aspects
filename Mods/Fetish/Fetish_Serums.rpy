init -2 python:
    def get_suggest_tier(the_person):   #Returns a value of 0-3 depending on the person's suggestibility.
        if the_person.suggestibility < 15:
            return 0
        elif the_person.suggestibility < 35:
            return 1
        elif the_person.suggestibility < 55:
            return 2
        elif the_person.suggestibility < 75:
            return 3
        else:
            return 4 #Edge case, has suggestibility not yet in game

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

init -1 python:
    def increase_fetish_sexy_opinion(the_person, fetish_list, max_score):
        random_fetish_key = get_random_from_list(fetish_list)
        opinion_score = the_person.get_opinion_score(random_fetish_key)
        if opinion_score < max_score:
            the_person.increase_opinion_score(random_fetish_key)
        return

    def fetish_basic_function_on_turn(the_person, add_to_log): #Developes basic sexual desires based on suggestability. At low tiers, turns hates to neutral.
        fetish_random_roll_1 = renpy.random.randint(0,100)
        fetish_random_roll_2 = renpy.random.randint(0,100)

        tier = get_suggest_tier(the_person)
        if fetish_random_roll_1 < 10 + (tier * 5):
            increase_person_sex_skill(the_person, "Foreplay", 2 + tier)
        if fetish_random_roll_2 < 25 + (tier * 5):
            increase_fetish_sexy_opinion(the_person, FETISH_BASIC_OPINION_LIST, tier - 1)
        return

    def fetish_exhibition_on_turn(the_person, add_to_log):
        fetish_random_roll_2 = renpy.random.randint(0,100)

        tier = get_suggest_tier(the_person)
        if fetish_random_roll_2 < 25 + (tier * 5):
            increase_fetish_sexy_opinion(the_person, FETISH_EXHIBITION_OPINION_LIST, tier - 1)
        return

    def fetish_oral_function_on_turn(the_person, add_to_log):
        fetish_random_roll_1 = renpy.random.randint(0,100)
        fetish_random_roll_2 = renpy.random.randint(0,100)

        tier = get_suggest_tier(the_person)
        if fetish_random_roll_1 < 10 + (tier * 5):
            increase_person_sex_skill(the_person, "Oral", 2 + tier)
        if fetish_random_roll_2 < 25 + (tier * 5):
            increase_fetish_sexy_opinion(the_person, FETISH_ORAL_OPINION_LIST, tier - 1)
        return

    def fetish_vaginal_function_on_turn(the_person, add_to_log):
        fetish_random_roll_1 = renpy.random.randint(0,100)
        fetish_random_roll_2 = renpy.random.randint(0,100)

        tier = get_suggest_tier(the_person)
        if fetish_random_roll_1 < 10 + (tier * 5):
            increase_person_sex_skill(the_person, "Vaginal", 2 + tier)
        if fetish_random_roll_2 < 25 + (tier * 5):
            increase_fetish_sexy_opinion(the_person, FETISH_VAGINAL_OPINION_LIST, tier - 1)

        if SB_FETISH_EVENT_ACTIVE(): # quick exit fetish event is active, so skip check
            return

        if tier >= 3 and the_person.sex_skills["Vaginal"] >= 5 and the_person.get_opinion_score("vaginal sex") >= 2:
            if the_person.sluttiness >= 80 and not SB_check_fetish(the_person, vaginal_fetish_role):
                if SB_get_fetish_count(the_person) < store.max_fetishes_per_person:
                    # renpy.say("", "Trigger vaginal fetish " + the_person.name)
                    if the_person is mom:
                        add_sb_fetish_mom_vaginal_event()
                    elif the_person is lily:
                        add_sb_fetish_lily_vaginal_event()
                    else:
                        add_sb_fetish_vaginal_crisis(the_person)
        return

    def fetish_anal_function_on_turn(the_person, add_to_log):
        fetish_random_roll_1 = renpy.random.randint(0,100)
        fetish_random_roll_2 = renpy.random.randint(0,100)

        tier = get_suggest_tier(the_person)
        if fetish_random_roll_1 < 10 + (tier * 5):
            increase_person_sex_skill(the_person, "Anal", 2 + tier)
        if fetish_random_roll_2 < 25 + (tier * 5):
            increase_fetish_sexy_opinion(the_person, FETISH_ANAL_OPINION_LIST, tier - 1)

        if SB_FETISH_EVENT_ACTIVE(): # quick exit fetish event is active, so skip check
            return

        if tier >= 3 and the_person.sex_skills["Anal"] >= 5 and the_person.get_opinion_score("anal sex") >= 2:
            if the_person.sluttiness >= 90 and not SB_check_fetish(the_person, anal_fetish_role):
                if SB_get_fetish_count(the_person) < store.max_fetishes_per_person:
                    # renpy.say("", "Trigger anal fetish " + the_person.name)
                    if the_person is lily:
                        add_SB_lily_anal_dp_fetish_event()
                    elif the_person is mom:
                        mom_weekly_pay = exists_in_mandatory_crisis_list("mom_weekly_pay_label")
                        if mom_weekly_pay: # replace default mom weekly pay with new event
                            # renpy.say("", "Replacing default mom weekly pay event")
                            mc.business.mandatory_crises_list.remove(mom_weekly_pay)
                            add_mom_anal_fetish_event()
                    elif the_person is starbuck:
                        if starbuck.shop_investment_rate == 6.0:
                            add_sb_starbuck_anal_intro_event()
                    elif the_person is stephanie and head_researcher in the_person.special_role and the_person.personality != bimbo_personality:
                        add_stephanie_anal_fetish_action()
                    elif employee_role in the_person.special_role:
                        add_sb_fetish_anal_crisis(the_person)
        return

    def fetish_cum_function_on_turn(the_person, add_to_log):
        fetish_random_roll_2 = renpy.random.randint(0,100)

        tier = get_suggest_tier(the_person)
        if fetish_random_roll_2 < 25 + (tier * 5):
            increase_fetish_sexy_opinion(the_person, FETISH_CUM_OPINION_LIST,  tier - 1)

        if SB_FETISH_EVENT_ACTIVE(): # quick exit fetish event is active, so skip check
            return

        if tier >= 3 and the_person.sex_skills["Oral"] >= 4:
            if the_person.sluttiness >= 90 and SB_get_cum_score(the_person) >= 8:
                # only allow one cum fetish either internal or external
                if not (SB_check_fetish(the_person, cum_external_role) or SB_check_fetish(the_person, cum_internal_role)):
                    if SB_get_fetish_count(the_person) < store.max_fetishes_per_person:
                        # renpy.say("", "Trigger cum fetish " + the_person.name)
                        if the_person is lily:
                            add_sb_fetish_lily_cum_event()
                        elif the_person is mom:
                            add_sb_fetish_mom_cum_event()
                        elif the_person is stephanie and head_researcher in the_person.special_role and the_person.personality != bimbo_personality:
                            add_sb_fetish_stephanie_cum_event()
                        elif employee_role in the_person.special_role:
                            add_sb_fetish_cum_crisis(the_person)
        return

    def increase_person_sex_skill(the_person, skill_name, max_skill):
        if the_person.sex_skills[skill_name] < max_skill:
            the_person.sex_skills[skill_name] += 1

    def add_fetish_serum_traits():
        FETISH_RESEARCH_PERCENT = 1     #1 = 100%
        FETISH_PRODUCTION_COST = 20     #Default 100
        FETISH_RESEARCH_BASE_TIER = 1        #Default = 1
        FETISH_RESEARCH_MID_TIER = 2          #Default = 2
        FETISH_RESEARCH_FINAL_TIER = 3      #Default = 3

        fetish_basic_ther = SerumTraitMod(name = "Initial Fetish Therapy",
                desc = "Over time, increases general positivity towards basic sexual acts. Increases effectiveness with greater suggestability.",
                positive_slug = "Slowly increases sexual opinions, Slowly increases Foreplay skill, +$20 Value",
                negative_slug = "+100 Serum Research, +20 Production Cost",
                value_added = 20,
                research_added = 100 * FETISH_RESEARCH_PERCENT,
                production_added = FETISH_PRODUCTION_COST,
                base_side_effect_chance = 25,
                on_turn = fetish_basic_function_on_turn,
                tier = FETISH_RESEARCH_BASE_TIER,
                start_researched =  False,
                research_needed = 400 * FETISH_RESEARCH_PERCENT,
            )

        fetish_exhibition_ther = SerumTraitMod(name = "Exhibitionism Fetish Therapy",
                desc = "Over time, increases the need to behave in an extravagant way in order to attract attention. Increases effectiveness with greater suggestability",
                positive_slug = "Slowly increases exhibionistic behaviour, +$20 Value",
                negative_slug = "+100 Serum Research, +20 Production Cost",
                value_added = 20,
                research_added = 100 * FETISH_RESEARCH_PERCENT,
                production_added = FETISH_PRODUCTION_COST,
                base_side_effect_chance = 25,
                on_turn = fetish_exhibition_on_turn,
                requires = [fetish_basic_ther],
                tier = FETISH_RESEARCH_BASE_TIER,
                start_researched =  False,
                research_needed = 400 * FETISH_RESEARCH_PERCENT,
            )

        fetish_oral_ther = SerumTraitMod(name = "Oral Fetish Therapy",
                desc = "Over time, increases general positivity towards Oral Sex. Increases effectiveness with greater suggestability",
                positive_slug = "Slowly increases oral sexual opinions, Slowly increases Oral skill, +$20 Value",
                negative_slug = "+200 Serum Research, +20 Production Cost",
                value_added = 20,
                research_added = 200 * FETISH_RESEARCH_PERCENT,
                production_added = FETISH_PRODUCTION_COST,
                base_side_effect_chance = 50,
                on_turn = fetish_oral_function_on_turn,
                requires = [fetish_basic_ther],
                tier = FETISH_RESEARCH_MID_TIER,
                start_researched =  False,
                research_needed = 500 * FETISH_RESEARCH_PERCENT,
            )

        fetish_vaginal_ther = SerumTraitMod(name = "Vaginal Fetish Therapy",
                desc = "Over time, increases general positivity towards Vaginal Sex. Increases effectiveness with greater suggestability. Warning: At high suggestability it may induce a fetish.",
                positive_slug = "Slowly increases Vaginal sexual opinions, Slowly increases Vaginal skill, +$20 Value",
                negative_slug = "+200 Serum Research, +20 Production Cost",
                value_added = 20,
                research_added = 200 * FETISH_RESEARCH_PERCENT,
                production_added = FETISH_PRODUCTION_COST,
                base_side_effect_chance = 50,
                on_turn = fetish_vaginal_function_on_turn,
                requires = [fetish_basic_ther],
                tier = FETISH_RESEARCH_MID_TIER,
                start_researched =  False,
                research_needed = 500 * FETISH_RESEARCH_PERCENT,
            )

        fetish_anal_ther = SerumTraitMod(name = "Anal Fetish Therapy",
                desc = "Over time, increases general positivity towards Anal Sex. Increases effectiveness with greater suggestability. Warning: At high suggestability it may induce a fetish.",
                positive_slug = "Slowly increases Anal sexual opinions, Slowly increases Anal skill, +$25 Value",
                negative_slug = "+200 Serum Research, +20 Production Cost",
                value_added = 25,
                research_added = 200 * FETISH_RESEARCH_PERCENT,
                production_added = FETISH_PRODUCTION_COST,
                base_side_effect_chance = 75,
                on_turn = fetish_anal_function_on_turn,
                requires = [fetish_vaginal_ther],
                tier = FETISH_RESEARCH_FINAL_TIER,
                start_researched =  False,
                research_needed = 800 * FETISH_RESEARCH_PERCENT,
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

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_fetish_serum_trait(stack):
    python:
        add_fetish_serum_traits()
        execute_hijack_call(stack)
    return
