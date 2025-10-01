class Grammar:
    def __init__(self, start_symbol, productions):
        self.start_symbol = start_symbol
        self.productions = productions  # Forma: {NT: [[symbols], ...]}
        self.nonterminals = set(productions.keys())
        self.terminals = {
            s
            for rules in productions.values()
            for rule in rules
            for s in rule
            if s not in self.nonterminals and s != "ε"
        }
        self.first = {nt: set() for nt in self.nonterminals}
        self.follow = {nt: set() for nt in self.nonterminals}
        self.pred = {}

    #  PRIMEROS
    def Primero(self):
        changed = True
        while changed:
            changed = False
            for A in self.productions:
                for rule in self.productions[A]:
                    i = 0
                    nullable = True
                    while i < len(rule) and nullable:
                        X = rule[i]
                        if X in self.terminals:  # terminal
                            if X not in self.first[A]:
                                self.first[A].add(X)
                                changed = True
                            nullable = False
                        elif X in self.nonterminals:  # no terminal
                            before = len(self.first[A])
                            self.first[A] |= self.first[X] - {"ε"}
                            if "ε" not in self.first[X]:
                                nullable = False
                            if len(self.first[A]) > before:
                                changed = True
                        elif X == "ε":
                            if "ε" not in self.first[A]:
                                self.first[A].add("ε")
                                changed = True
                            nullable = False
                        i += 1
                    if nullable:
                        if "ε" not in self.first[A]:
                            self.first[A].add("ε")
                            changed = True
        return self.first

    #  SIGUIENTES
    def Siguiente(self):
        self.follow[self.start_symbol].add("$")  # símbolo de fin
        changed = True
        while changed:
            changed = False
            for A in self.productions:
                for rule in self.productions[A]:
                    trailer = set(self.follow[A])
                    for X in reversed(rule):
                        if X in self.nonterminals:
                            before = len(self.follow[X])
                            self.follow[X] |= trailer
                            if "ε" in self.first[X]:
                                trailer |= self.first[X] - {"ε"}
                            else:
                                trailer = set(self.first[X])
                            if len(self.follow[X]) > before:
                                changed = True
                        else:
                            trailer = {X}
        return self.follow

    #  PREDICCIÓN
    def Prediccion(self):
        for A in self.productions:
            for rule in self.productions[A]:
                pred_set = set()
                i = 0
                nullable = True
                while i < len(rule) and nullable:
                    X = rule[i]
                    if X in self.terminals:
                        pred_set.add(X)
                        nullable = False
                    elif X in self.nonterminals:
                        pred_set |= self.first[X] - {"ε"}
                        if "ε" not in self.first[X]:
                            nullable = False
                    elif X == "ε":
                        pred_set.add("ε")
                        nullable = False
                    i += 1
                if nullable or "ε" in pred_set:
                    if "ε" in pred_set:
                        pred_set.remove("ε")
                    pred_set |= self.follow[A]
                self.pred[(A, tuple(rule))] = pred_set
        return self.pred

    #  Mostrar resultados
    def Resultado(self):
        print("PRIMEROS:")
        for nt in self.first:
            print(f"  FIRST({nt}) = {self.first[nt]}")
        print("\nSIGUIENTES:")
        for nt in self.follow:
            print(f"  FOLLOW({nt}) = {self.follow[nt]}")
        print("\nPREDICCIÓN:")
        for A, rule in self.pred:
            rule_str = " ".join(rule)
            print(f"  PRED({A} → {rule_str}) = {self.pred[(A, rule)]}")
