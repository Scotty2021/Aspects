init:
    python:
        SB_doggy_anal_dildo_dp = Position("Doggy Anal DP",80,110,"doggy","Lay","Vagina","Anal",25,18,[],
        "intro_SB_doggy_anal_dildo_dp",
        ["scene_SB_doggy_anal_dildo_dp_1","scene_SB_doggy_anal_dildo_dp_2"],
        "outro_SB_doggy_anal_dildo_dp",
        "transition_default_SB_doggy_anal_dildo_dp",
        "strip_SB_doggy_anal_dildo_dp", "strip_ask_SB_doggy_anal_dildo_dp",
        "orgasm_SB_doggy_anal_dildo_dp",
        opinion_tags = ["doggy style sex" "anal sex" "vaginal sex"])
        #list_of_positions.append(SB_doggy_anal_dildo_dp)

#init 1:
#    python:
#        SB_doggy_anal_dildo_dp.link_positions_two_way(doggy, "transition_SB_doggy_anal_dildo_dp_doggy", "transition_doggy_SB_doggy_anal_dildo_dp")

label intro_SB_doggy_anal_dildo_dp(the_person, the_location, the_object, the_round):
    mc.name "[the_person.title], I want you to get on your hands and knees for me. I want to fuck your ass and your pussy."
    "You secure the strap on dildo to your cock. A quick lube application later, you get behind [the_person.possessive_title]"
    if the_person.effective_sluttiness() > 110:
        the_person.char "Oh god I love it when you do this to me..."
    elif the_person.effective_sluttiness() > 80:
        the_person.char "Ok, just be careful [the_person.mc_title]..."
    else:
        the_person.char "I don't know, are you sure that thing is gonna fit in me back there?"
    "[the_person.possessive_title] gets onto all fours in front of you on the [the_object.name]. She arches her back and presents her ass."
    if the_person.arousal > 60:
        "Her pussy is already dripping with arousal. You line yourself up with her ass, while she reaches down and lines the dildo up with her pussy."
    else:
        "You line yourself up with her ass while [the_person.possessive_title] reaches down and lines the dildo up with her pussy."
    "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
    if the_person.get_opinion_score("anal sex") > 0 :
        the_person.char "Oh my god! I'm so full... Its so good [the_person.mc_title]!"
        $ the_person.discover_opinion("anal sex")
    else:
        the_person.char "Holy fuck! Go slow [the_person.mc_title]. This is really intense..."
    return

