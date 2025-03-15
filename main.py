from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
import json

app = FastAPI()
active_connections = {}  # 🔹 Usaremos WebSocket como clave

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    user_data = {
        "user_info": None
    }

    active_connections[websocket] = user_data  # 🔹 Guardar WebSocket como clave

    try:
        while True:
            try:
                data = await asyncio.wait_for(websocket.receive_text(), timeout=30)
                print(f"📩 Mensaje recibido: {data}")

                if data == "actualizar":
                    print("✅ Mensaje 'actualizar' recibido, actualizando datos...")
                    active_connections[websocket]["user_info"] = "12345"

                    json_data = json.dumps({
                        str(ws): {"user_info": info["user_info"]}
                        for ws, info in active_connections.items()
                    }, default=str)  # 🔹 Convertimos WebSocket en string

                    print(f"📤 Enviando JSON: {json_data}")
                    await websocket.send_text(json_data)

                await websocket.send_text(f"Recibido: {data}")
            except asyncio.TimeoutError:
                await websocket.send_text("ping")  # 🔹 Mantener conexión activa
    except WebSocketDisconnect:
        print("❌ Cliente desconectado")
    finally:
        active_connections.pop(websocket, None)  # 🔹 Eliminar correctamente
