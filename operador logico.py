print (True and True and True)
print (True and False and True)
print (False and False and False)
print (True or True or True)
print (True or False or False)
print (False or False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saldo
print(exp)
exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saldo)
print(exp2)