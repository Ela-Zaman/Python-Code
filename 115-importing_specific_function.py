#from module_name import function_name
#from module_name import function_0, function_1, function_2

from pizza import make_pizza

make_pizza(8,"mushrooms", "egg", "beef", "chicken")

#Here from module_name import function_name as fn
from pizza import make_pizza as mp # here mp is a short, unique alias -special nickname

mp(18,"egg","beef", "chicken")

# We can also make alias for a module name 
import pizza as p

p.make_pizza(10, "cheese", "musturd")

from pizza import *

make_pizza(10,"bellpaper")

