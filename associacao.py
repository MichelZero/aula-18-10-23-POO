# Criar duas classes, A e B:
# Sendo que a classe B tem um relacionamento 
# de associação com a classe A, para 
# isso use atributos específicos 
# de A no método somaTodosNum. 

#Associação
#classe A
class A:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
    
  def somaA(self):
    x = self.b + self.c
    return x


#classe B
class B:
  def __init__(self, d, e):
    self.d = d
    self.e = e

  def somaTodosNum(self, Ab, Ac):
    x = self.d + self.e + Ab + Ac
    return x

######################################################

a1 = A("soma = ", 2, 6)
b1 = B(5, 9)


# associação entre a1 e b1
print(f"{a1.a} {b1.somaTodosNum(a1.b, a1.c)}")

# só o a1
print(f"só a1 {a1.a} {a1.somaA()}")

# só b1
print(f"só b1 = {b1.d} + {b1.e}")