label scene_SB_doggy_anal_dildo_dp_1(the_person, the_location, the_object, the_round):
    "You give [the_person.possessive_title]'s ass a good hard spank. She lets out a loud yelp"
    $ the_person.call_dialogue("sex_responses")
    if the_person.sex_skills["Anal"] < 2: #Inexperienced
        "[the_person.possessive_title] reflexively starts to pull away after you spank her. You grab her hips to keep her from pulling off completely."
        the_person.char "Sorry, I just... I don't do this very often... please just be gentle with me!"
        "You pull her hips back toward you slowly. Her inexperienced ass yields to your penis and she sighs as you bottom out"
        "Pushing deep, the vibrating function on the dildo is in direct contact with her clit. She squirms and moans, being stuffed completely full."
        "You decide to give her a little break in the intensity of your fucking. Leaving yourself deep inside her, you kneed her ass cheeks with both hands."
        the_person.char "mmm, that feels good [the_person.mc_title]. Can I touch myself while you do that?"
        menu:
            "Masturbate for me":
                 "Encouraged by your response, [the_person.possessive_title] reaches down with one hand and begins to rub her clit."
                 "You take it slow, and you revel in the delicious pleasure of each penetration as you thrust. With each thrust the vibrator brushes against her fingers on her clit."
                 "[the_person.possessive_title] struggles to hold herself up with one hand while the other works circles around her clit"
                 if the_person.get_opinion_score("masturbating") > 0:
                     "[the_person.possessive_title] moves her fingers masterfully across her pussy. You can tell she masturbates often."
                     $ the_person.discover_opinion("masturbating")
                     $ the_person.change_arousal(the_person.get_opinion_score("masturbating" * 5))
                 if the_person.sluttiness > 100:
                     the_person.char "I'm sorry [the_person.mc_title], I'll try to get better at this. Having you in my ass is so intense..."
                     the_person.char "and then the dildo with it? I've never felt so full..."
                 else:
                     "[the_person.possessive_title] seems to be enjoying the anal penetration a bit more now that she is touching herself"
            "Fuck me with your ass":
                 if the_person.obedience > 130 or the_person.get_opinion_score("being submissive") > 0:
                     the_person.char "Yes sir. I'll do my best"
                 else:
                     the_person.char "I'll give it my best, but this better be worth it..."
                 "[the_person.possessive_title] slowly eases forward until just the tip remains inside, then slowly backs her ass back onto you. She is trying to obey but you can tell she is struggling to take you"
                 "The next time she starts to ease forward, you put your hand on her hips for a second to stop her. You spit into your hand then rub it along your shaft a bit, hoping it will make the penetration easier"
                 the_person.char "Mmm, that's a bit better..."
                 "With the extra lube, [the_person.possessive_title] resumes fucking you. She still has a fairy slow pace, but is a bit quicker than before."

    else:
        "In response to your spanking, [the_person.possessive_title] thrusts herself back against you. Your penis is completely consumed by her bowel and she moans lewdly."
        "When she starts to pull off you give her other ass check a hard swat. She buries her face in the [the_object.name] and moans as she pushes herself back onto you again."
        the_person.char "Oh fuck [the_person.mc_title], I needed this so bad. Make me cum all over that dildo!"
        "[the_person.possessive_title]'s ass feels so tight you are tempted to let her continue setting the pace, but you worry she might get the wrong idea if you let this little slut take charge."
        menu:
            "Fuck me with your ass":
                 "You decide to see what [the_person.possessive_title] can do if you let her take control of the pace. Encouraged by your words, she eagerly works your cock with her ass" ###FINISH
                 the_person.char "Mmm, does it feel good when I work it like this?"
                 "[the_person.possessive_title] begins to twerk up and down your shaft with quick, shallow movements."
                 if mc.arousal > 70:
                      mc.name "Damn that feels good. You're gonna make me cum if you keep that up. Where do you want my load?"
                      if the_person.get_opinion_score("creampies") > 0:
                           the_person.char "You should just shove it in as deep as you can and cum inside me."
                      elif the_person.get_opinion_score("being covered in cum") > 0:
                           the_person.char "You should pull out and cum all over my ass. That would be so hot..."
                      elif the_person.get_opinion_score("cum facials") > 0:
                           the_person.char "Tell me when you are about to cum and I'll let you cum all over my face..."
                      elif the_person.obedience > 130:
                           the_person.char "Cum wherever you want to... I just want to please you sir"
                      else:
                           the_person.char "I don't know... wherever you want I guess?"
                 else:
                      mc.name "Wow, your ass is amazing. I love watching my dick disappear in your ass and the dildo into your pussy."
                      if the_person.get_opinion_score("anal sex") > 0:
                           "In response, she slams her ass all the way back on your dick. She grinds her hips left and right up against you. The grinding motion stimulates her clit against the vibrator."
                           the_person.char "It's so good... I can't think... its so good!"
                           "You can feel her tense and relax her muscles in her ass rhythmically, messaging your shaft while you remain totally engulfed inside her."
                           mc.name "Wow, the things you do with this ass. You are amazing [the_person.title]"
                           "[the_person.possessive_title] sighs. You can tell the double penetration is very fulfilling for her."
                      else:
                           "[the_person.possessive_title] looks back at you."
                           the_person.char "Honestly, I'm not usually into butt stuff... but I just want to make you feel so good..."
                           the_person.char "And the dildo makes this so much better than just anal... its AMAZING."
                 "[the_person.possessive_title] continues to twerk her ass up and down on your penis. How does she make it look so easy?"
            "I'm in charge here":
                 "Sensing that your slut is getting out of hand, you quickly take charge. You grab her by the hair and pull her head back until her hands are no longer on the ground, taking away all her leverage."
                 $ the_person.call_dialogue("suprised_exclaim")
                 "You lean forward and whisper into [the_person.possessive_title]'s ear."
                 mc.name "I know you dream about my dick in your ass constantly and it feels good to finally have that dream come true, but don't forget who is in charge around here."
                 if SB_check_fetish(the_person, anal_fetish_role):
                     "[the_person.possessive_title] whimpers in total submission to you."
                     the_person.char "I dream about it... I beg for it... It completes me! I'm not me unless your dick is deep in my ass [the_person.mc_title]!"
                     "You give her a couple slow, heavy thrusts before releasing her hair. She returns her hands to the ground and moans when you resume your slow, methodical fucking."
                 elif the_person.obedience > 130 or the_person.get_opinion_score("being submissive") > 0:
                     $ the_person.discover_opinion("being submissive")
                     if the_person.get_opinion_score("being submissive") > 0:
                         $ the_person.change_arousal(the_person.get_opinion_score("being submissive" * 5))
                         "For once, [the_person.possessive_title] is speechless. She can only whimper softly in total submission to you."
                     else:
                         the_person.char "I'm sorry [the_person.mc_title], I couldn't help myself. Please use me however you want, I'll be good I promise!"
                     "You give her a couple slow, heavy thrusts before releasing her hair. She returns her hands to the ground and moans when you resume your slow, methodical fucking."
                 else :
                     the_person.char "Okay! Geesh! Be careful with my hair, that hurts!"
                #TODO this option is kinda boring... expand some?

    return


