from random import choice

vidas = 6

def elegir_palabra_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        palabras = [linea.strip() for linea in archivo if linea.strip()]
    return choice(palabras)

def poner_guiones(palabra):
    return ['_' for _ in palabra]

def actualizar_guiones(palabra, guiones, letra):
    for i, caracter in enumerate(palabra):
        if caracter == letra:
            guiones[i] = letra
    return guiones

def pedir_letra(palabra, guiones, letras_acertadas, letras_falladas):
    while True:
        letra = input("Introduce una letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Introduce solo una letra válida.")
            continue

        if letra in letras_acertadas or letra in letras_falladas:
            print("Ya has probado esa letra.")
            continue

        if letra in palabra:
            letras_acertadas.append(letra)
            guiones = actualizar_guiones(palabra, guiones, letra)
            print("✅ ¡Letra correcta!")
            return guiones, letras_acertadas, letras_falladas, True  # ✅ Devuelve acierto = True
        else:
            letras_falladas.append(letra)
            print("❌ Letra incorrecta.")
            return guiones, letras_acertadas, letras_falladas, False  # ✅ acierto = False

palabra = elegir_palabra_desde_archivo("palabras_ahorcado.txt")
guiones = poner_guiones(palabra)
letras_falladas = []
letras_acertadas = []

print("🎮 ¡Bienvenido al juego del ahorcado!")
print(' '.join(guiones))

while vidas > 0 and '_' in guiones:
    guiones, letras_acertadas, letras_falladas, acierto = pedir_letra(palabra, guiones, letras_acertadas, letras_falladas)

    if not acierto:
        vidas -= 1

    print("\nPalabra:", ' '.join(guiones))
    print("Letras incorrectas:", ', '.join(letras_falladas))
    print(f"Vidas restantes: {vidas}")
    print("====================================")

if '_' not in guiones:
    print(f"🎉 ¡Has ganado! La palabra era: {palabra}")
else:
    print(f"💀 Has perdido. La palabra era: {palabra}")



