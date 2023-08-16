# Author: Radoslaw Rezler
# Date: 2023-04-14
# Description:  Program that asks user to choose a dog or a cat and then asks some questions.
#               Then it gives them a list of the best breeds based on their answers.

# Define the class for the animals
class Animal:
    def __init__(self, name, size, activity, cost, children, info):
        self.name = name
        self.size = size
        self.activity = activity
        self.cost = cost
        self.children = children
        self.info = info
        # Temporary stats based on user answers
        self.fit_reasons = []
        self.not_fit_reasons = []
        self.score = []


# Make subclass called Dog
class Dog(Animal):
    def __init__(self, name, size, activity, cost, children, info):
        super().__init__(name, size, activity, cost, children, info)


# Make subclass called Cat
class Cat(Animal):
    def __init__(self, name, size, activity, cost, children, info):
        super().__init__(name, size, activity, cost, children, info)


# Make subclass called Rabbit
class Rabbit(Animal):
    def __init__(self, name, size, activity, cost, children, info):
        super().__init__(name, size, activity, cost, children, info)


# Make subclass called Rat
class Rat(Animal):
    def __init__(self, name, size, activity, cost, children, info):
        super().__init__(name, size, activity, cost, children, info)


# Make subclass called Fish
class Fish(Animal):
    def __init__(self, name, size, activity, cost, children, info):
        super().__init__(name, size, activity, cost, children, info)


# Make a list of Dogs and give them attributes
dogs = [Dog('German Shepherd', 3, 3, 3, True,
            "This breed is known for its loyalty, intelligence, and train ability, making them great police and \n"
            "military dogs. They require plenty of exercise and mental stimulation. An interesting fact is that \n"
            "German Shepherds were originally bred to herd sheep."),
        Dog('Maltese', 1, 1, 1, False,
            "These dogs are known for their small size and gentle nature. They are great lap dogs and are very \n"
            "affectionate with their owners. They do require regular grooming to keep their long, white coat looking \n"
            "its best. An interesting fact is that Maltese dogs were popular with women in ancient Greece and Rome \n"
            "and were often depicted in art."),
        Dog('French Bulldog', 2, 2, 3, True,
            "This breed is characterized by its unique appearance, with a short, stocky body and large, \n"
            "bat-like ears. They are affectionate and playful but can be stubborn when it comes to training. French \n"
            "Bulldogs are prone to breathing problems due to their short snouts. An interesting fact is that French \n"
            "Bulldogs were originally bred in England as miniature Bulldogs."),
        Dog('Miniature Schnauzer', 1, 2, 2, True,
            "These dogs are known for their alertness and intelligence. They are affectionate with their owners and \n"
            "do well in families with children. They do require regular grooming to maintain their distinctive, \n"
            "wiry coat. An interesting fact is that Miniature Schnauzers were originally bred in Germany to catch \n"
            "rats and guard homes."),
        Dog('American Pit Bull Terrier', 3, 3, 2, True,
            "This breed is often misunderstood due to its reputation for aggression, but when raised and trained \n"
            "properly, they can make loyal and affectionate family pets. They are highly energetic and require plenty \n"
            "of exercise. An interesting fact is that Pit Bulls were originally bred for bull-baiting and \n"
            "bear-baiting, but their breed was later refined to be a loyal companion dog."),
        Dog('Labrador Retriever', 3, 3, 3, True,
            "This breed is known for its friendly and outgoing nature. They are intelligent and easy to train, \n"
            "which makes them popular as guide dogs and search and rescue dogs. They require plenty of exercise and \n"
            "love to swim. An interesting fact is that Labrador Retrievers were originally bred in Newfoundland to \n"
            "retrieve fish for fishermen."),
        Dog('Chihuahua', 1, 1, 1, False,
            "These dogs are known for their small size and big personalities. They can be very loyal and affectionate \n"
            "with their owners but may be nervous around strangers. They do not require a lot of exercise but may \n"
            "need a sweater in cold weather due to their small size. An interesting fact is that Chihuahuas are \n"
            "believed to have originated in Mexico and were named after the state of Chihuahua."),
        Dog('Saint Bernard', 3, 1, 3, True,
            "This breed is known for its size and strength. They are gentle giants and make great family pets. They \n"
            "do require plenty of exercise and space due to their large size. An interesting fact is that Saint \n"
            "Bernards were originally bred in Switzerland to rescue lost and injured travelers in the Alps."),
        Dog('Shih Tzu', 1, 1, 1, False,
            "These dogs are known for their long, flowing coat and affectionate nature. They make great lap dogs and \n"
            "are good with children. They do require regular grooming to maintain their coat. An interesting fact is \n"
            "that Shih Tzus were originally bred in China and were considered a sacred breed."),
        Dog('Beagle', 2, 2, 2, True,
            "This breed is known for its excellent sense of smell, which makes them popular as hunting dogs. They are \n"
            "friendly and outgoing, making them great family pets. They require plenty of exercise and can be prone \n"
            "to obesity if not properly exercised. An interesting fact is that Beagles were originally bred in \n"
            "England to hunt rabbits."),
        Dog('Siberian Husky', 3, 3, 3, True,
            "These dogs are known for their endurance and their ability to thrive in cold weather. They are \n"
            "intelligent and independent, which can make them difficult to train. They require plenty of exercise and \n"
            "love to run, so they are a great fit for active owners. An interesting fact is that Siberian Huskies \n"
            "were originally bred in Siberia by the Chukchi people to pull sleds across long distances."),
        Dog('Boxer', 3, 3, 3, True,
            "This breed is known for its athleticism and playfulness. They are loyal and protective of their families \n"
            "and do well with children. They require plenty of exercise and mental stimulation. An interesting fact \n"
            "is that Boxers were originally bred in Germany to be hunting dogs, but they later became popular as \n"
            "guard dogs and family pets."),
        Dog('Poodle', 2, 1, 3, False,
            "This breed is known for its distinctive coat and intelligence. They come in three sizes (toy, miniature, \n"
            "and standard) and are popular as show dogs. They require regular grooming to maintain their coat. \n"
            "Poodles are highly trainable and make great companions. An interesting fact is that Poodles were \n"
            "originally bred in Germany to be water retrievers."),
        Dog('Border Collie', 2, 3, 2, True,
            "This breed is known for its intelligence and herding ability. They are highly trainable and excel at \n"
            "activities like agility and obedience. They require plenty of exercise and mental stimulation. Border \n"
            "Collies do well with active owners who can provide them with a job to do. An interesting fact is that \n"
            "Border Collies were originally bred in Scotland and England to work on farms herding sheep."),
        Dog('Bull Terrier', 2, 3, 2, True,
            "This breed is known for its distinctive egg-shaped head and muscular body. They are loyal and protective \n"
            "of their families and do well with children. They require plenty of exercise and mental stimulation. \n"
            "Bull Terriers are highly trainable and excel at activities like obedience and agility. An interesting \n"
            "fact is that Bull Terriers were originally bred in England for blood sports like bull-baiting and \n"
            "dog-fighting, but their breed was later refined to be a loyal companion dog.")]

