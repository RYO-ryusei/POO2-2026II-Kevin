# DISEÑO A — todo en una clase

class SistemaAcademico:

    def registrar_estudiante(self, nombre, codigo):
        ...

    def agregar_nota(self, codigo_est, curso, nota):
        ...

    def calcular_ppa(self, codigo_est):
        ...

    def exportar_csv(self, filename):
        ...

    def enviar_reporte(self, email):
        ...

    def conectar_bd(self, host, user, pw):
        ...


# DISEÑO B — responsabilidades separadas

class Estudiante:

    def agregar_nota(self, nota: Nota):
        ...

    def calcular_ppa(self) -> float:
        ...


class RepositorioEstudiante:

    def guardar(self, e: Estudiante):
        ...

    def buscar(self, codigo: int) -> Estudiante:
        ...


class ExportadorCSV:

    def exportar(
        self,
        estudiantes: list[Estudiante],
        archivo: str
    ):
        ...