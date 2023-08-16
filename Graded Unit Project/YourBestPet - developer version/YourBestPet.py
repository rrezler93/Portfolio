# Author: Radoslaw Rezler
# Date: 2023-04-19
# Description:  Program that asks users to choose a dog, a cat or a pet in general and then asks some questions.
#               Then it gives them a list of the best fits based on their answers.
#               Program also has an animal facts page and a page with a list of all the breeds.


# **********************************************************************************************************************
# Import modules:


from tkinter import *  # For GUI
from PIL import ImageTk, Image  # For images


# **********************************************************************************************************************
# Defining the classes and assigning attributes to them:


# Define the class for the animals
class Animal:
    def __init__(self, name, size, activity, cost, children, info, pic):
        self.name = name
        self.size = size
        self.activity = activity
        self.cost = cost
        self.children = children
        self.info = info
        self.pic = pic
        # Temporary stats based on user answers
        self.fit_reasons = []
        self.not_fit_reasons = []
        self.score = 0


# Make subclass called Dog
class Dog(Animal):
    # Define the general description of the dogs
    general_description = f"Dogs are incredible creatures that have been our loyal companions for " \
                          f"thousands of years. They are affectionate, playful, and always eager to " \
                          f"please their owners. " \
                          f"\n\nOwning a dog can be an incredibly rewarding " \
                          f"experience, but it is important to understand the responsibilities that " \
                          f"come with it. One of the most significant benefits of owning a dog is " \
                          f"the companionship they provide. " \
                          f"\n\nThey are known for their loyalty and " \
                          f"their ability to form strong bonds with their owners. A dog can be your " \
                          f"best friend, and their presence can bring immense joy and comfort to " \
                          f"your life. " \
                          f"\n\nThey have a remarkable ability to sense our emotions, " \
                          f"and they are always there to offer a wag of the tail or a comforting " \
                          f"lick when we need it the most. " \
                          f"\n\nIn addition to the emotional benefits, " \
                          f"owning a dog can also have numerous health benefits. Taking your dog for " \
                          f"a walk or playing with them can help you stay active and improve your " \
                          f"physical health. Studies have shown that pet owners have lower blood " \
                          f"pressure, reduced risk of heart disease, and decreased levels of stress " \
                          f"and anxiety. " \
                          f"\n\nChoosing the right breed of dog is also an important " \
                          f"consideration. There are hundreds of different breeds, each with their " \
                          f"unique characteristics, energy levels, and personalities. From small lap " \
                          f"dogs to large working breeds, there is a perfect dog for every lifestyle " \
                          f"and personality. " \
                          f"\n\nHowever, it is essential to remember that owning a dog " \
                          f"also comes with responsibilities. They require proper care, training, " \
                          f"and attention. It is important to provide them with regular exercise, " \
                          f"a healthy diet, and veterinary care. Training your dog is also essential " \
                          f"to ensure they behave appropriately in different situations and to " \
                          f"strengthen your bond with them." \
                          f"\n\nIn conclusion, owning a dog can be one " \
                          f"of the most rewarding experiences of your life. They offer love, " \
                          f"companionship, and endless joy, but it is crucial to approach pet " \
                          f"ownership with care and responsibility. With the right commitment and " \
                          f"dedication, owning a dog can be a life-changing experience that will " \
                          f"enrich your life in countless ways."


# Make subclass called Cat
class Cat(Animal):
    # Define the general description of the cats
    general_description = f"Cats are fascinating creatures that have been domesticated for thousands "\
                          f"of years. They are curious, independent, and make wonderful companions "\
                          f"for those who appreciate their unique personalities. "\
                          f"\n\nOwning a cat can be a deeply satisfying experience, but it's "\
                          f"important to understand "\
                          f"that they have their own individual needs and behaviors. One of the "\
                          f"biggest benefits of owning a cat is their ability to offer affection on "\
                          f"their own terms. "\
                          f"\n\nUnlike dogs, cats are more selective in their "\
                          f"attention, but when they do choose to cuddle up or rub against their "\
                          f"owners, it can be a deeply rewarding experience. They are often highly "\
                          f"intuitive, able to sense when their owners are upset or anxious, "\
                          f"and will offer quiet companionship when it is most needed. "\
                          f"\n\nCats also "\
                          f"have unique physical traits that make them excellent companions. They "\
                          f"are fastidious creatures who groom themselves regularly and rarely need "\
                          f"bathing. They are also often less demanding than dogs when it comes to "\
                          f"exercise and are generally content to lounge around the house. "\
                          f"\n\nHowever, it's important to remember that owning a cat is not without "\
                          f"its responsibilities. They require regular veterinary care, "\
                          f"a healthy diet, and daily attention to ensure their well-being. Training "\
                          f"is also essential to prevent destructive behaviors such as scratching "\
                          f"furniture or not using the litter box. "\
                          f"\n\nWhen it comes to choosing the "\
                          f"right breed of cat, there are many different options, each with their "\
                          f"own unique characteristics and needs. From the regal Siamese to the "\
                          f"laid-back Maine Coon, there is a perfect cat for every lifestyle and "\
                          f"personality. "\
                          f"\n\nIn conclusion, owning a cat can be a wonderful "\
                          f"experience that brings joy and companionship into our lives. With the "\
                          f"right care, attention, and understanding of their individual needs, "\
                          f"cats can be deeply satisfying and rewarding companions for years to come."


# Make subclass called Rabbit
class Rabbit(Animal):
    # Define the general description of the rabbits
    general_description = f"Rabbits are delightful creatures that have been domesticated for "\
                          f"centuries. They are known for their adorable appearance, gentle nature, "\
                          f"and affectionate personalities. "\
                          f"\n\nOwning a rabbit can be a wonderful "\
                          f"experience, but it is important to understand the responsibilities that "\
                          f"come with it. One of the most significant benefits of owning a rabbit is "\
                          f"the companionship they provide. They are social animals that crave "\
                          f"attention and love to interact with their owners. "\
                          f"\n\nRabbits are also "\
                          f"incredibly intelligent and can be trained to do a variety of tricks and "\
                          f"behaviors. They are curious creatures that love to explore and play, "\
                          f"which can provide endless entertainment for both you and your furry "\
                          f"friend. "\
                          f"\n\nIn addition to their emotional benefits, rabbits can also "\
                          f"have a positive impact on your physical health. They are low maintenance "\
                          f"pets that do not require daily walks, making them an ideal choice for "\
                          f"individuals with limited mobility or living in smaller spaces. However, "\
                          f"it is still important to provide them with proper exercise and a healthy "\
                          f"diet to keep them happy and healthy. "\
                          f"\n\nWhen choosing a breed of "\
                          f"rabbit, it is important to consider their unique characteristics and "\
                          f"needs. There are over 60 different breeds of rabbits, each with their "\
                          f"own personalities and physical traits. Some breeds are better suited for "\
                          f"families with children, while others are more independent and require "\
                          f"less attention. "\
                          f"\n\nHowever, owning a rabbit also comes with "\
                          f"responsibilities. They require proper care, including regular grooming, "\
                          f"feeding, and veterinary checkups. It is important to provide them with a "\
                          f"safe and comfortable living environment that includes plenty of space to "\
                          f"move around and play. "\
                          f"\n\nIn conclusion, owning a rabbit can be a "\
                          f"rewarding and enriching experience that brings joy and companionship "\
                          f"into your life. With the right care and attention, your furry friend can "\
                          f"become a beloved member of your family for years to come."


# Make subclass called Rat
class Rat(Animal):
    # Define the general description of the rats
    general_description = f"Rats are often misunderstood creatures, but they can make excellent pets "\
                          f"for the right person. They are intelligent, social, and highly trainable "\
                          f"animals that have been domesticated for over 100 years."\
                          f"\n\nOwning a pet "\
                          f"rat can be a very rewarding experience. They are incredibly social "\
                          f"animals and love to interact with their owners. They are known for their "\
                          f"intelligence and have been trained to do many different things, "\
                          f"such as come when called, use a litter box, and even perform tricks. "\
                          f""\
                          f"\n\nOne of the benefits of owning a pet rat is that they are relatively "\
                          f"easy to care for. They require a clean living environment, "\
                          f"a healthy diet, and regular exercise. They also do not require a lot of "\
                          f"space and can be kept in cages that fit comfortably in most homes. "\
                          f"\n\nAnother advantage of owning a pet rat is that they are relatively "\
                          f"low maintenance. They do not require grooming like dogs or cats, "\
                          f"and they are not as demanding in terms of attention. However, "\
                          f"they still require daily interaction with their owners to stay happy and "\
                          f"healthy. "\
                          f"\n\nIt is important to note that pet rats are not for everyone. "\
                          f"They have a lifespan of about 2-3 years and require a significant time "\
                          f"commitment during their lifespan. They also have a tendency to chew on "\
                          f"things, so it is important to rat-proof your home if you decide to get "\
                          f"one. "\
                          f"\n\nIn conclusion, owning a pet rat can be a highly rewarding "\
                          f"experience for those who are willing to put in the time and effort to "\
                          f"care for them properly. They are intelligent, social, and highly "\
                          f"trainable animals that make excellent companions for the right person. "\
                          f"If you are considering getting a pet rat, make sure to do your research "\
                          f"and be prepared to provide them with a happy and healthy home."


# Make subclass called Fish
class Fish(Animal):
    def __init__(self, name, size, activity, cost, children, info, pic):
        super().__init__(name, size, activity, cost, children, info, pic)

    # Define the general description of the fish
    general_description = f"Keeping fish as pets in an aquarium is a fascinating and rewarding hobby that has become " \
                          f"increasingly popular in recent years. " \
                          f"\n\nThere are many different types of fish that are " \
                          f"suitable for living in a tank, and each has its own unique characteristics and " \
                          f"requirements. " \
                          f"\n\nOne of the most significant benefits of keeping fish in an aquarium is the " \
                          f"sense of tranquility and relaxation that they can bring to your home. Watching fish swim " \
                          f"in their peaceful underwater world can be a calming and therapeutic experience, " \
                          f"and many people find it to be an excellent way to de-stress and unwind after a busy day. " \
                          f"\n\nAnother advantage of keeping fish is the beauty they can " \
                          f"bring to your home. With their bright colors, unique patterns, and graceful movements, " \
                          f"fish can add a touch of elegance and sophistication to any room. " \
                          f"\n\nThere are many types of fish that are prized for their " \
                          f"striking appearance, such as the vibrant neon tetra or the flowing fins of a Siamese " \
                          f"fighting fish. When setting up an aquarium, it is essential to create an environment that "\
                          f"is both comfortable and safe for your fish. This involves providing the appropriate " \
                          f"filtration and lighting, as well as ensuring that the water temperature, pH level, " \
                          f"and other chemical factors are within the appropriate range for the species of fish you " \
                          f"have. " \
                          f"\n\nIt is also important to choose the right type of fish for your tank, taking into " \
                          f"consideration factors such as their adult size, compatibility with other species, " \
                          f"and behavior. Some fish are more aggressive or territorial than others, and certain " \
                          f"species may require specific diets or special care. Maintaining a healthy and thriving " \
                          f"aquarium requires ongoing attention and care, including regular water changes, " \
                          f"filter maintenance, and monitoring of water chemistry. " \
                          f"\n\nHowever, with the right knowledge " \
                          f"and commitment, keeping fish in an aquarium can be a deeply satisfying and rewarding " \
                          f"experience that can provide you with many years of joy and entertainment. "


# **********************************************************************************************************************
# Assigning objects to the classes and giving them attributes:

# Make a list of Dogs and give them attributes
dogs = [Dog('German Shepherd', 3, 3, 3, True,
            "This breed is known for its loyalty, intelligence and train ability, making them great police and "
            "military dogs. They require plenty of exercise and mental stimulation. An interesting fact is that "
            "German Shepherds were originally bred to herd sheep.\n", "Dogs/German_Shepherd.jpg"),
        Dog('Maltese', 1, 1, 1, False,
            "These dogs are known for their small size and gentle nature. They are great lap dogs and are very "
            "affectionate with their owners. They do require regular grooming to keep their long, white coat looking "
            "its best. An interesting fact is that Maltese dogs were popular with women in ancient Greece and Rome \n"
            "and were often depicted in art.\n", "Dogs/Maltese.jpg"),
        Dog('French Bulldog', 2, 2, 3, True,
            "This breed is characterized by its unique appearance, with a short, stocky body and large, "
            "bat-like ears. They are affectionate and playful but can be stubborn when it comes to training. French "
            "Bulldogs are prone to breathing problems due to their short snouts. An interesting fact is that French "
            "Bulldogs were originally bred in England as miniature Bulldogs.\n", "Dogs/French_Bulldog.jpg"),
        Dog('Miniature Schnauzer', 1, 2, 2, True,
            "These dogs are known for their alertness and intelligence. They are affectionate with their owners and "
            "do well in families with children. They do require regular grooming to maintain their distinctive, "
            "wiry coat. An interesting fact is that Miniature Schnauzers were originally bred in Germany to catch "
            "rats and guard homes.\n", "Dogs/Miniature_Schnauzer.jpg"),
        Dog('American Pit Bull Terrier', 3, 3, 2, True,
            "This breed is often misunderstood due to its reputation for aggression, but when raised and trained "
            "properly, they can make loyal and affectionate family pets. They are highly energetic and require plenty "
            "of exercise. An interesting fact is that Pit Bulls were originally bred for bull-baiting and "
            "bear-baiting, but their breed was later refined to be a loyal companion dog.\n",
            "Dogs/American_Pit_Bull_Terrier.jpg"),
        Dog('Labrador Retriever', 3, 3, 3, True,
            "This breed is known for its friendly and outgoing nature. They are intelligent and easy to train, "
            "which makes them popular as guide dogs and search and rescue dogs. They require plenty of exercise and "
            "love to swim. An interesting fact is that Labrador Retrievers were originally bred in Newfoundland to "
            "retrieve fish for fishermen.\n", "Dogs/Labrador_Retriever.jpg"),
        Dog('Chihuahua', 1, 1, 1, False,
            "These dogs are known for their small size and big personalities. They can be very loyal and affectionate "
            "with their owners but may be nervous around strangers. They do not require a lot of exercise but may "
            "need a sweater in cold weather due to their small size. An interesting fact is that Chihuahuas are "
            "believed to have originated in Mexico and were named after the state of Chihuahua.\n",
            "Dogs/Chihuahua.jpg"),
        Dog('Saint Bernard', 3, 1, 3, True,
            "This breed is known for its size and strength. They are gentle giants and make great family pets. They "
            "do require plenty of exercise and space due to their large size. An interesting fact is that Saint "
            "Bernards were originally bred in Switzerland to rescue lost and injured travelers in the Alps.\n",
            "Dogs/Saint_Bernard.jpg"),
        Dog('Shih Tzu', 1, 1, 1, False,
            "These dogs are known for their long, flowing coat and affectionate nature. They make great lap dogs and "
            "are good with children. They do require regular grooming to maintain their coat. An interesting fact is "
            "that Shih Tzus were originally bred in China and were considered a sacred breed.\n", "Dogs/Shih_Tzu.jpg"),
        Dog('Beagle', 2, 2, 2, True,
            "This breed is known for its excellent sense of smell, which makes them popular as hunting dogs. They are "
            "friendly and outgoing, making them great family pets. They require plenty of exercise and can be prone "
            "to obesity if not properly exercised. An interesting fact is that Beagles were originally bred in \n"
            "England to hunt rabbits.\n", "Dogs/Beagle.jpg"),
        Dog('Siberian Husky', 3, 3, 3, True,
            "These dogs are known for their endurance and their ability to thrive in cold weather. They are "
            "intelligent and independent, which can make them difficult to train. They require plenty of exercise and "
            "love to run, so they are a great fit for active owners. An interesting fact is that Siberian Huskies "
            "were originally bred in Siberia by the Chukchi people to pull sleds across long distances.\n",
            "Dogs/Siberian_Husky.jpg"),
        Dog('Boxer', 3, 3, 3, True,
            "This breed is known for its athleticism and playfulness. They are loyal and protective of their families "
            "and do well with children. They require plenty of exercise and mental stimulation. An interesting fact "
            "is that Boxers were originally bred in Germany to be hunting dogs, but they later became popular as "
            "guard dogs and family pets.\n", "Dogs/Boxer.jpg"),
        Dog('Poodle', 2, 1, 3, False,
            "This breed is known for its distinctive coat and intelligence. They come in three sizes (toy, miniature, "
            "and standard) and are popular as show dogs. They require regular grooming to maintain their coat. "
            "Poodles are highly trainable and make great companions. An interesting fact is that Poodles were "
            "originally bred in Germany to be water retrievers.\n", "Dogs/Poodle.jpg"),
        Dog('Border Collie', 2, 3, 2, True,
            "This breed is known for its intelligence and herding ability. They are highly trainable and excel at "
            "activities like agility and obedience. They require plenty of exercise and mental stimulation. Border "
            "Collies do well with active owners who can provide them with a job to do. An interesting fact is that "
            "Border Collies were originally bred in Scotland and England to work on farms herding sheep.\n",
            "Dogs/Border_Collie.jpg"),
        Dog('Bull Terrier', 2, 3, 2, True,
            "This breed is known for its distinctive egg-shaped head and muscular body. They are loyal and protective "
            "of their families and do well with children. They require plenty of exercise and mental stimulation.n"
            "Bull Terriers are highly trainable and excel at activities like obedience and agility. An interesting "
            "fact is that Bull Terriers were originally bred in England for blood sports like bull-baiting and "
            "dog-fighting, but their breed was later refined to be a loyal companion dog.\n", "Dogs/Bull_Terrier.jpg")]

# Make a list of Cats and give them attributes
cats = [Cat('Siamese', 2, 3, 3, True,
            "This breed is known for its distinctive blue eyes and vocal nature. They are highly intelligent and can "
            "be very playful. They require plenty of exercise and mental stimulation. An interesting fact is that "
            "Siamese cats were originally bred in Thailand to be companions for Buddhist monks.\n", "Cats/Siamese.jpg"),
        Cat('Persian', 2, 1, 3, True,
            "This breed is known for its long, luxurious coat and laid-back personality. They are affectionate and do "
            "well in quiet households. They require daily grooming to keep their coat from matting. An interesting "
            "fact is that Persian cats were first introduced to Europe in the 17th century by Italian traders.\n",
            "Cats/Persian.jpg"),
        Cat('Bengal', 2, 3, 3, False,
            "These cats are known for their wild-looking coat, which comes from their Asian leopard cat ancestry. "
            "They are energetic and require plenty of playtime and stimulation. They can be trained to walk on a "
            "leash and even play fetch. An interesting fact is that Bengals are one of the few cat breeds that enjoy "
            "water and may even join their owners in the shower.\n", "Cats/Bengal.jpg"),
        Cat('Sphynx', 1, 1, 2, False,
            "This breed is known for its unique hairlessness, which requires regular bathing to maintain. They are "
            "friendly and enjoy being around people. Sphynx cats are also prone to certain health issues, "
            "such as skin problems and respiratory issues, due to their lack of fur. An interesting fact is that the "
            "Sphynx breed originated in Canada in the 1960s when a hairless kitten was born to a regular cat.\n",
            "Cats/Sphynx.jpg"),
        Cat('Scottish Fold', 1, 1, 3, True,
            "This breed is known for its distinctive folded ears and playful personality. They are affectionate and "
            "enjoy being around people. Scottish Folds are also prone to certain health issues, such as arthritis and "
            "ear infections, due to their folded ears. An interesting fact is that the Scottish Fold breed originated "
            "in Scotland in the 1960s from a barn cat with folded ears.\n", "Cats/Scottish_Fold.jpg"),
        Cat('Norwegian Forest Cat', 3, 2, 2, True,
            "These cats are known for their thick, fluffy coat and love of climbing. They are independent but "
            "affectionate with their families. They require regular grooming to maintain their coat. An interesting "
            "fact is that Norwegian Forest Cats are believed to have been the companions of Vikings and may have "
            "traveled with them on their voyages.\n", "Cats/Norwegian_Forest_Cat.jpg"),
        Cat('Russian Blue', 2, 2, 2, True,
            "This breed is known for its beautiful silver-blue coat and reserved nature. They are intelligent and "
            "enjoy playing games. Russian Blues are also prone to certain health issues, such as obesity and dental "
            "problems. An interesting fact is that Russian Blue cats were first introduced to Europe in the 1860s "
            "from Archangel, a port city in northern Russia.\n", "Cats/Russian_Blue.jpg"),
        Cat('Maine Coon', 3, 1, 3, True,
            "These cats are known for their large size and friendly personality. They are affectionate with their "
            "families and often enjoy playing with water. Maine Coons require regular grooming to maintain their "
            "long, silky coat. An interesting fact is that Maine Coons are believed to be the descendants of cats "
            "that traveled to America on ships with early European settlers.\n", "Cats/Maine_Coon.jpg"),
        Cat('British Shorthair', 2, 1, 2, True,
            "This breed is known for its round face and plush coat. They are easygoing and do well in families with "
            "children and other pets. British Shorthairs require regular grooming to maintain their coat. An "
            "interesting fact is that British Shorthairs were used during World War II to help control the rat "
            "population in London.\n", "Cats/British_Shorthair.jpg"),
        Cat('Egyptian Mau', 2, 3, 3, False,
            "These cats are known for their distinctive spots and love of playtime. They are intelligent and require "
            "plenty of stimulation. Egyptian Maus are also prone to certain health issues, such as dental problems"
            "and heart disease. An interesting fact is that Egyptian Maus are one of the oldest domesticated cat "
            "breeds and were worshiped in ancient Egypt.\n", "Cats/Egyptian_Mau.jpg"),
        Cat('American Shorthair', 2, 2, 1, True,
            "This breed is one of the most popular in the United States. They are known for their friendly and "
            "easygoing personalities. American Shorthairs were once used to help control rodent populations on farms "
            "and ships. Interesting fact: One American Shorthair named Creme Puff holds the record for being the "
            "oldest cat ever, living to be 38 years old.\n", "Cats/American_Shorthair.jpg"),
        Cat('Ragdoll', 3, 1, 3, True,
            "This breed is named for their tendency to go limp when picked up, similar to a ragdoll toy. They are "
            "large, gentle, and have a very calm demeanor. Ragdolls were originally bred in California in the 1960s. "
            "Interesting fact: Ragdolls are one of the few cat breeds that have blue eyes.\n", "Cats/Ragdoll.jpg"),
        Cat('Himalayan', 2, 1, 3, True,
            "This breed is a cross between the Persian and the Siamese, resulting in a cat with a striking appearance "
            "and a calm personality. Himalayans are also known for their vocalizations, which they use to communicate "
            "with their owners. Interesting fact: The Himalayan is also known as the Colorpoint Persian in some "
            "countries.\n", "Cats/Himalayan.jpg"),
        Cat('Bombay', 2, 3, 2, False,
            "This breed is named after the city of Bombay (now Mumbai) in India. They are a black, muscular, "
            "and intelligent breed that is known for their dog-like personalities. Bombays were first bred in the "
            "1950s in Kentucky. Interesting fact: Some Bombay cats have a unique copper eyes trait, where their eyes "
            "are a bright gold color.\n", "Cats/Bombay.jpg"),
        Cat('Devon Rex', 1, 3, 2, False,
            "This breed has a distinctive curly coat and large ears. They are known for being playful and "
            "affectionate, and they often form strong bonds with their owners. Devon Rex cats were first bred in "
            "England in the 1960s. Interesting fact: Devon Rex cats are sometimes referred to as poodle cats due to "
            "their curly fur.\n", "Cats/Devon_Rex.jpg")]

# **********************************************************************************************************************
# Global variables:


# Define the questions for cat and dog breed finder
questions_cats_dogs = ['How big is your house?',
                       'How many hours a day will you be able to spend with your pet?',
                       'How much money are you willing to spend on your pet monthly?',
                       'Do you have children?']

# Define the questions for pet finder
questions_pets = ['How much time are you able to dedicate to exercising your pet?',
                  'How important is it to you that your pet is social and enjoys human interaction?',
                  'How much space do you have available for your pet to live in?',
                  'How often are you willing to clean your pets living space?',
                  'How much time are you willing to spend on grooming and maintenance?']

# Global variable for temporary results for dog breed finder
new_best_dog_fits = []

# Global variable for temporary results for cat breed finder
new_best_cat_fits = []

# Global variable for the best results for pet finder
new_best_pet_fits = []

# Global variables for the answers for the dog breed finder
answer1_dog = 0
answer2_dog = 0
answer3_dog = 0
answer4_dog = 0

# Global variables for the answers for the cat breed finder
answer1_cat = 0
answer2_cat = 0
answer3_cat = 0
answer4_cat = 0

# Global variables for the answers for the pet finder
answer1_pet = 0
answer2_pet = 0
answer3_pet = 0
answer4_pet = 0
answer5_pet = 0


# **********************************************************************************************************************
# Functions for the GUI:
# (opens and closes windows, change button colors accordingly)

# Function to show the welcome message
def hide_welcome_message():
    global welcome_message_opened
    welcome_message.pack_forget()
    welcome_message_opened = False


# Function to show the pet finder
def show_pet_finder():
    global pet_finder_opened
    pet_finder.pack(fill=BOTH, expand=True)
    pet_finder_opened = True
    button_pet_finder.config(bg="#505d75")


# Function to hide the pet finder
def hide_pet_finder():
    global pet_finder_opened
    pet_finder.pack_forget()
    pet_finder_opened = False
    button_pet_finder.config(bg="#9da4b4")


# Function to show the pet finder results
def show_pet_finder_answers():
    global pet_finder_answers_opened
    pet_finder_answers.pack(fill=BOTH, expand=True)
    pet_finder_answers_opened = True
    button_pet_finder.config(bg="#505d75")


# Function to hide the pet finder results
def hide_pet_finder_answers():
    global pet_finder_answers_opened
    pet_finder_answers.pack_forget()
    pet_finder_answers_opened = False
    button_pet_finder.config(bg="#9da4b4")


# Function to show dog breed finder
def show_dog_finder():
    global dog_finder_opened
    dog_finder.pack(fill=BOTH, expand=True)
    dog_finder_opened = True
    button_dog_finder.config(bg="#505d75")


# Function to hide dog breed finder
def hide_dog_finder():
    global dog_finder_opened
    dog_finder.pack_forget()
    dog_finder_opened = False
    button_dog_finder.config(bg="#9da4b4")


# Function to show dog breed finder results
def show_dog_finder_answers():
    global dog_finder_answers_opened
    dog_finder_answers.pack(fill=BOTH, expand=True)
    dog_finder_answers_opened = True
    button_dog_finder.config(bg="#505d75")


# Function to hide dog breed finder results
def hide_dog_finder_answers():
    global dog_finder_answers_opened
    dog_finder_answers.pack_forget()
    dog_finder_answers_opened = False
    button_dog_finder.config(bg="#9da4b4")


# Function to show cat breed finder
def show_cat_finder():
    global cat_finder_opened
    cat_finder.pack(fill=BOTH, expand=True)
    cat_finder_opened = True
    button_cat_finder.config(bg="#505d75")


