#83) Crie um programa onde o usuario digite uma expressao qualquer que use parenteses,
# seu aplicativo devera analisar se a expressao passada esta com os parenteses abertos
# ou fechados na ordem correta.


expr = str(input('Digite a expressão: '))
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) >0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua Expressao esta valida!')
else:
    print('Sua expressao esta errada')
