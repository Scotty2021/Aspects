# Anorexia Serum by Tristimdorion

init -1 python:
    def anorexia_serum_on_turn(person, add_to_log):
        return person.change_weight(amount = -.2, chance = 20)       

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_anorexia_serum_trait(stack):
    python:
        anorexia_serum_trait = SerumTraitMod(name = "Anorexia Trait",
            desc = "Decrease target subject body mass, using peptide YY3-36 as a serum component that acts on the hypothalamic feeding centers to inhibit hunger and calorie intake.",
            positive_slug = "-$15 Value, 20% Chance/Turn to reduce body mass by 200 grams",
            negative_slug = "+125 Serum Research",
            value_added = -15,
            research_added = 125,
            base_side_effect_chance = 20,
            on_turn = anorexia_serum_on_turn,
            requires = basic_med_app,
            tier = 1,
            research_needed = 500)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return