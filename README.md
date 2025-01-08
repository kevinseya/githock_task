# Proyecto Flask - Hola Mundo con Git Hook

Este es un proyecto básico en Python utilizando Flask para crear una aplicación web sencilla que muestra el mensaje "Hola Mundo". Además, se incluye una configuración de **pre-commit hook** que detiene los commits si el archivo `app.py` contiene más de 5 comentarios.

## Requisitos

Asegúrate de tener Python 3 y `pip` instalados. Si no tienes Flask o `pre-commit` instalados, puedes instalar las dependencias utilizando el archivo `requirements.txt`.

### Instalación

1. Clona el repositorio:

   ```bash
   git clone <https://github.com/kevinseya/githock_task.git>
   cd <githock_task>
   ```
2. Crea un entorno virtual
    ```bash
   python -m venv venv
   ```
3. Activa entorno virtual
   ```bash
   .\venv\Scripts\activate
   ```
4. Instala las dependencias
   ```bash
   pip install -r requirements.txt
   ```
### Ejecutar la Aplicación
Para ejecutar la aplicación Flask en el puerto 5000, usa el siguiente comando:
   ```bash
   pip install -r requirements.txt
   ```
## Configuración del Git Hook
Este proyecto incluye un pre-commit hook que verifica el número de comentarios en el archivo `app.py`. Si hay más de 5 comentarios, el hook impedirá que el commit se realice.

### Instalación del Hook
1. Instala `pre-commit`:
   ```bash
   pip install pre-commit
   ```
2. Configura el hook:
   ```bash
    pre-commit install
   ```
3. Ahora, antes de hacer un commit, el hook se ejecutará automáticamente para contar los comentarios. Si el archivo app.py tiene más de 5 comentarios, el commit será detenido.

### Probar el Hook
Haz un cambio en el archivo app.py, por ejemplo, agregando más de 5 comentarios, y luego intenta hacer un commit:
 ```bash
    git add app.py
    git commit -m "Probar el pre-commit con más de 5 comentarios"
 ```
Si el archivo tiene más de 5 comentarios, verás un mensaje de error y el commit será detenido.

## Estructura del Proyecto
   ```bash
        mi-proyecto-flask/
        ├── app.py              # Código principal de la aplicación Flask
        ├── check_comments.py   # Script para verificar el número de comentarios
        ├── .gitignore          # Archivos y carpetas a ignorar por Git
        ├── .pre-commit-config.yaml  # Configuración del pre-commit hook
        ├── requirements.txt    # Dependencias del proyecto
        └── README.md           # Este archivo
   ```