# Make a list of Cats and give them attributes
cats = [Cat('Siamese', 2, 3, 3, False,
            "This breed is known for its distinctive blue eyes and vocal nature. They are highly intelligent and can \n"
            "be very playful. They require plenty of exercise and mental stimulation. An interesting fact is that \n"
            "Siamese cats were originally bred in Thailand to be companions for Buddhist monks."),
        Cat('Persian', 2, 1, 3, True,
            "This breed is known for its long, luxurious coat and laid-back personality. They are affectionate and do \n"
            "well in quiet households. They require daily grooming to keep their coat from matting. An interesting \n"
            "fact is that Persian cats were first introduced to Europe in the 17th century by Italian traders."),
        Cat('Bengal', 2, 3, 3, False,
            "These cats are known for their wild-looking coat, which comes from their Asian leopard cat ancestry. \n"
            "They are energetic and require plenty of playtime and stimulation. They can be trained to walk on a \n"
            "leash and even play fetch. An interesting fact is that Bengals are one of the few cat breeds that enjoy \n"
            "water and may even join their owners in the shower."),
        Cat('Sphynx', 1, 1, 2, False,
            "This breed is known for its unique hairlessness, which requires regular bathing to maintain. They are \n"
            "friendly and enjoy being around people. Sphynx cats are also prone to certain health issues, \n"
            "such as skin problems and respiratory issues, due to their lack of fur. An interesting fact is that the \n"
            "Sphynx breed originated in Canada in the 1960s when a hairless kitten was born to a regular cat."),
        Cat('Scottish Fold', 1, 1, 3, True,
            "This breed is known for its distinctive folded ears and playful personality. They are affectionate and \n"
            "enjoy being around people. Scottish Folds are also prone to certain health issues, such as arthritis and \n"
            "ear infections, due to their folded ears. An interesting fact is that the Scottish Fold breed originated \n"
            "in Scotland in the 1960s from a barn cat with folded ears."),
        Cat('Norwegian Forest Cat', 3, 2, 2, True,
            "These cats are known for their thick, fluffy coat and love of climbing. They are independent but \n"
            "affectionate with their families. They require regular grooming to maintain their coat. An interesting \n"
            "fact is that Norwegian Forest Cats are believed to have been the companions of Vikings and may have \n"
            "traveled with them on their voyages."),
        Cat('Russian Blue', 2, 2, 2, False,
            "This breed is known for its beautiful silver-blue coat and reserved nature. They are intelligent and \n"
            "enjoy playing games. Russian Blues are also prone to certain health issues, such as obesity and dental \n"
            "problems. An interesting fact is that Russian Blue cats were first introduced to Europe in the 1860s \n"
            "from Archangel, a port city in northern Russia."),
        Cat('Maine Coon', 3, 1, 3, True,
            "These cats are known for their large size and friendly personality. They are affectionate with their \n"
            "families and often enjoy playing with water. Maine Coons require regular grooming to maintain their \n"
            "long, silky coat. An interesting fact is that Maine Coons are believed to be the descendants of cats \n"
            "that traveled to America on ships with early European settlers."),
        Cat('British Shorthair', 2, 1, 2, True,
            "This breed is known for its round face and plush coat. They are easygoing and do well in families with \n"
            "children and other pets. British Shorthairs require regular grooming to maintain their coat. An \n"
            "interesting fact is that British Shorthairs were used during World War II to help control the rat \n"
            "population in London."),
        Cat('Egyptian Mau', 2, 3, 3, False,
            "These cats are known for their distinctive spots and love of playtime. They are intelligent and require \n"
            "plenty of stimulation. Egyptian Maus are also prone to certain health issues, such as dental problems \n"
            "and heart disease. An interesting fact is that Egyptian Maus are one of the oldest domesticated cat \n"
            "breeds and were worshiped in ancient Egypt."),
        Cat('American Shorthair', 2, 2, 1, True,
            "This breed is one of the most popular in the United States. They are known for their friendly and \n"
            "easygoing personalities. American Shorthairs were once used to help control rodent populations on farms \n"
            "and ships. Interesting fact: One American Shorthair named Creme Puff holds the record for being the \n"
            "oldest cat ever, living to be 38 years old."),
        Cat('Ragdoll', 3, 1, 3, True,
            "This breed is named for their tendency to go limp when picked up, similar to a ragdoll toy. They are \n"
            "large, gentle, and have a very calm demeanor. Ragdolls were originally bred in California in the 1960s. \n"
            "Interesting fact: Ragdolls are one of the few cat breeds that have blue eyes."),
        Cat('Himalayan', 2, 1, 3, True,
            "This breed is a cross between the Persian and the Siamese, resulting in a cat with a striking appearance \n"
            "and a calm personality. Himalayans are also known for their vocalizations, which they use to communicate \n"
            "with their owners. Interesting fact: The Himalayan is also known as the Colorpoint Persian in some \n"
            "countries."),
        Cat('Bombay', 2, 3, 2, False,
            "This breed is named after the city of Bombay (now Mumbai) in India. They are a black, muscular, \n"
            "and intelligent breed that is known for their dog-like personalities. Bombays were first bred in the \n"
            "1950s in Kentucky. Interesting fact: Some Bombay cats have a unique copper eyes trait, where their eyes \n"
            "are a bright gold color."),
        Cat('Devon Rex', 1, 3, 2, False,
            "This breed has a distinctive curly coat and large ears. They are known for being playful and \n"
            "affectionate, and they often form strong bonds with their owners. Devon Rex cats were first bred in \n"
            "England in the 1960s. Interesting fact: Devon Rex cats are sometimes referred to as poodle cats due to \n"
            "their curly fur")]