# Function to hide cat breed finder
def hide_cat_finder():
    global cat_finder_opened
    cat_finder.pack_forget()
    cat_finder_opened = False
    button_cat_finder.config(bg="#9da4b4")


# Function to show cat breed finder results
def show_cat_finder_answers():
    global cat_finder_answers_opened
    cat_finder_answers.pack(fill=BOTH, expand=True)
    cat_finder_answers_opened = True
    button_cat_finder.config(bg="#505d75")


# Function to hide cat breed finder results
def hide_cat_finder_answers():
    global cat_finder_answers_opened
    cat_finder_answers.pack_forget()
    cat_finder_answers_opened = False
    button_cat_finder.config(bg="#9da4b4")


# Function to show tips
def show_tips():
    global tips_opened
    tips.pack(fill=BOTH, expand=True, side=LEFT)
    tips_scrollbar.pack(side=RIGHT, fill=Y)
    tips_opened = True
    button_tips.config(bg="#505d75")


# Function to hide tips
def hide_tips():
    global tips_opened
    tips.pack_forget()
    tips_scrollbar.pack_forget()
    tips_opened = False
    button_tips.config(bg="#9da4b4")


# Function to show petbook
def show_petbook():
    global petbook_opened
    petbook.pack(fill=BOTH, expand=True, side=LEFT)
    petbook_scrollbar.pack(side=RIGHT, fill=Y)
    petbook_opened = True
    button_petbook.config(bg="#505d75")


# Function to hide petbook
def hide_petbook():
    global petbook_opened
    petbook.pack_forget()
    petbook_scrollbar.pack_forget()
    petbook_opened = False
    button_petbook.config(bg="#9da4b4")


# Function to open the dog breed finder
def open_dog_finder():
    if dog_finder_opened:
        pass
    else:
        hide_welcome_message()
        hide_petbook()
        hide_tips()
        hide_dog_finder_answers()
        hide_cat_finder()
        hide_cat_finder_answers()
        hide_pet_finder()
        hide_pet_finder_answers()
        show_dog_finder()


# Function to open the cat breed finder
def open_cat_finder():
    if cat_finder_opened:
        pass
    else:
        hide_welcome_message()
        hide_petbook()
        hide_tips()
        hide_cat_finder_answers()
        hide_dog_finder()
        hide_dog_finder_answers()
        hide_pet_finder()
        hide_pet_finder_answers()
        show_cat_finder()


# Function to open the pet finder
def open_pet_finder():
    if pet_finder_opened:
        pass
    else:
        hide_welcome_message()
        hide_petbook()
        hide_tips()
        hide_dog_finder()
        hide_dog_finder_answers()
        hide_cat_finder()
        hide_cat_finder_answers()
        hide_pet_finder_answers()
        show_pet_finder()


# Function to open the tips
def open_tips():
    if tips_opened:
        pass
    else:
        hide_dog_finder()
        hide_cat_finder()
        hide_petbook()
        hide_welcome_message()
        hide_dog_finder_answers()
        hide_cat_finder_answers()
        hide_pet_finder()
        hide_pet_finder_answers()
        show_tips()


# Function to open the petbook
def open_petbook():
    if petbook_opened:
        pass
    else:
        hide_tips()
        hide_welcome_message()
        hide_dog_finder()
        hide_dog_finder_answers()
        hide_cat_finder()
        hide_cat_finder_answers()
        hide_pet_finder()
        hide_pet_finder_answers()
        show_petbook()


# **********************************************************************************************************************
# Functions for the dog breed finder answers:
# (sets the answers for the questions and change the color of the buttons)
# (also checks if the user has answered all the questions, by button_find_a_dog_ready())
# (if so, changes the color of this button and assigns the function to show the results)

# Function to set the first question answer for first option
def answer_first_dog_question_A():
    global answer1_dog
    answer1_dog = 1
    button_dog_1a.config(bg="#505d75")
    button_dog_1b.config(bg="#9da4b4")
    button_dog_1c.config(bg="#9da4b4")
    button_find_a_dog_ready()


# Function to set the first question answer for second option
def answer_first_dog_question_B():
    global answer1_dog
    answer1_dog = 2
    button_dog_1a.config(bg="#9da4b4")
    button_dog_1b.config(bg="#505d75")
    button_dog_1c.config(bg="#9da4b4")
    button_find_a_dog_ready()


# Function to set the first question answer for third option
def answer_first_dog_question_C():
    global answer1_dog
    answer1_dog = 3
    button_dog_1a.config(bg="#9da4b4")
    button_dog_1b.config(bg="#9da4b4")
    button_dog_1c.config(bg="#505d75")
    button_find_a_dog_ready()


# Function to set the second question answer for first option
def answer_second_dog_question_A():
    global answer2_dog
    answer2_dog = 1
    button_dog_2a.config(bg="#505d75")
    button_dog_2b.config(bg="#9da4b4")
    button_dog_2c.config(bg="#9da4b4")
    button_find_a_dog_ready()


# Function to set the second question answer for second option
def answer_second_dog_question_B():
    global answer2_dog
    answer2_dog = 2
    button_dog_2a.config(bg="#9da4b4")
    button_dog_2b.config(bg="#505d75")
    button_dog_2c.config(bg="#9da4b4")
    button_find_a_dog_ready()


# Function to set the second question answer for third option
def answer_second_dog_question_C():
    global answer2_dog
    answer2_dog = 3
    button_dog_2a.config(bg="#9da4b4")
    button_dog_2b.config(bg="#9da4b4")
    button_dog_2c.config(bg="#505d75")
    button_find_a_dog_ready()


# Function to set the third question answer for first option
def answer_third_dog_question_A():
    global answer3_dog
    answer3_dog = 1
    button_dog_3a.config(bg="#505d75")
    button_dog_3b.config(bg="#9da4b4")
    button_dog_3c.config(bg="#9da4b4")
    button_find_a_dog_ready()


# Function to set the third question answer for second option
def answer_third_dog_question_B():
    global answer3_dog
    answer3_dog = 2
    button_dog_3a.config(bg="#9da4b4")
    button_dog_3b.config(bg="#505d75")
    button_dog_3c.config(bg="#9da4b4")
    button_find_a_dog_ready()


# Function to set the third question answer for third option
def answer_third_dog_question_C():
    global answer3_dog
    answer3_dog = 3
    button_dog_3a.config(bg="#9da4b4")
    button_dog_3b.config(bg="#9da4b4")
    button_dog_3c.config(bg="#505d75")
    button_find_a_dog_ready()


# Function to set the fourth question answer for first option
def answer_fourth_dog_question_A():
    global answer4_dog
    answer4_dog = 1
    button_dog_4a.config(bg="#505d75")
    button_dog_4b.config(bg="#9da4b4")
    button_find_a_dog_ready()


# Function to set the fourth question answer for second option
def answer_fourth_dog_question_B():
    global answer4_dog
    answer4_dog = 2
    button_dog_4a.config(bg="#9da4b4")
    button_dog_4b.config(bg="#505d75")
    button_find_a_dog_ready()


# Function to check if the user has answered all the questions
# (if so, changes the color of the button and assign a function to it)
def button_find_a_dog_ready():
    if answer1_dog != 0 and answer2_dog != 0 and answer3_dog != 0 and answer4_dog != 0:
        button_find_a_dog.configure(bg="#9da4b4", command=find_a_dog)
    else:
        button_find_a_dog.configure(bg="light grey")


# **********************************************************************************************************************
# Functions for the cat breed finder answers:
# (sets the answers for the questions and change the color of the buttons)
# (also checks if the user has answered all the questions, by button_find_a_cat_ready())
# (if so, changes the color of this button and assign a function to show the results)

# Function to set the first question answer for first option
def answer_first_cat_question_A():
    global answer1_cat
    answer1_cat = 1
    button_cat_1a.config(bg="#505d75")
    button_cat_1b.config(bg="#9da4b4")
    button_cat_1c.config(bg="#9da4b4")
    button_find_a_cat_ready()


# Function to set the first question answer for second option
def answer_first_cat_question_B():
    global answer1_cat
    answer1_cat = 2
    button_cat_1a.config(bg="#9da4b4")
    button_cat_1b.config(bg="#505d75")
    button_cat_1c.config(bg="#9da4b4")
    button_find_a_cat_ready()


# Function to set the first question answer for third option
def answer_first_cat_question_C():
    global answer1_cat
    answer1_cat = 3
    button_cat_1a.config(bg="#9da4b4")
    button_cat_1b.config(bg="#9da4b4")
    button_cat_1c.config(bg="#505d75")
    button_find_a_cat_ready()


# Function to set the second question answer for first option
def answer_second_cat_question_A():
    global answer2_cat
    answer2_cat = 1
    button_cat_2a.config(bg="#505d75")
    button_cat_2b.config(bg="#9da4b4")
    button_cat_2c.config(bg="#9da4b4")
    button_find_a_cat_ready()


# Function to set the second question answer for second option
def answer_second_cat_question_B():
    global answer2_cat
    answer2_cat = 2
    button_cat_2a.config(bg="#9da4b4")
    button_cat_2b.config(bg="#505d75")
    button_cat_2c.config(bg="#9da4b4")
    button_find_a_cat_ready()


# Function to set the second question answer for third option
def answer_second_cat_question_C():
    global answer2_cat
    answer2_cat = 3
    button_cat_2a.config(bg="#9da4b4")
    button_cat_2b.config(bg="#9da4b4")
    button_cat_2c.config(bg="#505d75")
    button_find_a_cat_ready()


# Function to set the third question answer for first option
def answer_third_cat_question_A():
    global answer3_cat
    answer3_cat = 1
    button_cat_3a.config(bg="#505d75")
    button_cat_3b.config(bg="#9da4b4")
    button_cat_3c.config(bg="#9da4b4")
    button_find_a_cat_ready()


# Function to set the third question answer for second option
def answer_third_cat_question_B():
    global answer3_cat
    answer3_cat = 2
    button_cat_3a.config(bg="#9da4b4")
    button_cat_3b.config(bg="#505d75")
    button_cat_3c.config(bg="#9da4b4")
    button_find_a_cat_ready()


# Function to set the third question answer for third option
def answer_third_cat_question_C():
    global answer3_cat
    answer3_cat = 3
    button_cat_3a.config(bg="#9da4b4")
    button_cat_3b.config(bg="#9da4b4")
    button_cat_3c.config(bg="#505d75")
    button_find_a_cat_ready()


# Function to set the fourth question answer for first option
def answer_fourth_cat_question_A():
    global answer4_cat
    answer4_cat = 1
    button_cat_4a.config(bg="#505d75")
    button_cat_4b.config(bg="#9da4b4")
    button_find_a_cat_ready()


# Function to set the fourth question answer for second option
def answer_fourth_cat_question_B():
    global answer4_cat
    answer4_cat = 2
    button_cat_4a.config(bg="#9da4b4")
    button_cat_4b.config(bg="#505d75")
    button_find_a_cat_ready()


# Function to check if the user has answered all the questions
# (if so, changes the color of the button and assign a function to it)
def button_find_a_cat_ready():
    if answer1_cat != 0 and answer2_cat != 0 and answer3_cat != 0 and answer4_cat != 0:
        button_find_a_cat.configure(bg="#9da4b4", command=find_a_cat)
    else:
        button_find_a_cat.configure(bg="light grey")


# **********************************************************************************************************************
# Functions for the pet breed finder answers:
# (sets the answers for the questions and change the color of the buttons)
# (also checks if the user has answered all the questions, by button_find_a_pet_ready())
# (if so, changes the color of this button and assign a function to show the results)

# Function to set the first question answer for first option
def answer_first_pet_question_A():
    global answer1_pet
    answer1_pet = 1
    button_pet_1a.config(bg="#505d75")
    button_pet_1b.config(bg="#9da4b4")
    button_pet_1c.config(bg="#9da4b4")
    button_pet_1d.config(bg="#9da4b4")
    button_pet_1e.config(bg="#9da4b4")
    button_find_a_pet_ready()


# Function to set the first question answer for second option
def answer_first_pet_question_B():
    global answer1_pet
    answer1_pet = 2
    button_pet_1a.config(bg="#9da4b4")
    button_pet_1b.config(bg="#505d75")
    button_pet_1c.config(bg="#9da4b4")
    button_pet_1d.config(bg="#9da4b4")
    button_pet_1e.config(bg="#9da4b4")
    button_find_a_pet_ready()


# Function to set the first question answer for third option
def answer_first_pet_question_C():
    global answer1_pet
    answer1_pet = 3
    button_pet_1a.config(bg="#9da4b4")
    button_pet_1b.config(bg="#9da4b4")
    button_pet_1c.config(bg="#505d75")
    button_pet_1d.config(bg="#9da4b4")
    button_pet_1e.config(bg="#9da4b4")
    button_find_a_pet_ready()


# Function to set the first question answer for fourth option
def answer_first_pet_question_D():
    global answer1_pet
    answer1_pet = 4
    button_pet_1a.config(bg="#9da4b4")
    button_pet_1b.config(bg="#9da4b4")
    button_pet_1c.config(bg="#9da4b4")
    button_pet_1d.config(bg="#505d75")
    button_pet_1e.config(bg="#9da4b4")
    button_find_a_pet_ready()


# Function to set the first question answer for fifth option
def answer_first_pet_question_E():
    global answer1_pet
    answer1_pet = 5
    button_pet_1a.config(bg="#9da4b4")
    button_pet_1b.config(bg="#9da4b4")
    button_pet_1c.config(bg="#9da4b4")
    button_pet_1d.config(bg="#9da4b4")
    button_pet_1e.config(bg="#505d75")
    button_find_a_pet_ready()


