from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
import json
import uuid

app = FastAPI()
active_connections = {}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    user_id = str(uuid.uuid4())

    active_connections[user_id] = {
        "websocket": websocket,
        "user_info": None
    }

    # 📢 Notificar a todos cuando un usuario se conecta
    connection_update = {"Total_user": len(active_connections)}
    for conn in list(active_connections.values()):
        try:
            await conn["websocket"].send_text(json.dumps(connection_update))
        except:
            pass     

    try:
        while True:
            try:
                data = await asyncio.wait_for(websocket.receive_text(), timeout=30)

                if data == "actualizar":
                    active_connections[user_id]["user_info"] = "12345"
                    users_info = {
                        uid: {"user_info": user["user_info"]} for uid, user in active_connections.items()
                    }
                    await websocket.send_text(json.dumps(users_info))

                elif data == "online":
                    total_users = len(active_connections)
                    await websocket.send_text(f"Usuarios conectados: {total_users}")  
                
                await websocket.send_text(f"Recibido: {data}")

            except asyncio.TimeoutError:
                server_data = {"Mensaje": "Ping del servidor"}
                await websocket.send_text(json.dumps(server_data)) 

    except WebSocketDisconnect:
        print(f"Cliente {user_id} desconectado")

    finally:
        # ✅ Cierra explícitamente el WebSocket
        try:
            await websocket.close()
        except:
            pass  # Por si ya está cerrado

        # ✅ Elimina la conexión correctamente
        active_connections.pop(user_id, None)

        # 📢 Ahora sí, enviar actualización a los demás usuarios
        disconnection_update = {"Total_user": len(active_connections)}
        for conn in list(active_connections.values()):
            try:
                await conn["websocket"].send_text(json.dumps(disconnection_update))
            except:
                pass  
