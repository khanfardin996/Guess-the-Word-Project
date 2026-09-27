import random

easy_words = [
    "Cricket","Football","Pizza","Skateboard","Basketball",
    "Video game","Minecraft","YouTube","Headphones","Cycle",
    "Superhero","Robot","Guitar","Dragon","Ice cream",
    "Chocolate","Butterfly","Elephant","Rainbow","Snowman",
    "Camera","Sunglasses","Watermelon","Kite","Balloon",
    "Penguin","Panda","Popcorn","Sandwich","Burger"
    ]

medium_words =  [
    "Telescope","Volcano","Passport","Ambulance","Tournament",
    "Headphones","Skateboard","Helicopter","Dictionary","Umbrella",
    "Backpack","Aquarium","Fireworks","Microphone","Robot",
    "Microscope","Satellite","Parachute","Tornado","Glacier",
    "Pendulum","Hourglass","Kaleidoscope","Chameleon","Submarine",
    "Lighthouse","Windmill","Waterfall","Trampoline","Escalator"
     ]

hard_words = [
    "Compass","Pyramid","Magnet","Fossil","Rocket",
    "Castle","Dolphin","Thunder","Lantern","Mirror",
    "Island","Jungle","Pirate","Treasure","Skeleton",
    "Tsunami","Earthquake","Meteor","Galaxy","Labyrinth",
    "Avalanche","Constellation","Eclipse","Gravity","Horizon",
    "Illusion","Turbulence","Pharaoh","Gladiator","Samurai"
     ]

