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
        oponente.hp -= dano

    def se_curar(self):
        self.hp = self.max_hp

    def vivo(self):
        return self.hp > 0

    def imprimida(self):
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


class Luta:
  def __init__(self, p1, p2) -> None:
      self.personagem_aliado = p1
      self.personagem_monstro = p2 or []

  def turno_aliado(self, aliado, monstro):
    aliado.atacar(monstro)
    print('O aliado atacou')


  def turno_monstro(self, monstro, aliado):
    monstro.atacar(aliado)
    print('O monstro atacou')

  def start(self, aliado, monstros):
    for inimigo in monstros:
        while aliado.vivo() and inimigo.vivo():

            self.turno_aliado(aliado, inimigo)
            if not inimigo.vivo():
                aliado.se_curar()
                aliado.xp += 100
                aliado.upar_level()
                print(aliado.imprimida())
                print('monstro falecido')
                break

            self.turno_monstro(inimigo, aliado)
            if not aliado.vivo():
                print('aliado falicido')
                break

        print("fim da treta")


tungtungsahur = Aliado('tungtungsahur')
monstros = [
        Monstro('tralalero_tralala', 40, 10),
        Monstro('bailerina_capuccina', 25, 20)
        ]

teste = Luta(tungtungsahur, monstros)
teste.start(tungtungsahur, monstros)
