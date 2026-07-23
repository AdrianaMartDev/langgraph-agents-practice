# AI Agents in LangGraph — Practice

Repositorio de práctica y seguimiento del curso **AI Agents in LangGraph**, enfocado en el diseño e implementación de agentes basados en LLMs usando [LangGraph](https://github.com/langchain-ai/langgraph) y la API de OpenAI.

> ⚠️ Este repositorio es material de estudio y práctica, no un proyecto de producción. El código evoluciona a medida que avanzo en el curso.

## Objetivo

Ampliar mi experiencia como desarrolladora Android hacia la integración de LLMs y arquitecturas de agentes, complementando el trabajo ya realizado en proyectos móviles con integración de IA (ej. Gemini API en [AdmRestaurant](https://github.com/AdrianaMartDev)).

## Tecnologías

- Python 3.14
- OpenAI API (`openai`)
- LangGraph / LangChain
- `python-dotenv` para gestión de variables de entorno

## Estructura

```
.
├── Main.py           # Punto de entrada / ejemplos del curso
├── .env               # Variables de entorno (NO incluido en el repo)
├── requirements.txt   # Dependencias del proyecto
└── venv/               # Entorno virtual (NO incluido en el repo)
```

## Setup local

1. Clona el repositorio
2. Crea el entorno virtual:
   ```
   python -m venv venv
   ```
3. Actívalo:
   - Windows (PowerShell): `.\venv\Scripts\Activate.ps1`
4. Instala dependencias:
   ```
   pip install -r requirements.txt
   ```
5. Crea un archivo `.env` en la raíz con tu API key:
   ```
   OPENAI_API_KEY=tu_clave_aqui
   ```
6. Ejecuta:
   ```
   python Main.py
   ```

## Progreso

- [x] Setup de entorno (VS Code, venv, OpenAI SDK)
- [x] Primera llamada a la API de OpenAI (chat completion)
- [ ] Construcción de agentes con LangGraph
- [ ] Herramientas custom (tools)
- [ ] Manejo de estado y grafos condicionales

## Autora

Adriana Martínez — Senior Android Developer explorando arquitecturas de agentes de IA.
