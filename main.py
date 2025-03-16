from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
import json
from jwt_auth import verify_jwt

app = FastAPI()
active_connections = {}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    query_params = websocket.query_params
    client_jwt = query_params.get("client_jwt", None)

    if not client_jwt:
        await websocket.send_text(json.dumps({"error": "JWT no proporcionado"}))
        await websocket.close()
        return

    try:
        user_data = verify_jwt(client_jwt)
        user_id = user_data["user"]
    except Exception:
        await websocket.send_text(json.dumps({"error": "JWT inválido"}))
        await websocket.close()
        return
    

    active_connections[user_id] = {
        "websocket": websocket,
        "user_info": None
    }

    print(active_connections)

    await broadcast_all_user()

    try:
        while True:
            try:
                data = await asyncio.wait_for(websocket.receive_text(), timeout=30)
                
                json_data = json.loads(data)

                message = json_data.get("message")
                action = json_data.get("action")
                destinatary = json_data.get("destinatary")


                if action == "send" and message:
                    await send_transaction_notification(destinatary,message)


                
                await websocket.send_text(f"Recibido: {data}")
            
            except asyncio.TimeoutError:
                await websocket.send_text(json.dumps({"Mensaje": "Ping del servidor"}))
    
    except WebSocketDisconnect:
        print(f"Cliente {user_id} desconectado")
    finally:
        active_connections.pop(user_id, None)
        await broadcast_all_user()


async def broadcast_all_user():
    connection_update = {"Total_user": len(active_connections)}
    for conn in list(active_connections.values()):
        try:
            await conn["websocket"].send_text(json.dumps(connection_update))
        except:
            pass  

async def send_transaction_notification(other_id, message):
    if other_id in active_connections:
        websocket = active_connections[other_id]["websocket"]
        data = {
            "signal": {
                "action": "transaction",
                "message": f"{message}",
                "date": "2025-03-15T12:34:56Z"
            }
        }


        await websocket.send_text(json.dumps(data))
