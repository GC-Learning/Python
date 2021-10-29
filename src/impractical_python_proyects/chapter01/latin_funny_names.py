"""Generate a Latin funny name."""
import sys
import random

def main():
    """Generate a Latin funny name."""
    first = ('Luz', 'Grato', 'Antonio', 'Alma', 'Eva', 'Jose', 'Rosario',
             'Dolores', 'Ana', 'Alfonso', 'Miguel', 'Juan', 'Luis')
    middle = ('Cuesta', 'Amor', 'Arrimadas', 'Marcela', 'Fina', 'de la',
              'del Cura', 'Pecho', 'Púlpito', 'Seisdedos', 'Sin',
              'Fuertes de', 'Marco', 'Estan', 'Gordo de')
    last = ('Mogollón', 'Jurado', 'Piernas', 'Gozo', 'Segura', 'Polla',
            'Sacristán', 'Barba', 'Salido', 'Pies Planos', 'Mayordomo',
            'Barriga', 'Gol', 'Camino', 'Día')

    while True:
        print("\nYour Latin funny name is:\n")
        first_name = random.choice(first)
        middle_name = random.choice(middle)
        f_last_name = random.choice(last)

        print(f"{first_name} {middle_name} {f_last_name}", file=sys.stderr)

        try_again = input("\n\nTry again? (Press Enter to continue and n to exit)")

        if try_again == 'n':
            break

    input("\nPress Enter to exit")

if __name__ == '__main__':
    main()
