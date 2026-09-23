import uuid

from pydantic import Field, field_validator
from pydantic.dataclasses import dataclass


@dataclass
class Usuario:
    cedula: str
    nombres: str
    apellidos: str
    usuario: str
    constraseña: str
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))

    # validar que cedula tenga 10 digitos
    # debo contar caracter por caracter
    @field_validator("cedula")
    @classmethod
    def validar_cedula(cls, cedula: str) -> str:
        caracteres = len(cedula)

        if caracteres != 10:
            raise ValueError(
                f"El numero de cedula debe tener 10 caracteres pero has ingresado {caracteres} caracteres"
            )

        return cedula


def main():
    cliente = Usuario("0987654321", "paulinho", "ramirez", "paulra", "admin")
    print(cliente)


if __name__ == "__main__":
    main()
