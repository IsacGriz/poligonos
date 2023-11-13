class Poligono:
  def __init__(self, paramSide, paramNumberOfSide, paramApothem, paramName, paramColor):
    self.atribSide = paramSide
    self.atribNumberOfSide = paramNumberOfSide
    self.atribApothem = paramApothem
    self.atribNumberOfAngle = paramNumberOfSide
    self.name = paramName
    self.atribName = self.name
    self.atribColor = paramColor


  def calculatePerimeter(self):
    perimeter = self.atribSide * self.atribNumberOfSide
    return perimeter


  def calculateArea(self):
    area = (self.calculatePerimeter() * self.atribApothem) / 2
    return area


  def calculateAngleSum(self):
    angleSum = 180 * (self.atribNumberOfAngle - 2)
    return angleSum


  def calculateInternalAngle(self):
    InternalAngle = self.calculateAngleSum() / self.atribNumberOfAngle
    return InternalAngle


  def calculateExternalAngle(self):
    externalAngle = 360 / self.atribNumberOfSide
    return externalAngle


triangulo = Poligono(5, 3, 5, 'triângulo', 'vermelho')
quadrado = Poligono(4, 4, 2, 'quadrado', 'verde')
hexagono = Poligono(6, 6, 5.2, 'hexágono', 'azul')
octagono = Poligono(5, 8, 6.04, 'octágono', 'rosa')
decagono = Poligono(8, 10, 12.07, 'decágono', 'roxo')

print(f'''
Triângulo:
  Lado: {triangulo.atribSide}
  Números de lados: {triangulo.atribNumberOfSide}
  Número de ângulos: {triangulo.atribNumberOfAngle}
  Apótema: {triangulo.atribApothem}
  Perímetro: {triangulo.calculatePerimeter()}
  Área: {triangulo.calculateArea()}
  Tamanho dos ângulos internos: {triangulo.calculateInternalAngle()}
  Valor dos ângulos externos: {triangulo.calculateExternalAngle()}
  Soma dos ângulos internos: {triangulo.calculateAngleSum()}

Quadrado:
  Lado: {quadrado.atribSide}
  Números de lados: {quadrado.atribNumberOfSide}
  Número de ângulos: {quadrado.atribNumberOfAngle}
  Apótema: {quadrado.atribApothem}
  Perímetro: {quadrado.calculatePerimeter()}
  Área: {quadrado.calculateArea()}
  Tamanho dos ângulos internos: {quadrado.calculateInternalAngle()}
  Valor dos ângulos externos: {quadrado.calculateExternalAngle()}
  Soma dos ângulos internos: {quadrado.calculateAngleSum()}

Hexágono:
  Lado: {hexagono.atribSide}
  Números de lados: {hexagono.atribNumberOfSide}
  Número de ângulos: {hexagono.atribNumberOfAngle}
  Apótema: {hexagono.atribApothem}
  Perímetro: {hexagono.calculatePerimeter()}
  Área: {hexagono.calculateArea()}
  Tamanho dos ângulos internos: {hexagono.calculateInternalAngle()}
  Valor dos ângulos externos: {hexagono.calculateExternalAngle()}
  Soma dos ângulos internos: {hexagono.calculateAngleSum()}

Octágono:
  Lado: {octagono.atribSide}
  Números de lados: {octagono.atribNumberOfSide}
  Número de ângulos: {octagono.atribNumberOfAngle}
  Apótema: {octagono.atribApothem}
  Perímetro: {octagono.calculatePerimeter()}
  Área: {octagono.calculateArea()}
  Tamanho dos ângulos internos: {octagono.calculateInternalAngle()}
  Valor dos ângulos externos: {octagono.calculateExternalAngle()}
  Soma dos ângulos internos: {octagono.calculateAngleSum()}

Decágono:
  Lado: {decagono.atribSide}
  Números de lados: {decagono.atribNumberOfSide}
  Número de ângulos: {decagono.atribNumberOfAngle}
  Apótema: {decagono.atribApothem}
  Perímetro: {decagono.calculatePerimeter()}
  Área: {decagono.calculateArea()}
  Tamanho dos ângulos internos: {decagono.calculateInternalAngle()}
  Valor dos ângulos externos: {decagono.calculateExternalAngle()}
  Soma dos ângulos internos: {decagono.calculateAngleSum()}
''')
