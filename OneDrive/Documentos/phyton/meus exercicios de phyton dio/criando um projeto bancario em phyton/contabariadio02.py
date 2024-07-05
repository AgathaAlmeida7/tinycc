class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaCorrente:
    num_conta = 0
    
    def __init__(self, agencia, numero, usuario):
        self.agencia = agencia
        self.numero = numero
        self.usuario = usuario

class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.num_saques_dia = 0
        self.max_saques_por_dia = 3
        self.limite_por_saque = 500
        self.usuarios = []
        self.contas = []

    def criar_usuario(self, nome, data_nascimento, cpf, endereco):
        # Verifica se já existe um usuário com o mesmo CPF
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                print(f"Já existe um usuário cadastrado com o CPF {cpf}.")
                return None
        
        # Cria o usuário e o adiciona à lista de usuários
        novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(novo_usuario)
        print(f"Usuário {nome} cadastrado com sucesso.")
        return novo_usuario

    def criar_conta_corrente(self, cpf):
        # Encontra o usuário com o CPF fornecido
        usuario = None
        for u in self.usuarios:
            if u.cpf == cpf:
                usuario = u
                break
        
        if usuario is None:
            print(f"Não foi encontrado nenhum usuário com o CPF {cpf}.")
            return None
        
        # Cria uma nova conta corrente vinculada ao usuário
        ContaCorrente.num_conta += 1
        nova_conta = ContaCorrente("0001", ContaCorrente.num_conta, usuario)
        self.contas.append(nova_conta)
        print(f"Conta corrente criada com sucesso para o usuário {usuario.nome}.")
        return nova_conta

    def depositar(self, saldo, *, valor, extrato=None):
        saldo += valor
        self.depositos.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        return saldo, extrato

    def sacar(self, *, saldo, valor, extrato, limite, numero_saques, limites_saques):
        if saldo >= valor and numero_saques < limites_saques and valor <= limite:
            saldo -= valor
            self.saques.append(valor)
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif numero_saques >= limites_saques:
            print("Número máximo de saques diários atingido.")
        elif valor > limite:
            print(f"O valor máximo por saque é de R$ {limite:.2f}.")
        else:
            print("Não será possível sacar o dinheiro por falta de saldo.")
        return saldo, extrato

    def extrato(self, saldo, *, extrato):
        print("\nExtrato Bancário")
        print("----------")
        print("Depósitos:")
        for deposito in self.depositos:
            print(f"R$ {deposito:.2f}")
        print("\nSaques:")
        for saque in self.saques:
            print(f"R$ {saque:.2f}")
        print("\nSaldo Atual:", f"R$ {saldo:.2f}")
        print("----------")
        return saldo, extrato

# Função para interagir com o usuário
def main():
    conta = ContaBancaria()

    while True:
        print("\nEscolha a operação:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Criar Usuário")
        print("5 - Criar Conta Corrente")
        print("6 - Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == "1":
            valor = float(input("Digite o valor a ser depositado: "))
            conta.saldo, _ = conta.depositar(conta.saldo, valor=valor)
        elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: "))
            conta.saldo, _ = conta.sacar(saldo=conta.saldo, valor=valor, extrato=None,
                                         limite=conta.limite_por_saque, numero_saques=conta.num_saques_dia,
                                         limites_saques=conta.max_saques_por_dia)
        elif opcao == "3":
            conta.saldo, _ = conta.extrato(conta.saldo, extrato=None)
        elif opcao == "4":
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
            cpf = input("Digite o CPF (somente números): ")
            endereco = input("Digite o endereço no formato 'logradouro,nro-bairro-cidade/sigla estado': ")
            conta.criar_usuario(nome, data_nascimento, cpf, endereco)
        elif opcao == "5":
            cpf = input("Digite o CPF do usuário para vincular à nova conta: ")
            conta.criar_conta_corrente(cpf)
        elif opcao == "6":
            print("Saindo do sistema bancário.")
            break
        else:
            print("Opção inválida. Por favor, digite novamente.")


if __name__ == "__main__":
    main()