# Define the questions
questions = ['How big is your house? (1 - 3): ',
             'How many hours a day will you be able to spend with your pet? (1 - 3): ',
             'How much money are you willing to spend on your pet? (1 - 3): ',
             'Do you have children? (1 for yes, 2 for no): ']

# Create a list of answers
answers = []

# Create a list of best fits
best_fits = []


# Get answers
def get_answers():
    for q in questions:
        answer = int(input(q))
        answers.append(answer)


# Find the best pets
def find_pets(pets):
    best_score = 0

    for pet in pets:
        # Resets pets temporary stats
        pet.fit_reasons = []
        pet.not_fit_reasons = []
        pet.score = 0

        # Check if the size is a fit
        if answers[0] == pet.size:
            pet.score += 2
            pet.fit_reasons.append(f'Question: {questions[0]}\nYour answer: {answers[0]} is perfect.\n'
                                   f'Your answer matches the ideal size for this pet. Choosing the right size of pet \n'
                                   f'is important because it can affect your lifestyle and living conditions. This \n'
                                   f'pet should fit well in your home and be easy for you to care for.\n')
        else:
            diff = abs(answers[0] - pet.size)
            if answers[0] < pet.size:
                if diff == 1:
                    pet.score += 1
                    pet.not_fit_reasons.append(f'Question: {questions[0]}\nYour answer: {answers[0]} is lower.\n'
                                               f'Your answer indicates that you may prefer a smaller pet. Keep in \n'
                                               f'mind that smaller pets may be better suited for smaller living \n'
                                               f'spaces, but they may also require more frequent exercise to keep \n'
                                               f'them healthy. Consider the size and activity level of this pet \n'
                                               f'before making a decision.\n')
                else:
                    pet.not_fit_reasons.append(f'Question: {questions[0]}\nYour answer: {answers[0]} is a much lower.\n'
                                               f'Your answer suggests that you may be looking for a much smaller pet. \n'
                                               f'Keep in mind that some smaller pets may still require a lot of \n'
                                               f'exercise or have specific care requirements, so make sure you \n'
                                               f'research the pet thoroughly before making a decision.\n')

                if diff == 1:
                    pet.score += 2
                    pet.fit_reasons.append(f'Question: {questions[0]}\nYour answer: {answers[0]} is higher.\n'
                                           f'Your answer for size is higher than the ideal size for this pet, \n'
                                           f'which can be a good thing if you have a bigger living space or are \n'
                                           f'looking for a pet that requires more exercise.\n')
                else:
                    pet.score += 2
                    pet.fit_reasons.append(f'Question: {questions[0]}\nYour answer: {answers[0]} is much higher.\n'
                                           f'Your answer suggests that you have a significantly larger living space \n'
                                           f'than what is required for this pet. While some may see this as a \n'
                                           f'disadvantage, having extra space can actually be beneficial for your \n'
                                           f'pets overall well-being. A larger living space can provide your pet with \n'
                                           f'more room to move and explore, which can help reduce stress and boredom. \n'
                                           f'Additionally, having a larger living space can also provide \n'
                                           f'opportunities for you to add more pets to your household in the \n'
                                           f'future.\n')

        # Check if the activity level is a fit
        if answers[1] == pet.activity:
            pet.score += 2
            pet.fit_reasons.append(f'Question: {questions[1]}\nYour answer: {answers[1]} is perfect.\n'
                                   f'Your answer matches the ideal activity level for this pet. This pet should be a \n'
                                   f'good match for your lifestyle and energy levels, allowing you to provide for its \n'
                                   f'needs without feeling overwhelmed or unfulfilled. Keep in mind that the activity \n'
                                   f'level of a pet can affect not only its own well-being, but also its \n'
                                   f'compatibility with your own lifestyle and living situation.\n')
        else:
            diff = abs(answers[1] - pet.activity)
            if answers[1] < pet.activity:
                if diff == 1:
                    pet.score += 1
                    pet.not_fit_reasons.append(f'Question: {questions[1]}\nYour answer: {answers[1]} is lower.\n'
                                               f'Your answer suggests that you may prefer a pet with a lower activity \n'
                                               f'level. While this may be a good fit for your lifestyle, keep in mind \n'
                                               f'that some pets may require more exercise and stimulation than others \n'
                                               f'to stay healthy and happy. Make sure that you are able to provide \n'
                                               f'for your pets needs without compromising its health or well-being.\n')
                else:
                    pet.not_fit_reasons.append(f'Question: {questions[1]}\nYour answer: {answers[1]} is a much lower.\n'
                                               f'Your answer suggests that you may be looking for a pet with a \n'
                                               f'significantly lower activity level than what is recommended. While \n'
                                               f'this may be a good fit for your lifestyle, keep in mind that some \n'
                                               f'pets may become lethargic or develop health issues if they are not \n'
                                               f'given enough exercise and stimulation.\n')
            else:
                if diff == 1:
                    pet.score += 1
                    pet.not_fit_reasons.append(f'Question: {questions[1]}\nYour answer: {answers[1]} is higher.\n'
                                               f'It means you are looking for a pet that is more active. Having a pet \n'
                                               f'with higher activity level can be great for your physical and mental \n'
                                               f'health, as it can motivate you to be more active and engage in more \n'
                                               f'physical activities with your pet. It can also help you bond with \n'
                                               f'your pet more and strengthen your relationship.\n')
                else:
                    pet.not_fit_reasons.append(f'Question: {questions[1]}\nYour answer: {answers[1]} is much higher.\n'
                                               f'It suggests that you are looking for a pet that is very active and \n'
                                               f'energetic. While this can be a great match for someone who enjoys an \n'
                                               f'active lifestyle and can dedicate a lot of time to exercising with \n'
                                               f'their pet, it is important to consider if you are able to meet the \n'
                                               f'high energy demands of such a pet. You also need to make sure that \n'
                                               f'you provide enough mental and physical stimulation for your pet to \n'
                                               f'prevent boredom and destructive behavior.\n')

        # Check if the cost is a fit
        if answers[2] == pet.cost:
            pet.score += 2
            pet.fit_reasons.append(f'Question: {questions[2]}\nYour answer: {answers[2]} is perfect.\n'
                                   f'Your answer matches the ideal cost range for this pet.\n'
                                   f'This pet should be within your budget, allowing you to provide for its needs \n'
                                   f'without sacrificing your own financial stability. Keep in mind that the cost of \n'
                                   f'owning a pet goes beyond just purchasing it - you will also need to consider \n'
                                   f'ongoing expenses such as food, veterinary care, and grooming.\n')
        else:
            diff = abs(answers[2] - pet.cost)
            if answers[2] < pet.cost:
                if diff == 1:
                    pet.score += 1
                    pet.not_fit_reasons.append(f'Question: {questions[2]}\nYour answer: {answers[2]} is lower.\n'
                                               f'Your answer suggests that you may prefer a pet with a lower cost.\n'
                                               f'While this pet may fit within your budget, keep in mind that the \n'
                                               f'cost of owning a pet goes beyond just purchasing it. You will also \n'
                                               f'need to consider ongoing expenses such as food, veterinary care, \n'
                                               f'and grooming. Make sure that you are able to provide for your pets \n'
                                               f'needs without compromising its health or well-being.\n')
                else:
                    pet.not_fit_reasons.append(f'Question: {questions[2]}\nYour answer: {answers[2]} is a much lower.\n'
                                               f'Your answer suggests that you are looking for a pet with a \n'
                                               f'significantly lower cost than what is recommended. While this may be \n'
                                               f'tempting, keep in mind that pets with lower upfront costs may end up \n'
                                               f'costing more in the long run due to health issues or other \n'
                                               f'unforeseen expenses. Consider the ongoing expenses of owning a pet \n'
                                               f'and make sure that you are able to provide for your pets needs \n'
                                               f'without compromising its health or well-being.\n')
            else:
                if diff == 1:
                    pet.score += 2
                    pet.not_fit_reasons.append(f'Question: {questions[2]}\nYour answer: {answers[2]} is higher.\n'
                                               f'Your answer indicates that you may be comfortable with a higher cost \n'
                                               f'for your pet. While this may allow you to provide your pet with the \n'
                                               f'best possible care, keep in mind that higher costs do not \n'
                                               f'necessarily guarantee better quality. Make sure to do your research \n'
                                               f'and choose a pet that fits within your budget while also providing \n'
                                               f'the level of care and attention that you are comfortable with.\n')
                else:
                    pet.score += 2
                    pet.not_fit_reasons.append(f'Question: {questions[2]}\nYour answer: {answers[2]} is much higher.\n'
                                               f'Your answer suggests that you may be looking for a pet with a \n'
                                               f'significantly higher cost than what is recommended. While this may \n'
                                               f'allow you to provide your pet with top-of-the-line care and \n'
                                               f'attention, keep in mind that there are many affordable pet options \n'
                                               f'that can also be wonderful companions.\n')

        # Add the pet to the best fits list and update the best score
        if pet.score >= best_score:
            best_score = pet.score
            best_fits.append(pet)

        # Remove the pet from the best fits list if it is not the best
        for fits in best_fits:
            if fits.score < best_score:
                best_fits.remove(fits)

        # Remove the pet from the best fits list if pet is not good for children
        if answers[3] == 1:
            for pet in best_fits:
                if pet.children == False:
                    best_fits.remove(pet)


