import random

while True:
    # BOT'S ACTION

    actions = ["ROCK", "PAPER", "SEZORS"]

    random_action_len = random.randrange(3)  # 0, 1, 2

    bots_action = actions[random_action_len]

    # CONVERTING TO NUMS
    # 0 = rock
    # 1 = paper
    # 2 = sezors
    # use random_actions_len

    # USER'S ACTION
    print("\n\t\t1. ROCK\n\t\t2. PAPER\n\t\t3. SEZORS\n")

    users_action = int(input("\n>>> "))

    # FINAL RESULT

    # algorithms
    #     users_action    bots_action    RESULT(USER)
    #
    #     rock            rock            draw
    #     rock            paper           lose
    #     rock            sezors          win
    #
    #     paper           rock            win
    #     paper           paper           draw
    #     paper           sezors          lose
    #
    #     sezors          rock            lose
    #     sezors          paper           win
    #     sezors          sezors          draw

    # MAIN RESULT

    # converting user's input to bot's input

    if users_action == 1:
        users_action = 0

    elif users_action == 2:
        users_action = 1

    elif users_action == 3:
        users_action = 2
    else:
        pass

    # compiling result
    if users_action == random_action_len:
        print("DRAW")
    else:
        if users_action == 0 and random_action_len == 1:
            print("LOSE")
        elif users_action == 0 and random_action_len == 2:
            print("WIN")

        elif users_action == 1 and random_action_len == 1:
            print("DRAW")
        elif users_action == 1 and random_action_len == 2:
            print("LOSE")

        elif users_action == 2 and random_action_len == 1:
            print("WIN")
        elif users_action == 2 and random_action_len == 2:
            print("DRAW")
        else:
            pass

    # more results
    users_action_str = ""
    if users_action == 0:
        users_action_str = "ROCK"
    elif users_action == 1:
        users_action_str = "PAPER"
    elif users_action == 2:
        users_action_str = "SEZORS"
    else:
        pass

    print(f"USER: {users_action_str}")
    print(f"BOT: {bots_action}")
