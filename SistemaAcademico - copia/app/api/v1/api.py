from fastapi import APIRouter
from app.api.v1.routes import (
    evento_routes,
    evaluacion_routes  
)
api_router_v1 = APIRouter()

api_router_v1.include_router(evento_routes.router, prefix="/eventos", tags=["Eventos"])
api_router_v1.include_router(evaluacion_routes.router, prefix="/evaluaciones", tags=["Evaluaciones"])