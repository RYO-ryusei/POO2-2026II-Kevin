# Actividad 1 — Código refactorizado

from dataclasses import dataclass


@dataclass
class Nota:
    curso: str
    calificacion: float


class Estudiante:
    def __init__(self, nombre: str, codigo: int, escuela: str):
        self._nombre = nombre
        self._codigo = codigo
        self._escuela = escuela
        self._notas = []

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def codigo(self) -> int:
        return self._codigo

    @property
    def escuela(self) -> str:
        return self._escuela

    def agregar_nota(self, curso: str, calificacion: float) -> None:
        if calificacion < 0 or calificacion > 20:
            raise ValueError("La calificación debe estar entre 0 y 20.")

        self._notas.append(Nota(curso, calificacion))

    def calcular_ppa(self) -> float:
        if len(self._notas) == 0:
            return 0.0

        total = 0
        for nota in self._notas:
            total = total + nota.calificacion

        return total / len(self._notas)

    def mostrar(self) -> None:
        print(self._nombre, self._codigo, self._escuela)
        for nota in self._notas:
            print(nota)


# Prueba

e1 = Estudiante("Juan Mamani", 20210500, "Ing. Sistemas")

e1.agregar_nota("POO II", 16)
e1.agregar_nota("BD I", 14)

e1.mostrar()

print("PPA:", e1.calcular_ppa())