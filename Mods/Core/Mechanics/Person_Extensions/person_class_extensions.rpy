init -1 python:
    import hashlib

    def remove_person_from_game(self):
        my_location = self.location()
        if my_location:
            my_location.remove_person(self) # remove person from current location
        if self.home in list_of_places:
            list_of_places.remove(self.home) # remove home location from list_of_places
        if "people_to_process" in globals():
            found = find_in_list(lambda x: x[0].name == self.name and x[0].last_name == self.last_name and x[0].age == self.age, people_to_process)
            if found: # remove from processing list
                people_to_process.remove(found)

        self.base_outfit = None
        self.planned_outfit = None
        self.planned_uniform = None

        for outfit in self.wardrobe.outfits + self.wardrobe.underwear_sets + self.wardrobe.overwear_sets:
            outfit.upper_body.clear()
            outfit.lower_body.clear()
            outfit.feet.clear()
            outfit.accessories.clear()

        self.wardrobe.outfits.clear()
        self.wardrobe.underwear_sets.clear()
        self.wardrobe.overwear_sets.clear()
        self.wardrobe = None

        self.special_role.clear()
        self.on_room_enter_event_list.clear()
        self.event_triggers_dict.clear()
        self.suggest_bag.clear()
        self.broken_taboos.clear()
        self.sex_record.clear()

        # clear all references held by person object.
        self.home = None
        self.work = None
        self.schedule = None
        self.job = None
        self.relationship = None
        self.personality = None
        self.char = None
        self.body_images = None
        self.face_style = None
        self.expression_images = None
        self.hair_colour = None
        self.hair_style = None
        self.pubes_style = None
        self.skin = None
        self.eyes = None
        self.serum_effects = None
        self.idle_animation = None
        self.personal_region_modifiers = None
        self.situational_sluttiness = None
        self.situational_obedience = None
        # now let the Garbage Collector do the rest (we are no longer referenced in any objects).
        return

    Person.remove_person_from_game = remove_person_from_game

    def location(self): # Check what location a person is in e.g the_person.location() == downtown. Use to trigger events?
        for location in list_of_places:
            if self in location.people:
                return location

    Person.location = location

    def get_follow_me(self):
        if not hasattr(self, "_follow_me"):
            self._follow_me = False
        return self._follow_me

    def set_follow_me(self, value):
        self._follow_me = value

    def del_follow_me(self):
        del self._follow_me

    # add follow_mc attribute to person class (without sub-classing)
    Person.follow_mc = property(get_follow_me, set_follow_me, del_follow_me, "I'm the follow_me property.")

    def get_person_identifier(self):
        if not hasattr(self, "_identifier"):
            self._identifier = hashlib.md5(self.name + self.last_name + str(self.age)).hexdigest()
        return self._identifier

    def set_person_identifier(self, value):
        self._identifier = value

    def del_person_identifier(self):
        del self._identifier

    # add follow_mc attribute to person class (without sub-classing)
    Person.identifier = property(get_person_identifier, set_person_identifier, del_person_identifier, "Unique identifier for person class.")

    ## MATCH SKIN COLOR
    # Matches skin, body, face and expression images based on input of skin color
    def match_skin(self, color):
        if " skin" in color: # If using the_person.body_images.name as a reference, remove the " skin" part.
            color = color[:-5]

        self.skin = str(color)
        if self.skin == "white":
            self.body_images = white_skin
        elif self.skin == "tan":
            self.body_images = tan_skin
        elif self.skin == "black":
            self.body_images = black_skin
        self.expression_images = Expression("default", self.skin, self.face_style)
        return
    Person.match_skin = match_skin

    ## CHANGE HEIGHT EXTENSION
    # Returns True when the persons height has changed; otherwise False
    # chance is probability percentage that height change for amount will occur (used by serums)
    def change_height(self, amount, chance):
        lower_limit = 1 - .2
        upper_limit = 1

        if amount == 0 or (self.height == lower_limit and amount < 0) or (self.height == upper_limit and amount > 0):
            return False

        if renpy.random.randint(0, 100) <= chance:
            self.height += amount
        else:
            return False

        if self.height > upper_limit:
            self.height == upper_limit

        if self.height < lower_limit:
            self.height = lower_limit

        return True

    # attach change height function to the Person class
    Person.change_height = change_height

    ## CHANGE WEIGHT EXTENSION
    # Returns True when the persons body type has changed; otherwise False
    # chance is probability percentage that weight change for amount will occur (used by serums)
    def change_weight(self, amount, chance):
        check_person_weight_attribute(self)
        if (amount == 0):
            return False

        if renpy.random.randint(0, 100) <= chance:
            self.weight += amount

        # maximum and minimum weight are dependant on height
        max_weight = (self.height) * 100
        min_weight = (self.height) * 50
        switch_point_low = (self.height) * 68
        switch_point_high = (self.height) * 83

        if (amount > 0):
            if self.weight > switch_point_low + 3 and self.body_type == "thin_body":
                self.body_type = "standard_body"
                return True
            if self.weight > switch_point_high + 3 and self.body_type == "standard_body":
                self.body_type = "curvy_body"
                return True
            if self.weight > max_weight: #Maximum weight
                self.weight = max_weight
            return False

        if (amount < 0):
            if self.weight < min_weight:  #Minimum weight
                self.weight = min_weight
                return False
            if self.weight < switch_point_low - 3 and self.body_type == "standard_body":
                self.body_type = "thin_body"
                return True
            if self.weight < switch_point_high - 3 and self.body_type == "curvy_body":
                self.body_type = "standard_body"
                return True
            return False

    # attach change weight function to the Person class
    Person.change_weight = change_weight

    ## HAPPINESS SCORE ENHANCED VERSION
    # Takes into account their liking for working (if she doesn't she is more likely to quit)
    def get_job_happiness_score_enhanced(self):
        happy_points = self.happiness - 100 #Happiness over 100 gives a bonus to staying, happiness less than 100 gives a penalty
        happy_points += self.obedience - 95 #A more obedient character is more likely to stay, even if they're unhappy. Default characters can be a little disobedint without any problems.
        happy_points += self.salary - self.calculate_base_salary() #A real salary greater than her base is a bonus, less is a penalty. TODO: Make this dependent on salary fraction, not abosolute pay.
        happy_points += self.get_opinion_score("working") * 5 # Does she like working? It affects her happiness score.

        if (day - self.event_triggers_dict.get("employed_since",0)) < 14:
            happy_points += 14 - (day - self.event_triggers_dict.get("employed_since",0)) #Employees are much less likely to quit over the first two weeks.
        return happy_points

    Person.get_job_happiness_score = get_job_happiness_score_enhanced

    def is_employee(self):
        employment_title = mc.business.get_employee_title(self)
        if employment_title != "None":
            return True
        return False

    Person.is_employee = is_employee

    ## LEARN HOME EXTENSION
    def learn_home(self): # Adds the_person.home to mc.known_home_locations allowing it to be visited without having to go through date label
        if not self.home in mc.known_home_locations:
            mc.known_home_locations.append(self.home)
            return True # Returns true if it succeeds
        return False # Returns false otherwise, so it can be used for checks.

    # Adds learn_home function to the_person.
    Person.learn_home = learn_home

    def get_known_opinion_list(self, include_sexy = False, include_normal = True, only_positive = False, only_negative = False): #Gets the topic string of a random opinion this character holds. Includes options to include known opinions and sexy opinions. Returns None if no valid opinion can be found.
        the_dict = {} #Start our list of valid opinions to be listed as empty

        if include_normal: #if we include normal opinions build a dict out of the two
            the_dict = dict(the_dict, **self.opinions)

        if include_sexy: #If we want sexy opinions add them in too.
            the_dict = dict(the_dict, **self.sexy_opinions)

        unknown_keys = []
        for k in the_dict: #Go through each value in our combined normal and sexy opinion dict
            if not the_dict[k][1]: #Check if we know about it...
                unknown_keys.append(k) #We build a temporary list of keys to remove because otherwise we are modifying the dict while we traverse it.
        for del_key in unknown_keys:
            del the_dict[del_key]

        remove_keys = []
        if only_positive:
            for k in the_dict:
                if self.get_opinion_score(k) <= 0:
                    remove_keys.append(k)

        if only_negative:
            for k in the_dict:
                if self.get_opinion_score(k) > 0:
                    remove_keys.append(k)

        for del_key in remove_keys:
            del the_dict[del_key]

        return the_dict.keys()

    Person.get_known_opinion_list = get_known_opinion_list

    def generate_daughter_enhanced(self): #Generates a random person who shares a number of similarities to the mother
        age = renpy.random.randint(18, self.age-16)

        if renpy.random.randint(0,100) < 60:
            body_type = self.body_type
        else:
            body_type = None

        if renpy.random.randint(0,100) < 40: #Slightly lower for facial similarities to keep characters looking distinct
            face_style = self.face_style
        else:
            face_style = None

        if renpy.random.randint(0,100) < 60: #60% of the time they share hair colour
            hair_colour = self.hair_colour
        else:
            hair_colour = None

        if renpy.random.randint(0,100) < 60: # 60% they share the same breast size
            tits = self.tits
        else:
            tits = None

        if renpy.random.randint(0,100) < 60: #Share the same eye colour
            eyes = self.eyes
        else:
            eyes = None

        if renpy.random.randint(0,100) < 60: #Have heights that roughly match (but o
            height = (self.height / 0.8) * (renpy.random.randint(95,105)/100.0)
            if height > 1.0:
                height = 1.0
            elif height < 0.8:
                height = 0.8
        else:
            height = None

        if renpy.random.randint(0,100) < 85 - age: #It is less likely she lives at home the older she is.
            start_home  = self.home
        else:
            start_home  = None


        the_daughter = make_person(last_name = self.last_name, age = age, body_type = body_type, face_style = face_style, tits = tits, height = height,
            hair_colour = hair_colour, skin = self.skin, eyes = eyes, start_home = start_home, force_random = True)

        if start_home is None:
            the_daughter.generate_home()
        the_daughter.home.add_person(the_daughter)

        for sister in town_relationships.get_existing_children(self): #First find all of the other kids this person has
            town_relationships.update_relationship(the_daughter, sister, "Sister") #Set them as sisters

        town_relationships.update_relationship(self, the_daughter, "Daughter", "Mother") #Now set the mother/daughter relationship (not before, otherwise she's a sister to herself!)

        return the_daughter

    Person.generate_daughter = generate_daughter_enhanced

    ## STRIP OUTFIT TO MAX SLUTTINESS EXTENSION
    # Strips down the person to a clothing their are comfortable with (starting with top, before bottom)
    # narrator_messages: narrator voice after each item of clothing stripped, use '[person.<title>]' for titles and '[strip_choice.name]' for clothing item.
        # Can be an array of messages for variation in message per clothing item or just a single string or None for silent stripping
    # scene manager parameter is filled from that class so that all people present in scene are drawn
    def strip_outfit_to_max_sluttiness(self, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, narrator_messages = None, character_placement = None, lighting = None, temp_sluttiness_boost = 0, position = None, emotion = None, scene_manager = None):
        # internal function to strip top clothing first.
        def get_strip_choice_max(outfit, top_layer_first, exclude_upper, exclude_lower, exclude_feet):
            strip_choice = None
            if not exclude_upper:
                strip_choice = outfit.remove_random_upper(top_layer_first)
            if strip_choice is None:
                strip_choice = outfit.remove_random_any(top_layer_first, exclude_upper, exclude_lower, exclude_feet)
            return strip_choice

        def get_messages(narrator_messages):
            messages = []
            if not narrator_messages:
                pass
            elif not isinstance(narrator_messages, list):
                messages = [narrator_messages]
            else:
                messages = narrator_messages
            return messages

        messages = get_messages(narrator_messages)
        msg_count = len(messages)

        test_outfit = self.outfit.get_copy()
        removed_something = False

        strip_choice = get_strip_choice_max(test_outfit, top_layer_first, exclude_upper, exclude_lower, exclude_feet)
        # renpy.say("", strip_choice.name + "  (required: " + str(test_outfit.slut_requirement) +  ", sluttiness: " +  str(self.effective_sluttiness() + temp_sluttiness_boost) + ")")
        while strip_choice and self.judge_outfit(test_outfit, temp_sluttiness_boost):
            self.draw_animated_removal(strip_choice, character_placement = character_placement, position = position, emotion = emotion, lighting = lighting, scene_manager = scene_manager) #Draw the strip choice being removed from our current outfit
            self.apply_outfit(test_outfit, ignore_base = True) #Swap our current outfit out for the test outfit.
            removed_something = True
            if msg_count > 0:   # do we need to show a random message and replace titles and outfit name
                msg_idx = renpy.random.randint(1, msg_count)
                msg = messages[msg_idx - 1]
                msg = msg.replace("[the_person.possessive_title]", self.possessive_title).replace("[the_person.title]", self.title).replace("[the_person.mc_title]", self.mc_title).replace("[strip_choice.name]", strip_choice.name)
                renpy.say(None, msg)
            else:
                renpy.pause(1) # if no message to show, wait a short while before automatically continue stripping

            strip_choice = get_strip_choice_max(test_outfit, top_layer_first, exclude_upper, exclude_lower, exclude_feet)

        return removed_something

    # Monkey wrench Person class to have automatic strip function
    Person.strip_outfit_to_max_sluttiness = strip_outfit_to_max_sluttiness

    def strip_outfit(self, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, delay = 1, character_placement = None, position = None, emotion = None, lighting = None, scene_manager = None):
        def extra_strip_check(person, top_layer_first, exclude_upper, exclude_lower, exclude_feet):
            if top_layer_first: # normal strip continue
                return True

            done = exclude_upper or person.outfit.tits_available()
            if done and (exclude_lower or person.outfit.vagina_available()):
                if done and (exclude_feet or person.outfit.feet_available()):
                    return False

            return True # not done continue stripping

        if position is None:
            self.position = self.idle_pose

        if emotion is None:
            self.emotion = self.get_emotion()

        if lighting is None:
            lighting = mc.location.get_lighting_conditions()

        if character_placement is None:
            self.character_placement = character_right

        strip_choice = self.outfit.remove_random_any(top_layer_first, exclude_upper, exclude_lower, exclude_feet, do_not_remove = True)
        while not strip_choice is None and extra_strip_check(self, top_layer_first, exclude_upper, exclude_lower, exclude_feet):
            self.draw_animated_removal(strip_choice, character_placement = character_placement, position = position, emotion = emotion, lighting = lighting, scene_manager = scene_manager) #Draw the strip choice being removed from our current outfit
            strip_choice = self.outfit.remove_random_any(top_layer_first, exclude_upper, exclude_lower, exclude_feet, do_not_remove = True)
            renpy.pause(delay)

        # special case where she is wearing a two-part item that blocks her vagina, but we need it be available
        if not exclude_lower and not self.outfit.vagina_available():
            strip_choice = self.outfit.remove_random_any(top_layer_first, False, exclude_lower, exclude_feet, do_not_remove = True)
            while not strip_choice is None:
                self.draw_animated_removal(strip_choice, character_placement = character_placement, position = position, emotion = emotion, lighting = lighting, scene_manager = scene_manager) #Draw the strip choice being removed from our current outfit
                strip_choice = self.outfit.remove_random_any(top_layer_first, False, exclude_lower, exclude_feet, do_not_remove = True)
                renpy.pause(delay)

    Person.strip_outfit = strip_outfit

    def run_move_enhanced(self,location):
        self.sexed_count = 0 #Reset the counter for how many times you've been seduced, you might be seduced multiple times in one day!

        if time_of_day == 0: #It's a new day, get a new outfit out to wear!
            self.planned_outfit = self.wardrobe.decide_on_outfit2(self)
            self.apply_outfit(self.planned_outfit)
            self.planned_uniform = None

        destination = self.schedule[time_of_day] #None destination means they have free time
        if destination == self.work and not mc.business.is_open_for_business(): #NOTE: Right now we give everyone time off based on when the mc has work scheduled.
            destination = None

        if destination is not None: #We have somewhere scheduled to be for this time chunk. Let's move over there.
            location.move_person(self, destination) #Always go where you're scheduled to be.
            if self.schedule[time_of_day] == self.work: #We're going to work.
                if self.should_wear_uniform(): #Get a uniform if we should be wearing one.
                    self.wear_uniform()
                    self.change_happiness(self.get_opinion_score("work uniforms"),add_to_log = False)
                    # only changes sluttiness in low sluttiness range after that she won't care anymore
                    if self.sluttiness < 40 and self.planned_uniform and self.planned_uniform.slut_requirement > self.sluttiness*0.75: #A skimpy outfit/uniform is defined as the top 25% of a girls natural sluttiness.
                        self.change_slut_temp(self.get_opinion_score("skimpy uniforms"), add_to_log = False)

            elif destination == self.home:
                self.apply_outfit(self.planned_outfit) #We're at home, so we can get back into our casual outfit.

            #NOTE: There is no else here because all of the destinations should be set. If it's just a location they travel there and that's the end of it.

        else:
            #She finds somewhere to burn some time
            self.apply_outfit(self.planned_outfit) #Get changed back into our proper outfit if we aren't in it already.
            available_locations = [] #Check to see where is public (or where you are white listed) and move to one of those locations randomly
            for potential_location in list_of_places:
                if potential_location.public:
                    available_locations.append(potential_location)
            location.move_person(self, get_random_from_list(available_locations))

        #A skimpy outfit is defined as the top 25% of a girls natural sluttiness.
        if self.outfit and self.planned_outfit.slut_requirement > self.sluttiness * 0.75:
            # only changes sluttiness in low sluttiness range after that she won't care anymore
            if self.sluttiness < 40:
                self.change_slut_temp(self.get_opinion_score("skimpy outfits"), add_to_log = False)

        #A conservative outfit is defined as the bottom 25% of a girls natural sluttiness.
        if self.outfit and self.planned_outfit.slut_requirement < self.sluttiness * 0.25:
            # happiness won't go below 80 or over 120 by this trait and only affects in low sluttiness range, after that she won't care
            if self.happiness > 80 and self.happiness < 120 and self.sluttiness < 40:
                self.change_happiness(self.get_opinion_score("conservative outfits"), add_to_log = False)

        # lingerie only impacts to sluttiness level 40
        if self.sluttiness < 40 and (self.outfit.get_bra() or self.outfit.get_panties()):
            lingerie_bonus = 0
            if self.outfit.get_bra() and self.outfit.get_bra().slut_value > 1: #We consider underwear with an innate sluttiness of 2 or higher "lingerie" rather than just underwear.
                lingerie_bonus += self.get_opinion_score("lingerie")
            if self.outfit.get_panties() and self.outfit.get_panties().slut_value > 1:
                lingerie_bonus += self.get_opinion_score("lingerie")
            lingerie_bonus = __builtin__.int(lingerie_bonus/2.0)
            self.change_slut_temp(lingerie_bonus, add_to_log = False)

        # not wearing underwear only impacts sluttiness to level 60
        if self.sluttiness < 60 and (not self.outfit.wearing_bra() or not self.outfit.wearing_panties()): #We need to determine how much underwear they are not wearing. Each piece counts as half, so a +2 "love" is +1 slut per chunk.
            underwear_bonus = 0
            if not self.outfit.wearing_bra():
                underwear_bonus += self.get_opinion_score("not wearing underwear")
            if not self.outfit.wearing_panties():
                underwear_bonus += self.get_opinion_score("not wearing underwear")
            underwear_bonus = __builtin__.int(underwear_bonus/2.0) #I believe this rounds towards 0. No big deal if it doesn't, very minor detail.
            self.change_slut_temp(underwear_bonus, add_to_log = False)

        # showing the goods only impacts sluttiness to level 80
        if self.sluttiness < 80 and self.outfit.tits_visible():
            self.change_slut_temp(self.get_opinion_score("showing her tits"), add_to_log = False)
        if self.sluttiness < 80 and self.outfit.vagina_visible():
            self.change_slut_temp(self.get_opinion_score("showing her ass"), add_to_log = False)

        # showing everything only impacts sluttiness to level 80
        if self.sluttiness < 80 and self.outfit.full_access():
            self.change_slut_temp(self.get_opinion_score("not wearing anything"), add_to_log = False)

        for event_list in [self.on_room_enter_event_list, self.on_talk_event_list]: #Go through both of these lists and curate them, ie trim out events that should have expired.
            removal_list = [] #So we can iterate through without removing and damaging the list.
            for an_action in event_list:
                if isinstance(an_action, Limited_Time_Action): #It's a LTA holder, so it has a turn counter
                    an_action.turns_valid += -1
                    if an_action.turns_valid <= 0:
                        removal_list.append(an_action)

            for action_to_remove in removal_list:
                event_list.remove(action_to_remove)

    Person.run_move = run_move_enhanced

    # BUGFIX: Remove suggest effect
    # Sometimes an effect is no longer in bag causing an exception, fix: check if effect exists before trying to remove
    def remove_suggest_effect_fixed(self, amount):
        self.change_suggest(- __builtin__.max(self.suggest_bag or [0])) #Subtract the max
        if amount in self.suggest_bag:
            self.suggest_bag.remove(amount)
        self.change_suggest(__builtin__.max(self.suggest_bag or [0])) # Add the new max. If we were max, it is now lower, otherwise it cancels out.

    Person.remove_suggest_effect = remove_suggest_effect_fixed

    ## ADD OPINION EXTENSION
    ## Adds add_opinion function to Person class
    def add_opinion(self, topic, degree, discovered = None, sexy_opinion = None, add_to_log = True): # Gives a message stating the opinion has been changed.
        if topic in self.opinions:  # we passed None for discovered so use existing discovered info
            if sexy_opinion is None:
                sexy_opinion = False
            if discovered is None:
                discovered = self.opinions[topic][1]

        if topic in self.sexy_opinions: # we passed None for discovered so use existing discovered info
            if sexy_opinion is None:
                sexy_opinion = True
            if discovered is None:
                discovered = self.sexy_opinions[topic][1]

        if discovered is None: # we didn't find any discovery information for opinion, so it's new and we passed None, so default set to false
            discovered = False
        if sexy_opinion is None:
            if topic in sexy_opinions_list: # We didn't find the topic in existing opinions for person, check global list if it is sexy
                sexy_opinion = True
            sexy_opinion = False

        if sexy_opinion:
            self.sexy_opinions[topic] = [degree, discovered]

            if topic not in sexy_opinions_list: # Appends to the opinion pool #TODO: should we add this to the game pool here? Prevents person specific opinions...
                sexy_opinions_list.append(topic)
        else:
            self.opinions[topic] = [degree, discovered]
            if topic not in opinions_list: # Appends to the opinion pool #TODO: should we add this to the game pool here? Prevents person specific opinions...
                opinions_list.append(topic)

        if add_to_log:
            mc.log_event((self.title or self.name) + " " + opinion_score_to_string(degree) + " " + str(topic), "float_text_green")

    # Adds a function that edits and adds opinions. It also appends to the vanilla opinion pool.
    Person.add_opinion = add_opinion

    ## Increase the opinion on a specific topic (opinion)
    def increase_opinion_score(self, topic, add_to_log = True):
        score = self.get_opinion_score(topic)

        if score < 2:
            score += 1

        if topic in self.sexy_opinions:
            self.sexy_opinions[topic][0] = score
        if topic in self.opinions:
            self.opinions[topic][0] = score

        if add_to_log:
            mc.log_event((self.title or self.name) + " " + opinion_score_to_string(score) + " " + str(topic), "float_text_green")
        return
    # Add increase opinion function to person class
    Person.increase_opinion_score = increase_opinion_score

    ## Decrease the opinion on a specific topic (opinion)
    def decrease_opinion_score(self, topic, add_to_log = True):
        score = self.get_opinion_score(topic)

        if score > -2:
            score -= 1

        if topic in self.sexy_opinions:
            self.sexy_opinions[topic][0] = score
        if topic in self.opinions:
            self.opinions[topic][0] = score

        if add_to_log:
            mc.log_event((self.title or self.name) + " " + opinion_score_to_string(score) + " " + str(topic), "float_text_green")
        return
    # Add decrease opinion function to person class
    Person.decrease_opinion_score = decrease_opinion_score

    ##Max the opinion on a specific topic (opinion)
    def max_opinion_score(self, topic, add_to_log = True):
        score = self.get_opinion_score(topic)
        if score < 2:
            if topic in self.sexy_opinions:
                self.sexy_opinions[topic][0] = 2
            if topic in self.opinions:
                self.opinions[topic][0] = 2

            if add_to_log:
                mc.log_event((self.title or self.name) + " " + opinion_score_to_string(2) + " " + str(topic), "float_text_green")
        return

    # Add max opinion function to person class
    Person.max_opinion_score = max_opinion_score

    # Change Multiple Stats for a person at once (less lines of code, better readability)
    def change_stats(self, obedience = None, happiness = None, arousal = None, love = None, slut_temp = None, slut_core = None, add_to_log = True):
        if not obedience is None:
            self.change_obedience(obedience, add_to_log)
        if not happiness is None:
            self.change_happiness(happiness, add_to_log)
        if not arousal is None:
            self.change_arousal(arousal, add_to_log)
        if not love is None:
            self.change_love(love, add_to_log)
        if not slut_temp is None:
            self.change_slut_temp(slut_temp, add_to_log)
        if not slut_core is None:
            self.change_slut_core(slut_core, add_to_log)
        return

    Person.change_stats = change_stats

    ## CHANGE WILLPOWER EXTENSION
    # changes the willpower of a person by set amount
    def change_willpower(self, amount): #Logs change in willpower and shows new total.
        self.willpower += amount
        if self.willpower < 0:
            self.willpower = 0
        return person.willpower

    # attach to person object
    Person.change_willpower = change_willpower

    def review_outfit_enhanced(self, dialogue = True):
        self.outfit.remove_all_cum()

        if self.should_wear_uniform():
            self.wear_uniform() # Reset uniform
        else:
            self.outfit.update_slut_requirement()
            # only show review message when parameter is true and she doesn't feel comfortable in her current outfit
            dialogue = dialogue and self.outfit.slut_requirement > self.sluttiness
            self.apply_outfit(self.planned_outfit)    # always restore outfit
            if dialogue:
                self.call_dialogue("clothing_review") # must be last call in function

    Person.review_outfit = review_outfit_enhanced

    def draw_person_enhanced(self,position = None, emotion = None, special_modifier = None, show_person_info = True, lighting = None, background_fill = "#0026a5", the_animation = None, animation_effect_strength = 1.0, character_placement = None, from_scene = False): #Draw the person, standing as default if they aren't standing in any other position.
        if position is None:
            position = self.idle_pose

        if emotion is None:
            emotion = self.get_emotion()

        if the_animation is None:
            the_animation = self.idle_animation

        if not can_use_animation():
            the_animation = None

        if character_placement is None: # make sure we don't need to pass the position with each draw
            character_placement = character_right

        if lighting is None:
            lighting = mc.location.get_lighting_conditions()

        # sometimes there is no outfit set, causing the generate drawlist to fail, not sure why, but try to fix it here.
        if self.outfit is None:
            if self.planned_outfit is None:
                self.planned_outfit = self.wardrobe.decide_on_outfit2(self) # Use enhanced outfit function
            self.apply_outfit(self.planned_outfit)
            self.review_outfit(dialogue = False)

        # if normal draw person call, clear scene
        if not from_scene:
            renpy.scene("Active")
            if show_person_info:
                renpy.show_screen("person_info_ui",self)

        if the_animation:
            final_image = self.build_person_animation(the_animation, position, emotion, special_modifier, lighting, background_fill, animation_effect_strength)
        else:
            final_image = self.build_person_displayable(position, emotion, special_modifier, lighting, background_fill)

        renpy.show(self.name + self.last_name + "_anim",at_list=[character_placement, scale_person(self.height)],layer="Active",what=final_image,tag=self.name + self.last_name +"_anim")

    # replace the default draw_person function of the person class
    Person.draw_person = draw_person_enhanced
    # add location to store original personality
    Person.original_personality = None

    def draw_animated_removal_enhanced(self, the_clothing, position = None, emotion = None, special_modifier = None, lighting = None, background_fill = "#0026a5", the_animation = None, animation_effect_strength = 1.0, character_placement = None, scene_manager = None): #A special version of draw_person, removes the_clothing and animates it floating away. Otherwise draws as normal.
        #Note: this function includes a call to remove_clothing, it is not needed seperately.
        if position is None:
            position = self.idle_pose

        if emotion is None:
            emotion = self.get_emotion()

        if lighting is None:
            lighting = mc.location.get_lighting_conditions()

        if character_placement is None: # make sure we don't need to pass the position with each draw
            character_placement = character_right

        if not can_use_animation():
            the_animation = None

        renpy.scene("Active") # clear layer for new draw action
        if scene_manager is None:
            renpy.show_screen("person_info_ui",self)
        else:   # when we are called from the scene manager we have to draw the other characters
            scene_manager.draw_scene_without(self)

        if the_animation:
            bottom_displayable = self.build_person_animation(the_animation, position, emotion, special_modifier, lighting, background_fill, animation_effect_strength = 1.0)
        else:
            bottom_displayable = Flatten(self.build_person_displayable(position, emotion, special_modifier, lighting, background_fill))

        self.outfit.remove_clothing(the_clothing)

        if the_animation:
            top_displayable = self.build_person_animation(the_animation, position, emotion, special_modifier, lighting, background_fill, animation_effect_strength)
        else:
            top_displayable = Flatten(self.build_person_displayable(position, emotion, special_modifier, lighting, background_fill))

        renpy.show(self.name+self.last_name+"_new", at_list=[character_placement, scale_person(self.height)], layer = "Active", what = top_displayable, tag = self.name + self.last_name +"_new")
        renpy.show(self.name+self.last_name+"_old", at_list=[character_placement, scale_person(self.height), clothing_fade], layer = "Active", what = bottom_displayable, tag = self.name + self.last_name +"_old")

    Person.draw_animated_removal = draw_animated_removal_enhanced

    ####### Begin cum override functions ######

    def cum_in_mouth_enhanced(self): #Add the appropriate stuff to their current outfit, and peform any personal checks if rquired.
        mc.listener_system.fire_event("sex_cum_mouth", the_person = self)
        if self.outfit.can_add_accessory(mouth_cum):
            the_cumshot = mouth_cum.get_copy()
            the_cumshot.layer = 0
            self.outfit.add_accessory(the_cumshot)

        self.change_slut_temp(5*self.get_opinion_score("drinking cum"))
        self.change_happiness(5*self.get_opinion_score("drinking cum"))
        self.discover_opinion("drinking cum")

        self.sex_record["Cum in Mouth"] += 1


    def cum_in_vagina_enhanced(self):
        mc.listener_system.fire_event("sex_cum_vagina", the_person = self)
        if self.outfit.can_add_accessory(creampie_cum):
            the_cumshot = creampie_cum.get_copy()
            the_cumshot.layer = 0
            self.outfit.add_accessory(the_cumshot)

        self.change_slut_temp(5*self.get_opinion_score("creampies"))
        self.change_happiness(5*self.get_opinion_score("creampies"))
        self.discover_opinion("creampies")

        self.sex_record["Vaginal Creampies"] += 1

    def cum_in_ass_enhanced(self):
        mc.listener_system.fire_event("sex_cum_ass", the_person = self)
        #TODO: Add an anal specific cumshot once we have renders for it.
        if self.outfit.can_add_accessory(creampie_cum):
            the_cumshot = creampie_cum.get_copy()
            the_cumshot.layer = 0
            self.outfit.add_accessory(the_cumshot)
        self.change_slut_temp(5*self.get_opinion_score("anal creampies"))
        self.change_happiness(5*self.get_opinion_score("anal creampies"))
        self.discover_opinion("anal creampies")

        self.sex_record["Anal Creampies"] += 1

    def cum_on_face_enhanced(self):
        mc.listener_system.fire_event("sex_cum_on_face", the_person = self)
        if self.outfit.can_add_accessory(face_cum):
            the_cumshot = face_cum.get_copy()
            the_cumshot.layer = 0
            self.outfit.add_accessory(the_cumshot)

        self.change_slut_temp(5*self.get_opinion_score("cum facials"))
        self.change_happiness(5*self.get_opinion_score("cum facials"))
        self.discover_opinion("cum facials")

        self.change_slut_temp(5*self.get_opinion_score("being covered in cum"))
        self.change_happiness(5*self.get_opinion_score("being covered in cum"))
        self.discover_opinion("being covered in cum")

        self.sex_record["Cum Facials"] += 1

    def cum_on_tits_enhanced(self):
        mc.listener_system.fire_event("sex_cum_on_tits", the_person = self)
        if self.outfit.can_add_accessory(tits_cum):
            the_cumshot = tits_cum.get_copy()
            if self.outfit.get_upper_visible():
                top_layer = self.outfit.get_upper_visible()[0].layer #Get the top most pice of clothing and get it's layer.
            else:
                top_layer = -1
            the_cumshot.layer = top_layer+1 #The cumshot lives on a layer it hit, above the one it hit. Accessories are drawn first in the hirearchy, so they have to be on a level higehr than what they hit.
            self.outfit.add_accessory(the_cumshot)

        self.change_slut_temp(5*self.get_opinion_score("being covered in cum"))
        self.change_happiness(5*self.get_opinion_score("being covered in cum"))
        self.discover_opinion("being covered in cum")

        self.sex_record["Cum Covered"] += 1

    def cum_on_stomach_enhanced(self):
        mc.listener_system.fire_event("sex_cum_on_stomach", the_person = self)
        if self.outfit.can_add_accessory(stomach_cum):
            the_cumshot = stomach_cum.get_copy()
            if self.outfit.get_upper_visible():
                top_layer = self.outfit.get_upper_visible()[0].layer #Get the top most pice of clothing and get it's layer.
            else:
                top_layer = -1
            the_cumshot.layer = top_layer+1 #The cumshot lives on a layer it hit, above the one it hit. Accessories are drawn first in the hirearchy, so they have to be on a level higehr than what they hit.
            self.outfit.add_accessory(the_cumshot)

        self.change_slut_temp(5*self.get_opinion_score("being covered in cum"))
        self.change_happiness(5*self.get_opinion_score("being covered in cum"))
        self.discover_opinion("being covered in cum")

        self.sex_record["Cum Covered"] += 1

    def cum_on_ass_enhanced(self):
        mc.listener_system.fire_event("sex_cum_on_ass", the_person = self)
        if self.outfit.can_add_accessory(ass_cum):
            the_cumshot = ass_cum.get_copy()
            if self.outfit.get_lower_visible():
                top_layer = self.outfit.get_lower_visible()[0].layer #Get the top most pice of clothing and get it's layer.
            else:
                top_layer = -1
            the_cumshot.layer = top_layer+1 #The cumshot lives on a layer it hit, above the one it hit. Accessories are drawn first in the hirearchy, so they have to be on a level higehr than what they hit.
            self.outfit.add_accessory(the_cumshot)

        self.change_slut_temp(5*self.get_opinion_score("being covered in cum"))
        self.change_happiness(5*self.get_opinion_score("being covered in cum"))
        self.discover_opinion("being covered in cum")

        self.sex_record["Cum Covered"] += 1

    Person.cum_in_mouth = cum_in_mouth_enhanced
    Person.cum_in_vagina = cum_in_vagina_enhanced
    Person.cum_in_ass = cum_in_ass_enhanced
    Person.cum_on_face = cum_on_face_enhanced
    Person.cum_on_tits = cum_on_tits_enhanced
    Person.cum_on_stomach = cum_on_stomach_enhanced
    Person.cum_on_ass = cum_on_ass_enhanced

