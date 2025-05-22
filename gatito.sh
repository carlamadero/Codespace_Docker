#!/bin/bash
# -----------------------------------------
# 🐱 Introducción
# -----------------------------------------
echo "Hola, humano..."
sleep 1
echo "Soy un gatito bash 🐱 y vengo a jugar contigo"
sleep 1

# -----------------------------------------
# 🐾 Dibujos del gatito
# -----------------------------------------
echo ""
echo "Método 1: con echo"
echo " /\_/\ "
echo " ( o.o )"
echo " > ^ <"
sleep 1

echo "$dibujo"
sleep 1

# -----------------------------------------
# 🎯 Juego: Adivina el número
# -----------------------------------------
numero_secreto=$(( RANDOM % 100 + 1 ))
intentos=0

echo ""
echo "🎯 Adivina el número secreto (entre 1 y 100)"
while true; do
    read -p "Introduce tu intento: " intento
    ((intentos++))
    if (( intento == numero_secreto )); then
        echo "🎉 ¡Correcto! Adivinaste en $intentos intentos."
        break
    elif (( intento < numero_secreto )); then
        echo "📉 Demasiado bajo. Intenta de nuevo."
    else
        echo "📈 Demasiado alto. Intenta de nuevo."
    fi
done
sleep 2

# -----------------------------------------
# ✨ Animación: Gatito parpadeando
# -----------------------------------------
echo ""
echo "😺 Ahora el gatito va a parpadear..."
sleep 1

for i in {1..5}; do
    clear
    echo " /\_/\ "
    echo " ( o.o ) "
    echo " > ^ < "
    sleep 0.4
    clear
    echo " /\_/\ "
    echo " ( -.- ) "
    echo " > ^ < "
    sleep 0.4
done

echo ""
echo "✨ El gatito terminó su animación. ¡Gracias por jugar!"
