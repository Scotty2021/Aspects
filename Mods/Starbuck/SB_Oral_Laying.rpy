﻿init:
    python:
        SB_Oral_Laying = Position("Cunnilingus",30,55,"missionary","Lay","Vagina","Oral",25,15,[],
        "intro_SB_Oral_Laying",
        ["scene_SB_Oral_Laying_1","scene_SB_Oral_Laying_2"],
        "outro_SB_Oral_Laying",
        "transition_default_SB_Oral_Laying",
        "strip_SB_Oral_Laying", "strip_ask_SB_Oral_Laying",
        "orgasm_SB_Oral_Laying",
        opinion_tags = ["being fingered","getting head"])
        list_of_positions.append(SB_Oral_Laying)

init 1:
    python:
        SB_Oral_Laying.link_positions_two_way(missionary, "transition_SB_Oral_Laying_missionary", "transition_missionary_SB_Oral_Laying")

label intro_SB_Oral_Laying(the_girl, the_location, the_object, the_round):
    "You run your hands along [the_girl.possessive_title]'s hips. You grab her ass and pull her close to you."
    mc.name "I want you to lie down for me. I want to taste you."
    "She nods and lies down on the [the_object.name]. You get on top off her for moment, grinding into her while you make out for a few seconds."
    if the_girl.outfit.tits_available():
        "You slowly start to move down her body. You stop on the way down to lick and suck her puffy nipples."
    else:
        "You slowly start to move down her body. You kiss and caress her as you go."
    "[the_girl.possessive_title] opens her legs wide as your get to her cunt. You breath in sharply through your nose, enjoying the tangy, musky scent of her arousal."
    if the_girl.arousal > 50:
        "[the_girl.possessive_title]'s pussy lips are engorged. They glisten with moisture from her excitement. You can't wait to taste it."
    else:
        "[the_girl.possessive_title]'s pussy is like a pristine flower. You can't wait to taste it."
    "A moan escapes her lips as you run your tongue up [the_girl.possessive_title]'s slit."
    return

label scene_SB_Oral_Laying_1(the_girl, the_location, the_object, the_round):
    # CHOICE CONCEPT: Finger Fuck // Tongue Fuck her
    # Intro concept. Short difference depending on if she's wet or not.
    if the_girl.arousal > 70:
        "[the_girl.possessive_title]'s juices are beginning to flow freely from her slit. You lap them up before circling your tongue aroud her clit a few times."
    else:
        "[the_girl.possessive_title]'s pussy is still getting wet. You lick it slow, giving her time to warm up."

    menu:
        "Finger Her.":
            #Generic choice with bonus based on girl opinion and MC foreplay skill
            "As you continue to lick all around [the_girl.possessive_title]'s cunt, you slowly push a finger up inside of her."
            if mc.sex_skills["Foreplay"] > 2:
                "You spend a few seconds slowly stirring her vagina, then curl your finger up, rubbing her G-spot"
                if the_girl.get_opinion_score("being fingered") > 0:
                    $ the_girl.discover_opinion("being fingered")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered") + mc.sex_skills["Foreplay"])
                the_girl.char "[the_girl.mc_title]! Oh [the_girl.mc_title] that feels so good."
                "She moans and runs her hands through your hair."
                "You lightly suck on her clit as you finger her, caressing her most sensitive places."
            else:
                "You do your best to split your focus between kissing [the_girl.possessive_title]'s pussy and fingering her, but you find yourself struggling to do both."
                "You take a break from licking her and focus pleasing her with your finger for a bit."
                if the_girl.get_opinion_score("being fingered") > 0:
                    $ the_girl.discover_opinion("being fingered")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered"))
                    the_girl.char "Mmmm, I love it when you stick your fingers inside me..."
                else:
                    "[the_girl.possessive_title] enjoys your fingering, but soon you feel her hands running through your hair. She's lightly pulling your head down, trying to get you to resume licking her."
                "You slowly pull your finger out, then focus on pleasing her orally."

        "Push Your Tongue Deep.":
            ##Based on player oral skill. High oral skill gives good arousal return, low skill falters
            "After licking at her clit, you move your tongue down to her entrance. You push your tongue up inside her as far as it will go."
            if mc.sex_skills["Oral"] > 3:
                "You push your tongue deep and twirl it all around her juicy canal. Your nose is pressing up against her clit, making her gasp."
                if the_girl.get_opinion_score("taking control") > 0:
                    "[the_girl.possessive_title] puts her hand on the back of your head, urging your tongue deeper and your nose more firmly against her clit."
                    "She starts to rock her hips, grinding herself against your face."
                    the_girl.char "Mmm, that's it [the_girl.mc_title]! Fuck that feels good!"
                    $ the_girl.discover_opinion("taking control")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("taking control") * 3)
                else:
                    the_girl.char "Oh [the_girl.mc_title]! That feels so good..."
                    $ the_girl.change_arousal(2)

                "[the_girl.possessive_title] moans and trembles as you please her."
            else:
                "You push your tongue deep and twirl it all around insdie her. You poke it around all the soft, slick crevices that it can reach."
                "[the_girl.possessive_title] puts her hand on the back of your head. She starts to pull your head back a bit, guiding you back to her clit."
                the_girl.char "That feels good [the_girl.mc_title], but it feels even better when you kiss me here..."
                "You accept her guidance and begin to lick and suck at her clit again."
        "Finger Her Ass." if (the_girl.get_opinion_score("anal sex") > 0 and the_girl.get_opinion_status("anal sex")):
            "As you continue to lick all around [the_girl.possessive_title]'s cunt, you slowly push a finger up inside of her pussy."
            if the_girl.arousal > 50:
                "It isn't long until your finger is well lubricated from her sopping wet cunt."
            else:
                "It takes a bit, but soon your finger is lubricated by her natural juices."
            "You bring your finger down to her puckered hole and give he a little bit of pressure up against it. She sighs and you can feel her body relax, allowing you to push your finger into her ass."
            the_girl.char "Oh god I love it when you do this..."
            "[the_girl.possessive_title] is running her hands through your hair, her breathing heavy. You push your finger deep into her bowel."
            "You attack her clit with your tongue and lips. She bucks her hips against your face, pulling off your finger a bit. She rocks her hips back down, your finger pushing deep into her again."
            "[the_girl.title]'s hips begin to grind forward and back. With each peak she grinds her clit against your face, and with each trough your finger is fully embedded in her backdoor."
            the_girl.char "Oh!!! [the_girl.mc_title] yes!"
            "You continue for a while. [the_girl.title] clearly enjoys the anal penetration. Eventually you pull your finger out and resume eating her out normally."
            $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex") * 10)
            the_girl.char "Fuck that was intense..."
        "Finger Her Ass.\n{size=22}Must like anal sex{/size} (disabled)" if (the_girl.get_opinion_score("anal sex") <= 0 or not the_girl.get_opinion_status("anal sex")):
            pass


    if mc.arousal > 70:
        "[the_girl.possessive_title]'s constant moans and gasps are incredibly arousing. You can't help but stroke yourself as you eat her out."
        "You should probably fuck her soon before you cum in your pants!"
    elif mc.arousal > 40:
        "[the_girl.possessive_title]'s moaning and heavy breathing are arousing. You give yourself a couple strokes through your clothes while you eat her."
    else:
        "While you aren't being stimulated, [the_girl.possessive_title]'s gasps and breathing are starting to turn you on."
    return