######################################
# Override give serum for added goal #
######################################

    def give_serum_enhanced(self,the_serum_design): ##Make sure you are passing a copy of the serum, not a reference.
        mc.listener_system.fire_event("give_random_serum", the_person = self)
        self.serum_effects.append(the_serum_design)
        the_serum_design.run_on_apply(self) # add to log is done through SerumTrait.on_apply(), each trait effect gets logged

    Person.give_serum = give_serum_enhanced


#######################################
# HELPER METHODS FOR CLASS EXTENSIONS #
#######################################

    # Check if weight property exists on person, if not, add based on body type
    def check_person_weight_attribute(person):
        if not hasattr(person, "weight"):
            if (person.body_type == "thin_body"):
                setattr(person, "weight", 60 * person.height)   # default weight thin body
            elif (person.body_type == "standard_body"):
                setattr(person, "weight", 75 * person.height)   # default weight standard body
            else:
                setattr(person, "weight", 90 * person.height)   # default weight curvy body
        return

    # calculates current player mental powers
    def player_willpower():
        mc.power = 0

        mc.power += int(mc.charisma*5) # Positive character modifiers
        mc.power += int((mc.energy / 20) * 1.5)
        return mc.power

    # calculates current willpower of a person
    def calculate_willpower(person):
        willpower = int(person.focus * 10 + person.happiness * 0.2 - person.obedience * 0.1 - person.love * 0.2 - person.suggestibility * 0.5)

        if willpower < 0:
            willpower = 0
        return willpower

    # log will power to event log in ui
    def log_willpower(person):
        if (person is mc):
            message = "Your: " + str(person.power)
        else:
            message = (person.title or person.name) + ": " + str(person.willpower)
        message += " Willpower"
        mc.log_event(message, "float_text_blue")
        return

#########################################
# Add hash (unique id) to Person object #
#########################################

    def person__hash__(self):
        return hash((self.name, self.last_name, self.age))

    Person.__hash__ = person__hash__
    Person.hash = person__hash__

    def person__eq__(self, other):
        if isinstance(self, other.__class__):
            return hash((self.name, self.last_name, self.age)) == hash((other.name, other.last_name, other.age))
        return False

    Person.__eq__ = person__eq__

    def person__ne__(self, other):
        if isinstance(self, other.__class__):
            return hash((self.name, self.last_name, self.age)) != hash((other.name, other.last_name, other.age))
        return True

    Person.__ne__ = person__ne__
