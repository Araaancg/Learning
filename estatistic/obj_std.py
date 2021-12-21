'''
Objeto estadística para poder analizar datos, en este caso los casos de covid confirmados en la c. Madrid
Términos de estadística
'''
import datetime as dt

class Std:
    def __init__(self, x, y):
        self.x = x #Variable independiente
        self.y = y #Variable dependiente

    @property 
    def n(self):
        return len(self.x)
    


    '''
    MEDIA: La media es el valor promedio de un conjunto de datos numéricos, 
    calculada como la suma del conjunto de valores dividida entre el número total de valores.
    Ecuación: Σ(x)/n
    '''
    @property   
    def x_avg(self):
        return sum(self.x)/self.n

    @property   
    def y_avg(self):
        return sum(self.y)/self.n
    


    '''
    VARIANZA: medida de dispersión
    que se utiliza para representar la variabilidad de un conjunto de datos 
    respecto de la media aritmética de los mismo.
    Ecuación: Σi(xi-x_avg)^2/n
    '''
    @property    
    def x_variance(self):
        de = sum([(xi - self.x_avg)**2 for xi in self.x])
        return de/self.n
    
    @property    
    def y_variance(self): 
        de = sum([(yi - self.y_avg)**2 for yi in self.y])
        return de/self.n
    


    '''
    CUASIVARIANZA: es semejante a la Varianza, excepto que la división es por n-1 (tamaño de la muestra).
    medida estadística de la dispersión de los datos de una muestra respecto a la media.

    Con frecuencia se desea conocer las características de una población cualquiera: de personas, animales, 
    plantas y en general cualquier tipo de objetos. Pero analizar la población entera puede no ser tarea fácil, 
    sobre todo si el número de elementos es muy grande.
    Entonces se toman muestras, con la esperanza de que el comportamiento de ellas refleje al de la población y así 
    poder realizar inferencias sobre la misma, gracias a las cuales se optimizan los recursos. 
    A esto se le conoce como inferencia estadística.

    La cuasivarianza lo que hace es poner el listón más alto por así decirlo, ya que es una estimación en base a una muestra
    '''
    @property
    def x_cuasivar(self):
        de = sum([(xi - self.x_avg)**2 for xi in self.x])
        return de/(self.n - 1)
    
    @property
    def y_cuasivar(self):
        de = sum([(yi - self.y_avg)**2 for yi in self.y])
        return de/(self.n - 1)



    '''
    COVARIANZA: La covarianza es el valor que refleja en qué cuantía dos variables aleatorias varían 
    de forma conjunta respecto a sus medias. 
    Nos permite saber cómo se comporta una variable en función de lo que hace otra variable
    Ecuación: Σi((xi-x_avg)(yi-y_avg))/n
    '''
    @property
    def covariance(self):
        x_list = [(xi-self.x_avg) for xi in self.x]
        y_list = [(yi-self.y_avg) for yi in self.y]
        nu = sum([tup[0]*tup[1] for tup in zip(x_list,y_list)])
        return nu/self.n
    
    

    '''
    COEFICIENTE DE CORRELACIÓN LINEAL (DE PEARSON): Es una medida estadística que cuantifica 
    la dependencia lineal entre dos variables.
    Ecuación: cov(x,y)/σ(x)*σ(y)
    σ -> es el símbolo para la desviación típica, el cual se calcula haciendo la raíz
    cuadrada a la varianza, más bien la varianza es el cuadrado de la desviación típica
    '''
    @property
    def r(self):
        de = self.covariance
        nu = ((self.x_variance) ** 0.5) * ((self.y_variance) ** 0.5)
        return de/nu


    '''
    B
    Ecuación:  (nΣXY-ΣX*ΣY) / (nΣ(X^2)-(ΣX)^2)
    '''
    @property
    def B(self):
        de = self.n*sum([xi*yi for xi,yi in zip(self.x,self.y)]) - sum(self.x)*sum(self.y)
        nu = self.n*sum([xi**2 for xi in self.x]) - (sum(self.x)**2)
        return de/nu
    
    @property
    def B0(self):
        return self.y_avg - self.B*self.x_avg
    

    '''
    VALORES DE Y EN BASE A X:
    Ecuación y' = B*x + B0
    '''
    def y_prediction(self,x_value):
        return self.B * x_value + self.B0

    @property
    def lineals(self): 
        return [self.y_prediction(week) for week in self.x]
    
    def specific_date(self,wanted_date,last_known_date):
        last_known_date = dt.datetime.fromisoformat(last_known_date)
        wanted_date = dt.datetime.fromisoformat(wanted_date)
        difference = wanted_date - last_known_date
        weeks = difference.days / 7
        total = self.n + weeks
        return self.y_prediction(total)


    def __str__(self):
        return f"x: {self.x }\ny: {self.y }\nn: {self.n}\n"

aula_5 = Std([1,2,3], [10,20,27])
# print(aula_5)
# print(aula_5.B)