label scene_SB_Oral_Laying_2(the_girl, the_location, the_object, the_round):
    # CHOICE CONCEPT: Submit // Control her
    "[the_girl.possessive_title]'s hips are beginng to rock side to side, grinding against you as you lick her."
    "You feel her legs cross behind your back while she runs her hands through your hair. She starts to grind against you more aggresively."
    "It feels like [the_girl.possessive_title] is trying to take control!"
    menu:
        "Let Her Take Control":
            "You take her enthusiasm as a sign that you must be doing well. You double down on her clit, sucking and licking at it."
            if the_girl.get_opinion_score("taking control") > 0:
                "[the_girl.possessive_title] uses the leverage her legs give her, wrapped around your back, to force your face down into her cunt roughly."
                "She starts to rock her hips, grinding herself against your face."
                the_girl.char "Mmm, that's it [the_girl.mc_title]! Fuck that feels good!"
                $ the_girl.discover_opinion("taking control")
                $ the_girl.change_arousal(the_girl.get_opinion_score("taking control") * 3)
            else:
                "She starts to rock her hips, grinding herself against your face."
                the_girl.char "Oh [the_girl.mc_title]! That feels so good..."
                $ the_girl.change_arousal(2)
            "She grinds against you hard, but your are quickly running out of air. When it gets to be too intense you break her hold on you by pushing yourself up on your hands."
            the_girl.char "Mmmm, sorry [the_girl.mc_title], it feels so good when you lick me like this!"
        "Subdue Her":
            "You grab her hand off the back of your head. You arch your back to take away the leverage her legs give."
            mc.name "If you can't behave yourself, I'll have to spank that naughtiness out of you."
            if the_girl.get_opinion_score("being submissive") > 0:
                the_girl.char "Sorry! But maybe you should spank me... I've been a pretty bad girl lately."
                "You give her pussy a moderate spank."
                mc.name "I wasn't talking about your ass."
                "[the_girl.possessive_title] quivers at your rough touch and words. She pretends she doesn't like it."
                the_girl.char "Sorry sir! It won't happen again, I promise!"
            else:
                the_girl.char "Sorry! It won't happen again!"
            "You don't believe her, but you quickly dive into her pussy again, wary of her trying to take control again."




    if mc.arousal > 70:
        "[the_girl.possessive_title]'s constant moans and gasps are incredibly arousing. You can't help but stroke yourself as you eat her out."
        "You should probably fuck her soon before you cum in your pants!"
    elif mc.arousal > 40:
        "[the_girl.possessive_title]'s moaning and heavy breathing are arousing. You give yourself a couple strokes through your clothes while you eat her."
    else:
        "While you aren't being stimulated, [the_girl.possessive_title]'s gasps and breathing are starting to turn you on."
    return

