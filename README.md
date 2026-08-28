# Parachute S.A. FAQ RAG Agent

Agente de preguntas frecuentes desarrollado en Python utilizando una arquitectura RAG simple. El agente responde consultas relacionadas con el evento de Parachute S.A. utilizando únicamente la información disponible en el archivo de preguntas frecuentes proporcionado.

## Descripción

El programa carga un archivo de texto con las preguntas frecuentes de Parachute S.A. y utiliza su contenido como contexto para un modelo de lenguaje.

El agente está diseñado para:

- Responder únicamente con información disponible en el archivo de FAQs.
- Evitar utilizar conocimiento externo o inventar información.
- Indicar cuando una pregunta no puede ser respondida con la información disponible.
- Permitir múltiples preguntas durante una misma sesión.
- Finalizar la ejecución escribiendo `Bye` o utilizando `Ctrl+C`.

## Arquitectura

El proyecto utiliza una arquitectura RAG simplificada, en la cual el documento completo se recupera desde el filesystem y se proporciona como contexto al modelo.

```text
FAQs_Parachute_SA_Guatemala_2026.txt
                  |
                  v
         Lectura del archivo
                  |
                  v
       Contexto del sistema
                  |
                  v
            OpenAI SDK
                  |
                  v
             Groq API
                  |
                  v
        openai/gpt-oss-20b
                  |
                  v
             Respuesta
```

Debido al tamaño reducido del documento, no se utilizan embeddings, una base de datos vectorial ni división del documento en chunks.

## Tecnologías utilizadas

- Python
- OpenAI Python SDK
- Groq API
- Modelo `openai/gpt-oss-20b`
- python-dotenv

## Estructura del proyecto

```text
parachute-rag/
├── .env.example
├── .gitignore
├── FAQs_Parachute_SA_Guatemala_2026.txt
├── main.py
├── README.md
└── requirements.txt
```

El archivo `.env` y el entorno virtual `.venv` no se incluyen en el repositorio.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/RNGAlef2026/parachute-rag.git
cd parachute-rag
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

En Git Bash para Windows:

```bash
source .venv/Scripts/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Configuración de la API Key

Crear un archivo llamado `.env` en la raíz del proyecto:

```env
GROQ_API_KEY=your_api_key_here
```

La API key puede obtenerse desde Groq.

> **Importante:** El archivo `.env` está incluido en `.gitignore` para evitar publicar accidentalmente la API key en el repositorio.

## Ejecución

Con el entorno virtual activado:

```bash
python main.py
```

El programa mostrará:

```text
======================================
   Agente FAQ - Parachute S.A.
======================================
Escribe 'Bye' para salir.

Tú:
```

El usuario puede realizar múltiples preguntas durante la misma sesión.

## Ejemplo de uso

```text
Tú: ¿Cuándo es el evento?
Agente: El evento tendrá lugar el 29 de septiembre de 2026.

Tú: ¿Cuál es el peso máximo?
Agente: El límite de peso máximo para realizar el salto es 100 kg (220 lb).

Tú: ¿Cuál es el precio del boleto?
Agente: No puedo responder esa pregunta con la información disponible.

Tú: Bye
Agente: ¡Hasta luego!
```

## Seguridad

La API key no está almacenada directamente en el código fuente.

El proyecto utiliza un archivo `.env` para almacenar la variable `GROQ_API_KEY`, mientras que `.gitignore` evita que dicho archivo y el entorno virtual sean incluidos en el repositorio.

El archivo `.env.example` muestra la configuración requerida sin contener credenciales reales.