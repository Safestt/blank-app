from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()

# Configuración de CORS para permitir conexiones WebSocket desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las conexiones (ajusta según sea necesario)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
active_connections = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.add(websocket)

    try:
        while True:
            try:
                # Intenta recibir un mensaje con timeout
                data = await asyncio.wait_for(websocket.receive_text(), timeout=30)  
                print(f"Mensaje recibido: {data}")
                await websocket.send_text(f"Recibido: {data}")
            except asyncio.TimeoutError:
                # Si no hay mensajes en 30s, envía un ping para mantener la conexión
                await websocket.send_text("ping")
    except WebSocketDisconnect:
        print("Cliente desconectado")
    finally:
        active_connections.discard(websocket)
