# 📚 **Login y registro basico con streamlit**

¡Bienvenido a **Mi Proyecto**! Este es un proyecto donde el **frontend** está construido con **Streamlit** y el **backend** con **FastAPI**. El **frontend** se comunica con el **backend** mediante peticiones HTTP para realizar diversas operaciones de datos, utilizando **Firebase Firestore** como base de datos.

## 🚀 **Características**

- **Frontend**: Aplicación construida con **Streamlit** para ofrecer una interfaz de usuario sencilla y atractiva.
- **Backend**: API RESTful creada con **FastAPI**, que maneja la lógica del negocio y las operaciones de base de datos.
- **Base de Datos**: Utilizamos **Firebase Firestore** para almacenar la información de los usuarios y otros datos.

## 💻 **Tecnologías Utilizadas**

Este proyecto utiliza las siguientes tecnologías:

- **Frontend**: [Streamlit](https://streamlit.io/) – Para construir aplicaciones web interactivas de manera rápida.
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) – Un framework moderno y rápido para crear APIs.
- **Base de Datos**: [Firebase Firestore](https://firebase.google.com/docs/firestore) – Base de datos NoSQL en tiempo real.

## 🧰 **Instalación**

Sigue estos pasos para configurar el proyecto en tu máquina local:

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu_usuario/mi_proyecto.git
    cd mi_proyecto
    ```

2. Crea un entorno virtual:

    ```bash
    python -m venv venv
    ```

3. Activa el entorno virtual:

    - En **Windows**:

      ```bash
      venv\Scripts\activate
      ```

    - En **MacOS/Linux**:

      ```bash
      source venv/bin/activate
      ```

4. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

5. Configura tus credenciales de **Firebase**:

    - Descarga el archivo **JSON** con las credenciales de Firebase de tu proyecto.
    - Colócalo en la raíz del proyecto o en una carpeta específica.

6. Si vas a usar **Render** u otro servicio en la nube, configura el archivo de **start command** para apuntar al backend:

    ```bash
    cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

## 🔧 **Uso**

### Backend (API):

1. Dirígete a la carpeta `backend`:

    ```bash
    cd backend
    ```

2. Inicia el servidor de la API usando **Uvicorn**:

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

    El servidor backend estará disponible en `http://localhost:8000`.

3. Accede a la interfaz de documentación interactiva de la API en **Swagger**:

    Abre tu navegador y ve a [http://localhost:8000/docs](http://localhost:8000/docs) para ver y probar las rutas de la API.

### Frontend (Streamlit):

1. Dirígete a la carpeta `frontend`:

    ```bash
    cd frontend
    ```

2. Ejecuta la aplicación de **Streamlit**:

    ```bash
    streamlit run streamlit_app.py
    ```

    Esto abrirá la aplicación en `http://localhost:8501`.

## 📦 **Funcionalidades**

### **Frontend:**

- Interfaz para interactuar con el **backend** y realizar operaciones sobre los datos almacenados.
- Conexión con el backend para la creación, modificación y visualización de datos.

### **Backend:**

- **Operaciones de Base de Datos**: Permite crear, leer, actualizar y eliminar datos en **Firebase Firestore**.
- **Modelos de Datos**: Gestión de la estructura de datos de la aplicación.
- **Seguridad**: Funciones de autenticación y autorización para proteger el acceso a los datos.

## 📄 **Estructura del Proyecto**

La estructura del proyecto está organizada de la siguiente manera:

