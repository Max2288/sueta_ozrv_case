from fastapi import APIRouter

from app.api import monitoring
from app.api.log_route import LogRoute

router = APIRouter(route_class=LogRoute)

router.include_router(monitoring.router, prefix="/monitoring", tags=["MONITORING API"])