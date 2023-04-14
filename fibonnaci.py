def fibonacci(numero):
    # Inicializa a sequência com os dois primeiros números (0 e 1)
    sequencia = [0, 1]

    # Enquanto o último número da sequência for menor ou igual ao número informado,
    # continua adicionando novos números à sequência
    while sequencia[-1] <= numero:
        novo_numero = sequencia[-1] + sequencia[-2]
        sequencia.append(novo_numero)

    # Verifica se o número informado pertence à sequência
    if numero in sequencia:
        print(f'O número {numero} pertence à sequência de Fibonacci!')
    else:
        print(f'O número {numero} não pertence à sequência de Fibonacci.')

fibonacci(21)