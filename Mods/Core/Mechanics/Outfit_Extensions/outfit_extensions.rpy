

init -1 python:
    def remove_all_cum(self):
        remove_list = []
        for acc in self.accessories:
            if acc in [mouth_cum, tits_cum, stomach_cum, face_cum, ass_cum]:
                remove_list.append(acc)
        for acc in remove_list:
            self.accessories.remove(acc)
        return
    
    Outfit.remove_all_cum = remove_all_cum

    def get_overwear_slut_score_enhanced(self): #Calculates the sluttiness of this outfit assuming it's an overwear set. That means we assume a modest underwear set is used (ie. one that denies access).
        new_score = 0
        if self.tits_visible():
            new_score += 20
        elif self.tits_available():
            new_score += 10          

        if self.vagina_visible():
            new_score += 20
        elif self.vagina_available():
            new_score += 10

        new_score += self.get_total_slut_modifiers()

        return new_score

    Outfit.get_overwear_slut_score = get_overwear_slut_score_enhanced

    def build_outfit_name_custom(self):
        def get_name_classification(slut_requirement):
            if slut_requirement <= 20:
                return "Conservative"
            if slut_requirement <= 40:
                return "Casual"
            if slut_requirement <= 60:
                return "Relaxed"
            if slut_requirement <= 80:
                return "Sexy"
            return "Slutty"

        def get_cloting_items(outfit_part):
            items = filter(lambda x: x.layer == 2, outfit_part)
            if not items:
                items = filter(lambda x: x.layer == 1, outfit_part)
            return items

        outfitname = ""

        upper = get_cloting_items(self.upper_body)
        if upper:
            outfitname += upper[0].name
        
        if not upper or not upper[0].has_extension:
            lower = get_cloting_items(self.lower_body)
            if upper and lower:
                outfitname += " and "
            if lower:
                outfitname += lower[0].name

        if len(outfitname) == 0:
            feet = get_clothing_items(self.feet)
            if feet:
                outfitname = feet[0].name
        
        if len(outfitname) == 0:
            return "Naked"

        self.update_slut_requirement()           
        self.name = get_name_classification(self.slut_requirement) + " " + outfitname

        return self.name

    Outfit.build_outfit_name = build_outfit_name_custom