# Function to set the second question answer for first option
def answer_second_pet_question_A():
    global answer2_pet
    answer2_pet = 1
    button_pet_2a.config(bg="#505d75")
    button_pet_2b.config(bg="#9da4b4")
    button_pet_2c.config(bg="#9da4b4")
    button_find_a_pet_ready()


# Function to set the second question answer for second option
def answer_second_pet_question_B():
    global answer2_pet
    answer2_pet = 2
    button_pet_2a.config(bg="#9da4b4")
    button_pet_2b.config(bg="#505d75")
    button_pet_2c.config(bg="#9da4b4")
    button_find_a_pet_ready()


# Function to set the second question answer for third option
def answer_second_pet_question_C():
    global answer2_pet
    answer2_pet = 3
    button_pet_2a.config(bg="#9da4b4")
    button_pet_2b.config(bg="#9da4b4")
    button_pet_2c.config(bg="#505d75")
    button_find_a_pet_ready()


# Function to set the third question answer for first option
def answer_third_pet_question_A():
    global answer3_pet
    answer3_pet = 1
    button_pet_3a.config(bg="#505d75")
    button_pet_3b.config(bg="#9da4b4")
    button_pet_3c.config(bg="#9da4b4")
    button_pet_3d.config(bg="#9da4b4")
    button_pet_3e.config(bg="#9da4b4")
    button_find_a_pet_ready()


# Function to set the third question answer for second option
def answer_third_pet_question_B():
    global answer3_pet
    answer3_pet = 2
    button_pet_3a.config(bg="#9da4b4")
    button_pet_3b.config(bg="#505d75")
    button_pet_3c.config(bg="#9da4b4")
    button_pet_3d.config(bg="#9da4b4")
    button_pet_3e.config(bg="#9da4b4")
    button_find_a_pet_ready()


# Function to set the third question answer for third option
def answer_third_pet_question_C():
    global answer3_pet
    answer3_pet = 3
    button_pet_3a.config(bg="#9da4b4")
    button_pet_3b.config(bg="#9da4b4")
    button_pet_3c.config(bg="#505d75")
    button_pet_3d.config(bg="#9da4b4")
    button_pet_3e.config(bg="#9da4b4")
    button_find_a_pet_ready()


def answer_third_pet_question_D():
    global answer3_pet
    answer3_pet = 4
    button_pet_3a.config(bg="#9da4b4")
    button_pet_3b.config(bg="#9da4b4")
    button_pet_3c.config(bg="#9da4b4")
    button_pet_3d.config(bg="#505d75")
    button_pet_3e.config(bg="#9da4b4")
    button_find_a_pet_ready()


def answer_third_pet_question_E():
    global answer3_pet
    answer3_pet = 5
    button_pet_3a.config(bg="#9da4b4")
    button_pet_3b.config(bg="#9da4b4")
    button_pet_3c.config(bg="#9da4b4")
    button_pet_3d.config(bg="#9da4b4")
    button_pet_3e.config(bg="#505d75")
    button_find_a_pet_ready()


# Function to set the fourth question answer for first option
def answer_fourth_pet_question_A():
    global answer4_pet
    answer4_pet = 1
    button_pet_4a.config(bg="#505d75")
    button_pet_4b.config(bg="#9da4b4")
    button_find_a_pet_ready()


# Function to set the fourth question answer for second option
def answer_fourth_pet_question_B():
    global answer4_pet
    answer4_pet = 2
    button_pet_4a.config(bg="#9da4b4")
    button_pet_4b.config(bg="#505d75")
    button_find_a_pet_ready()


# Function to set the fifth question answer for first option
def answer_fifth_pet_question_A():
    global answer5_pet
    answer5_pet = 1
    button_pet_5a.config(bg="#505d75")
    button_pet_5b.config(bg="#9da4b4")
    button_pet_5c.config(bg="#9da4b4")
    button_find_a_pet_ready()


# Function to set the fifth question answer for second option
def answer_fifth_pet_question_B():
    global answer5_pet
    answer5_pet = 2
    button_pet_5a.config(bg="#9da4b4")
    button_pet_5b.config(bg="#505d75")
    button_pet_5c.config(bg="#9da4b4")
    button_find_a_pet_ready()


# Function to set the fifth question answer for third option
def answer_fifth_pet_question_C():
    global answer5_pet
    answer5_pet = 3
    button_pet_5a.config(bg="#9da4b4")
    button_pet_5b.config(bg="#9da4b4")
    button_pet_5c.config(bg="#505d75")
    button_find_a_pet_ready()


# Function to check if the user has answered all the questions
# (if so, changes the color of the button and assign a function to it)
def button_find_a_pet_ready():
    if answer1_pet != 0 and answer2_pet != 0 and answer3_pet != 0 and answer4_pet != 0 and answer5_pet != 0:
        button_find_a_pet.configure(bg="#9da4b4", command=find_a_pet)
    else:
        button_find_a_pet.configure(bg="light grey")


# **********************************************************************************************************************
# Functions for a specific options needed for each page:
# (like the function to find a breed of dog/cat, or the function to find a type of pet)
# (they are needed, as all of this is done in two different pages (questions and answers))

# Function to find a breed of dog
def find_a_dog():
    # Global variables needed for the function
    global new_best_dog_fits, dog_finder_temporary_results, dog_finder_temporary_results_scrollbar

    # Sets the local variables (or resets them, if the function is called again)
    best_dog_score = 0
    best_dog_fits = []

    # Go through all the dogs and check if they are a fit
    for pet in dogs:
        # Resets pets temporary stats
        pet.fit_reasons = []
        pet.not_fit_reasons = []
        pet.score = 0

        # Check if the size is a fit
        if answer1_dog == pet.size:
            # If it is, add 2 points to the score and add a reason to the list of fit reasons
            pet.score += 2
            pet.fit_reasons.append(f'Question: {questions_cats_dogs[0]}\nYour answer is a MATCH.\n\n'
                                   f'Your answer matches the ideal size for this pet. Choosing the right size of pet '
                                   f'is important because it can affect your lifestyle and living conditions. This '
                                   f'pet should fit well in your home and be easy for you to care for.')
        else:
            diff = abs(answer1_dog - pet.size)
            # If it is not, check if the answer is higher or lower than the ideal size
            if answer1_dog < pet.size:
                # If it is lower
                if diff == 1:
                    # If it is a small difference, add 1 point and add a reason to the list of not fit reasons
                    pet.score += 1
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[0]}\nYour answer is LOWER.\n\n'
                                               f'Your answer indicates that you may prefer a smaller pet. Keep in '
                                               f'mind that smaller pets may be better suited for smaller living '
                                               f'spaces, but they may also require more frequent exercise to keep '
                                               f'them healthy. Consider the size and activity level of this pet '
                                               f'before making a decision.')
                else:
                    # If it is a big difference, no points and add a reason to the list of not fit reasons
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[0]}\nYour answer is a MUCH LOWER.\n\n'
                                               f'Your answer suggests that you may be looking for a much smaller pet. '
                                               f'Keep in mind that some smaller pets may still require a lot of '
                                               f'exercise or have specific care requirements, so make sure you '
                                               f'research the pet thoroughly before making a decision.')
            else:
                # If it is higher
                if diff == 1:
                    # If it is a small difference, add 2 points and add a reason to the list of fit reasons
                    pet.score += 2
                    pet.fit_reasons.append(f'Question: {questions_cats_dogs[0]}\nYour answer is HIGHER.\n\n'
                                           f'Your answer for size is higher than the ideal size for this pet, '
                                           f'which can be a good thing if you have a bigger living space or are '
                                           f'looking for a pet that requires more exercise.')
                else:
                    # If it is a big difference, add 2 points and add a reason to the list of fit reasons
                    pet.score += 2
                    pet.fit_reasons.append(f'Question: {questions_cats_dogs[0]}\nYour answer is MUCH HIGHER.\n\n'
                                           f'Your answer suggests that you have a significantly larger living space '
                                           f'than what is required for this pet. While some may see this as a '
                                           f'disadvantage, having extra space can actually be beneficial for your '
                                           f'pets overall well-being. A larger living space can provide your pet with '
                                           f'more room to move and explore, which can help reduce stress and boredom. '
                                           f'Additionally, having a larger living space can also provide '
                                           f'opportunities for you to add more pets to your household in the '
                                           f'future.')

        # Check if the activity level is a fit
        if answer2_dog == pet.activity:
            # If it is, add 2 points to the score and add a reason to the list of fit reasons
            pet.score += 2
            pet.fit_reasons.append(f'Question: {questions_cats_dogs[1]}\nYour answer is MATCH.\n\n'
                                   f'Your answer matches the ideal activity level for this pet. This pet should be a '
                                   f'good match for your lifestyle and energy levels, allowing you to provide for its '
                                   f'needs without feeling overwhelmed or unfulfilled. Keep in mind that the activity '
                                   f'level of a pet can affect not only its own well-being, but also its '
                                   f'compatibility with your own lifestyle and living situation.')
        else:
            # If it is not, check if the answer is higher or lower than the ideal activity level
            diff = abs(answer2_dog - pet.activity)
            if answer2_dog < pet.activity:
                # If it is lower
                if diff == 1:
                    # If it is a small difference, add 1 point and add a reason to the list of not fit reasons
                    pet.score += 1
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[1]}\nYour answer: is LOWER.\n\n'
                                               f'Your answer suggests that you may prefer a pet with a lower activity '
                                               f'level. While this may be a good fit for your lifestyle, keep in mind '
                                               f'that some pets may require more exercise and stimulation than others '
                                               f'to stay healthy and happy. Make sure that you are able to provide '
                                               f'for your pets needs without compromising its health or well-being.')
                else:
                    # If it is a big difference, no points and add a reason to the list of not fit reasons
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[1]}\nYour answer is a MUCH LOWER.\n\n'
                                               f'Your answer suggests that you may be looking for a pet with a '
                                               f'significantly lower activity level than what is recommended. While '
                                               f'this may be a good fit for your lifestyle, keep in mind that some '
                                               f'pets may become lethargic or develop health issues if they are not '
                                               f'given enough exercise and stimulation.')
            else:
                # If it is higher
                if diff == 1:
                    # If it is a small difference, add 1 point and add a reason to the list of not fit reasons
                    pet.score += 1
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[1]}\nYour answer is HIGHER.\n\n'
                                               f'It means you are looking for a pet that is more active. Having a pet '
                                               f'with higher activity level can be great for your physical and mental '
                                               f'health, as it can motivate you to be more active and engage in more '
                                               f'physical activities with your pet. It can also help you bond with '
                                               f'your pet more and strengthen your relationship.')
                else:
                    # If it is a big difference, no points and add a reason to the list of not fit reasons
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[1]}\nYour answer is much higher.\n\n'
                                               f'It suggests that you are looking for a pet that is very active and '
                                               f'energetic. While this can be a great match for someone who enjoys an '
                                               f'active lifestyle and can dedicate a lot of time to exercising with '
                                               f'their pet, it is important to consider if you are able to meet the '
                                               f'high energy demands of such a pet. You also need to make sure that '
                                               f'you provide enough mental and physical stimulation for your pet to '
                                               f'prevent boredom and destructive behavior.')

        # Check if the cost is a fit
        if answer3_dog == pet.cost:
            # If it is, add 2 points to the score and add a reason to the list of fit reasons
            pet.score += 2
            pet.fit_reasons.append(f'Question: {questions_cats_dogs[2]}\nYour answer is MATCH.\n\n'
                                   f'Your answer matches the ideal cost range for this pet.'
                                   f'This pet should be within your budget, allowing you to provide for its needs '
                                   f'without sacrificing your own financial stability. Keep in mind that the cost of '
                                   f'owning a pet goes beyond just purchasing it - you will also need to consider '
                                   f'ongoing expenses such as food, veterinary care, and grooming.')
        else:
            # If it is not, check if the answer is higher or lower than the ideal cost
            diff = abs(answer3_dog - pet.cost)
            if answer3_dog < pet.cost:
                # If it is lower
                if diff == 1:
                    # If it is a small difference, add 1 point and add a reason to the list of not fit reasons
                    pet.score += 1
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[2]}\nYour answer is LOWER.\n\n'
                                               f'Your answer suggests that you may prefer a pet with a lower cost.'
                                               f'While this pet may fit within your budget, keep in mind that the '
                                               f'cost of owning a pet goes beyond just purchasing it. You will also '
                                               f'need to consider ongoing expenses such as food, veterinary care, '
                                               f'and grooming. Make sure that you are able to provide for your pets '
                                               f'needs without compromising its health or well-being.')
                else:
                    # If it is a big difference, no points and add a reason to the list of not fit reasons
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[2]}\nYour answer is a MUCH LOWER.\n\n'
                                               f'Your answer suggests that you are looking for a pet with '
                                               f'significantly lower cost than what is recommended. While this may b'
                                               f'tempting, keep in mind that pets with lower upfront costs may end u'
                                               f'costing more in the long run due to health issues or other'
                                               f'unforeseen expenses. Consider the ongoing expenses of owning a pe'
                                               f'and make sure that you are able to provide for your pets need'
                                               f'without compromising its health or well-bein')
            else:
                # If it is higher
                if diff == 1:
                    # If it is a small difference, add 2 points and add a reason to the list of fit reasons
                    pet.score += 2
                    pet.fit_reasons.append(f'Question: {questions_cats_dogs[2]}\nYour answer is HIGHER.\n\n'
                                           f'Your answer indicates that you may be comfortable with a higher cost '
                                           f'for your pet. While this may allow you to provide your pet with the '
                                           f'best possible care, keep in mind that higher costs do not '
                                           f'necessarily guarantee better quality. Make sure to do your research '
                                           f'and choose a pet that fits within your budget while also providing '
                                           f'the level of care and attention that you are comfortable with.')
                else:
                    # If it is a big difference, add 2 points and add a reason to the list of fit reasons
                    pet.score += 2
                    pet.fit_reasons.append(f'Question: {questions_cats_dogs[2]}\nYour answer is MUCH HIGHER.\n\n'
                                           f'Your answer suggests that you may be looking for a pet with a '
                                           f'significantly higher cost than what is recommended. While this may '
                                           f'allow you to provide your pet with top-of-the-line care and '
                                           f'attention, keep in mind that there are many affordable pet options '
                                           f'that can also be wonderful companions.')

        # Add the pet to the best fits list and update the best score
        if pet.score >= best_dog_score:
            best_dog_score = pet.score
            best_dog_fits.append(pet)

    # Create a new list for the best fits (needed, as going through the list while removing items can cause errors)
    new_best_dog_fits = []

    # Remove pets with a score lower than the best score
    for pet in best_dog_fits:
        if pet.score >= best_dog_score:
            new_best_dog_fits.append(pet)

    # Remove pets that are not suitable for children if applicable
    if answer4_dog == 1:
        new_best_dog_fits = [pet for pet in new_best_dog_fits if pet.children]

    # Print answers in console, for testing purposes

    # Print the title
    print('Dog Finder')
    print(f'Your answers: {answer1_dog}, {answer2_dog}, {answer3_dog}, {answer4_dog}')
    # Print the best fits
    print('Best fits:')
    for _ in new_best_dog_fits:
        print(f'{_.name} - {_.score}')
    print('Other dogs:')
    for _ in dogs:
        if _ not in new_best_dog_fits:
            print(f'{_.name} - {_.score}')
    # Print the empty line
    print()

    # When new_best_fits is empty (no results), change the button text to "No results, try again!"
    if len(new_best_dog_fits) == 0:
        button_find_a_dog.config(text="No results, try again!")

    # Update dog finder title and button, then hide dog finder (questions) window and show results window
    else:
        # Change menu button and title text for another turn
        button_find_a_dog.config(text="Find a dog!")
        dog_finder_title.config(text="Wanna try again? Your last answers:")
        # Hide dog finder window
        hide_dog_finder()
        # Show results window
        show_dog_finder_answers()
        # Destroy temporary results and create a new ones (to clear the previous results)
        dog_finder_temporary_results.destroy()
        dog_finder_temporary_results_scrollbar.destroy()
        # Create a canvas to hold the new temporary results
        dog_finder_temporary_results = Canvas(dog_finder_answers)
        dog_finder_temporary_results.pack(side=LEFT, fill=BOTH, expand=True)
        # Create a scrollbar for the canvas
        dog_finder_temporary_results_scrollbar = Scrollbar(dog_finder_answers,
                                                           command=dog_finder_temporary_results.yview)
        dog_finder_temporary_results_scrollbar.pack(side=RIGHT, fill=Y)
        # Configure the canvas to use the scrollbar
        dog_finder_temporary_results.configure(yscrollcommand=dog_finder_temporary_results_scrollbar.set)

        # Create a frame to hold the labels
        results1_frame = Frame(dog_finder_temporary_results, bg="white")
        results1_frame.pack(fill=X)

        # Create a label for the title
        Label(results1_frame, text="Take a look!", bg="white", fg="#505d75", pady=10, font=("Helvetica", 16)).pack(
            fill=X, expand=True)

        # Go through the new best fits list and add the results to the frame
        for _ in new_best_dog_fits:
            # Load the image and resize it
            img1 = Image.open(_.pic)
            img1 = img1.resize((130, 130), Image.LANCZOS)
            # Convert the image to a tkinter-compatible format
            img_tk1 = ImageTk.PhotoImage(img1)

            # Add a line between each dog
            Label(results1_frame, width=67, bg="#d8dbe1").pack()

            # Create a label for the image and add it to the frame
            img_label1 = Label(results1_frame, image=img_tk1, width=470, bg="#d8dbe1")
            img_label1.image = img_tk1
            img_label1.pack(fill=X)

            # Create a label for the name and add it to the frame
            Label(results1_frame, text=_.name, bg="#d8dbe1", fg="#505d75", width=52, font=("Helvetica", 12)).pack(
                fill=X)
            Label(results1_frame, text=_.info, bg="#d8dbe1", fg="#505d75", font=("Helvetica", 10), wraplength=450).pack(
                fill=X)

            # Create a label for the fit reasons and add it to the frame
            Label(results1_frame, text="\nReasons why this dog is a good fit for you:\n", bg="white", fg="#505d75",
                  font=("Helvetica", 11)).pack(fill=X)
            # Go through the fit reasons and add them to the frame
            for reason in _.fit_reasons:
                Label(results1_frame, text=reason, fg="#505d75", font=("Helvetica", 10), wraplength=450).pack(fill=X)
                Label(results1_frame, bg="white").pack()

            # Go through the not fit reasons and add them to the frame (if there are any)
            if len(_.not_fit_reasons) > 0:
                # Create a label for not fit reasons and add it to the frame
                Label(results1_frame, text="Reasons why this dog is not a good fit for you:\n", bg="white",
                      fg="#505d75",
                      font=("Helvetica", 11)).pack(fill=X)
                for reason in _.not_fit_reasons:
                    Label(results1_frame, text=reason, fg="#505d75", font=("Helvetica", 10), wraplength=450).pack(
                        fill=X)
                Label(results1_frame, bg="white").pack()

        # update the canvas to fit the frame
        dog_finder_temporary_results.create_window((0, 0), window=results1_frame, anchor=NW)
        results1_frame.update_idletasks()
        dog_finder_temporary_results.config(scrollregion=dog_finder_temporary_results.bbox("all"))


