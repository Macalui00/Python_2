#Generar una funcion que retorne si y luego no y asi sucesivamente

def si_o_no():
    resp = "si"
    while True:
        yield resp
        resp = "no" if resp == "si" else "yes"