label scene_SB_doggy_anal_dildo_dp_2(the_person, the_location, the_object, the_round):
    "[the_person.possessive_title] lowers her shoulders against the [the_object.name] and groans as you fuck her from behind."
    the_person.char "Ah... I feel so full!"
    "The dildo is clearly making the experience much more intense for her."
    "You reach forward and place your hands on [the_person.possessive_title]'s shoulders. With each thrust you pull her back onto you forcefully, your hips smacking her ass cheeks loudly. She arches her back and lets out a series of satisfied yelps."
    $the_person.call_dialogue("sex_responses")
    if the_person.arousal > 130:
        "[the_person.possessive_title]'s pussy is now constantly spasming in orgasm. Her juices are running out from around the dildo and down the inside of her legs."
        "With every quiver and every spasm, her buttery butthole contracts and squeezes your cock, begging you to cum for her."
    if the_person.arousal > 80:
        "[the_person.possessive_title]'s pussy is dripping wet. A damp spot has begun to accumulate below her pussy as a result of your rutting."
        the_person.char "Ohhh, you feel so fucking good in my ass."
    else:
        "[the_person.possessive_title] seems to be enjoying the double penetration you are giving her. She yelps in response to one particularly eager thrust."
        the_person.char "God dammit, you're so fucking big. You feel huge... I'm so full."
    if the_person.get_opinion_score("masturbating") > 0:
        "You notice that[the_person.possessive_title] now has one hand on her pussy, rubbing her clit, and with the other hand she reaches back and pulls her ass cheeks apart."
        $ the_person.change_arousal(the_person.get_opinion_score("masturbating" * 3))
    else:
        "[the_person.possessive_title] reaches back with both hands and spreads her ass cheeks apart."
        "You decide with her cheeks spread wide to see how deep you can get yourself into [the_person.possessive_title]. "
        "With her hands busy, she has no way of holding up your weight as you push yourself forward and then down on top of her, your full body weight pushing her prone down onto the [the_object.name]"
        "[the_person.possessive_title] whimpers, her body now pinned between your body and [the_object.name]. The vibrating dildo stimulates her pussy mercilessly."
        if SB_check_fetish(the_person, anal_fetish_role):
            "Despite having no leverage, [the_person.possessive_title] wriggles her ass against you as best as she can. Even with no room to move, her love for anal sex drives her to try to milk your cock"
            "You enjoy her efforts before you speak clearly to her."
            mc.name "You are such a slut. Is it nice to finally have a real cock, stuffed deep in your tight little asshole?"
            "[the_person.possessive_title] is writhing in pleasure, having her fetish of anal sex fulfilled. The extra stimulation from the dildo just makes it even better."
            the_person.char "Oh god it is. Everytime I play with my ass and all I can think about is your big meaty dick buried inside me."
            "You grab her hair at the base of her scalp and pull her head back before whispering into her ear."
            mc.name "Don't worry, slut. This won't be the last time I stuff your holes. This one especially."
            "You give her prone body a forceful thrust."
            "You can see goosebumps all over [the_person.possessive_title]'s skin. She moans and then begs you to keep fucking her."
            the_person.char "I was made to be your little cock sleeve. Fuck me [the_person.mc_title]!"
        elif the_person.get_opinion_score("creampies") > 0:
            the_person.char "Holy hell that is deep... tell me... tell me you'll push it this deep again when you cum... that would be so hot!"
            $mc.change_arousal(5)
            "In your mind, you play out the fantasy of cumming so deep in [the_person.possessive_title]'s ass, even when you pull out not a drop of your seed leaks out."
            "You give the idea serious consideration. You can tell she would love it if you did."
        elif the_person.get_opinion_score("anal sex") > 0:
            "Despite having no leverage, [the_person.possessive_title] wriggles her ass against you as best as she can. Even with no room to move, her love for anal sex drives her to milk your cock"
            "You lower your face down behind her head and whisper into her ear."
            mc.name "Mmm, so rear entry is how you like it, slut? Don't worry, this won't be the last time you feel my cock ravage your back door."
            "You can see goosebumps all over [the_person.possessive_title]'s skin. You wonder how many times you can make her cum before you blow your load."
            $ the_person.change_slut_temp(2)
        elif the_person.sluttiness > 100:
            the_person.char "Oh fuck, bury it in me [the_person.mc_title]! I don't think I've ever felt so full..."
        else:
            "[the_person.possessive_title] lets out a loud groan. You can tell she isn't used to being penetrated like this, but she is taking it as best as she can."
            the_person.char "God [the_person.mc_title] that is so intense... please just try to be gentle okay?"
        "You take a few seconds to enjoy being engulfed by her back passage, then give her a few slow, probing thrusts."
        "After a minute or two slow, deep thrusts you decide to move back to doggy. You push yourself up off of [the_person.possessive_title]'s back, and she follows, getting on all fours again to resume your fucking."

    return


