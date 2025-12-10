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
    def __init__(self, nome, hp, poder_ataque): #TODO não precisa declarar o init, pois ja ta imlementado na classe pai
        super().__init__(nome=nome, hp=hp, poder_ataque=poder_ataque, xp=None, nivel=None)


class Luta:
  def __init__(self, p1, p2) -> None:
      self.personagem_aliado = p1
      # TODO ou o atributo é uma lista de personagens ou um objeto Personagem. Mas tem q ser apenas de um tipo (evita bugs)
      self.personagem_monstro = p2 or []  

  def turno_aliado(self, aliado, monstro):
    aliado.atacar(monstro)
    print('O aliado atacou')

  #TODO da pra fazer na mesma função esse turno_aliado e turno_monstro, nao precisa ter duas
  def turno_monstro(self, monstro, aliado):
    monstro.atacar(aliado)
    print('O monstro atacou')

  def start(self, aliado, monstros):
    for inimigo in monstros:
        while aliado.vivo() and inimigo.vivo():

            self.turno_aliado(aliado, inimigo)
            # TODO tu pode mover esse if pra depois do while acho, ai tu nao precisa testar a cada iteraçao.
            # ai dentro do while tu só deixa os turnos mesmo.
            # na verdade tu nem precisa de if. É só depois do while tu chamar uma funcao progredir() ou 
            # algo nesse sentido, e la tu testa se ele tiver vivo tu upa level e se tiver morto tu faz outra coisa
            
            if not inimigo.vivo():  
                aliado.se_curar()
                aliado.xp += 100  # TODO o ideal é cada monstro dar um certo valor de xp,e não ser uma xp fixa ne
                aliado.upar_level()  # TODO tu ta curando o aliado nessa função e 2 linhas acima tb.
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
