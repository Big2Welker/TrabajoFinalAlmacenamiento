from fastapi import APIRouter, status
from typing import List

from app.crud.evento_crud import (
    crear_evento,
    listar_eventos,
    obtener_evento,
    actualizar_evento,
    eliminar_evento
)
from app.schemas.evento_schema import EventoCreate, EventoUpdate, EventoResponse

router = APIRouter(prefix="/eventos", tags=["Eventos"])


# ✅ Crear evento
@router.post("/", response_model=EventoResponse, status_code=status.HTTP_201_CREATED)
async def crear(data: EventoCreate):
    return await crear_evento(data)


# ✅ Listar todos los eventos
@router.get("/", response_model=List[EventoResponse])
async def listar():
    return await listar_eventos()


# ✅ Obtener evento por ID
@router.get("/{id}", response_model=EventoResponse)
async def obtener(id: str):
    return await obtener_evento(id)


# ✅ Actualizar evento
@router.put("/{id}", response_model=EventoResponse)
async def actualizar(id: str, data: EventoUpdate):
    return await actualizar_evento(id, data)


# ✅ Eliminar evento
@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def eliminar(id: str):
    return await eliminar_evento(id)