# Function to find a breed of cat
def find_a_cat():
    # Global variables needed for the function
    global new_best_cat_fits, cat_finder_temporary_results, cat_finder_temporary_results_scrollbar

    # Sets the local variables (or resets them, if the function is called again)
    best_cat_score = 0
    best_cat_fits = []

    # Go through all the cats and check if they are a fit
    for pet in cats:
        # Resets pets temporary stats
        pet.fit_reasons = []
        pet.not_fit_reasons = []
        pet.score = 0

        # Check if the size is a fit
        if answer1_cat == pet.size:
            # If it is, add 2 points to the score and add a reason to the list of fit reasons
            pet.score += 2
            pet.fit_reasons.append(f'Question: {questions_cats_dogs[0]}\nYour answer is a MATCH.\n\n'
                                   f'Your answer matches the ideal size for this pet. Choosing the right size of pet '
                                   f'is important because it can affect your lifestyle and living conditions. This '
                                   f'pet should fit well in your home and be easy for you to care for.')
        else:
            diff = abs(answer1_cat - pet.size)
            # If it is not, check if the answer is higher or lower than the ideal size
            if answer1_cat < pet.size:
                # If it is lower
                if diff == 1:
                    # If it is a small difference, add 1 point and add a reason to the list of not fit reasons
                    pet.score += 1
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[0]}\nYour answer is LOWER.\n\n'
                                               f'Your answer indicates that you may prefer a smaller pet. Keep in '
                                               f'mind that smaller pets may be better suited for smaller living '
                                               f'spaces, but they may also require more frequent exercise to keep '
                                               f'them healthy. Consider the size and activity level of this pet '
                                               f'before making a decision.')
                else:
                    # If it is a big difference, no points and add a reason to the list of not fit reasons
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[0]}\nYour answer is a MUCH LOWER.\n\n'
                                               f'Your answer suggests that you may be looking for a much smaller pet. '
                                               f'Keep in mind that some smaller pets may still require a lot of '
                                               f'exercise or have specific care requirements, so make sure you '
                                               f'research the pet thoroughly before making a decision.')
            else:
                # If it is higher
                if diff == 1:
                    # If it is a small difference, add 2 points and add a reason to the list of fit reasons
                    pet.score += 2
                    pet.fit_reasons.append(f'Question: {questions_cats_dogs[0]}\nYour answer is HIGHER.\n\n'
                                           f'Your answer for size is higher than the ideal size for this pet, '
                                           f'which can be a good thing if you have a bigger living space or are '
                                           f'looking for a pet that requires more exercise.')
                else:
                    # If it is a big difference, add 2 points and add a reason to the list of fit reasons
                    pet.score += 2
                    pet.fit_reasons.append(f'Question: {questions_cats_dogs[0]}\nYour answer is MUCH HIGHER.\n\n'
                                           f'Your answer suggests that you have a significantly larger living space '
                                           f'than what is required for this pet. While some may see this as a '
                                           f'disadvantage, having extra space can actually be beneficial for your '
                                           f'pets overall well-being. A larger living space can provide your pet with '
                                           f'more room to move and explore, which can help reduce stress and boredom. '
                                           f'Additionally, having a larger living space can also provide '
                                           f'opportunities for you to add more pets to your household in the '
                                           f'future.')

        # Check if the activity level is a fit
        if answer2_cat == pet.activity:
            # If it is, add 2 points to the score and add a reason to the list of fit reasons
            pet.score += 2
            pet.fit_reasons.append(f'Question: {questions_cats_dogs[1]}\nYour answer is MATCH.\n\n'
                                   f'Your answer matches the ideal activity level for this pet. This pet should be a '
                                   f'good match for your lifestyle and energy levels, allowing you to provide for its '
                                   f'needs without feeling overwhelmed or unfulfilled. Keep in mind that the activity '
                                   f'level of a pet can affect not only its own well-being, but also its '
                                   f'compatibility with your own lifestyle and living situation.')
        else:
            # If it is not, check if the answer is higher or lower than the ideal activity level
            diff = abs(answer2_cat - pet.activity)
            if answer2_cat < pet.activity:
                # If it is lower
                if diff == 1:
                    # If it is a small difference, add 1 point and add a reason to the list of not fit reasons
                    pet.score += 1
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[1]}\nYour answer: is LOWER.\n\n'
                                               f'Your answer suggests that you may prefer a pet with a lower activity '
                                               f'level. While this may be a good fit for your lifestyle, keep in mind '
                                               f'that some pets may require more exercise and stimulation than others '
                                               f'to stay healthy and happy. Make sure that you are able to provide '
                                               f'for your pets needs without compromising its health or well-being.')
                else:
                    # If it is a big difference, no points and add a reason to the list of not fit reasons
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[1]}\nYour answer is a MUCH LOWER.\n\n'
                                               f'Your answer suggests that you may be looking for a pet with a '
                                               f'significantly lower activity level than what is recommended. While '
                                               f'this may be a good fit for your lifestyle, keep in mind that some '
                                               f'pets may become lethargic or develop health issues if they are not '
                                               f'given enough exercise and stimulation.')
            else:
                # If it is higher
                if diff == 1:
                    # If it is a small difference, add 1 point and add a reason to the list of not fit reasons
                    pet.score += 1
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[1]}\nYour answer is HIGHER.\n\n'
                                               f'It means you are looking for a pet that is more active. Having a pet '
                                               f'with higher activity level can be great for your physical and mental '
                                               f'health, as it can motivate you to be more active and engage in more '
                                               f'physical activities with your pet. It can also help you bond with '
                                               f'your pet more and strengthen your relationship.')
                else:
                    # If it is a big difference, no points and add a reason to the list of not fit reasons
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[1]}\nYour answer is much higher.\n\n'
                                               f'It suggests that you are looking for a pet that is very active and '
                                               f'energetic. While this can be a great match for someone who enjoys an '
                                               f'active lifestyle and can dedicate a lot of time to exercising with '
                                               f'their pet, it is important to consider if you are able to meet the '
                                               f'high energy demands of such a pet. You also need to make sure that '
                                               f'you provide enough mental and physical stimulation for your pet to '
                                               f'prevent boredom and destructive behavior.')

        # Check if the cost is a fit
        if answer3_cat == pet.cost:
            # If it is, add 2 points to the score and add a reason to the list of fit reasons
            pet.score += 2
            pet.fit_reasons.append(f'Question: {questions_cats_dogs[2]}\nYour answer is MATCH.\n\n'
                                   f'Your answer matches the ideal cost range for this pet.'
                                   f'This pet should be within your budget, allowing you to provide for its needs '
                                   f'without sacrificing your own financial stability. Keep in mind that the cost of '
                                   f'owning a pet goes beyond just purchasing it - you will also need to consider '
                                   f'ongoing expenses such as food, veterinary care, and grooming.')
        else:
            # If it is not, check if the answer is higher or lower than the ideal cost
            diff = abs(answer3_cat - pet.cost)
            if answer3_cat < pet.cost:
                # If it is lower
                if diff == 1:
                    # If it is a small difference, add 1 point and add a reason to the list of not fit reasons
                    pet.score += 1
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[2]}\nYour answer is LOWER.\n\n'
                                               f'Your answer suggests that you may prefer a pet with a lower cost.'
                                               f'While this pet may fit within your budget, keep in mind that the '
                                               f'cost of owning a pet goes beyond just purchasing it. You will also '
                                               f'need to consider ongoing expenses such as food, veterinary care, '
                                               f'and grooming. Make sure that you are able to provide for your pets '
                                               f'needs without compromising its health or well-being.')
                else:
                    # If it is a big difference, no points and add a reason to the list of not fit reasons
                    pet.not_fit_reasons.append(f'Question: {questions_cats_dogs[2]}\nYour answer is a MUCH LOWER.\n\n'
                                               f'Your answer suggests that you are looking for a pet with '
                                               f'significantly lower cost than what is recommended. While this may b'
                                               f'tempting, keep in mind that pets with lower upfront costs may end u'
                                               f'costing more in the long run due to health issues or other'
                                               f'unforeseen expenses. Consider the ongoing expenses of owning a pe'
                                               f'and make sure that you are able to provide for your pets need'
                                               f'without compromising its health or well-bein')
            else:
                # If it is higher
                if diff == 1:
                    # If it is a small difference, add 2 points and add a reason to the list of fit reasons
                    pet.score += 2
                    pet.fit_reasons.append(f'Question: {questions_cats_dogs[2]}\nYour answer is HIGHER.\n\n'
                                           f'Your answer indicates that you may be comfortable with a higher cost '
                                           f'for your pet. While this may allow you to provide your pet with the '
                                           f'best possible care, keep in mind that higher costs do not '
                                           f'necessarily guarantee better quality. Make sure to do your research '
                                           f'and choose a pet that fits within your budget while also providing '
                                           f'the level of care and attention that you are comfortable with.')
                else:
                    # If it is a big difference, add 2 points and add a reason to the list of fit reasons
                    pet.score += 2
                    pet.fit_reasons.append(f'Question: {questions_cats_dogs[2]}\nYour answer is MUCH HIGHER.\n\n'
                                           f'Your answer suggests that you may be looking for a pet with a '
                                           f'significantly higher cost than what is recommended. While this may '
                                           f'allow you to provide your pet with top-of-the-line care and '
                                           f'attention, keep in mind that there are many affordable pet options '
                                           f'that can also be wonderful companions.')

        # Add the pet to the best fits list and update the best score
        if pet.score >= best_cat_score:
            best_cat_score = pet.score
            best_cat_fits.append(pet)

    # Create a new list for the best fits (needed, as going through the list while removing items can cause errors)
    new_best_cat_fits = []

    # Remove pets with a score lower than the best score
    for pet in best_cat_fits:
        if pet.score >= best_cat_score:
            new_best_cat_fits.append(pet)

    # Remove pets that are not suitable for children if applicable
    if answer4_cat == 1:
        new_best_cat_fits = [pet for pet in new_best_cat_fits if pet.children]

    # Print answers in console, for testing purposes

    # Print the title
    print('Cat Finder')
    print(f'Your answers: {answer1_cat}, {answer2_cat}, {answer3_cat}, {answer4_cat}')
    # Print the best fits
    print('Best fits:')
    for pet in new_best_cat_fits:
        print(f'{pet.name} - {pet.score}')
    print('Other cats:')
    for _ in cats:
        if _ not in new_best_cat_fits:
            print(f'{_.name} - {_.score}')
    # Print the empty line
    print()

    # When new_best_fits is empty (no results), change the button text to "No results, try again!"
    if len(new_best_cat_fits) == 0:
        button_find_a_cat.config(text="No results, try again!")

    # Update cat finder title and button, then hide cat finder (questions) window and show results window
    else:
        # Change menu button and title text for another turn
        button_find_a_cat.config(text="Find a cat!")
        cat_finder_title.config(text="Wanna try again? Your last answers:")
        # Hide cat finder window
        hide_cat_finder()
        # Show results window
        show_cat_finder_answers()
        # Destroy temporary results and create a new ones (to clear the previous results)
        cat_finder_temporary_results.destroy()
        cat_finder_temporary_results_scrollbar.destroy()
        # Create a canvas to hold the new temporary results
        cat_finder_temporary_results = Canvas(cat_finder_answers)
        cat_finder_temporary_results.pack(side=LEFT, fill=BOTH, expand=True)
        # Create a scrollbar for the canvas
        cat_finder_temporary_results_scrollbar = Scrollbar(cat_finder_answers,
                                                           command=cat_finder_temporary_results.yview)
        cat_finder_temporary_results_scrollbar.pack(side=RIGHT, fill=Y)
        # Configure the canvas to use the scrollbar
        cat_finder_temporary_results.configure(yscrollcommand=cat_finder_temporary_results_scrollbar.set)

        # Create a frame to hold the labels
        results1_frame = Frame(cat_finder_temporary_results, bg="white")
        results1_frame.pack(fill=X)

        # Create a label for the title
        Label(results1_frame, text="Take a look!", bg="white", fg="#505d75", pady=10, font=("Helvetica", 16)).pack(
            fill=X, expand=True)

        # Go through the new best fits list and add the results to the frame
        for _ in new_best_cat_fits:
            # Load the image and resize it
            img1 = Image.open(_.pic)
            img1 = img1.resize((130, 130), Image.LANCZOS)
            # Convert the image to a tkinter-compatible format
            img_tk1 = ImageTk.PhotoImage(img1)

            # Add a line between each cat
            Label(results1_frame, width=67, bg="#d8dbe1").pack()

            # Create a label for the image and add it to the frame
            img_label1 = Label(results1_frame, image=img_tk1, width=470, bg="#d8dbe1")
            img_label1.image = img_tk1
            img_label1.pack(fill=X)

            # Create a label for the name and add it to the frame
            Label(results1_frame, text=_.name, bg="#d8dbe1", fg="#505d75", width=52, font=("Helvetica", 12)).pack(
                fill=X)
            Label(results1_frame, text=_.info, bg="#d8dbe1", fg="#505d75", font=("Helvetica", 10), wraplength=450).pack(
                fill=X)

            # Create a label for the fit reasons and add it to the frame
            Label(results1_frame, text="\nReasons why this cat is a good fit for you:\n", bg="white", fg="#505d75",
                  font=("Helvetica", 11)).pack(fill=X)
            # Go through the fit reasons and add them to the frame
            for reason in _.fit_reasons:
                Label(results1_frame, text=reason, fg="#505d75", font=("Helvetica", 10), wraplength=450).pack(fill=X)
                Label(results1_frame, bg="white").pack()

            # Go through the not fit reasons and add them to the frame (if there are any)
            if len(_.not_fit_reasons) > 0:
                # Create a label for not fit reasons and add it to the frame
                Label(results1_frame, text="Reasons why this cat is not a good fit for you:\n", bg="white",
                      fg="#505d75",
                      font=("Helvetica", 11)).pack(fill=X)
                for reason in _.not_fit_reasons:
                    Label(results1_frame, text=reason, fg="#505d75", font=("Helvetica", 10), wraplength=450).pack(
                        fill=X)
                Label(results1_frame, bg="white").pack()

        # update the canvas to fit the frame
        cat_finder_temporary_results.create_window((0, 0), window=results1_frame, anchor=NW)
        results1_frame.update_idletasks()
        cat_finder_temporary_results.config(scrollregion=cat_finder_temporary_results.bbox("all"))


