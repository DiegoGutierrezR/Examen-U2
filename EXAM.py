import time
import sys

# Mensaje de salida
msg = ("UN4 LL4V3 QU3 48R3 CU4LQU13R C4ND4D0 35 UN4 LL4V3 M4357R4, "
       "P3R0 CU4ND0 353 C4ND4D0 L0 48R3 CU4LQU13R LL4V3, 53 D353CH4.")

def echo() -> str:
    """Retorna str con estampa de tiempo."""
    return time.ctime()

def controlar_cerradura1(A: bool, B: bool, C: bool) -> str:
    """Controla la primera cerradura electromecánica."""
    D = True  
    if (A and B) or (not C and A and B) or (D and A and B and C):
        return f"Primer cerradura:ABIERTO {msg}"  
    else:
        return "Primer cerradura: Pasador bloqueado."

def controlar_cerradura2(A: bool, B: bool, C: bool) -> str:
    """Controla la segunda cerradura electromecánica."""
    if A and not B and not C:
        return "Segundo cerradura: Pasador liberado."
    else:
        return "Segundo cerradura: Pasador bloqueado."

def main() -> int:
    """Ejecuta un listado de funciones."""
    A1, B1, C1 = True, True, False  # Primer cerradura
    A2, B2, C2 = True, False, False  # Segunda cerradura

    print(echo())
    print(controlar_cerradura1(A1, B1, C1))
    print(controlar_cerradura2(A2, B2, C2))

    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nPrograma finalizado por usuario.")
        sys.exit(0)
