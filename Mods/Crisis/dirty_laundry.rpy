# Dirty Laundy crisis by Starbuck!
# Scene: You go to do your laundry before bed, but notice your sister / mom has clean clothes stacked next to the dryer.
# Player has option to masturbate into clean panties and put them back.
# 50% chance mom or sister catches MC in the act. TODO higher chance at higher sluttiness? 50/50? Have cum soaked panties have some kind of effect on the person?
# Zero sluttiness they get angry, gives chance for obedience check?
# Low sluttiness they watch and touch themselves
# Mid sluttiness they give MC a handjob with the panties in their hand
# high sluttiness they put the panties on and have MC cum in the panties while they wear them

init -1 python:
    dirty_laundry_weight = 4  

init 2 python:
    def dirty_laundry_requirement():
        if mc_asleep():
            if mc_at_home():
                return True
        return False

    dirty_laundry_action = ActionMod("Dirty Laundry", dirty_laundry_requirement, "dirty_laundry_action_label",
        menu_tooltip = "Start your laundry before bed.", category = "Home", is_crisis = True, crisis_weight = dirty_laundry_weight)

label dirty_laundry_action_label:

    $ the_person = get_random_from_list(people_in_mc_home())
    #$ the_panties = get_random_from_list(people_in_mc_home())
    $ the_panties = the_person

    "You are just drifting off to sleep when you suddenly you remember. You don't have any clean clothes for tomorrow!"
    "You look a the clock. It is already pretty late. You guess that your family is already asleep, so you grab your laundry and take it to the laundry room just wearing your boxers."
    "You throw your laundry in the washing machine, add some detergent and start it up."
    "As you are thinking about what to do for the next 30 minutes while the washer runs and you can move your clothes to the dryer, you notice a laundry basket on the floor filled with clean, folded clothes."
    "It looks like they all belong to [the_panties.title]. Sitting on top of the laundy is a pair of sexy black panties."
    "You feel your cock stir when you think about the ass those panties cover. Maybe while you wait for your laundry you could relieve some tension fantasizing about that..."
    menu:
        "Masturbate with panties":
            "You take a quick look out the door to make sure the coast is clear, then close it behind you. You grab the panties and then pull your pants down."
            "You wrap the cloth of the panties around your cock and start to work them up and down. The satin texture feels great."
            "You close your eyes and imagine [the_panties.title]. You imagine her in the morning, pulling up her cum filled panties up and wearing them around all day long."
            if renpy.random.randint(1,2) == 1: #No one catches you
                "Images of [the_panties.title] flood you brain as you continue to jack off. She's bent over now, begging you to cum all over her ass."
                "You go past the point of no return. You wrap the panties around the tip and then fire your load off into them."
                "When you finish, you take a look at them. Your cum is all over [the_panties.title]'s panties."
                "You do your best to fold them back up and put them back at the top of her laundry pile. You wonder if she'll notice."
                "Soon the washer is done. You swap your clothes to the dryer and start it, then head for bed. They should be dry in the morning!"
                #TODO mandatory event the next day when the girl discovers her used panties
            elif the_person == the_panties:                               #the panty owner catches you!
                "Your imagination is running wild and lewd images of [the_person.title] run through your head. Suddenly, you hear the laundry room door open!"
                the_person.char "Holy fuck!"
                $ the_person.draw_person()
                "You are totally busted! You stop what you are doing and open you eyes, seeing [the_person.title] looking at you wide eyed."
                if the_person.sluttiness < 20:
                    $ the_person.draw_person(position = "stand4", emotion= "angry")
                    the_person.char "[the_person.mc_title]! Those are my panties! What the fuck do you think you're doing? "
                    "You try to respond but just stammer. You're pretty sure theres no way to salvage this."
                    the_person.char "God I can't believe you. Don't touch my stuff! This is so gross! I'm gonna have to rewash these!"
                    "She quickly grabs her panties from your hand. She grabs the rest of her laundry and walks out of the laundry room."
                    $ the_person.change_happiness(-10)
                    $ the_person.change_obedience(-10)
                    $ the_person.change_slut_temp(10)
                    "Soon the washer is done. You swap your clothes to the dryer and start it, then head for bed. They should be dry in the morning!"
                elif the_person.sluttiness < 50:
                    $ the_person.draw_person(position = "stand4")
                    the_person.char "Is that... are those MY panties?"
                    "Her eyes are glued on your crotch. She actually doesn't seem mad?"
                    the_person.char "I didn't realize that my panties made you feel that way..."
                    "You decide to take a risk. You look her in the eyes and start to stroke your cock. The movement shocks her out of her staring and you make eye contact."
                    the_person.char "Oh god... can I... can I watch you?"
                    mc.name "Go ahead."
                    "Her eyes go back down to your crotch as you continue to stroke yourself."
                    mc.name "You should do it to. We all need to get off once a while!"
                    "She looks at you, still a bit conflicted."
                    the_person.char "I could... I mean... you aren't going to tell anyone about this are you?"
                    mc.name "Of course not."
                    $ the_person.draw_person(position = "kneeling1")
                    "[the_person.possessive_title] begins to rub her crotch. She gets down on her knees and continues to watch as you stroke yourself."
                    the_person.char "It looks so hard, I bet you are gonna cum so much."
                    "Her hand is moving rapidly between her legs. She is really getting off on this!"
                    the_person.char "You should do it... cum in my panties! I want to watch you hose them down!"
                    "Her encouragement and attention drive you over the edge.  You wrap the panties around the tip and then fire your load off into them."
                    the_person.char "Oh wow! There's so much!"
                    "You glance down and see her rapidly rubbing circles around her pussy."
                    mc.name "Do you want some help getting off?"
                    if the_person.obedience > 130:          #
                        the_person.char "Oh, I mean umm, I couldn't possibly ask you to do something like that..."
                        "You decide to take charge."
                        mc.name "Nonsense. Here, let me help you up."
                        "You put her cum soaked panties back on top of her clean laundry, then pick her up and put her on the edge of the dryer with her ass on the edge."
                        "You gently push her on her back."
                        $ the_person.draw_person (position = "missionary")
                        the_person.char "[the_person.mc_title]? Oh god, what are you going to do to me?"
                        "You put your finger over her lips to silence her."
                        if the_person.outfit.vagina_available():           #If its available no need to strip.
                             "You lower your face down between her legs. With her pussy exposed you waste no time diving right in"
                        else:                                              #Otherwise, strip her down.
                             "You don't bother to reply, instead you begin stripping away anything between you and her delicious pussy"

                             python:
                                    for clothing in the_person.outfit.get_lower_ordered():
                                         the_person.outfit.remove_clothing(clothing)
                                         the_person.draw_person(position = "missionary")
                                         renpy.say("","")

                             "With her pussy finally exposed you waste no time diving right in"
                        "Cupping her ass with your hands, you circle your tongue all around her wet, inviting cunt."
                        the_person.char "Oh [the_person.mc_title], you have no idea how bad I need this."
                        "[the_person.possessive_title] runs her hands your hair. You bury your nose in her mound and flick your tongue in and out of her slick hole"
                        "You circle her clit a few times with your tongue. You suck it into your mouth roughly a couple of times and then release it, you lips making a wet, lewd smacking noise"
                        the_person.char "I am so close... you're gonna make me cum!"
                        $ the_person.draw_person(emotion="orgasm", position ="missionary")
                        "You double your efforts, licking, sucking, and teasing every corner of her pleasing slit"
                        "[the_person.possessive_title] begins to orgasm convulsively, and she cries out."
                        the_person.char "Yes [the_person.mc_title]! Yes! Yes! Oh fuck how do you do that"
                        $ mc.listener_system.fire_event("girl_climax", the_person = the_person, the_position = "missionary")
                        $ the_person.change_happiness(5)
                        $ the_person.change_obedience(5)
                        $ the_person.change_slut_core(2)
                        $ the_person.change_slut_temp(5)
                        $ the_person.change_love(3)
                        "[the_person.possessive_title] runs her hands through your hair one last time. She sits up and gives you a kiss, tasting herself on your tongue."
                        the_person.char "Remember... this is our little secret... okay?"
                        "You hear the sound of the washing machine stopping. You start to open it up and move your laundry over to the dryer."
                        "Each time you move some clothing over, you bend over unneccesarily far so your face is near her cunt again. A couple times you give her a quick lick and she shudders."
                        $ the_person.draw_person()
                        "[the_person.title] slowly gets to her feet, but she is a little unsteady. You start the dryer with all your clothes in it, then grab her clean laundry."
                        mc.name "I'll get this for you."
                        the_person.char "Thanks, just give me a second."
                        "You slowly escort her to her room with her clean laundry, her cum filled panties sitting on the top of the pile. You set the clothes down and say goodnight."
                        "You go back to your room and get to sleep. Your laundry should be dry in the morning!"
                    else:
                        the_person.char "Oh, that's okay [the_person.mc_title]. I'm just gonna grab my laundry and go back to my room for some private time..."
                        mc.name "You should let me help, after all..."
                        "She cuts you off mid-sentence."
                        the_person.char "No, you've done quite enough already! Thanks though!"
                        "She grabs her cum filled panties from your hands, then grabs her laundry and quickly leaves the room."
                        $ renpy.scene("Active")
                        "You wait a few minutes until the washer is done. You move your laundry over to the dryer then walk to your room."
                        "You walk by [the_person.title]'s room as you go. You stop for a second outside her door and can hear soft moans coming from inside. You wonder if she is playing with those panties..."
                        "You go back to your room and get to sleep. Your laundry should be dry in the morning!"
                        $ the_person.change_happiness(3)
                        $ the_person.change_slut_core(2)
                        $ the_person.change_slut_temp(3)
                elif the_person.sluttiness < 75:
                    $ the_person.draw_person(position = "stand4", emotion = "happy")
                    the_person.char "Oh! You're using my panties!"
                    "You stand there for a few seconds, dumbfounded."
                    the_person.char "Well? Go ahead! I don't want to be the one to stop your fun."
                    "It takes a second for your brain to process what she just said. You slowly start to stroke yourself again."
                    "[the_person.possessive_title] watches you intently as you jack yourself off with her panties. It's actually a little distracting..."
                    mc.name "Umm, you know what, maybe this is a bad idea..."
                    the_person.char "What? Don't be silly! Here, why don't you let me help you?"
                    "She walks over to you and puts her arms around your neck."
                    $ the_person.draw_person(position = "kissing")
                    "[the_person.title] starts to kiss you softly on the side of your neck. She nibbles at your ear and then whispers."
                    if the_person == mom:
                        the_person.char "Mommy wants your cum in her panties. I wanna wear them to work tomorrow, knowing your cum is rubbing against me all day long."
                    elif the_person == lily:
                        the_person.char "Your little sister wants your cum in her panties. I wanna wear them when I go to class tomorrow, squirming in my seat through the lecture, knowing your cum is rubbing against me."
                    elif the_person == aunt:        #Wow, congrats on getting her so slutty while shes living with you!
                        the_person.char "Your aunt wants your cum in her panties. When I wear them around tomorrow I'll remember your cum is filling them up."
                    elif the_person == cousin:        #Wow, congrats on getting her so slutty while shes living with you!
                        the_person.char "Go ahead and fill up my panties, you perv. Turns out, I'm as much of a perv as you are. I'm totally wearing these all day tomorrow."
                    else:                           #Someone else someday? A live in girlfriend maybe?
                        the_person.char "I want you to cum in my panties. I'm going to wear them all day tomorrow, knowing you've marked me as yours with your hot cum..."
                    "Wow! The dirty talking really turns you on. You start stroking yourself again."
                    "Soon, you feel a hand on yours. There's another whisper in your ear."
                    the_person.char "Let me... I want to feel you in my hand when you blow your load."
                    "You let go, and feel [the_person.title]'s hand take over. She continues you kiss and nibble on your neck."
                    "The sensations are overwhelming, and soon you are ready to cum. She can sense it and jacks you enthusiastically."
                    the_person.char "Do it! Cum in my panties!"
                    "You moan as your orgasm hits you. You dump spurt after spurt into [the_person.possessive_title]'s panties as she jacks you off with them."
                    $ the_person.draw_person(emotion = "happy")
                    "When you come back to your senses, you look and see [the_person.title]. She is licking a little bit of cum that got on her hand."
                    the_person.char "Mmm... that was hot! I can't wait to wear these tomorrow."
                    $ the_person.change_happiness(5)
                    $ the_person.change_obedience(5)
                    $ the_person.change_slut_temp(5)
                    "She grabs her other laundry and you say goodnight before she leaves you alone in the laundry room, recovering."
                    $ renpy.scene("Active")
                    "You wait a few minutes until the washer is done. You move your laundry over to the dryer then walk to your room."
                    "You go back to your room and get to sleep. Your laundry should be dry in the morning!"
                    #TODO event having her wear the panties the next day
                else:
                    $ the_person.draw_person(position = "stand4", emotion = "happy")
                    the_person.char "Oh! You're using my panties! That looks like fun!"
                    "She walks over to you, then hops on on the side of the dryer with her legs hanging off the end."
                    $ the_person.draw_person(position = "sitting")
                    "She looks at you, expectantly."
                    the_person.char "What are you waiting for? Keep going!"
                    "She continues to watch you. You gives yourself a few tentative strokes."
                    the_person.char "Mmm, I love watching a man get himself off..."
                    "You try to get back into the swing of things, you have a hard time with [the_person.title] in the room. She seems to be oblivious though."
                    the_person.char "I can't wait to wear those panties after you cum in them... I think I'll wear them to bed tonight! Actually... maybe I could wear them before that..."
                    "She looks at you for another second. What is she talking about?"
                    "She suddenly stands up and starts stripping."
                    $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                    while strip_choice is not None:
                        $ the_person.draw_animated_removal(strip_choice)
                        "You watch as [the_person.possessive_title] take off her [strip_choice.name]."
                        $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                    "Once she is naked, [the_person.title] turns to you."
                    the_person.char "Here, let me have those!"
                    "You hand her the panties. She quickly puts them on."
                    #TODO add panties to outfit
                    the_person.char "Mmm, yeah this will be more fun! Don't worry, you can still cum in my panties... but you have to do it while I'm wearing them!"
                    $ the_person.draw_person(position = "standing_doggy")
                    "[the_person.possessive_title] turns around and bends over with her hands on the dryer. She looks back at you."
                    the_person.char "Go ahead! Rub your cock against me..."
                    "You step up behind [the_person.title] and put your hands on her hips. She wiggles her ass back at you. You nestle your cock between her ass cheeks and start to hump against her panties."
                    the_person.char "Mmm... that's it..."
                    "Her ass looks great, barely covered in her satin panties. The combination of the soft cloth with the heat of her body feels great."
                    "You pull back for a second, then reach down and angle your cock down more, then slide it between her thighs. Now as your begin to hump her it is rubbing right up against her panty covered slit."
                    the_person.char "Oh! Yeah I knew this would be fun... keep going that feels so good!"
                    "You grab her ass with both hands and hump her aggressively. You can feel the heat and humidity coming from her cunt as her panties get damp with her excitement."
                    "It feels great, but you can tell you probably won't be able to get off this way."
                    "You stop when you feel [the_person.title]'s hand on your cock. She pulls her panties to the side then slides your cock underneath them."
                    "You give a slow thrust and feel your dick now rubbing directly against her labia."
                    the_person.char "Mmmm... I want you to cum like this, all over the inside of my panties, while I'm wearing them!"
                    "You work your hips against hers for a bit, enjoying the feeling of her wet slit as you rub yourself along the length of it."
                    "The heat and the moisture of it feels great... but your cock is aching to bury itself inside of her!"
                    menu:
                        "'Accidentally' slip it in":
                            "You slowly start to change the angle of your thrusting, and making thrusts a bit shallower. She gets frustrated that you aren't going full forward against her clit and starts to push herself back against you."
                            "One time, when she is about to thrust back, you bend your knees a bit, but angle your hips back up. When she thrusts back your cock slips inside her."
                            "You grab [the_person.title]'s hips and thrust your hips forward, pushing yourself deep inside her. You hold her hips place, enjoying being finally buried in her cunt. She moans loudly at the sudden penetration."
                            mc.name "Whoops! Sorry about that!"
                            "You apologize, but don't let go of her hips. She starts to grind against you."
                            the_person.char "Mmm, that's okay! Just try to pull out when you cum! I still want you to finish in my panties..."
                            "[the_person.possessive_title] is being a good sport, so you decide to try and do that for her. You start to fuck her now, your hips smacking up against her ass."
                            "With all the action you've had up until this point, you feel yourself getting ready to finish."
                            "At the last second, you pull back just enough to pull out of her pussy."
                            "Your first couple of spurts erupt and splash up against her cunt and all long the front of her panties. She moans when she feels the splash."
                            "You pull back completely now and grab your cock. You aim another spurt and one ass check, then for the next one at the other."
                            $ the_person.cum_on_ass()

                        "Finish like this":
                            "You decide to humor [the_person.title]'s wishes and continue the way you are going now."
                            "The heat coming from her sopping wet slit feels amazing, sliding up and down your erection."
                            "With all the action you've had up until this point, you feel yourself getting ready to finish."
                            "Your first couple of spurts erupt and splash up against her cunt and all long the front of her panties. She moans when she feels the splash."
                            "You pull back completely now and grab your cock. You aim another spurt and one ass check, then for the next one at the other."
                            $ the_person.cum_on_ass()
                    $ the_person.draw_person(position="back_peek")
                    "As you step back, [the_person.title] slowly stands up and looks back at you."
                    the_person.char "Wow, that was so hot..."
                    "You see her hand go down her side and she starts to touch herself through her cum soaked panties."
                    the_person.char "I think umm... I'm gonna retire to my room for the night..."
                    menu:
                        "Masturbate for me" if the_person.obedience > 130:
                            mc.name "I mean, its my cum you're using, just get yourself off right here."
                            "She thinks about it for second, then agrees."
                            the_person.char "Okay! Just do me a favor and don't get dressed."
                            $ the_person.draw_person( position = "against_wall")
                            "[the_person.title] sits on the edge of the dryer now and starts to touch herself."
                            "Her hand is making big circles around her clit. You can see some of your cum starting to leak out the sides of her panties."
                            the_person.char "Mmm, your cum feels so good..."
                            "She strokes herself as you watch. She looks you right in the eyes."
                            the_person.char "Oh god, I'm gonna cum!"
                            "Her body quakes and spasms. She is moaning loudly as she continues to stroke herself through her panties."
                            $ the_person.change_happiness(5)
                            mc.name "Damn, that was hot."
                            the_person.char "Ahh, thanks for the help. I really needed that..."
                            "[the_person.title] slowly gets up. She grabs her laundry and says goodnight."
                            $ renpy.scene("Active")
                            "You wait a few minutes until the washer is done. You move your laundry over to the dryer then walk to your room."
                            "You go back to your room and get to sleep. Your laundry should be dry in the morning!"
                        "Say Goodnight":
                            "You say goodnight to [the_person.title]. She slowly walks out of the laundry room. You note that she forgot to take her laundry with her."
                            $ renpy.scene("Active")
                            "You wait a few minutes until the washer is done. You move your laundry over to the dryer then walk to your room."
                            "You go back to your room and get to sleep. Your laundry should be dry in the morning!"
                        "Masturbate for me.\n{size=22}Requires Obedience{/size} (disabled)" if the_person.obedience < 131:
                            pass
                    $ the_person.change_happiness(5)
                    $ the_person.change_obedience(5)
                    $ the_person.change_slut_temp(5)
            else:                                                        #Someone else catches you! for now this is disabled
                pass
                #TODO this
            pass
        "Find something else to do":
            "You decide to do something else. You head back to room and hop on your PC, doing work related tasks until the washer is done."
            "You go back to swap your laundry to the dryer."
            $ the_panties.draw_person()
            "[the_panties.title] is just coming out of the laundry room with her laundry basket."
            #TODO outfit and text based on her sluttiness.
            "You say goodnight to [the_panties.title] and then swap your clothes from the washer to the dryer. They should be dry in the morning!"
            $ renpy.scene("Active")
            return



    $ renpy.scene("Active")
    $ the_person.review_outfit(show_review_message = False)
    return
