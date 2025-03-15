from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
import json

app = FastAPI()
active_connections = {}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    ip_client = websocket.client.host
    
    active_connections[ip_client] = {
        "websocket": websocket,  # ✅ Guarda el objeto WebSocket correctamente
        "user_info": None
    }

    try:
        while True:
            try:
                
                data = await asyncio.wait_for(websocket.receive_text(), timeout=30)

                if data == "actualizar":
                    active_connections[ip_client]["user_info"] = "12345"

                   
                    users_info = {
                        ip: {"user_info": user["user_info"]} for ip, user in active_connections.items()}
                    await websocket.send_text(json.dumps(users_info))

                elif data == "online":
                    total_users = len(active_connections)
                    await websocket.send_text(f"Usuarios conectados: {total_users}")  
                
                await websocket.send_text(f"Recibido: {data}")

            except asyncio.TimeoutError:
                server_data = {
                "Total_user": f"usuarios totales: {len(active_connections)}",
                "Mensaje": "Ping del servidor",
                }

                await websocket.send_text(json.dumps(server_data)) 

    except WebSocketDisconnect:
        print(f"Cliente {ip_client} desconectado")
    
    finally:
        # ✅ Elimina la conexión del diccionario correctamente
        active_connections.pop(ip_client, None)