# Print the best pets
def print_best_fits():
    # Print error message if no pets are a good fit
    if len(best_fits) == 0:
        print('\nThere are no pets that are a good fit for you.')

    else:
        print('\nThe best pets for you are:\n')
    for pet in best_fits:
        print(f'{pet.name}:\n')
        print('Reasons why it is a good fit:')
        for reason in pet.fit_reasons:
            print(reason)
        # Print why is not a good fit only if there are reasons
        if len(pet.not_fit_reasons) > 0:
            print('Reasons why it is not a good fit:')
            for reason in pet.not_fit_reasons:
                print(reason)
        print()


def find_breed():
    # Define the questions and corresponding answer choices
    questions = [
        "How much time are you able to dedicate to exercising your pet?\n"
        "1. Not applicable\n"
        "2. 15-20 minutes a day\n"
        "3. 20-30 minutes a day\n"
        "4. 30-45 minutes a day\n"
        "5. At least an hour a day",
        "How important is it to you that your pet is social and enjoys human interaction?\n"
        "1. Very important\n"
        "2. Moderately important\n"
        "3. Not applicable",
        "How much space do you have available for your pet to live in?\n"
        "1. Large backyard or plenty of indoor space\n"
        "2. Indoor living with occasional outdoor access\n"
        "3. Small space\n"
        "4. Large cage or designated indoor space\n"
        "5. Large cage or designated indoor space with occasional outdoor access",
        "How often are you willing to clean your pet's living space?\n"
        "1. Once a week or more\n"
        "2. Once a week or less",
        "How much time are you willing to spend on grooming and maintenance?\n"
        "1. Daily grooming and maintenance\n"
        "2. Weekly grooming and maintenance\n"
        "3. Minimal grooming and maintenance"
    ]

    # Initialize the points for each pet to zero
    dog_points = 0
    cat_points = 0
    fish_points = 0
    rat_points = 0
    rabbit_points = 0

    # Ask each question and add points for the corresponding pet based on the user's answer
    for question in questions:
        print(question)
        answer = int(input("Answer: "))
        # First question
        if question == questions[0]:
            if answer == 1:
                fish_points += 1
            elif answer == 2:
                rat_points += 1
            elif answer == 3:
                cat_points += 1
            elif answer == 4:
                rabbit_points += 1
            elif answer == 5:
                dog_points += 1
        # Second question
        elif question == questions[1]:
            if answer == 1:
                dog_points += 1
                rat_points += 1
            elif answer == 2:
                cat_points += 1
                rabbit_points += 1
            elif answer == 3:
                fish_points += 1
        # Third question
        elif question == questions[2]:
            if answer == 1:
                dog_points += 1
            elif answer == 2:
                cat_points += 1
            elif answer == 3:
                fish_points += 1
            elif answer == 4:
                rat_points += 1
            elif answer == 5:
                rabbit_points += 1
        # Fourth question
        elif question == questions[3]:
            if answer == 1:
                dog_points += 1
                cat_points += 1
            elif answer == 2:
                fish_points += 1
                rat_points += 1
                rabbit_points += 1
        # Fifth question
        elif question == questions[4]:
            if answer == 1:
                dog_points += 1
                rabbit_points += 1
            elif answer == 2:
                cat_points += 1
                rat_points += 1
            elif answer == 3:
                fish_points += 1

    # Find the pet(s) with the most points
    max_points = max(dog_points, cat_points, fish_points, rat_points, rabbit_points)
    best_pets = []
    if dog_points == max_points:
        best_pets.append(Dog.__name__)
    if cat_points == max_points:
        best_pets.append(Cat.__name__)
    if fish_points == max_points:
        best_pets.append(Fish.__name__)
    if rat_points == max_points:
        best_pets.append(Rat.__name__)
    if rabbit_points == max_points:
        best_pets.append(Rabbit.__name__)

    # Print the best pet(s)
    if len(best_pets) == 1:
        print(f"The best pet for you is a {best_pets[0]}!")
    else:
        print("The best pets for you are:")
        for pet in best_pets:
            print(f"- {pet}")

