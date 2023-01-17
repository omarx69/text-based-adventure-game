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
               print("You picked up a hunting rifle and some ammo")
               print()
               answer = input("Do you want to hunt or go away [hunt/go] : ")
               if answer == "hunt":
                answer = input("Do you want to hunt a bear or a duck [bear/duck] : ")
                if answer == "bear":
                    print("Bears are really strong! You lose! :(")
                elif answer == "duck":
                    print("Good, You win! :)")

            elif answer == "leave":
                print("You didn't get anything!, You lose! :(")

        elif answer == "kill":
            answer = input("Good, the guard is dead. loot his items or leave [loot/leave] : ")
            if answer == "loot":
                print("you picked up an armor and sword")
                print()
                answer = input("Do you want to fight other guards or run [fight/run] : ")  
                if answer == "fight":
                    print("You fought and defeated them")
                    print()
                    answer = input("You should get out [out] : ")
                    if answer == "out":
                        print("Good, you win! :)")
                elif answer == "run":
                    print("You didn't get anything!, You lose! :(")                     
            elif answer == "leave":
                print("You didn't get anything!, You lose! :(")

    else:
        print("Invalid option, you lose!")


else:
    print("But this is really awesome game :(")