label scene_SB_doggy_anal_dildo_dp_3(the_person, the_location, the_object, the_round):
    "third scene here"





    return

label outro_SB_doggy_anal_dildo_dp(the_person, the_location, the_object, the_round):
    "[the_person.possessive_title]'s tight ass draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    $the_person.call_dialogue("sex_responses")
    mc.name "Ah, I'm going to cum!"
    menu:
        "Cum inside of her.":
            "You pull back on [the_person.possessive_title]'s hips and drive your cock deep inside of her as you cum. She gasps softly in time with each new shot of hot semen inside of her."
            if the_person.get_opinion_score("creampies") > 0:
                the_person.char "Yes! Fill my ass with your cum!"
            $ cum_in_ass(the_person)
            $ SB_doggy_anal_dildo_dp.redraw_scene(the_person)
            if the_person.sluttiness > 110:
                the_person.char "Oh god it's so good. It doesn't matter which hole you do it in, I love it when you cum inside me."
            else:
                the_person.char "Oh fuck, I can't believe I let you cum in my ass..."

            "You wait until your orgasm has passed completely, then pull out and sit back. Her asshole gapes slightly and you can see a hint of your cum start to dribble out, but most of it stays buried with her bowel"

        "Cum on her ass.":
            "You pull out of [the_person.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
            if the_person.get_opinion_score("being covered in cum") > 0:
                 the_person.char "Yes! Paint me with your sticky cum!"
            $ the_person.cum_on_ass()
            $ SB_doggy_anal_dildo_dp.redraw_scene(the_person)
            if the_person.sluttiness > 120:
                the_person.char "Oh god your seed is so hot! Does it look sexy, having it plastered all over my ass?"
                "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
            else:
                the_person.char "Oh! Its so warm..."
            "You sit back and sigh contentedly, enjoying the sight of [the_person.possessive_title]'s ass covered in your semen."
        "Cum on her face.":
            mc.name "Fuck, get ready [the_person.title], I wanna cum on your face!"
            "You pull your cock out of [the_person.possessive_title]'s ass with a satisfying pop. She immediately turns around on gets on her knees in front of you."
            $ the_person.draw_person(position = "blowjob")
            if the_person.sluttiness > 80:
                "[the_person.possessive_title] sticks out her tongue for you and holds still, eager to take your hot load."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_person.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
                the_person.char "Oh god... it feels so good on my skin..."
            elif the_person.sluttiness > 60:
                "[the_person.possessive_title] closes her eyes and waits patiently for you to cum."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_person.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
            else:
                "[the_person.possessive_title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_person.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
            "You take a deep breath to steady yourself once you've finised orgasming. [the_person.possessive_title] looks up at you from her knees, face covered in your semen."
            $ the_person.call_dialogue("cum_face")


    return

