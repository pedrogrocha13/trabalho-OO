import json

# Classe base
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    # Getters e Setters
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    def exibir_info(self):
        return f"Nome: {self.__nome}, Idade: {self.__idade}"


# Classe Jogador
class Jogador(Pessoa):
    def __init__(self, nome, idade, posicao, gols):
        super().__init__(nome, idade)
        self.__posicao = posicao
        self.__gols = gols

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

    @property
    def gols(self):
        return self.__gols

    @gols.setter
    def gols(self, gols):
        self.__gols = gols

    def exibir_info(self):
        return f"{super().exibir_info()}, Posição: {self.__posicao}, Gols: {self.__gols}"


# Classe Treinador
class Treinador(Pessoa):
    def __init__(self, nome, idade, experiencia):
        super().__init__(nome, idade)
        self.__experiencia = experiencia

    @property
    def experiencia(self):
        return self.__experiencia

    @experiencia.setter
    def experiencia(self, experiencia):
        self.__experiencia = experiencia

    def exibir_info(self):
        return f"{super().exibir_info()}, Experiência: {self.__experiencia} anos"


# Classe Time
class Time:
    def __init__(self, nome):
        self.__nome = nome
        self.__jogadores = []
        self.__treinador = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def adicionar_jogador(self, jogador):
        if isinstance(jogador, Jogador):
            self.__jogadores.append(jogador)

    def definir_treinador(self, treinador):
        if isinstance(treinador, Treinador):
            self.__treinador = treinador

    def exibir_info(self):
        info = f"Time: {self.__nome}\n"
        info += f"Treinador: {self.__treinador.exibir_info() if self.__treinador else 'Sem treinador'}\n"
        info += "Jogadores:\n"
        for jogador in self.__jogadores:
            info += f"  - {jogador.exibir_info()}\n"
        return info

    def salvar_em_arquivo(self, arquivo):
        dados = {
            "nome": self.__nome,
            "treinador": self.__treinador.exibir_info() if self.__treinador else None,
            "jogadores": [jogador.exibir_info() for jogador in self.__jogadores]
        }
        with open(arquivo, 'w') as f:
            json.dump(dados, f, indent=4)

    @staticmethod
    def carregar_de_arquivo(arquivo):
        try:
            with open(arquivo, 'r') as f:
                dados = json.load(f)

            if not isinstance(dados, dict) or "nome" not in dados:
                raise ValueError("Formato de arquivo inválido")

            time = Time(dados["nome"])

            # Treinador
            if dados.get("treinador"):
                try:
                    treinador_dados = dados["treinador"].split(", ")
                    treinador = Treinador(
                        treinador_dados[0].split(": ")[1],              # Nome
                        int(treinador_dados[1].split(": ")[1]),         # Idade
                        int(treinador_dados[2].split(": ")[1].split()[0])  # Experiência
                    )
                    time.definir_treinador(treinador)
                except (IndexError, ValueError) as e:
                    print(f"Erro ao carregar treinador: {e}")

            # Jogadores
            for jogador_info in dados.get("jogadores", []):
                try:
                    jogador_dados = jogador_info.split(", ")
                    # Agora esperamos 4 campos (Nome, Idade, Posição, Gols)
                    if len(jogador_dados) < 4:
                        print(f"Dados incompletos para jogador: {jogador_info}")
                        continue

                    jogador = Jogador(
                        jogador_dados[0].split(": ")[1],  # Nome
                        int(jogador_dados[1].split(": ")[1]),  # Idade
                        jogador_dados[2].split(": ")[1],   # Posição
                        int(jogador_dados[3].split(": ")[1])   # Gols
                    )
                    time.adicionar_jogador(jogador)
                except (IndexError, ValueError) as e:
                    print(f"Erro ao carregar jogador: {e}")

            return time
        except Exception as e:
            print(f"Erro ao carregar arquivo: {e}")
        return None


# Obter informações do time
nome_time = input("Digite o nome do time: ")
time = Time(nome_time)

# Adicionar jogadores
while True:
    adicionar = input("\nDeseja adicionar um jogador? (s/n): ").lower()
    if adicionar != 's':
        break

    nome = input("Nome do jogador: ")
    idade = int(input("Idade do jogador: "))
    posicao = input("Posição do jogador: ")
    gols = int(input("Gols marcados: "))

    # Agora a classe Jogador só recebe nome, idade, posicao e gols
    jogador = Jogador(nome, idade, posicao, gols)
    time.adicionar_jogador(jogador)

# Informações do treinador
print("\nInformações do Treinador:")
nome_treinador = input("Nome do treinador: ")
idade_treinador = int(input("Idade do treinador: "))
experiencia = int(input("Anos de experiência: "))

treinador = Treinador(nome_treinador, idade_treinador, experiencia)
time.definir_treinador(treinador)

# Salvar e carregar
arquivo = "time.json"
time.salvar_em_arquivo(arquivo)
time_carregado = Time.carregar_de_arquivo(arquivo)

if time_carregado:
    print(time_carregado.exibir_info())
else:
    print("Erro ao carregar o time do arquivo.")