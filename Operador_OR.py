# Operador Lógico Or (ou) - Pelo menos uma das condições deve ser verdadeira para que o resultado seja verdadeiro.

entrada = input('Escolha uma alternativa: {E}para Entrada ou {S} para Saída:')
Digite_Sua_Senha = input('Digite sua senha:')
senha_Permitida = '22429441'

if (entrada == 'E' or entrada == 'e') and Digite_Sua_Senha == senha_Permitida:
    print('Acesso Concebido:')

else:
    print('Acesso Negado:')
