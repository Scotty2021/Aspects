init 1301 python:              #Because Vren Init personality functionns at 1300

    def ellie_titles(person):
        valid_titles = []
        valid_titles.append(person.name)

        return valid_titles

    def ellie_possessive_titles(person):
        valid_possessive_titles = [person.title]
        return valid_possessive_titles
    def ellie_player_titles(person):
        return mc.name

    ellie_personality = Personality("ellie", default_prefix = "relaxed",
    common_likes = ["skirts", "dresses", "the weekend", "the colour red", "makeup", "flirting", "high heels"],
    common_sexy_likes = ["doggy style sex", "giving blowjobs", "vaginal sex", "public sex", "lingerie", "skimpy outfits", "being submissive", "drinking cum", "cheating on men"],
    common_dislikes = ["polyamory", "pants", "working", "the colour yellow", "conservative outfits", "sports"],
    common_sexy_dislikes = ["taking control", "giving handjobs", "not wearing anything"],
    titles_function = ellie_titles, possessive_titles_function = ellie_possessive_titles, player_titles_function = ellie_player_titles)
