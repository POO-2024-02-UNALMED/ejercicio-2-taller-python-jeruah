from Apostador import Apostador

# code to change the probability of the game
# from Loteria import Loteria
# Loteria.changeProbability(0.6)

if __name__ == "__main__":
    apostador1 = Apostador(1, "Juan", 302, "j@gmail.com")
    apostador1.deposit(300)
    print(apostador1.wallet)
    apostador1.play(400)
    print(apostador1.wallet)

    apostador2 = Apostador(2, "Ricardo", 548, "r@gmail.com")
    apostador2.deposit(400)
    print(apostador2.wallet)
    apostador2.play(400)
    print(apostador2.wallet)