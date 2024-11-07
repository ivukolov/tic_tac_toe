from gameparts import Board

if __name__ == '__main__':
    game = Board()
    game.display()
    game.make_move(1, 1, 'X')
    print('Ход сделан!')
    game.display() 