label transition_SB_doggy_anal_dildo_dp_doggy(the_person, the_location, the_object, the_round):
    "You decide to give [the_person.possessive_title] a break. She murmurs a bit in disappointment when you slowly pull your dick out of her ass completely."
    "You bounce your hard shaft on her ass a couple of times before lining yourself up with her pussy."
    the_person.char "Wait, are you sure its okay to stick in there after its been in my ass?"
    "You ignore her question and push forward, slipping your shaft deep inside of [the_person.possessive_title]'s cunt. She gasps and quivers ever so slightly as you start to pump in and out."
    return

label transition_doggy_SB_doggy_anal_dildo_dp(the_person, the_location, the_object, the_round):
    "You stop your thrusting for a moment and she looks back at you. You put two fingers in front of her mouth, and after a moment she takes them in her mouth and starts to suck on them"
    "[the_person.possessive_title] slobbers all over your fingers for a few a seconds before you pull them out with a loud pop"
    "You use your fingers to crudely work in and out of her ass a few times to help get it lubricated. [the_person.possessive_title] moans at the feeling of your penis in one hole and your fingers in another"
    mc.name "Are you ready for me, [the_person.possessive_title]? I'm going to stick it in your ass now"
    the_person.char "Take me however you want, [the_person.mc_title], just be careful with me!"
    "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
    if the_person.get_opinion_score("anal sex") > 0 :
        the_person.char "Oh my god it's so dirty... but it is so good too..."
        $ the_person.discover_opinion("anal sex")
    return

label transition_default_SB_doggy_anal_dildo_dp(the_person, the_location, the_object, the_round):
    "[the_person.possessive_title] gets on her hands and knees as you kneel behind her. You bounce your hard shaft on her ass a couple of times before lining yourself up with her sphincter."
    "Once you're both ready you push yourself forward, slipping your hard shaft deep inside of her. She lets out a gasp under her breath."
    return

label strip_SB_doggy_anal_dildo_dp(the_person, the_clothing, the_location, the_object, the_round):
    "[the_person.possessive_title] leans forward a little further and pops off your cock."
    $ the_person.call_dialogue("sex_strip")
    $ the_person.draw_animated_removal(the_clothing, position = doggy.position_tag)
    "[the_person.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She groans happily when you push back inside of her."
    return

label strip_ask_SB_doggy_anal_dildo_dp(the_person, the_clothing, the_location, the_object, the_round):
    the_person.char "Sir, I'd like to take off my [the_clothing.name], would you mind?"
    "[the_person.char] pants as you fuck her from behind."
    menu:
        "Let her strip.":
            mc.name "Take it off for me."
            $ the_person.draw_animated_removal(the_clothing, position = doggy.position_tag)
            "[the_person.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
            "She groans happily when you push back inside of her."

        "Leave it on.":
            mc.name "No, I like how you look with it on."
            if the_person.sluttiness < 80:
                the_person.char "Do you think I look sexy in it?"
                "You speed up, fucking her faster in response to her question."
            elif the_person.sluttiness < 100:
                the_person.char "Does it make me look like a good little slut? All I want to be is your good little slut sir."
                "She pushes her hips back into you and moans happily."
            else:
                the_person.char "Does it make me look like the cum hungry slut that I am? That's all I want to be for you sir, your dirty little cum dumpster!"
                "She grinds her hips back into you and moans ecstatically."
    return

label orgasm_SB_doggy_anal_dildo_dp(the_person, the_location, the_object, the_round):
    if the_person.arousal > 150:
        "[the_person.possessive_title] has stopped being able to put together coherant sentences. She moans and gasps as yet another orgasm wracks her body."
        "You bury your cock in deep in [the_person.possessive_title]'s ass while she cums. Her bowel grips you tightly. The vibrations from the dildo intensify her orgasm."
        "Her body is now in a near constant state of orgasm. The constant quivering and her sexy moans are almost too much to bear."
        $ mc.change_arousal(10)
        the_person.char "Oh fuck... fuck... yes!"
        return
    "[the_person.possessive_title]'s tight back passage start to quiver, and suddenly tenses up."
    $ the_person.call_dialogue("climax_responses")
    "You bury your cock in deep in [the_person.possessive_title]'s ass while she cums. Her bowel grips you tightly. The vibrations from the dildo intensify her orgasm."
    "After a couple of seconds [the_person.possessive_title] sighs and the tension drains from her body."
    if the_person.get_opinion_score("anal sex") < 0:
        the_person.char "I can't believe that just happened... oh god now you're going to keep going, aren't you?"
    else:
        the_person.char "Don't stop... it still feels so good!"
    return
