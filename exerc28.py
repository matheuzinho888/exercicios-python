n1 = int(input("digite o 1° numero: "))
n2 = int(input("digite o 2° numero: "))
n3 = int(input("digite o 3° numero: "))
if (n1>n2 and n1>n3 and n2>n3):
  print (f"o numero maior é {n1}")
elif (n2>n1 and n2>n3 and n1>n3):
  print (f"o numero maior é {n2}")
elif (n3>n2 and n3>n1 and n2>n1):
  print (f"o numero maior é {n3}")
elif (n3>n1 and n3>n2 and n1>n2):
  print (f"o numero maior é {n3}")
elif (n2>n3 and n2>n1 and n3>n1):
  print (f"o numero maior é {n2}")
elif (n1>n3 and n1>n2 and n3>n2):
  print (f"o numero maior é {n1}")