# Print all cats and dogs (name and info)
def print_all_pets():
    print('Dogs:\n')
    for pet in dogs:
        print(f'{pet.name}:\n')
        print(pet.info)
        print()
    print('Cats:\n')
    for pet in cats:
        print(f'{pet.name}:\n')
        print(pet.info)
        print()

def print_about():
    print("Welcome to our pet selection and care app! Are you considering getting a furry friend but dont know which \n"
          "one to choose? Or perhaps you already have a pet but want to learn more about how to provide the best care \n"
          "possible? Look no further - our app is here to help! With our app, you will have access to a wealth of \n"
          "information about pet care, from nutrition and exercise to grooming and health. But thats not all - we \n"
          "also offer a fun and interactive quiz that will help you find the perfect pet for you based on your \n"
          "preferences and lifestyle. And dont worry about getting lost in the app - all of the options are \n"
          "conveniently located at the bottom of the screen, so you can easily navigate between the different \n"
          "sections. \n\n"
          "Responsible Pet Ownership: Tips and Information for Pet Owners\n\n"
          "Nutrition\n\n"
          "Proper nutrition is essential for your pet's health and wellbeing. It's important\n"
          "to provide them with a balanced diet that meets their nutritional needs. This\n"
          "may include high-quality commercial pet food or a home-cooked diet that is\n"
          "formulated with the guidance of a veterinarian.\n\n"
          "Exercise\n\n"
          "Just like humans, pets need regular exercise to stay healthy and happy. Exercise\n"
          "helps keep their weight in check, strengthens their muscles and joints, and\n"
          "improves their mental wellbeing. Depending on your pet's breed and age, they may\n"
          "need anywhere from 30 minutes to several hours of exercise each day.\n\n"
          "Medical Care\n\n"
          "Regular visits to the veterinarian are important for your pet's overall health.\n"
          "This includes routine checkups, vaccinations, and preventative care. If your pet\n"
          "is sick or injured, it's important to seek medical attention as soon as possible.\n\n"
          "Safety\n\n"
          "Creating a safe environment for your pet is crucial. This includes keeping\n"
          "hazardous substances out of reach, securing fences and gates, and providing them\n"
          "with proper identification, such as a collar with tags or a microchip.\n\n"
          "Training\n\n"
          "Proper training can help ensure that your pet is well-behaved and a joy to be\n"
          "around. This may include basic obedience training, as well as socialization with\n"
          "other animals and people.\n\n"
          "Adoption\n\n"
          "If you're considering getting a pet, adoption is a great option. There are many\n"
          "animals in shelters and rescues that are in need of loving homes. By adopting,\n"
          "you'll be giving a pet a second chance at life and helping to reduce the number\n"
          "of animals in shelters.\n\n"
          "Conclusion\n\n"
          "By following these tips and taking your role as a responsible pet owner seriously,\n"
          "you can provide your furry friend with the best possible care. Remember, pets are\n"
          "a lifelong commitment and require time, effort, and resources. But the love and joy\n"
          "they bring into our lives are priceless.")


# Make menu for each function
def main_menu():
    while True:
        print('************************************')
        print('1. Find the best pet for you')
        print('2. Find the best breed')
        print('3. Print all pets')
        print('4. Read about responsible pet ownership')
        print('5. Exit')
        print('************************************')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            # Ask if its cat or dog
            print('1. Dog')
            print('2. Cat')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                get_answers()
                find_pets(dogs)
                print_best_fits()
            elif choice == 2:
                get_answers()
                find_pets(cats)
                print_best_fits()
        elif choice == 2:
            find_breed()
        elif choice == 3:
            print_all_pets()
        elif choice == 4:
            print_about()
        elif choice == 5:
            break

# Run the program
main_menu()
