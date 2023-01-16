answer = input("Do you want to play this text adventure game? [yes/no] : ")

if answer == "yes":
    print("That's great!")
    print()
    answer = input("Do you want to explore a cave or jungle? [cave/jungle] : ")

    if answer == "cave":
        print("You go into the cave and see a sleeping bear")
        print()
        answer = input("Do you want to fight or run? [fight/run] : ")
        
        if answer == "fight":
            print("Bears are really strong! You lose! :(")
        elif answer == "run":
            print("You ran away! You win! :)")

    elif answer == "jungle":
        print("You go into the jungle and see a sleeping guard and a treasure chest")
        print()
        answer = input("Do you want to kill the guard or steal the chest? [steal/kill] : ")
        if answer == "steal":
            print("You opened the chest")
            print()
            answer = input("Do you want to loot items or leave it? [loot/leave] : ")
            if answer == "loot":
               answer = input("you picked up some items, You should get out now! [out] : ")
            elif answer == "leave":
                print("You didn't get anything!, You lose! :(")
            elif answer == "out":
                print("Good, You win! :)")

        elif answer == "kill":
            answer = input("Good, the guard is dead. loot his items or leave [loot/leave] : ")
            if answer == "loot":
                answer = input("you picked up some items, You should get out now! [out] : ")
            elif answer == "out":
                print("Good, You win! :)")    
            elif answer == "leave":
                print("You didn't get anything!, You lose! :(")

    else:
        print("Invalid option, you lose!")


else:
    print("But this is really awesome game :(")