# Function to find a pet
def find_a_pet():
    # Global variables needed for the function
    global pet_finder_temporary_results, pet_finder_temporary_results_scrollbar

    # Initialize the points for each pet to zero
    dog_points = 0
    cat_points = 0
    fish_points = 0
    rat_points = 0
    rabbit_points = 0

    # Add points to the pets based on the answers

    # First question
    if answer1_pet == 1:
        fish_points += 1
    elif answer1_pet == 2:
        rat_points += 1
    elif answer1_pet == 3:
        cat_points += 1
    elif answer1_pet == 4:
        rabbit_points += 1
    elif answer1_pet == 5:
        dog_points += 1

    # Second question
    if answer2_pet == 1:
        dog_points += 1
        rat_points += 1
    elif answer2_pet == 2:
        cat_points += 1
        rabbit_points += 1
    elif answer2_pet == 3:
        fish_points += 1

    # Third question
    if answer3_pet == 1:
        dog_points += 1
    elif answer3_pet == 2:
        cat_points += 1
    elif answer3_pet == 3:
        fish_points += 1
    elif answer3_pet == 4:
        rat_points += 1
    elif answer3_pet == 5:
        rabbit_points += 1

    # Fourth question
    if answer4_pet == 1:
        dog_points += 1
        cat_points += 1
    elif answer4_pet == 2:
        fish_points += 1
        rat_points += 1
        rabbit_points += 1

    # Fifth question
    if answer5_pet == 1:
        dog_points += 1
        rabbit_points += 1
    elif answer5_pet == 2:
        cat_points += 1
        rat_points += 1
    elif answer5_pet == 3:
        fish_points += 1

    # Find the pet(s) with the most points
    max_points = max(dog_points, cat_points, fish_points, rat_points, rabbit_points)
    best_pet_fits = []

    if dog_points == max_points:
        best_pet_fits.append(Dog.__name__)
    if cat_points == max_points:
        best_pet_fits.append(Cat.__name__)
    if fish_points == max_points:
        best_pet_fits.append(Fish.__name__)
    if rat_points == max_points:
        best_pet_fits.append(Rat.__name__)
    if rabbit_points == max_points:
        best_pet_fits.append(Rabbit.__name__)

    # Print answers in console, for testing purposes

    # Print the title
    print('Pet Finder')
    print(f'Your answers: {answer1_pet}, {answer2_pet}, {answer3_pet}, {answer4_pet}, {answer5_pet}')
    # Print the best fits
    print('Best fits:')
    for _ in best_pet_fits:
        print(f'{_}')
    print('All pets with score:')
    print(f'Dog: {dog_points}')
    print(f'Cat: {cat_points}')
    print(f'Fish: {fish_points}')
    print(f'Rat: {rat_points}')
    print(f'Rabbit: {rabbit_points}')

    # Print the empty line
    print()

    # When new_best_fits is empty (no results), change the button text to "No results, try again!"
    if len(best_pet_fits) == 0:
        button_find_a_pet.config(text="No results, try again!")

    # Update pet finder title and button, then hide pet finder (questions) window and show results window
    else:
        # Change menu button and title text for another turn
        button_find_a_pet.config(text="Find a pet!")
        pet_finder_title.config(text="Wanna try again? Your last answers:")
        # Hide pet finder window
        hide_pet_finder()
        # Show results window
        show_pet_finder_answers()
        # Destroy temporary results and create a new ones (to clear the previous results)
        pet_finder_temporary_results.destroy()
        pet_finder_temporary_results_scrollbar.destroy()
        # Create a canvas to hold the new temporary results
        pet_finder_temporary_results = Canvas(pet_finder_answers)
        pet_finder_temporary_results.pack(side=LEFT, fill=BOTH, expand=True)
        # Create a scrollbar for the canvas
        pet_finder_temporary_results_scrollbar = Scrollbar(pet_finder_answers,
                                                           command=pet_finder_temporary_results.yview)
        pet_finder_temporary_results_scrollbar.pack(side=RIGHT, fill=Y)
        # Configure the canvas to use the scrollbar
        pet_finder_temporary_results.configure(yscrollcommand=pet_finder_temporary_results_scrollbar.set)

        # Create a frame to hold the labels
        results1_frame = Frame(pet_finder_temporary_results, bg="white")
        results1_frame.pack(fill=X)

        # Create a label for the title
        Label(results1_frame, text="Take a look!", bg="white", fg="#505d75", pady=10, font=("Helvetica", 16)).pack(
            fill=X, expand=True)

        # Go through the new best fits list and add the results to the frame
        for _ in best_pet_fits:

            # Create a label for the name and add it to the frame
            Label(results1_frame, text=f"{_}", bg="#d8dbe1", fg="#505d75", width=52, font=("Helvetica", 12)).pack(
                fill=X)
            # Create an empty label to separate the name and description
            Label(results1_frame, bg="white", font=("Helvetica", 12)).pack(fill=X)

            # Assign description to the pets

            # Dog
            if _ == Dog.__name__:
                Label(results1_frame, text=Dog.general_description,
                      fg="#505d75", width=52, wraplength=450, font=("Helvetica", 10)).pack(fill=X)
            # Cat
            elif _ == Cat.__name__:
                Label(results1_frame, text=Cat.general_description,
                      fg="#505d75", width=52, font=("Helvetica", 10), wraplength=450).pack(fill=X)
            # Fish
            elif _ == Fish.__name__:
                Label(results1_frame, text=Fish.general_description,
                      fg="#505d75", width=52, font=("Helvetica", 10), wraplength=450).pack(fill=X)
            # Rat
            elif _ == Rat.__name__:
                Label(results1_frame, text=Rat.general_description,
                      fg="#505d75", width=52, font=("Helvetica", 10), wraplength=450).pack(fill=X)
            # Rabbit
            elif _ == Rabbit.__name__:
                Label(results1_frame, text=Rabbit.general_description,
                      fg="#505d75", width=52, font=("Helvetica", 10), wraplength=450).pack(fill=X)

            # Create an empty label to separate the description and the next name
            Label(results1_frame, bg="white", font=("Helvetica", 12)).pack(fill=X)

        # update the canvas to fit the frame
        pet_finder_temporary_results.create_window((0, 0), window=results1_frame, anchor=NW)
        results1_frame.update_idletasks()
        pet_finder_temporary_results.config(scrollregion=pet_finder_temporary_results.bbox("all"))


# **********************************************************************************************************************
# GUI starts here:

# Create a window and set its size
root = Tk()
# Set the size of the window
root.geometry("490x630")
# Change icon
icon = PhotoImage(file="Logo/Logo_Icon_2.ico")
root.iconphoto(True, icon)
# Set the window to be non-resizable
root.resizable(False, False)
# Title
root.title("YourBestPet")

# Title strip ----------------------------------------------------------------------------------------------------------

# Create a strip for the title
title = Label(root, bg="#505d75", height=2)
title.pack(fill=X)
# Add picture to the title strip and resize it, so it fits the strip
logo = ImageTk.PhotoImage(Image.open("Logo/Logo_Title.png").resize((250, 50)))
Label(title, image=logo, bg="#505d75").pack(side=BOTTOM)

# Main section (used for all pages) ------------------------------------------------------------------------------------

