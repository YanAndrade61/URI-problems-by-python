cod1,qtd1,price1 = map(float,input().split())
cod2,qtd2,price2 = map(float,input().split())
total = qtd1*price1 + qtd2*price2
print("VALOR A PAGAR: R$ %.2f"%total)
