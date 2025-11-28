class Personagem:

    def __init__(self, nome, hp, poder_ataque, xp, nivel):
        self.nome = nome
        self.hp = hp
        self.max_hp = hp
        self.poder_ataque = poder_ataque
        self.xp = xp
        self.nivel = nivel

    def atacar(self, oponente):
        dano = self.poder_ataque
        oponente.receber_dano(dano)

    def receber_dano(self, dano):
        self.hp -= dano
        if self.hp < 0:
            self.hp = 0

    def se_curar(self):
        self.hp = self.max_hp
    
    def vivo(self):
        return self.hp > 0
    
    def to_dict(self):
        return (f'Nome: {self.nome}\nHP:{self.hp}\nPA:{self.poder_ataque}\nXP:{self.xp}\nLevel:{self.nivel}')


class Aliado(Personagem):
    def __init__(self, nome):
        super().__init__(nome=nome, hp=100, poder_ataque=20, xp=0, nivel=1)

    def upar_level(self):
        upar = 100
        while self.xp >= upar:
            self.xp -= upar
            self.poder_ataque += 5
            self.hp += 20
            self.max_hp = self.hp
            self.nivel += 1



class Monstro(Personagem):
    def __init__(self, nome, hp, poder_ataque):
        super().__init__(nome=nome, hp=hp, poder_ataque=poder_ataque, xp=None, nivel=None)


def turno_aliado(aliado, monstro):
    aliado.atacar(monstro)
    print('O aliado atacou')


def turno_monstro(monstro, aliado):
    monstro.atacar(aliado)
    print('O monstro atacou')


def treta():
    tungtungsahur = Aliado('tungtungsahur')
    monstros = [
        Monstro('tralalero_tralala', 40, 10),
        Monstro('bailerina_capuccina', 25, 20)
        ]
    for inimigo in monstros:
        while tungtungsahur.vivo() and inimigo.vivo():

            turno_aliado(tungtungsahur, inimigo)
            if not inimigo.vivo():
                tungtungsahur.se_curar()
                tungtungsahur.xp += 1000
                tungtungsahur.upar_level()
                print(tungtungsahur.to_dict())
                print('mosntro falecido')
                break

            turno_monstro(inimigo, tungtungsahur)
            if not tungtungsahur.vivo():
                print('aliado falicido')
                break

        print("fim da treta")


print(treta())