# Create a canvas for the main section
middle_space = Canvas(root)
middle_space.pack(fill=BOTH, expand=True, side=TOP)

# Welcome message ------------------------------------------------------------------------------------------------------

# Create a frame for the welcome message and add it to the canvas
welcome_message = Label(middle_space, wraplength=450,
                        text="Welcome to our pet selection and care app! \n\nAre you considering getting a furry "
                             "friend but dont know which \n "
                             "one to choose? Or perhaps you already have a pet but want to learn more about how to "
                             "provide the best care "
                             "possible? \n\nLook no further - our app is here to help!\n\n With our app, you will "
                             "have access to a wealth of "
                             "information about pet care, from nutrition and exercise to grooming and health. \n\nBut "
                             "that's not all - we "
                             "also offer a fun and interactive quiz that will help you find the perfect pet for you "
                             "based on your "
                             "preferences and lifestyle. \n\nAnd dont worry about getting lost in the app - all of "
                             "the options are "
                             "conveniently located at the bottom of the screen, so you can easily navigate between "
                             "the different "
                             "sections.", fg="#505d75", font=("Helvetica", 12))
welcome_message.pack(fill=X, expand=True)
welcome_message_opened = True

# Dog Finder -----------------------------------------------------------------------------------------------------------

# Create a canvas widget
dog_finder = Canvas(middle_space, bg="white")
dog_finder.pack(side=LEFT, fill=BOTH, expand=True)

# Create a title
dog_finder_title = Label(dog_finder, text="Please answer the questions:", bg="white", fg="#505d75", pady=10,
                         font=("Helvetica", 16))
dog_finder_title.pack(fill=X)

