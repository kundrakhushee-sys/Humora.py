import random
import time

class Humora:
    """
    A simple console application that acts as a joke therapist, offering jokes
    and encouragement based on the user's current feeling.
    """
    def __init__(self):
        # Corrected: Changed 'init' to '__init__' for the constructor
        self.name = "Humora"
        self.jokes = {
            "stress": [
                "Why did the stressed-out computer go to therapy? It had too many tabs open in its mind!",
                "What do you call a relaxed potato? A medi-tater!",
                "Why don't scientists trust atoms when they're stressed? Because they make up everything!",
                "What did the tomato say to the other tomato during a race?Ketchup.",

            ],
            "sad": [
                "Why did the sad cookie go to therapy? Because it was feeling crumbly!",
                "What did the sad calculator say? You can count on me to feel better!",
                "Why was the math book sad? It had too many problems... but we're here to solve them together!",
                "Have you heard the rumor about butter?Never mind, I should not be spreading it",
            ],
            "anxious": [
                "Why did the anxious tomato turn red? It saw the salad dressing... but everything's going to be okay!",
                "What did the therapist say to the anxious ocean? Just go with the flow!",
                "Why don't worries ever win at poker? They always fold under pressure!",
                "What kind of music do mummies listen to?Wrap music.",
            ],
            "tired": [
                "Why did the tired coffee file a police report? It got mugged!",
                "What do you call a sleeping bull? A bulldozer... and you deserve some rest too!",
                "Why did the pillow go to therapy? It was feeling down... literally!",
                "Why did the banana go to the doctor?It wasn’t peeling well.",
            ],
            "general": [
                "Why did the therapist bring a ladder to work? To help people reach new heights!",
                "What's a therapist's favorite type of music? Soul music!",
                "Why did the smile go to school? To get a little brighter!",
                "What did the egg say to another egg?Have an eggselent day!",
            ]
        }

    def greet(self):
        """Displays the welcome and introductory message."""
        print(f"\n{'='*50}")
        print(f"🌟 Welcome to {self.name} - Your AI Joke Therapist! 🌟")
        print(f"{'='*50}")
        print("\nHello! I'm here to brighten your day with humor.")
        print("Remember: Laughter is the best medicine!\n")

    def ask_feeling(self):
        """Presents the menu and collects user input."""
        print("How are you feeling today?")
        print("1. Stressed")
        print("2. Sad")
        print("3. Anxious")
        print("4. Tired")
        print("5. Just want a joke")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()
        return choice

    def tell_joke(self, category):
        """Selects and prints a random joke from the specified category."""
        joke = random.choice(self.jokes[category])
        print("\n" + "-"*50)
        print(f"😄 {joke}")
        print("-"*50 + "\n")
        time.sleep(1) # Pause for better readability in console

    def give_encouragement(self):
        """Provides a random encouraging message to the user."""
        encouragements = [
            "You're doing great! Keep that smile going! 😊",
            "Remember, every day is a fresh start! 🌅",
            "You've got this! I believe in you! 💪",
            "Keep your head up! Better days are coming! 🌈",
            "You're stronger than you think! ⭐",
        ]
        print(f"💝 {random.choice(encouragements)}\n")

    def run(self):
        """The main execution loop of the application."""
        self.greet()

        while True:
            choice = self.ask_feeling()

            if choice == '1':
                self.tell_joke("stress")
                self.give_encouragement()
            elif choice == '2':
                self.tell_joke("sad")
                self.give_encouragement()
            elif choice == '3':
                self.tell_joke("anxious")
                self.give_encouragement()
            elif choice == '4':
                self.tell_joke("tired")
                self.give_encouragement()
            elif choice == '5':
                self.tell_joke("general")
                self.give_encouragement()
            elif choice == '6':
                print("\n✨ Thank you for visiting Humora! ✨")
                print("Remember to laugh often! Goodbye! 👋\n")
                break
            else:
                print("\n❌ Invalid choice. Please try again.\n")

            time.sleep(0.5)

# Run the app
if __name__ == "__main__":
    # Corrected: Changed 'if name == "main"' to 'if __name__ == "__main__":'
    humora = Humora()
    humora.run()