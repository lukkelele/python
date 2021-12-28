import time


indent_sensitivity = 2      # Used for the indentation BEFORE string begins
line_size = 100
indent = 4
cheat_types = ["Money", "Pets", "Character", "Weather", "Help"]



def welcome_message(name):
    print(f"\nWelcome {name}, how may I be of service?")
    time.sleep(1.5)



def menu():
    flag = True
    welcome_message("Linnea")
    border(line_size)

    while flag: 
        menu_choice()
        flag = prompt_quit()



def prompt_quit():
        print("\n=================\nQuit?\n1. yes\n2. no")
        answer = input("==> ")
        return (answer != "1")



def menu_choice():

    print("All cheats available:")
    i = 0

    for cheat_type in cheat_types:
        i += 1
        print(f"{i}. {cheat_types[i-1]}")

    choice = int(input("== What cheat do you want?\n--> "))
    while (choice > i) or (choice < 1):
        choice = int(input(f"== Enter a number between 1 and {i}..\n--> "))
    
    if choice == 1:
        money()
    elif choice == 2:
        pets()
    elif choice == 3:
        sim_character()
    elif choice == 4:
        weather()
    elif choice == 5:
        help()


def chosen_alternative(user_choice):
    switcher = {
            1: money(),
            
            3: sim_character(),

            5: help(),
            }
    return switcher.get(user_choice, 5)




def money():
    print("== $ $ $ $ $ $ $ $ $ $ $ $ $ $ ")
    time.sleep(1)
    user_input = int(input(f"== How much money do you want?\n--> (k) "))
    border(line_size)
    time.sleep(1)
    if user_input > 0:
        print(f"COPY THIS LINE ====> sims.modify_funds+{user_input}000")
    else:
        print(f"COPY THIS LINE ====> sims.modify_funds{user_input}000")
    border(line_size)
    print("")
    time.sleep(1)
    print("== Other commands:")
    print("== rosebud --> +1000 Simoleons\n== motherlode --> +50K Simoleons\n== money [AMOUNT] --> Sets the money to this absolute value")
    print("== FreeRealEstate On / Off --> All lots in the world view are free")
    border(line_size)
    time.sleep(1)


def pets():
    border(line_size)
    print("""stats.set_skill_level skill_dog [#]: maxes out your pet training skill (five is the maximum)
stats.set_skill_level major_vet [#]: maxes out your vet skill (ten is the maximum)""")
    print("traits.equip_trait attraction: The animal affection perk makes relationships with pets begin at a higher level than usual")


def object_state():
    print("Not implemented..")


def help():
    print("\n== Help")
    print("To open the console in-game, press the following combination:\n\n==> SHIFT + CTRL + C\n\n== Enter \"testingcheats true\" or \"testingcheats on\" to activate cheats.\n\n")



def career():
    print("Not implemented..")




def weather():
    time.sleep(1.5)
    border(line_size)
    time.sleep(1.0)
    print("""
seasons.set_season [#]: 0 = summer, 1 = fall, 2 = winter, 3 = spring
weather.start_weather_event weather_cloudy_cool: set the weather to cloudy and cool
weather.start_weather_event weather_cloudy_warm: set the weather to cloudy and warm
weather.start_weather_event weather_heatwave: cause a heatwave (set weather to dangerously hot)
weather.start_weather_event weather_rain_heavy_warm: set the weather to heavy rain while warm
weather.start_weather_event weather_rain_light_cool: set the weather to light rain while cool
weather.start_weather_event weather_rain_storm_cold: cause a thunderstorm
weather.start_weather_event weather_snow_heavy_freezing: set the weather to heavy snow and freezing
            """)
    time.sleep(1.5)
    border(line_size)
    time.sleep(0.5)
    print("""
weather.start_weather_event weather_snow_light_freezing: set the weather to light snow while freezing
weather.start_weather_event weather_snow_thundersnow: cause a thunderstorm while it snows
weather.start_weather_event weather_sunny_burning: set the weather to sunny and dangerously hot
weather.start_weather_event weather_sunny_cool: set the weather to sunny and cool
weather.start_weather_event weather_sunny_freezing: set the weather to sunny and freezing
weather.start_weather_event weather_sunny_warm: set the weather to sunny and warm
weather.start_weather_event weather_sunshower_hot – set the weather to rain while hot
            """)