# First question
Label(dog_finder, text=f"{questions_cats_dogs[0]}\n", fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
answers1_bar = Label(dog_finder)
answers1_bar.pack(fill=X)
button_dog_1a = Button(answers1_bar, width=10, text="Flat", bg="#9da4b4", fg="white",
                       command=answer_first_dog_question_A,
                       font=("Helvetica", 10))
button_dog_1a.pack(side=LEFT, expand=True)
button_dog_1b = Button(answers1_bar, width=10, text="House", bg="#9da4b4", fg="white",
                       command=answer_first_dog_question_B,
                       font=("Helvetica", 10))
button_dog_1b.pack(side=LEFT, expand=True)
button_dog_1c = Button(answers1_bar, width=10, text="Big house", bg="#9da4b4", fg="white",
                       command=answer_first_dog_question_C,
                       font=("Helvetica", 10))
button_dog_1c.pack(side=LEFT, expand=True)
Label(dog_finder, bg="white").pack()

# Second question
Label(dog_finder, text=f"{questions_cats_dogs[1]}\n", fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
answers2_bar = Label(dog_finder)
answers2_bar.pack(fill=X)
button_dog_2a = Button(answers2_bar, width=10, text="1 or less", bg="#9da4b4", fg="white",
                       command=answer_second_dog_question_A,
                       font=("Helvetica", 10))
button_dog_2a.pack(side=LEFT, expand=True)
button_dog_2b = Button(answers2_bar, width=10, text="2-3 hours", bg="#9da4b4", fg="white",
                       command=answer_second_dog_question_B,
                       font=("Helvetica", 10))
button_dog_2b.pack(side=LEFT, expand=True)
button_dog_2c = Button(answers2_bar, width=10, text="3 and more", bg="#9da4b4", fg="white",
                       command=answer_second_dog_question_C, font=("Helvetica", 10))
button_dog_2c.pack(side=LEFT, expand=True)
Label(dog_finder, bg="white").pack()

# Third question
Label(dog_finder, text=f"{questions_cats_dogs[2]}\n", fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
answers3_bar = Label(dog_finder)
answers3_bar.pack(fill=X)
button_dog_3a = Button(answers3_bar, width=10, text="£40 - £70", bg="#9da4b4", fg="white",
                       command=answer_third_dog_question_A,
                       font=("Helvetica", 10))
button_dog_3a.pack(side=LEFT, expand=True)
button_dog_3b = Button(answers3_bar, width=10, text="£70 - £100", bg="#9da4b4", fg="white",
                       command=answer_third_dog_question_B,
                       font=("Helvetica", 10))
button_dog_3b.pack(side=LEFT, expand=True)
button_dog_3c = Button(answers3_bar, width=10, text="£100 - £150", bg="#9da4b4", fg="white",
                       command=answer_third_dog_question_C, font=("Helvetica", 10))
button_dog_3c.pack(side=LEFT, expand=True)
Label(dog_finder, bg="white").pack()

# Fourth question
Label(dog_finder, text=f"{questions_cats_dogs[3]}\n", fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
answers4_bar = Label(dog_finder)
answers4_bar.pack(fill=X)
button_dog_4a = Button(answers4_bar, width=10, text="Yes", bg="#9da4b4", fg="white",
                       command=answer_fourth_dog_question_A,
                       font=("Helvetica", 10))
button_dog_4a.pack(side=LEFT, expand=True)
Label(answers4_bar, text="                          ").pack(side=LEFT, expand=True)
button_dog_4b = Button(answers4_bar, width=10, text="No", bg="#9da4b4", fg="white",
                       command=answer_fourth_dog_question_B,
                       font=("Helvetica", 10))
button_dog_4b.pack(side=LEFT, expand=True)

# Find my pet button
button_find_a_dog = Button(dog_finder, text="Find a dog!", width=20, bg="light grey", fg="white",
                           font=("Helvetica", 10))
button_find_a_dog.pack(expand=True)

# Hide dog finder at the beginning
dog_finder.pack_forget()
dog_finder_opened = False

# Dog finder answer page -----------------------------------------------------------------------------------------------

# create a canvas widget
dog_finder_answers = Canvas(middle_space)
dog_finder_answers.pack(fill=BOTH, expand=True)

# create a second widget inside with a scrollbar
dog_finder_temporary_results = Canvas(dog_finder_answers)
dog_finder_temporary_results.pack(side=LEFT, fill=BOTH, expand=True)
dog_finder_temporary_results_scrollbar = Scrollbar(dog_finder_answers, command=dog_finder_temporary_results.yview)
dog_finder_temporary_results_scrollbar.pack(side=RIGHT, fill=Y)

# Hide dog finder answer page at the beginning
dog_finder_temporary_results_scrollbar.pack_forget()
dog_finder_answers.pack_forget()
dog_finder_answers_opened = False

# Pet Finder -----------------------------------------------------------------------------------------------------------

# Create a canvas widget
pet_finder = Canvas(middle_space, bg="white")
pet_finder.pack(side=LEFT, fill=BOTH, expand=True)

# Create a title
pet_finder_title = Label(pet_finder, text="Please answer the questions:", bg="white", fg="#505d75", pady=10,
                         font=("Helvetica", 16))
pet_finder_title.pack(fill=X)

# First question
Label(pet_finder, text=f"{questions_pets[0]}\n", fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
answers1_bar = Label(pet_finder)
answers1_bar.pack(fill=X)
button_pet_1a = Button(answers1_bar, width=10, text="No time", bg="#9da4b4", fg="white",
                       command=answer_first_pet_question_A,
                       font=("Helvetica", 10))
button_pet_1a.pack(side=LEFT, expand=True)
button_pet_1b = Button(answers1_bar, width=10, text="15-20 min.", bg="#9da4b4", fg="white",
                       command=answer_first_pet_question_B,
                       font=("Helvetica", 10))
button_pet_1b.pack(side=LEFT, expand=True)
button_pet_1c = Button(answers1_bar, width=10, text="20-30 min.", bg="#9da4b4", fg="white",
                       command=answer_first_pet_question_C,
                       font=("Helvetica", 10))
button_pet_1c.pack(side=LEFT, expand=True)
button_pet_1d = Button(answers1_bar, width=10, text="30-45 min.", bg="#9da4b4", fg="white",
                       command=answer_first_pet_question_D,
                       font=("Helvetica", 10))
button_pet_1d.pack(side=LEFT, expand=True)
button_pet_1e = Button(answers1_bar, width=10, text="An hour", bg="#9da4b4", fg="white",
                       command=answer_first_pet_question_E,
                       font=("Helvetica", 10))
button_pet_1e.pack(side=LEFT, expand=True)
Label(pet_finder, bg="white").pack()

# Second question
Label(pet_finder, text=f"{questions_pets[1]}\n", fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
answers2_bar = Label(pet_finder)
answers2_bar.pack(fill=X)
button_pet_2a = Button(answers2_bar, width=10, text="It's a must!", bg="#9da4b4", fg="white",
                       command=answer_second_pet_question_A,
                       font=("Helvetica", 10))
button_pet_2a.pack(side=LEFT, expand=True)
button_pet_2b = Button(answers2_bar, width=10, text="So-so", bg="#9da4b4", fg="white",
                       command=answer_second_pet_question_B,
                       font=("Helvetica", 10))
button_pet_2b.pack(side=LEFT, expand=True)
button_pet_2c = Button(answers2_bar, width=10, text="Not important", bg="#9da4b4", fg="white",
                       command=answer_second_pet_question_C, font=("Helvetica", 10))
button_pet_2c.pack(side=LEFT, expand=True)
Label(pet_finder, bg="white").pack()

# Third question
Label(pet_finder, text=f"{questions_pets[2]}\n", fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
answers3_bar = Label(pet_finder)
answers3_bar.pack(fill=X)
button_pet_3a = Button(answers3_bar, width=10, text="House/Flat", bg="#9da4b4", fg="white",
                       command=answer_third_pet_question_A,
                       font=("Helvetica", 10))
button_pet_3a.pack(side=LEFT, expand=True)
button_pet_3b = Button(answers3_bar, width=10, text="House & yard", bg="#9da4b4", fg="white",
                       command=answer_third_pet_question_B,
                       font=("Helvetica", 10))
button_pet_3b.pack(side=LEFT, expand=True)
button_pet_3c = Button(answers3_bar, width=10, text="Small space", bg="#9da4b4", fg="white",
                       command=answer_third_pet_question_C, font=("Helvetica", 10))
button_pet_3c.pack(side=LEFT, expand=True)
button_pet_3d = Button(answers3_bar, width=10, text="Large cage", bg="#9da4b4", fg="white",
                       command=answer_third_pet_question_D, font=("Helvetica", 10))
button_pet_3d.pack(side=LEFT, expand=True)
button_pet_3e = Button(answers3_bar, width=10, text="Cage & yard", bg="#9da4b4", fg="white",
                       command=answer_third_pet_question_E, font=("Helvetica", 10))
button_pet_3e.pack(side=LEFT, expand=True)
Label(pet_finder, bg="white").pack()

# Fourth question
Label(pet_finder, text=f"{questions_pets[3]}\n", fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
answers4_bar = Label(pet_finder)
answers4_bar.pack(fill=X)
button_pet_4a = Button(answers4_bar, width=10, text="Daily", bg="#9da4b4", fg="white",
                       command=answer_fourth_pet_question_A,
                       font=("Helvetica", 10))
button_pet_4a.pack(side=LEFT, expand=True)
button_pet_4b = Button(answers4_bar, width=10, text="Weekly", bg="#9da4b4", fg="white",
                       command=answer_fourth_pet_question_B,
                       font=("Helvetica", 10))
button_pet_4b.pack(side=LEFT, expand=True)
Label(pet_finder, bg="white").pack()

# Fifth question
Label(pet_finder, text=f"{questions_pets[4]}\n", fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
answers5_bar = Label(pet_finder)
answers5_bar.pack(fill=X)
button_pet_5a = Button(answers5_bar, width=10, text="Daily", bg="#9da4b4", fg="white",
                       command=answer_fifth_pet_question_A,
                       font=("Helvetica", 10))
button_pet_5a.pack(side=LEFT, expand=True)
button_pet_5b = Button(answers5_bar, width=10, text="Weekly", bg="#9da4b4", fg="white",
                       command=answer_fifth_pet_question_B,
                       font=("Helvetica", 10))
button_pet_5b.pack(side=LEFT, expand=True)
button_pet_5c = Button(answers5_bar, width=10, text="Minimal", bg="#9da4b4", fg="white",
                       command=answer_fifth_pet_question_C, font=("Helvetica", 10))
button_pet_5c.pack(side=LEFT, expand=True)

# Find my pet button
button_find_a_pet = Button(pet_finder, text="Find a pet!", width=20, bg="light grey", fg="white",
                           font=("Helvetica", 10))
button_find_a_pet.pack(expand=True)

# Hide pet finder at the beginning
pet_finder.pack_forget()
pet_finder_opened = False

# Pet finder answer page -----------------------------------------------------------------------------------------------

# create a canvas widget
pet_finder_answers = Canvas(middle_space)
pet_finder_answers.pack(fill=BOTH, expand=True)

# create a second widget inside with a scrollbar
pet_finder_temporary_results = Canvas(pet_finder_answers)
pet_finder_temporary_results.pack(side=LEFT, fill=BOTH, expand=True)
pet_finder_temporary_results_scrollbar = Scrollbar(pet_finder_answers, command=pet_finder_temporary_results.yview)
pet_finder_temporary_results_scrollbar.pack(side=RIGHT, fill=Y)

# Hide pet finder answer page at the beginning
pet_finder_temporary_results_scrollbar.pack_forget()
pet_finder_answers.pack_forget()
pet_finder_answers_opened = False

# Cat Finder -----------------------------------------------------------------------------------------------------------

# Create a canvas widget
cat_finder = Canvas(middle_space, bg="white")
cat_finder.pack(side=LEFT, fill=BOTH, expand=True)

# Create a title
cat_finder_title = Label(cat_finder, text="Please answer the questions:", bg="white", fg="#505d75", pady=10,
                         font=("Helvetica", 16))
cat_finder_title.pack(fill=X)

# First question
Label(cat_finder, text=f"{questions_cats_dogs[0]}\n", fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
answers1_bar = Label(cat_finder)
answers1_bar.pack(fill=X)
button_cat_1a = Button(answers1_bar, width=10, text="Flat", bg="#9da4b4", fg="white",
                       command=answer_first_cat_question_A,
                       font=("Helvetica", 10))
button_cat_1a.pack(side=LEFT, expand=True)
button_cat_1b = Button(answers1_bar, width=10, text="House", bg="#9da4b4", fg="white",
                       command=answer_first_cat_question_B,
                       font=("Helvetica", 10))
button_cat_1b.pack(side=LEFT, expand=True)
button_cat_1c = Button(answers1_bar, width=10, text="Big house", bg="#9da4b4", fg="white",
                       command=answer_first_cat_question_C,
                       font=("Helvetica", 10))
button_cat_1c.pack(side=LEFT, expand=True)
Label(cat_finder, bg="white").pack()

# Second question
Label(cat_finder, text=f"{questions_cats_dogs[1]}\n", fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
answers2_bar = Label(cat_finder)
answers2_bar.pack(fill=X)
button_cat_2a = Button(answers2_bar, width=10, text="1 or less", bg="#9da4b4", fg="white",
                       command=answer_second_cat_question_A,
                       font=("Helvetica", 10))
button_cat_2a.pack(side=LEFT, expand=True)
button_cat_2b = Button(answers2_bar, width=10, text="2-3 hours", bg="#9da4b4", fg="white",
                       command=answer_second_cat_question_B,
                       font=("Helvetica", 10))
button_cat_2b.pack(side=LEFT, expand=True)
button_cat_2c = Button(answers2_bar, width=10, text="3 and more", bg="#9da4b4", fg="white",
                       command=answer_second_cat_question_C, font=("Helvetica", 10))
button_cat_2c.pack(side=LEFT, expand=True)
Label(cat_finder, bg="white").pack()

# Third question
Label(cat_finder, text=f"{questions_cats_dogs[2]}\n", fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
answers3_bar = Label(cat_finder)
answers3_bar.pack(fill=X)
button_cat_3a = Button(answers3_bar, width=10, text="£40 - £70", bg="#9da4b4", fg="white",
                       command=answer_third_cat_question_A,
                       font=("Helvetica", 10))
button_cat_3a.pack(side=LEFT, expand=True)
button_cat_3b = Button(answers3_bar, width=10, text="£70 - £100", bg="#9da4b4", fg="white",
                       command=answer_third_cat_question_B,
                       font=("Helvetica", 10))
button_cat_3b.pack(side=LEFT, expand=True)
button_cat_3c = Button(answers3_bar, width=10, text="£100 - £150", bg="#9da4b4", fg="white",
                       command=answer_third_cat_question_C, font=("Helvetica", 10))
button_cat_3c.pack(side=LEFT, expand=True)
Label(cat_finder, bg="white").pack()

# Fourth question
Label(cat_finder, text=f"{questions_cats_dogs[3]}\n", fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
answers4_bar = Label(cat_finder)
answers4_bar.pack(fill=X)
button_cat_4a = Button(answers4_bar, width=10, text="Yes", bg="#9da4b4", fg="white",
                       command=answer_fourth_cat_question_A,
                       font=("Helvetica", 10))
button_cat_4a.pack(side=LEFT, expand=True)
Label(answers4_bar, text="                          ").pack(side=LEFT, expand=True)
button_cat_4b = Button(answers4_bar, width=10, text="No", bg="#9da4b4", fg="white",
                       command=answer_fourth_cat_question_B,
                       font=("Helvetica", 10))
button_cat_4b.pack(side=LEFT, expand=True)

# Find my pet button
button_find_a_cat = Button(cat_finder, text="Find a cat!", width=20, bg="light grey", fg="white",
                           font=("Helvetica", 10))
button_find_a_cat.pack(expand=True)

# Hide cat finder at the beginning
cat_finder.pack_forget()
cat_finder_opened = False

# Cat finder answer page -----------------------------------------------------------------------------------------------

# create a canvas widget
cat_finder_answers = Canvas(middle_space)
cat_finder_answers.pack(fill=BOTH, expand=True)

# create a second widget inside with a scrollbar
cat_finder_temporary_results = Canvas(cat_finder_answers)
cat_finder_temporary_results.pack(side=LEFT, fill=BOTH, expand=True)
cat_finder_temporary_results_scrollbar = Scrollbar(cat_finder_answers, command=cat_finder_temporary_results.yview)
cat_finder_temporary_results_scrollbar.pack(side=RIGHT, fill=Y)

# Hide cat finder answer page at the beginning
cat_finder_temporary_results_scrollbar.pack_forget()
cat_finder_answers.pack_forget()
cat_finder_answers_opened = False

# Petbook --------------------------------------------------------------------------------------------------------------

# Create a canvas widget
petbook = Canvas(middle_space)
petbook.pack(side=LEFT, fill=BOTH, expand=True)

# Add a scrollbar to the canvas
petbook_scrollbar = Scrollbar(middle_space, command=petbook.yview)
petbook_scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas to use the scrollbar
petbook.configure(yscrollcommand=petbook_scrollbar.set)

# Create a frame inside the canvas with all dogs name and info
frame = Frame(petbook, bg="white")
frame.pack(fill=X)

# Print "Dogs" title
Label(frame, text="Dogs", bg="white", fg="#505d75", pady=10, font=("Helvetica", 16)).pack(fill=X, expand=True)
# Add all dogs name and info to the frame
for dog in dogs:
    # Load the image and resize it
    img = Image.open(dog.pic)
    img = img.resize((130, 130), Image.LANCZOS)

    # Convert the image to a tkinter-compatible format
    img_tk = ImageTk.PhotoImage(img)
    Label(frame, width=67).pack()
    # Create a label for the image and add it to the frame
    img_label = Label(frame, image=img_tk)
    img_label.image = img_tk
    img_label.pack(fill=X)

    # Create a label for the dog name and info, then add it to the frame
    Label(frame, text=dog.name, fg="#505d75", font=("Helvetica", 12)).pack(fill=X)
    Label(frame, text=dog.info, fg="#505d75", font=("Helvetica", 10), wraplength=450).pack(fill=X)

    # Add a line between each dog
    Label(frame, bg="white").pack()

    # For last dog, delete the line at the end
    if dog == dogs[-1]:
        Label(frame, bg="white", width=67).pack()

# Print "Cats" title
Label(frame, text="Cats", bg="white", fg="#505d75", pady=10, font=("Helvetica", 16)).pack(fill=X)
# Add all cats name and info to the frame
for cat in cats:
    # Load the image and resize it
    img = Image.open(cat.pic)
    img = img.resize((130, 130), Image.LANCZOS)

    # Convert the image to a tkinter-compatible format
    img_tk = ImageTk.PhotoImage(img)
    Label(frame, width=67).pack()
    # Create a label for the image and add it to the frame
    img_label = Label(frame, image=img_tk, width=470)
    img_label.image = img_tk
    img_label.pack(fill=X)

    # Create a label for the cat name and info, then add it to the frame
    Label(frame, text=cat.name, fg="#505d75", width=52, font=("Helvetica", 12)).pack(fill=X)
    Label(frame, text=cat.info, fg="#505d75", font=("Helvetica", 10), wraplength=450).pack(fill=X)

    # Add a line between each cat
    Label(frame, bg="white").pack()

# Update the scroll region
petbook.create_window((0, 0), window=frame, anchor=NW)
frame.update_idletasks()
# Set the scroll region to the frame's dimensions
petbook.config(scrollregion=petbook.bbox("all"))

# Hide petbook at the beginning
petbook.pack_forget()
petbook_scrollbar.pack_forget()
petbook_opened = False

# Tips -----------------------------------------------------------------------------------------------------------------

# Create a canvas widget
tips = Canvas(middle_space)
tips.pack(side=LEFT, fill=BOTH, expand=True)

# Add a scrollbar to the canvas
tips_scrollbar = Scrollbar(middle_space, command=tips.yview)
tips_scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas to use the scrollbar
tips.configure(yscrollcommand=tips_scrollbar.set)

# Create a frame inside the canvas
frame = Frame(tips, bg="white")
frame.pack(fill=X)

# Print title
Label(frame, text="Tips for Pet Owners", bg="white", fg="#505d75", pady=10, font=("Helvetica", 16)).pack(fill=X,
                                                                                                         expand=True)

# Print tips
Label(frame, wraplength=470, text="\nWelcome to our guide on responsible pet ownership. As a pet owner, it's your"
                                  "responsibility to provide the best possible care for your furry friend. This"
                                  "includes providing them with proper nutrition, exercise, and medical attention,"
                                  "as well as creating a safe and loving environment for them to thrive in.\n",
      fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
Label(frame, text="\nNutrition", fg="#505d75", bg="white", width=52, font=("Helvetica", 12)).pack(fill=X)
Label(frame, wraplength=470, text="\nProper nutrition is essential for your pet's health and well-being. It's important"
                                  "to provide them with a balanced diet that meets their nutritional needs. This"
                                  "may include high-quality commercial pet food or a home-cooked diet that is"
                                  "formulated with the guidance of a veterinarian.\n",
      fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
Label(frame, text="\nExercise", fg="#505d75", bg="white", width=52, font=("Helvetica", 12)).pack(fill=X)
Label(frame, wraplength=470, text="\nJust like humans, pets need regular exercise to stay healthy and happy. Exercise"
                                  "helps keep their weight in check, strengthens their muscles and joints, and"
                                  "improves their mental well-being. Depending on your pet's breed and age, they may"
                                  "need anywhere from 30 minutes to several hours of exercise each day.\n",
      fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
Label(frame, text="\nMedical Care", fg="#505d75", bg="white", width=52, font=("Helvetica", 12)).pack(fill=X)
Label(frame, wraplength=470, text="\nRegular visits to the veterinarian are important for your pet's overall health."
                                  "This includes routine checkups, vaccinations, and preventative care. If your pet"
                                  "is sick or injured, it's important to seek medical attention as soon as possible.\n",
      fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
Label(frame, text="\nSafety", fg="#505d75", bg="white", width=52, font=("Helvetica", 12)).pack(fill=X)
Label(frame, wraplength=470, text="\nCreating a safe environment for your pet is crucial. This includes keeping"
                                  "hazardous substances out of reach, securing fences and gates, and providing them"
                                  "with proper identification, such as a collar with tags or a microchip.\n",
      fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
Label(frame, text="\nTraining", fg="#505d75", bg="white", width=52, font=("Helvetica", 12)).pack(fill=X)
Label(frame, wraplength=470, text="\nProper training can help ensure that your pet is well-behaved and a joy to be"
                                  "around. This may include basic obedience training, as well as socialization with"
                                  "other animals and people.\n",
      fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
Label(frame, text="\nAdoption", fg="#505d75", bg="white", width=52, font=("Helvetica", 12)).pack(fill=X)
Label(frame, wraplength=470, text="\nIf you're considering getting a pet, adoption is a great option. There are many"
                                  "animals in shelters and rescues that are in need of loving homes. By adopting,"
                                  "you'll be giving a pet a second chance at life and helping to reduce the number"
                                  "of animals in shelters.\n",
      fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
Label(frame, text="\nConclusion", fg="#505d75", bg="white", width=52, font=("Helvetica", 12)).pack(fill=X)
Label(frame, wraplength=470, text="\nBy following these tips and taking your role as a responsible pet owner seriously,"
                                  "you can provide your furry friend with the best possible care. Remember, pets are"
                                  "a lifelong commitment and require time, effort, and resources. But the love and joy"
                                  "they bring into our lives are priceless.\n",
      fg="#505d75", font=("Helvetica", 10)).pack(fill=X)
Label(frame, fg="#505d75", bg="white", width=52, font=("Helvetica", 12)).pack(fill=X)

# Update the canvas to fit the frame
tips.create_window((0, 0), window=frame, anchor=NW)
frame.update_idletasks()
tips.config(scrollregion=tips.bbox("all"))

# Hide the petbook at the beginning
tips.pack_forget()
tips_scrollbar.pack_forget()
tips_opened = False

# Footer ---------------------------------------------------------------------------------------------------------------

# Footer strip
footer = Label(root, height=2, bg="#505d75")
footer.pack(fill=X, side=BOTTOM)

# Button 1 Petbook
button_petbook = Button(footer, text="Petbook", bg="#9da4b4", fg="white", font=("Helvetica", 13), width=10,
                        command=open_petbook)
button_petbook.pack(side=LEFT)
# Button 2 Dog finder
button_dog_finder = Button(footer, text="Dog finder", bg="#9da4b4", fg="white", font=("Helvetica", 13), width=10,
                           command=open_dog_finder)
button_dog_finder.pack(side=LEFT)
# Button 3 Cat finder
button_cat_finder = Button(footer, text="Cat finder", bg="#9da4b4", fg="white", font=("Helvetica", 13), width=10,
                           command=open_cat_finder)
button_cat_finder.pack(side=LEFT)
# Button 4 Pet finder
button_pet_finder = Button(footer, text="Pet finder", bg="#9da4b4", fg="white", font=("Helvetica", 13), width=10,
                           command=open_pet_finder)
button_pet_finder.pack(side=LEFT)
# Button 5 Tips
button_tips = Button(footer, text="Tips", bg="#9da4b4", fg="white", font=("Helvetica", 13), width=10,
                     command=open_tips)
button_tips.pack(side=LEFT)

# **********************************************************************************************************************
# Run the main loop

root.mainloop()
