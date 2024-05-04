class forma: 
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2 
    def obtener_area(self):
        return self.lado1*self.lado2 
    def print(self):
        return f'Area ={self.__class__.__name__} is {self.obtener_area()}' 
    
class rectangulo(forma):
    pass

class cuadrado(rectangulo):
    def __init__(self, lado):
        super().__init__(lado,lado)

class triangulo(rectangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def obtener_area(self):
        return super().obtener_area()/2
        
class circulo(cuadrado):
    def obtener_area(self):
        return(3.1415 * (self.lado1/2)**2)
            

rectangulo_1 = rectangulo(4,5)

print(rectangulo_1.obtener_area())
print(rectangulo_1.print())

cuadrado1 = cuadrado(5) 
print(cuadrado1.obtener_area())
print(cuadrado1.print())

t1 = triangulo(4,5)
print(t1.obtener_area())

circulo1 = circulo(5)
print(circulo1.obtener_area())

