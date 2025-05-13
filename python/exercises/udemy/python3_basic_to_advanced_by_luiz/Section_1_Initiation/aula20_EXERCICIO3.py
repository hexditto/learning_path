primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor >= int_segundo_valor:
    print(
        f"Primeiro valor = '{int_primeiro_valor}' é maior ou igual "
        f"do que segundo valor = '{int_segundo_valor}'"
    )

elif int_segundo_valor >= int_primeiro_valor:
    print(
        f"Segundo valor = '{int_segundo_valor}' é maior ou igual "
        f"do que primeiro valor = '{int_primeiro_valor}'"
    )
