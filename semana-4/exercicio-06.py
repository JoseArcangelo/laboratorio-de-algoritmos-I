quantidadeMaca = int(input("Quantos quilos de maça voce quer comprar?"))

quantidadeMorango = int(input("Quantos quilos de morango voce quer comprar?"))

quantidadeTotal = quantidadeMaca + quantidadeMorango

if quantidadeTotal <= 5:
    valorMaca = quantidadeMaca * 1.8
    
    valorMorango = quantidadeMorango * 2.5
    
    valorTotal = valorMorango + valorMaca
    
    print("Você adquiriu", quantidadeMaca, "Kg de maças e", quantidadeMorango,
    "Kg de morangos, o valor total da compra foi de R$", valorTotal)
    
elif quantidadeTotal > 5:
    valorMaca = quantidadeMaca * 1.5
    
    valorMorango = quantidadeMorango * 2.2
    
    valorTotal = valorMaca + valorMorango
    
    if quantidadeTotal >= 8 or valorTotal > 25:
        valorTotal = valorTotal * 0.9
        
    print("Foi adquirido", quantidadeMaca, "Kg de maças e", quantidadeMorango,
    "Kg de morangos, o valor total da compra foi de R$", valorTotal)
        
    
