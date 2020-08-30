#Custom For loop

# for num in [1,2,3]
# for char in "hi there"

# def my_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             # print("¡FIN DEL ITERADOR!")
#             break

# my_for("hello")
# my_for([1,2,3,4])

#A esto podemos hacerle incluso una mejora, indicarle la funcion que queremos que se aplique:
def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)

def alCuad(x):
    print(x*x)

my_for("hello", print)
my_for([1,2,3,4],alCuad)