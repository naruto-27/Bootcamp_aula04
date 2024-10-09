#idade: int = 30
#altura: float = 1.75
#nome: str = "Alice"
#is_estudante: bool = True


nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

while not nome_valido:
    try:
        nome: str = input("Digite seu nome: ")
        #verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        #verifica se há numeros no nome
        elif any(char.isdigit()for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome Válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)
    
    #Solicita ao usuário que digite o valor do seu salário e converte para float

    try:
        salario: float = float(input("Digite o valor do seu sálario: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")
        exit()

    #Solicita que o usuário digite o valor do bônus recebido e converte em float

    try:
        bonus: float = float(input("Digite o valor do bonus recebido: "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")
        exit()

    bonus_recebido: float = 1000 + salario * bonus