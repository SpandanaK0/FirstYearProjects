
import random

class Card( object ):
    rank_list = [' x',' A',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9','10',' J',' Q',' K']

    suit_list = ['x','\u2663','\u2666','\u2665','\u2660']
    
    def __init__( self, rank=0, suit=0 ):
        self.__rank = 0
        self.__suit = 0
        self.__face_up = None
        if type(rank) == int and type(suit) == int:
            if rank in range(1,14) and suit in range(1,5):
                self.__rank = rank
                self.__suit = suit
                self.__face_up = True
        
    def rank( self ):
        """ Return card's rank (1-13). """
        return self.__rank

    def value( self ):
        return self.__rank if self.__rank < 10 else 10

    def suit( self ):
        return self.__suit
    
    def is_face_up( self ):
        return self.__face_up
    
    def flip_card( self ):
        self.__face_up = not self.__face_up

    def __str__( self ):
        if self.__face_up:
            return "{}{}".format( (self.rank_list)[self.__rank], \
                                  (self.suit_list)[self.__suit] )
        else:
            return "{}{}".format( " X", "X")

    def __repr__( self ):

        return self.__str__()
        
    def __eq__( self, other ):

        if not isinstance(other, Card):
            return False
            
        return self.rank() == other.rank() and self.suit() == other.suit()
        
class Deck( object ):


    def __init__( self ):

        self.__deck = [Card(10,1),Card(4,3),Card(12,4),Card(12,1),Card(7,4),Card(13,2),Card(10,2),Card(2,3),Card(7,3),Card(8,1),Card(9,3),Card(4,4),Card(6,1),Card(11,4),Card(4,2),Card(4,1),Card(1,2),Card(9,2),Card(2,2),Card(7,2),Card(10,3),Card(5,3),Card(1,4),Card(5,1),Card(7,1),Card(10,4),Card(1,3),Card(8,2),Card(6,3),Card(6,4),Card(13,1),Card(8,3),Card(5,2),Card(9,1),Card(3,4),Card(13,3),Card(11,3),Card(3,1),Card(1,1),Card(13,4),Card(9,4),Card(12,2),Card(5,4),Card(11,1),Card(3,2),Card(2,1),Card(11,2),Card(8,4),Card(2,4),Card(6,2),Card(3,3),Card(12,3)]

    def shuffle( self ):
        """ Shuffle deck using shuffle method in random module. """

    def deal( self ):

        return self.__deck.pop() if len(self.__deck) else None

    def is_empty( self ):
        return len(self.__deck) == 0

    def __len__( self ):
        return len(self.__deck)
    
    def __str__( self ):
        return ", ".join([str(card) for card in self.__deck])
            
    def __repr__( self ):
        return self.__str__()

    def display( self, cols=13 ):
        for index, card in enumerate(self.__deck):
            if index%cols == 0:
                print()
            print("{:3s} ".format(str(card)), end="" )
        print()
        print()


