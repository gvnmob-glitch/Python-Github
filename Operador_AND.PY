# Operador Lógico And
# Todas as condições devem ser verdadeiras para que o resultado seja verdadeiro.

print('Escolha uma das opções abaixo E ou S:')

entrada = input("{E}ntrada: ou {S}aida: ")
senha_digitada = input("Digite a senha: ")
senha_permitida = "123"

if entrada == "E" and senha_digitada == senha_permitida:
    print("Entre.")
    # Aqui você pode adicionar mais lógica para a entrada
else:
    print("Saia.")
    # Aqui você pode adicionar mais lógica para a saída