label outro_SB_Oral_Laying(the_girl, the_location, the_object, the_round):
    if the_girl.arousal > 100:
        "Watching her cum has gotten you more excited than you thought you would be. You're grinding your face into her pussy, rubbing your erection through your pants."
    elif the_girl.arousal > 40:
        "Her soft moans and eager movement make you even more excited. You're grinding your face into her pussy, rubbing your erection through your pants."
    "You get to hear every little gasp and moan from [the_girl.possessive_title] as you lick up and down her cunt. As you stroke yourself you accidentally push yourself past the point of no return."

    "You finally let out a low moan and hold [the_girl.possessive_title] close. A shiver runs up your spine as your climax, shooting your load out into your underwear."
    "It takes a moment for you to recover from your orgasm. Once you're able to you step back and smooth out your shirt, the crotch of your pants uncomfortably wet now."
    return


label transition_default_SB_Oral_Laying(the_girl, the_location, the_object, the_round):
    "You put [the_girl.possessive_title] on her back and lie down on top of her, lining your hard cock up with her tight cunt."
    "After running the tip of your penis along her slit a few times you press forward, sliding inside of her. She gasps softly and closes her eyes."
    return

label strip_SB_Oral_Laying(the_girl, the_clothing, the_location, the_object, the_round):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = SB_Oral_Laying.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side."
    "She sighs happily as you lap at her cunt with your tongue."
    return

label strip_ask_SB_Oral_Laying(the_girl, the_clothing, the_location, the_object, the_round):
    the_girl.char "Sir, I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.possessive_title] pants as you lick her."
    menu:
        "Let her strip.":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = SB_Oral_Laying.position_tag)
            "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side."
            "She sighs happily as you lap at her cunt with your tongue."

        "Leave it on.":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 80:
                the_girl.char "Do you think I look sexy in it?"
                "You speed up, licking her faster in response to her question."
            elif the_girl.sluttiness < 100:
                the_girl.char "Does it make me look like a good little slut? All I want to be is your good little slut sir."
                "She pushes her hips against your face and moans happily."
            else:
                the_girl.char "Does it make me look like the cum hungry slut that I am? That's all I want to be for you sir, your dirty little cum dumpster!"
                "She grinds her hips against your face and moans ecstatically."
    return

label orgasm_SB_Oral_Laying(the_girl, the_location, the_object, the_round):
    "[the_girl.possessive_title] is bucking her hips wildy as you lick her. Suddenly, she grabs the back of your head and gasps."
    $ the_girl.call_dialogue("climax_responses_oral")
    "Her pussy is drooling wet as she climaxes. She paws at the [the_object.name], trying to find something to hold onto."
    "After a few seconds she lets out a long sigh and all the tension drains out of her body. You slow down a bit and lap up her sweet, creamy juices."
    the_girl.char "Oh fuck [the_girl.mc_title], your tongue feels so good."
    return

label transition_SB_Oral_Laying_missionary(the_girl, the_location, the_object, the_round):
    "You push yourself up on your hands, satisfied with the licking you gave her pussy. You slowly start to crawl up [the_girl.possessive_title]'s body."
    "[the_girl.possessive_title] wraps her arms around you and holds you close as you line your cock up with her pussy. She sighs happily into your ear as you slide into her."
    if the_girl.arousal > 100:
        "Her pussy feels amazing, soaked from her orgasm. You kiss her, and she hungrily kisses you back, tasting her cum on your lips."
    else:
        "Her pussy feels great, with an intense heat build from your oral pleasure giving. You kiss her, and she kisses you back, tasting her juices on your lips."

    return

label transition_missionary_SB_Oral_Laying(the_girl, the_location, the_object, the_round):
    "You pull out of her pussy. She begins to protest."
    mc.name "I want to taste you."
    "[the_girl.possessive_title] nods"
    if the_girl.outfit.tits_available():
        "You slowly start to move down her body. You stop on the way down to lick and suck her puffy nipples."
    else:
        "You slowly start to move down her body. You kiss and caress her as you go."
    "[the_girl.possessive_title] opens her legs wide as your get to her cunt. You breath in sharply through your nose, enjoying the tangy, musky scent of her arousal."
    if the_girl.arousal > 50:
        "[the_girl.possessive_title]'s pussy lips are engorged. They glisten with moisture from your previous fucking. You can't wait to taste it."
    else:
        "[the_girl.possessive_title]'s pussy is like a pristine flower. You can't wait to taste it."
    "A moan escapes her lips as you run your tongue up [the_girl.possessive_title]'s slit."
    return
