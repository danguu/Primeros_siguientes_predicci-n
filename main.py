from funciones import Grammar


def leer_gramaticas(path):
    gramaticas = []
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    producciones = {}
    start_symbol = None

    for line in lines:
        if "->" not in line:
            continue

        nt, reglas = line.split("->")
        nt = nt.strip()
        if start_symbol is None:
            start_symbol = nt

        rhs = []
        for r in reglas.split("|"):
            symbols = r.strip().split()
            if symbols == ["ε"]:  # epsilon literal
                symbols = ["ε"]
            rhs.append(symbols)

        producciones[nt] = rhs

    if producciones:
        gramaticas.append((start_symbol, producciones))

    return gramaticas


def main():
    gramaticas = leer_gramaticas("gramaticas.txt")
    for i, (start, prods) in enumerate(gramaticas, 1):
        print("\nGRAMÁTICA")
        g = Grammar(start, prods)
        g.Primero()
        g.Siguiente()
        g.Prediccion()
        g.Resultado()


main()
