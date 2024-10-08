import random

class TimeTravelAdventure:
    def __init__(self):
        self.player_name = ""
        self.current_time = "present"

    def start_adventure(self):
        print("Welcome to the Time Travel Adventure!")
        self.player_name = input("Enter your name: ")
        print(f"Hello, {self.player_name}! Your journey through time begins now.")
        self.introduction()

    def introduction(self):
        print("\nYou find yourself in a mysterious laboratory filled with strange devices.")
        print("In front of you is a time machine, but it looks unstable.")
        print("Do you:")
        print("1. Examine the time machine.")
        print("2. Search the laboratory for clues.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.examine_time_machine()
        elif choice == '2':
            self.search_laboratory()
        else:
            print("Invalid choice! Please try again.")
            self.introduction()

    def examine_time_machine(self):
        print("\nYou approach the time machine and notice several buttons and levers.")
        print("Do you:")
        print("1. Press a random button.")
        print("2. Attempt to stabilize the machine first.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.press_random_button()
        elif choice == '2':
            self.stabilize_machine()
        else:
            print("Invalid choice! Please try again.")
            self.examine_time_machine()

    def search_laboratory(self):
        print("\nYou search the laboratory and find a hidden book titled 'Secrets of Time Travel'.")
        print("Do you:")
        print("1. Read the book.")
        print("2. Ignore it and return to the time machine.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.read_book()
        elif choice == '2':
            self.return_to_machine()
        else:
            print("Invalid choice! Please try again.")
            self.search_laboratory()

    def press_random_button(self):
        print("\nYou press a button, and the machine starts to shake!")
        print("Suddenly, you're transported to ancient Egypt.")
        self.current_time = "ancient Egypt"
        self.egypt_adventure()

    def stabilize_machine(self):
        print("\nYou carefully adjust the settings on the time machine.")
        print("After a few moments, it stabilizes, allowing you to choose a time period.")
        print("Do you want to travel to:")
        print("1. Ancient Egypt")
        print("2. Medieval Europe")
        print("3. The Future")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.current_time = "ancient Egypt"
            self.egypt_adventure()
        elif choice == '2':
            self.current_time = "medieval Europe"
            self.medieval_adventure()
        elif choice == '3':
            self.current_time = "the future"
            self.future_adventure()
        else:
            print("Invalid choice! Please try again.")
            self.stabilize_machine()

    def read_book(self):
        print("\nThe book explains the importance of maintaining the timeline.")
        print("If you alter significant events, it could create paradoxes.")
        print("Do you:")
        print("1. Take the book with you.")
        print("2. Leave the book and return to the time machine.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            print("You take the book with you, feeling more prepared for your journey.")
            self.return_to_machine()
        elif choice == '2':
            self.return_to_machine()
        else:
            print("Invalid choice! Please try again.")
            self.read_book()

    def return_to_machine(self):
        print("\nYou return to the time machine and prepare for your journey.")
        self.stabilize_machine()

    def egypt_adventure(self):
        print("\nYou arrive in ancient Egypt and see the Great Pyramids.")
        print("Suddenly, a guard approaches you.")
        print("Do you:")
        print("1. Try to explain your situation.")
        print("2. Pretend to be a traveler from a distant land.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.explain_situation()
        elif choice == '2':
            self.pretend_traveler()
        else:
            print("Invalid choice! Please try again.")
            self.egypt_adventure()

    def explain_situation(self):
        print("\nYou explain to the guard that you are from the future.")
        print("He seems skeptical and calls for his captain.")
        print("Do you:")
        print("1. Stand your ground and tell your story.")
        print("2. Try to escape while you can.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.stand_ground()
        elif choice == '2':
            self.escape()
        else:
            print("Invalid choice! Please try again.")
            self.explain_situation()

    def pretend_traveler(self):
        print("\nYou pretend to be a traveler and share tales of distant lands.")
        print("The guard seems intrigued but still suspicious.")
        print("Do you:")
        print("1. Offer him a valuable item from your time.")
        print("2. Ask him about the Pharaoh's current situation.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.offer_item()
        elif choice == '2':
            self.ask_pharaoh()
        else:
            print("Invalid choice! Please try again.")
            self.pretend_traveler()

    def stand_ground(self):
        print("\nYou stand your ground, explaining your time travel.")
        print("The captain arrives and is surprisingly open-minded.")
        print("Do you:")
        print("1. Ask for assistance to navigate this time.")
        print("2. Offer to help them with a task.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.request_assistance()
        elif choice == '2':
            self.offer_task_help()
        else:
            print("Invalid choice! Please try again.")
            self.stand_ground()

    def escape(self):
        print("\nYou attempt to escape but are caught by the guards.")
        print("They imprison you for your strange behavior.")
        print("Do you:")
        print("1. Try to escape from the prison cell.")
        print("2. Plan an escape from within.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.attempt_escape()
        elif choice == '2':
            self.plan_escape()
        else:
            print("Invalid choice! Please try again.")
            self.escape()

    def offer_item(self):
        print("\nYou offer a valuable item from your time.")
        print("The guard is impressed and allows you to leave.")
        print("Do you:")
        print("1. Explore the city.")
        print("2. Look for the Pharaoh.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.explore_city()
        elif choice == '2':
            self.search_pharaoh()
        else:
            print("Invalid choice! Please try again.")
            self.offer_item()

    def ask_pharaoh(self):
        print("\nYou ask the guard about the Pharaoh's current situation.")
        print("He informs you that the Pharaoh is seeking help with a crisis.")
        print("Do you:")
        print("1. Offer your assistance.")
        print("2. Decide to leave the city.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.assist_pharaoh()
        elif choice == '2':
            self.leave_city()
        else:
            print("Invalid choice! Please try again.")
            self.ask_pharaoh()

    def request_assistance(self):
        print("\nYou request assistance from the captain.")
        print("He agrees to help you in exchange for your knowledge of the future.")
        print("Do you:")
        print("1. Share your knowledge.")
        print("2. Hold back information.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.share_future_knowledge()
        elif choice == '2':
            self.keep_secret()
        else:
            print("Invalid choice! Please try again.")
            self.request_assistance()

    def offer_task_help(self):
        print("\nYou offer to help the captain with a task.")
        print("He assigns you to gather information about a rebel faction.")
        print("Do you:")
        print("1. Accept the mission.")
        print("2. Refuse and return to the time machine.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.accept_mission()
        elif choice == '2':
            self.refuse_mission()
        else:
            print("Invalid choice! Please try again.")
            self.offer_task_help()

    def attempt_escape(self):
        print("\nYou attempt to escape but fail, leading to a harsh punishment.")
        print("You are left to contemplate your fate.")
        self.game_over()

    def plan_escape(self):
        print("\nYou plan your escape carefully.")
        print("After days of plotting, you finally break free!")
        print("Do you:")
        print("1. Find a way back to the time machine.")
        print("2. Stay in this time and integrate.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.find_time_machine()
        elif choice == '2':
            self.integrate_time()
        else:
            print("Invalid choice! Please try again.")
            self.plan_escape()

    def explore_city(self):
        print("\nYou explore the vibrant city of ancient Egypt.")
        print("You learn about their culture and politics.")
        print("Do you:")
        print("1. Speak to the locals about their beliefs.")
        print("2. Search for hidden secrets.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.speak_locals()
        elif choice == '2':
            self.search_secrets()
        else:
            print("Invalid choice! Please try again.")
            self.explore_city()

    def search_pharaoh(self):
        print("\nYou search for the Pharaoh and finally meet him.")
        print("He is intrigued by your stories.")
        print("Do you:")
        print("1. Offer to help him with a task.")
        print("2. Ask for safe passage back to your time.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.assist_pharaoh()
        elif choice == '2':
            self.request_safe_passage()
        else:
            print("Invalid choice! Please try again.")
            self.search_pharaoh()

    def assist_pharaoh(self):
        print("\nYou assist the Pharaoh, helping him navigate a crisis.")
        print("Your actions change the course of history.")
        print("Do you:")
        print("1. Stay and continue helping.")
        print("2. Return to your time.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.stay_and_help()
        elif choice == '2':
            self.return_to_time()
        else:
            print("Invalid choice! Please try again.")
            self.assist_pharaoh()

    def leave_city(self):
        print("\nYou decide to leave the city.")
        print("You return to the time machine and prepare for your next adventure.")
        self.stabilize_machine()

    def share_future_knowledge(self):
        print("\nYou share your knowledge of the future with the captain.")
        print("He is impressed and agrees to help you.")
        print("Do you:")
        print("1. Request his assistance in traveling back.")
        print("2. Stay and help him with his problems.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.request_assistance()
        elif choice == '2':
            self.stay_and_help()
        else:
            print("Invalid choice! Please try again.")
            self.share_future_knowledge()

    def keep_secret(self):
        print("\nYou keep your knowledge a secret.")
        print("The captain grows suspicious and has you watched.")
        print("Do you:")
        print("1. Attempt to flee.")
        print("2. Reveal some information to gain his trust.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.attempt_escape()
        elif choice == '2':
            self.reveal_information()
        else:
            print("Invalid choice! Please try again.")
            self.keep_secret()

    def accept_mission(self):
        print("\nYou accept the mission and gather information.")
        print("Your findings could alter the future!")
        print("Do you:")
        print("1. Report back to the captain.")
        print("2. Investigate further on your own.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.report_findings()
        elif choice == '2':
            self.investigate_further()
        else:
            print("Invalid choice! Please try again.")
            self.accept_mission()

    def refuse_mission(self):
        print("\nYou refuse the mission.")
        print("The captain grows angry and threatens you.")
        print("Do you:")
        print("1. Stand your ground.")
        print("2. Apologize and try to explain.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.stand_ground()
        elif choice == '2':
            self.apologize()
        else:
            print("Invalid choice! Please try again.")
            self.refuse_mission()

    def find_time_machine(self):
        print("\nYou find your way back to the time machine.")
        print("Do you:")
        print("1. Travel back to the present.")
        print("2. Explore another time period.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.current_time = "present"
            self.return_home()
        elif choice == '2':
            self.explore_other_times()
        else:
            print("Invalid choice! Please try again.")
            self.find_time_machine()

    def integrate_time(self):
        print("\nYou decide to stay in ancient Egypt.")
        print("You live your life here, but sometimes wonder about your home.")
        self.game_over()

    def speak_locals(self):
        print("\nYou speak with the locals and learn about their culture.")
        print("You discover they believe in time travel as a myth.")
        print("Do you:")
        print("1. Tell them the truth about time travel.")
        print("2. Leave them with their beliefs.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.share_time_travel()
        elif choice == '2':
            self.leave_beliefs()
        else:
            print("Invalid choice! Please try again.")
            self.speak_locals()

    def search_secrets(self):
        print("\nYou search for hidden secrets and find an ancient artifact.")
        print("This artifact is said to possess time-bending powers!")
        print("Do you:")
        print("1. Keep the artifact.")
        print("2. Return it to the Pharaoh.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.keep_artifact()
        elif choice == '2':
            self.return_artifact()
        else:
            print("Invalid choice! Please try again.")
            self.search_secrets()

    def share_time_travel(self):
        print("\nYou tell them the truth about time travel.")
        print("They are fascinated but fear what they do not understand.")
        print("Do you:")
        print("1. Help them embrace the concept of time travel.")
        print("2. Leave them confused.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.help_embrace()
        elif choice == '2':
            self.leave_confusion()
        else:
            print("Invalid choice! Please try again.")
            self.share_time_travel()

    def leave_beliefs(self):
        print("\nYou decide to leave the locals with their beliefs.")
        print("As you walk away, you feel a sense of peace.")
        self.game_over()

    def keep_artifact(self):
        print("\nYou keep the artifact and feel its power surging.")
        print("This could change everything!")
        print("Do you:")
        print("1. Use its power to change the past.")
        print("2. Keep it safe for future use.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.use_artifact_power()
        elif choice == '2':
            self.keep_for_future();
        else:
            print("Invalid choice! Please try again.")
            self.keep_artifact()

    def return_artifact(self):
        print("\nYou return the artifact to the Pharaoh.")
        print("He rewards you for your honesty.")
        print("Do you:")
        print("1. Stay in Egypt.")
        print("2. Continue your travels.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.integrate_time()
        elif choice == '2':
            self.find_time_machine()
        else:
            print("Invalid choice! Please try again.")
            self.return_artifact()

    def use_artifact_power(self):
        print("\nYou use the artifact's power to change a small event.")
        print("But this creates unforeseen consequences!")
        self.game_over()

    def keep_for_future(self):
        print("\nYou keep the artifact safe for future use.")
        print("You feel its power within you.")
        print("Do you:")
        print("1. Return to your time.")
        print("2. Explore another time period.")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            self.current_time = "present"
            self.return_home()
        elif choice == '2':
            self.explore_other_times()
        else:
            print("Invalid choice! Please try again.")
            self.keep_for_future()

    def stay_and_help(self):
        print("\nYou choose to stay and help the Pharaoh.")
        print("Your actions reshape the future.")
        self.game_over()

    def return_home(self):
        print("\nYou return to your time, feeling different.")
        print("You realize how much you've changed.")
        self.game_over()

    def investigate_further(self):
        print("\nYou investigate further, discovering hidden plots.")
        print("This knowledge could change history!")
        self.game_over()

    def report_findings(self):
        print("\nYou report your findings to the captain.")
        print("He appreciates your diligence and promotes you!")
        self.game_over()

    def stand_ground(self):
        print("\nYou stand your ground.")
        print("The captain respects your bravery.")
        self.game_over()

    def apologize(self):
        print("\nYou apologize for your previous refusal.")
        print("The captain forgives you, but you are now watched closely.")
        self.game_over()

    def game_over(self):
        print("\nGame Over! Thank you for playing.")
        exit()

# To run the game, you need to instantiate the class
if __name__ == "__main__":
    adventure = TimeTravelAdventure()  # This line should work without error now
    adventure.start_game()
