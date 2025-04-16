import random
from colorama import init, Fore, Style

init(autoreset=True)

stories = [
    {
        "title": "Magical Forest Adventure",
        "prompts": ["name", "magical creature", "place", "object", "adjective"],
        "template": lambda w: f"""
        One day, {w[0]} was walking through the {w[4]} forest when they saw a {w[1]} holding a {w[3]}.
        The creature invited {w[0]} to the {w[2]}, where magical adventures awaited!
        """
    },
    {
        "title": "Space Mission Gone Wrong",
        "prompts": ["astronaut name", "planet", "object", "emotion", "verb"],
        "template": lambda w: f"""
        Captain {w[0]} landed on planet {w[1]} with only a {w[2]}.
        Suddenly, they felt {w[3]} and decided to {w[4]} as aliens approached!
        What will happen next?
        """
    },
    {
        "title": "Crazy School Day",
        "prompts": ["student name", "subject", "teacher name", "object", "adjective"],
        "template": lambda w: f"""
        {w[0]} was having a {w[4]} day at school.
        During {w[1]} class, {w[2]} threw a {w[3]} across the room and started dancing!
        Everyone laughed and joined in.
        """
    },
    {
        "title": "Zombie Apocalypse",
        "prompts": ["name", "weapon", "vehicle", "place", "adjective"],
        "template": lambda w: f"""
        In the middle of the night, {w[0]} grabbed a {w[1]} and jumped into their {w[2]}.
        Zombies were coming fast from the {w[3]}!
        The only hope was to escape through the {w[4]} tunnel.
        Will they survive the apocalypse?
        """
    },
    {
        "title": "The Haunted House",
        "prompts": ["name", "adjective", "object", "sound", "emotion"],
        "template": lambda w: f"""
        {w[0]} entered the {w[1]} old house, holding a {w[2]}.
        Suddenly, there was a loud '{w[3]}' noise.
        Frozen with {w[4]}, they tried to escape before it was too late!
        """
    },
    {
        "title": "The Alien Interview",
        "prompts": ["name", "alien name", "planet", "object", "weird verb"],
        "template": lambda w: f"""
        {w[0]} was invited to an interview with {w[1]} from planet {w[2]}.
        They offered a glowing {w[3]} as a gift.
        Suddenly, they started {w[4]} and vanished into thin air.
        What just happened!?
        """
    }
]

story = random.choice(stories)
print(Fore.CYAN + f"\nWelcome to Mad Libs - {story['title']}!\n")

user_inputs = []
for prompt in story["prompts"]:
    user_input = input(Fore.YELLOW + f"Please enter a {prompt}: ")
    user_inputs.append(user_input)

final_story = story["template"](user_inputs)

print(Fore.GREEN + "\nHere's your crazy story!\n")
print(Fore.MAGENTA + final_story)
