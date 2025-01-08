#trabalho OO
# Sistema de Gestão de Times de Futebol

Este sistema permite criar e gerenciar times de futebol, incluindo jogadores e treinador, com funcionalidades para salvar e carregar os dados de um time em arquivos JSON. Foi implementado em Python seguindo conceitos de Orientação a Objetos (OO).

## Funcionalidades

1. **Criação de um time de futebol:**
   - Nome do time
   - Adição de jogadores
   - Definição de treinador

2. **Exibição de informações do time:**
   - Lista de jogadores com seus dados (nome, idade, posição e gols marcados).
   - Informações do treinador (nome, idade e experiência).

3. **Persistência de dados:**
   - Salva o time em um arquivo JSON.
   - Carrega o time a partir de um arquivo JSON.

## Estrutura do Projeto

### Classes

1. **`Pessoa`** (classe base):
   - **Atributos:**
     - `nome` (privado): Nome da pessoa.
     - `idade` (privado): Idade da pessoa.
   - **Métodos:**
     - Getters e setters para os atributos.
     - `exibir_info`: Retorna as informações básicas da pessoa.

2. **`Jogador`** (herda de `Pessoa`):
   - **Atributos adicionais:**
     - `posicao` (privado): Posição do jogador no time.
     - `gols` (privado): Quantidade de gols marcados.
   - **Métodos adicionais:**
     - Getters e setters para os atributos.
     - Sobrescrita de `exibir_info` para incluir informações específicas do jogador.

3. **`Treinador`** (herda de `Pessoa`):
   - **Atributos adicionais:**
     - `experiencia` (privado): Anos de experiência como treinador.
   - **Métodos adicionais:**
     - Getters e setters para os atributos.
     - Sobrescrita de `exibir_info` para incluir informações específicas do treinador.

4. **`Time`**:
   - **Atributos:**
     - `nome` (privado): Nome do time.
     - `jogadores` (privado): Lista de jogadores.
     - `treinador` (privado): Objeto do treinador.
   - **Métodos:**
     - `adicionar_jogador`: Adiciona um jogador à lista de jogadores.
     - `definir_treinador`: Define o treinador do time.
     - `exibir_info`: Exibe as informações completas do time.
     - `salvar_em_arquivo`: Salva os dados do time em um arquivo JSON.
     - `carregar_de_arquivo`: Carrega os dados do time de um arquivo JSON.

## Uso do Sistema

### 1. Criar um time
Ao iniciar o sistema, você será solicitado a:
- Inserir o nome do time.
- Adicionar jogadores:
  - Nome, idade, posição e quantidade de gols marcados.
- Inserir as informações do treinador:
  - Nome, idade e anos de experiência.

### 2. Persistir os dados
- Os dados do time podem ser salvos em um arquivo JSON utilizando o método `salvar_em_arquivo`.
- Posteriormente, o time pode ser carregado a partir do arquivo JSON usando o método `carregar_de_arquivo`.

### 3. Exibir informações
- As informações completas do time, incluindo treinador e jogadores, podem ser exibidas no console.

## Exemplo de Uso

```python
nome_time = "Estrelas FC"
time = Time(nome_time)

jogador1 = Jogador("João", 24, "Atacante", 15)
jogador2 = Jogador("Carlos", 28, "Zagueiro", 2)
treinador = Treinador("Mário", 45, 20)

time.adicionar_jogador(jogador1)
time.adicionar_jogador(jogador2)
time.definir_treinador(treinador)

print(time.exibir_info())

time.salvar_em_arquivo("time.json")
time_carregado = Time.carregar_de_arquivo("time.json")
print(time_carregado.exibir_info())
```

## Requisitos

- **Python 3.8 ou superior**.
- Módulo `json` embutido no Python.

## Observações

- Certifique-se de que o arquivo JSON fornecido está no formato esperado ao usar o método `carregar_de_arquivo`.
- O sistema é sensível a dados incorretos ao carregar jogadores ou treinador do arquivo. Erros de formatação serão exibidos no console.
