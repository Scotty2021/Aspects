label SB_tutorial_event():

    $ other_people = [person for person in mc.location.people]
    $ the_person = get_random_from_list(other_people)

    $ the_person.draw_person()
    show screen person_info_ui(the_person)

    the_person.char "Oh, hey [mc.name]!"
    mc.name "Hello, [the_person.name]. How are you doing today."
    "[the_person.name] smiles and bats her eyelashes a few times."
    the_person.char "Well, to be honest, its much better now that you are here!"
    menu:
        "Looking good girl!":
            the_person.char "Aww, thanks! You're looking pretty sexy yourself..."
            "[the_person.name] looks your up and down a few times. Her eyes tend to linger on your crotch each time they pass."
            $ the_person.change_slut_temp(5)
            "You flirt back and forth with [the_person.name], but soon it is time to part ways."
            the_person.char "It was great seeing you! Take care [mc.name]!"
        "Thank you.":
            "You make some small talk with [the_person.name]. You catch up on a few various things, but soon it is time to part ways."
            the_person.char "It was great seeing you! Take care [mc.name]!"
            $ the_person.change_happiness(5)

    return

init 2 python:
    def SB_tutorial_event_requirement():
        if mc.location == mall:
            if (len(mc.location.people) > 0):
                return True
        return False

    SB_tutorial_crisis = Action("Mall Flirt Crisis", SB_tutorial_event_requirement, "SB_tutorial_event")
    crisis_list.append([SB_tutorial_crisis,5])
