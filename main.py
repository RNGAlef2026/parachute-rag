import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno
load_dotenv()

# Crear cliente para conectarnos con Groq
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Leer el archivo de preguntas frecuentes
archivo_faq = "FAQs_Parachute_SA_Guatemala_2026.txt"

with open(archivo_faq, "r", encoding="utf-8") as archivo:
    contenido_faq = archivo.read()

# Instrucciones del agente
system_prompt = f"""
Eres un agente de preguntas frecuentes de Parachute S.A.

Tu única fuente de información es el documento de preguntas frecuentes
que aparece a continuación.

REGLAS:
1. Responde únicamente utilizando información presente en el documento.
2. No utilices conocimiento externo.
3. No inventes información.
4. Si la respuesta no aparece en el documento, responde:
   "No puedo responder esa pregunta con la información disponible."

DOCUMENTO DE PREGUNTAS FRECUENTES:

{contenido_faq}
"""

# Historial de conversación
messages = [
    {
        "role": "system",
        "content": system_prompt
    }
]

print("======================================")
print("   Agente FAQ - Parachute S.A.")
print("======================================")
print("Escribe 'Bye' para salir.\n")

try:
    while True:
        pregunta = input("Tú: ").strip()

        if pregunta.lower() == "bye":
            print("Agente: ¡Hasta luego!")
            break

        if not pregunta:
            continue

        messages.append({
            "role": "user",
            "content": pregunta
        })

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages
        )

        respuesta = response.choices[0].message.content

        print(f"Agente: {respuesta}\n")

        messages.append({
            "role": "assistant",
            "content": respuesta
        })

except KeyboardInterrupt:
    print("\nAgente: ¡Hasta luego!")