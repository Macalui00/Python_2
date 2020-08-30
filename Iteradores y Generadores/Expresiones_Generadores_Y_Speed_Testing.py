import time

#De esta manera puedo saber cuando tiempo tardo en ejecutarse 
gen_start_time = time.time()
print(sum(n for n in range(10000000)))
gen_stop = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(10000000)]))
list_stop = time.time() - list_start_time

print(f"sum(n for n in range(10000000)) tomo: {gen_stop}")
print(f"sum([n for n in range(10000000)]) tomo: {list_stop}")