#entendendo linha print(response.text[:600])

#texto = 'Estudando slices'
texto = list(range(1,20)) # pode ser usado para lista

subtexto = texto[:12] # Estudando sl -> 12 Caracteres da esquerda para direita
print(subtexto)

subtexto = texto[5:] # ando slices -> Tira os 5 primeiros da esquerda
print(subtexto)

subtexto = texto[-5:] # lices -> Pega os 5 últimos caracteres da string
print(subtexto)

subtexto = texto[3:8] # udand -> Tira os 3 primeiros, faz um intervalo, e tira os 8 ultimos
print(subtexto)