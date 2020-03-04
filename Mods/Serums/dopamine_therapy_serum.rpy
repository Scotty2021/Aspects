# Dopamine Therapy Serum by Starbuck

init -1 python:
    def dopamine_therapy_on_turn(the_person, add_to_log, fire_event = True):
        if renpy.random.randint(0,100) < (the_person.suggestibility - (the_person.happiness - 100)) * 5:
            the_person.change_happiness(1, add_to_log)

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_dopamine_therapy_serum_trait(stack):
    python:
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

        execute_hijack_call(stack)
    return