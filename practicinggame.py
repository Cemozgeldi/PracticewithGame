print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 3

if age >= 18:
    print("Good",name, "!You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are staring with", health, "health")
        print("Let's play!")

        left_or_right = input("First choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a river... Do you swim across or search a bridge (across/search)? ")

            if ans == "search":
                print("You were search and reached the other side of the river.")
            elif ans == "across":
                print("You managed to get across, but were bit by a crocodile and lost 2 health.")
                health -= 2

            ans = input("You notice a lumberjacks cabin and a cave. Which do you go to (cabin/cave)? ")
            if ans == "cabin":
                print("You go to the house and are greeted by the owner... Luckily he liked you and gave you a bread")
                health += 2

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived... You win!")

            else:
                print("You bitten by a bear and lost...")


        else:
            print("You fell down and lost...")

    else:
        print("Cya...")
else:
    print("You are not old enough to play...")
