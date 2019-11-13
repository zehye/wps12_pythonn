from game import play_game
from shop import play_game as play_game_shop
import shop


if __name__ == '__main__':
    print('= Turn on game =')

    while True:
        choice = input('choice 0, 1, 2 : ')
        if choice == '1':
            play_game()
            play_game_shop()
        elif choice == '0':
            break
        elif choice == '2':
            shop.buy_item()
        else:
            print('멍청아! 다시 해!')
