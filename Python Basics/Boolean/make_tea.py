#Tarefa
#Make Tea
#Existem três variáveis:
#is_water_hot indica a disponibilidade de água quente.
#have_tea indica a disponibilidade de chá.
#can_make_tea indica a disponibilidade de ambos os ingredientes.
#Altere is_water_hot ou have_tea para que can_make_tea seja False.

# change code below this line

is_water_hot = True
have_tea = False

# change code above this line

can_make_tea = is_water_hot and have_tea  # don't change this line
print(can_make_tea)