def sim_character():
    print("""
    cheat need > disable need decay: stops your Sims needing… anything – can be reversed by swapping ‘disable’ or ‘enable’
    cheat need > make happy: fulfills all needs and makes Sim happy
    make dirty: dirties an object, not sure why you’d want to
    make clean: makes objects clean, to save your Sim from household chores
    add to family: want to add a random citizen to your family? This is the Sims 4 cheat for you
    cas.fulleditmode: this lets you edit any Sim in Create-A-Sim mode
    Shift + Click anywhere on the ground: this will give you the option to instantly teleport your Sim, which means no more waiting for your character to able their way to the car pool
""")
    time.sleep(1.5)
    border(line_size)
    time.sleep(0.5)
    print("""PREGNANCY AND GHOSTS\n=====================================================================\n
    sims.add_buff buff_pregnancy_inlabor: make a Sim or ghost pregnant and in labor
    sims.add_buff buff_pregnancy_trimester1: make a Sim or ghost pregnant and in their first trimester – you can cycle between the trimesters by choosing between 1,2, or 3
    pregnancy.force_offspring_count [simID] [count]: change the count to reflect how many kids you want to have all at once
    death.toggle true: save a Sim from death forever, reverse by switching ‘true’ to ‘false’
    sims.add_buff buff_death_electrocution_warning: cause death while using an electric item
    sims.add_buff buff_death_elderexhaustion_warning: cause death after exercising
    sims.add_buff buff_mortified: cause death by embarrassment
    sims.add_buff buff_motives_hunger_starving: you guessed it, death by malnutrition
    sims.add_buff Ghostly: temporarily turn your Sim into a ghost
""")
    time.sleep(1.5)
    border(line_size)
    time.sleep(0.5)
    print("== FAMOUS CHEATS")
    print(""" 
    stats.set_skill_level Major_Acting [#]: set your acting skill level (ten is the maximum)
    stats.set_skill_level Minor_Media [#]: set your media production skill level (five is the maximum)
    famepoints [#]: give your Sim some fame points

Through hard work and dedication, your Sim can earn special traits to make them unflappable… or you use these cheats to create a superstar.

    traits.equip_trait UnstoppableFame: the unstoppable fame trait stops your Sim from ever having their fame decay. Your Sim will also never react poorly to paparazzi
    traits.equip_trait WorldRenownedActor: the world renowned actor trait stops your Sim from ever failing an acting action

If you’re worried about your Sim not having enough time to make their way through the acting world, use these promotion cheats to give them a helping hand.

    careers.promote Actor: your Sim gains an instant promotion in their acting career
    careers.promote DramaClub: your Sim gains an instant promotion in their Drama Club career
            """)

    time.sleep(1.5)
    border(line_size)
    time.sleep(0.5)
    print("== COTTAGE LIVING")
    print("""==> With enabling testingcheats to true, you can access the following cheats by SHIFT-CLICKING livestock to bring up a menu. 
    Unlock all animal homes
    Cheat relationship
    Get all animal clothes
    Buy animal clothing
    Create wool inventory
    Create all feed recipes
    Cheat outcomes
    \n========    
    stats.setgskillglevel SkillgCrossStitch 5: sets your cross stitch skill to maximum (five)
    traits.equip_trait trait_LactoseIntolerant: gives your sim the Lactose Intolerant trait
    traits.equip_trait trait_AnimalEnthusiast: gives your sim the Animal Enthusiast trait
    traits.equip_trait trait_Nature_Country: gives your sim the Nature Conversationalist trait

            """)



def border(length=0):
    if length == 0:
        length = 30
    border = "=" * (length + indent_sensitivity) 
    print(border)


