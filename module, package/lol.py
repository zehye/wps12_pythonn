import game
import shop


if __name__ == '__main__':
    print('= Turn on game =')

    while True:
        choice = input('choice 0, 1, 2 : ')
        if choice == '1':
            game.play_game()
        elif choice == '0':
            break
        elif choice == '2':
            shop.buy_item()
        else:
            print('멍청아! 다시 해!')