hints = {
      #From here the Hint for Easy words are made

    "Cricket": "A sport played by 11 players with a bat and ball.",
    "Football": "A sport played by 22 people on a field with a goal.",
    "Pizza": "A round Italian food with cheese and toppings.",
    "Skateboard": "A board with wheels used to ride and do tricks.",
    "Basketball": "A sport where you throw a ball into a hoop.",
    "Video game": "Something you play on a console or computer.",
    "Minecraft": "A blocky sandbox game where you build and survive.",
    "YouTube": "A website where people watch and upload videos.",
    "Headphones": "You wear these on your ears to listen to music.",
    "Cycle": "A two-wheeled vehicle you pedal.",
    "Superhero": "A fictional character with special powers who saves people.",
    "Robot": "A machine that can do tasks automatically.",
    "Guitar": "A musical instrument with strings you strum.",
    "Dragon": "A mythological being who can fly and breathe out fire.",
    "Ice cream": "A cold sweet dessert you lick from a cone or cup.",
    "Chocolate": "A sweet brown treat made from cocoa.",
    "Butterfly": "A colorful insect with big wings that flies around flowers.",
    "Elephant": "A huge gray animal with a long trunk and big ears.",
    "Rainbow": "Colorful arcs in the sky that appear after rain.",
    "Snowman": "A figure made of snow with a carrot nose.",
    "Camera": "A device you use to take photos.",
    "Sunglasses": "Dark glasses you wear to protect your eyes from the sun.",
    "Watermelon": "A big green fruit that is red inside with black seeds.",
    "Kite": "A light frame with paper that flies in the wind on a string.",
    "Balloon": "A rubber bag filled with air that floats.",
    "Penguin": "A black and white bird that lives in cold places and swims.",
    "Panda": "A black and white bear that eats bamboo.",
    "Popcorn": "A snack made from corn that pops when heated.",
    "Sandwich": "Food made with bread and fillings in between.",
    "Burger": "A round bun with a patty and veggies inside.",

    #From here the Hint for Medium words are made

    "Telescope": "An instrument used to see faraway stars and planets.",
    "Volcano": "A mountain that can erupt with lava and ash.",
    "Passport": "A document you need to travel to another country.",
    "Ambulance": "A vehicle that takes sick people to the hospital.",
    "Tournament": "A competition where many players or teams play.",
    "Helicopter": "An aircraft with spinning blades that can hover.",
    "Dictionary": "A book that lists words and their meanings.",
    "Umbrella": "You use this to stay dry in the rain.",
    "Backpack": "A bag you carry on your back.",
    "Aquarium": "A place or tank where fish are kept.",
    "Fireworks": "Colorful explosions in the sky on special nights.",
    "Microphone": "A device you speak into to make your voice louder.",
    "Microscope": "An instrument used to see very tiny things.",
    "Satellite": "A machine sent into space to orbit the Earth.",
    "Parachute": "A cloth canopy that slows your fall from the sky.",
    "Tornado": "A spinning funnel of wind that touches the ground.",
    "Glacier": "A huge slow-moving mass of ice.",
    "Pendulum": "A weight that swings back and forth on a string.",
    "Hourglass": "A glass device with sand that measures time.",
    "Kaleidoscope": "A tube you look through to see colorful patterns.",
    "Chameleon": "A lizard that changes color to blend in.",
    "Submarine": "A boat that travels underwater.",
    "Lighthouse": "A tall tower with a light that guides ships.",
    "Windmill": "A structure with blades turned by the wind.",
    "Waterfall": "Water that flows over a cliff and falls down.",
    "Trampoline": "A stretched fabric you jump on and bounce high.",
    "Escalator": "Moving stairs that carry you up or down.",
    "Catapult": "An ancient machine that throws heavy objects.",
    "Chandelier": "A hanging light fixture with many bulbs or candles.",
    "Barometer": "An instrument that measures air pressure.",

    #From here the Hint for Hard words are made
    "Compass": "A tool that always points north.",
    "Pyramid": "A huge triangular stone structure in Egypt.",
    "Magnet": "An object that attracts iron and steel.",
    "Fossil": "The preserved remains of an ancient animal or plant.",
    "Rocket": "A vehicle that flies into space.",
    "Castle": "A large stone building where kings and queens lived.",
    "Dolphin": "A smart sea animal that jumps and clicks.",
    "Thunder": "The loud sound you hear after lightning.",
    "Lantern": "A portable light you carry in your hand.",
    "Mirror": "You look into this to see your own face.",
    "Island": "A piece of land surrounded by water.",
    "Jungle": "A thick forest with wild animals and tall trees.",
    "Pirate": "A sea robber who sails on a ship looking for treasure.",
    "Treasure": "Hidden gold, jewels, or valuable items.",
    "Skeleton": "The bones that make up a body.",
    "Tsunami": "A giant ocean wave caused by an underwater quake.",
    "Earthquake": "A sudden shaking of the ground.",
    "Meteor": "A space rock that burns bright in the sky.",
    "Galaxy": "A huge system of stars and planets.",
    "Labyrinth": "A maze with many paths where you can get lost.",
    "Avalanche": "A large mass of snow sliding down a mountain.",
    "Constellation": "A group of stars forming a pattern in the sky.",
    "Eclipse": "When one heavenly body blocks the light of another.",
    "Gravity": "The force that pulls things toward the Earth.",
    "Horizon": "The line where the sky seems to meet the ground.",
    "Illusion": "Something that tricks your eyes or mind.",
    "Turbulence": "Rough shaking of air during a flight.",
    "Pharaoh": "An ancient Egyptian king.",
    "Gladiator": "A fighter who battled in ancient Roman arenas.",
    "Samurai": "A warrior of ancient Japan who carried a sword.",
}

print("Welcome to the Word Guessing Game")
print("Please choose the difficulty level: Easy, Medium or Hard")

level = input("Enter difficulty: ").lower().strip()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid input. You are forwarded to EASY level.")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the word :-")
print("Hint:", hints[secret])   # show the HINT in the starting

while True:
    guess = input("Enter your guess: ").strip().capitalize()
    if not guess:
        print("Please enter a word.")
        continue

    attempts += 1

    if guess == secret:
        print(f"CONGO! You guessed '{secret}' in {attempts} attempts.")
        break

    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Letter Hint:", hint)
    print("Description Hint:", hints[secret])

print("GAME OVER")