#Mid game quest. Is available mid game, will help with profitability.
#Requires a couple of employees available for quests atleast 60+ sluttiness.
#Porn video circulates around the company of one of the employees in a porn video. Its a very popular video.
#MC approaches the porn star. Asks her to be moved to marketing.
#Girl is having trouble finding an actor for a new vid, says she will if MC helps her produce her next video.
#Make video
#Video gains popularity based on quality, determined by positions, # female orgasms, and unique cumshots.
#After, she joins marketting. While she is in marketting, gain a bonus to profitability.
#Gain the ability to "Shoot porn video" with her. Can be done once per week and brings in extra cash.
#Once complete, can refer to girl as porn star, slight personality tweek.

# flags
# 1: Quest has been initiated
# 11: MC has seen video.
# 19: MC makes memo not to bother girl about making porn. (Bad End)
# 21: MC talks to girl about video and how good it was, girl asks MC to make a new one within X days (how we time limit this)
# 29: MC does not make video in time. Receives text from girl saying she found another actor but thanks anyway.
# 31: Porn video created, wait a few days to see how popular it is.
# 39: Porn video is a dud. Lose obedience from all girls in the office (They all see it and know how poorly MC performed) (Bad end).
# 41: If popular, girl says she really appreciates it, would be open to using you as an actor in the future. Offers to promote MC.business.name
# 42: If very popular, all girls at office get obedience and sluttiness bonus.
# 49: MC says thats okay, just had fun making video. (Bad End)
# 101: Girl moves to marketing. Gain marketability based on sex video rating. (Good end)
# Any 100 ending adds marketability. Also 40+ can refer to girl as porn star, personality tweak.


init 1 python:
    def setup_quest_porn_actress():
        able_person_list = []
        for person in mc.business.get_employee_list(): #TODO is there a method that grabs ENTIRE employee list?
            if person not in quest_director.unavailable_persons:
                if person.core_sluttiness > 60:
                    able_person_list.append(person)

        quest_porn_actress.quest_event_dict["start_day"] = 9999
        quest_porn_actress.quest_event_dict["target"] = get_random_from_list(able_person_list)
        quest_porn_actress.quest_event_dict["disease_name"]  = quest_cure_discovery_disease_name()
        quest_porn_actress.quest_event_dict["market_contact"] = None
        quest_porn_actress.quest_event_dict["market_day"] = 9999
        quest_porn_actress.set_quest_flag(1)
        return

    def rate_porn_video(the_report, the_person):  #Takes a sex report and person and returns a score of 1-10 on how good the video isself.
        porn_score = 0
        if len(the_report.get("positions_used", [])) <= 1:  #Max three points for number of positions used
            porn_score += 1
        elif the_report.get("positions_used", []) <= 4:
            porn_score += 2
        else:
            porn_score += 3

        if the_report.get("girl orgasms", 0) <= 4:   #Max 4 points for as many female orgasms
            porn_score += the_report.get("girl orgasms", 0)
        else:
            porn_score += 4
        cum_score = 0   #Max three points based on cum shots.
        if the_person.outfit.has_ass_cum():
            cum_score += 1
        if the_person.outfit.has_mouth_cum():
            cum_score += 1
        if the_person.outfit.has_tits_cum():
            cum_score += 1
        if the_person.outfit.has_stomach_cum():
            cum_score += 1
        if the_person.outfit.has_face_cum():
            cum_score += 1
        if the_person.outfit.has_creampie_cum():
            cum_score += 1
        if cum_score > 3:
            cum_score = 3
        porn_score += cum_score

        return porn_score

#Quest defining functions

    def quest_porn_actress_tracker():

        return

    def quest_porn_actress_start_requirement():

        return
    def quest_porn_actress_cleanup():

         # cleanup dictionary to save space and memory
        quest_porn_actress.quest_event_dict.clear()
        return

#Label requirement functions



#Action declarations


#Quest Labels
label quest_porn_actress_init_label():
    $ setup_quest_porn_actress()
    return

label quest_porn_actress_intro_label():
    $ the_target = quest_porn_actress.quest_event_dict.get("target", None)
    $ personnel_list = mc.business.get_employee_list()
    $ personnel_list.remove(the_target)
    $ the_person_one = get_random_from_list(personnel_list)
    $ personnel_list.remove(the_person_one)
    $ the_person_two = get_random_from_list(personnel_list)
    while the_target == the_person:   #If they are same, get a different employee
        $ the_person = get_random_from_list(mc.business.get_employee_list())
    "You get up to stretch your legs for a bit and to check on the different departments, making sure everything is running smoothly."
    "As you pass by the break room, you overhear something."
    the_person_one.char "Oh my... is that really [the_target.name]? It looks just like her... That's what the other girls are saying!"
    the_person_two.char "Wow, I think it is! If not its her twin sister!"
    "You walk into the break room."
    $ scene_manager = Scene() # make sure we have a clean scene manager
    $ scene_manager.add_actor(the_person_one)
    $ scene_manager.add_actor(the_person_two, character_placement = character_center_flipped)
    "You see [the_person_one.possessive_title] and [the_person_two.title] looking at a phone. The sound of erotic moaning is coming from the phone."
    "[the_person_one.title] notices you walk in."
    the_person_one.char "Oh hey [the_person_one.mc_title]. Have you seen this?"
    the_person_two.char "Yeah, it looks just like [the_target.name]!"
    "[the_person_one.title] turns the phone to you. It is a porn video of a woman who looks exactly like [the_target.title]. She is taking a cock like a champ doggy style."
    "... And sounds suspiciously like [the_target.title]..."
    "... Wow, that has to be her!"
    mc.name "Looks like her? That... I'm almost positive that it IS her!"
    the_person_two.char "I know! That's what a lot of the other girls around the office are saying!"
    mc.name "Hmm... maybe I should ask her."
    the_person_one.char "Oh, I mean... wouldn't that be kind of violating her privacy? Like, she probably didn't realize we would all be passing this video around..."
    mc.name "You're right. If she wants to do porn videos in her spare time, she can certainly do so. I'll approach the subject carefully with her."
    the_person_two.char "Yeah but... I wonder if she even knows this video is on the internet? It's pretty amateur... maybe it was supposed to be private?"
    "This is a sticky situation. Should you respect her privacy? Or inspect the video?"
    menu:
        "Respect her privacy":
            pass
            #TODO this
        "Investigate the video":
            mc.name "Would you mind forwarding me the video? I'd like to look into it a bit more."
            the_person_one.char "Look into it? Hah, that's funny! It's a good video, don't worry I'll send you the link, [the_person_one.mc_title]."
            the_person_two.char "Hey, while you're at it, could you forward it to me too? I umm, might want to investigate it later too..."
            "The girls laugh. In a few moments you have a link to the video in your messages."


    $ scene_manager.remove_actor(the_person_one)
    $ scene_manager.remove_actor(the_person_two)
    "You excuse yourself from the break room and head to your office you pull up the video and watch it."
    "It definitely has an amateur feel to it. It is one of the POV videos where the man is also the cameraman."
    "[the_target.title], if it is her, has a pretty good performance in the video. But you have to wonder if she even knows the video is online."
    "You decide to speak with [the_target.title]. At the very least, make sure she knows the video is out there."

    $ del the_target
    $ del personnel_list
    return