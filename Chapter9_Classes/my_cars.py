from car import Car #importing more than one class
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())


#When importing an entire module, and access classes needed using . notation, for example:

# import car 

# my_beetle = car.Car('volkswagen', 'beetle', 2019)



# can import every module using * - not recommended
#For eg:
#From module_name import *

#Better off using module_name.ClassName
#This helps us follow which class is imported from which module, etc. 