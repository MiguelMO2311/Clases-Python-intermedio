class ConstructorQuerySQL:
    def __init__(self):
        self.reset()

    def reset(self):
        self._select = []
        self._distinct = False
        self._from = ""
        self._where = []
        self._group_by = []
        self._having = []
        self._order_by = []
        self._limit = None
        return self

    def select(self, *campos: str):
        self._select.extend(campos)
        return self

    def distinct(self):
        self._distinct = True
        return self

    def from_(self, tabla: str):
        self._from = tabla
        return self

    def where(self, condicion: str):
        self._where.append(condicion)
        return self

    def group_by(self, *campos: str):
        self._group_by.extend(campos)
        return self

    def having(self, condicion: str):
        self._having.append(condicion)
        return self

    def order_by(self, campo: str, ascendente: bool = True):
        orden = f"{campo} {'ASC' if ascendente else 'DESC'}"
        self._order_by.append(orden)
        return self

    def limit(self, cantidad: int):
        self._limit = cantidad
        return self

    def construir(self) -> str:
        if not self._select or not self._from:
            raise ValueError("SELECT y FROM son obligatorios")

        partes = []

        # SELECT + DISTINCT
        select_clause = "SELECT "
        if self._distinct:
            select_clause += "DISTINCT "
        select_clause += ", ".join(self._select)
        partes.append(select_clause)

        partes.append(f"FROM {self._from}")

        if self._where:
            partes.append(f"WHERE {' AND '.join(self._where)}")

        if self._group_by:
            partes.append(f"GROUP BY {', '.join(self._group_by)}")

        if self._having:
            partes.append(f"HAVING {' AND '.join(self._having)}")

        if self._order_by:
            partes.append(f"ORDER BY {', '.join(self._order_by)}")

        if self._limit is not None:
            partes.append(f"LIMIT {self._limit}")

        return " ".join(partes) + ";"

constructor = ConstructorQuerySQL()
query = (
    constructor
    .distinct()
    .select("nombre", "AVG(salario)")
    .from_("empleados")
    .where("departamento = 'IT'")
    .group_by("nombre")
    .having("AVG(salario) > 50000")
    .order_by("AVG(salario)", ascendente=False)
    .limit(10)
    .construir()
)

print(query)
