from fastapi import APIRouter
from loguru import logger

from app.api.log_route import LogRoute


router = APIRouter(route_class=LogRoute)


@router.get(
    "/basic-line",
    name="",
)
def get_basic_line_chart():
    return {
        "xAxis": ['22->54', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        "series": [
            {
                "data": [150, 230, 224, 218, 135, 147, 260],
                "type": 'line'
            }
        ]
    }


@router.get(
    "/waterfall",
    name="",
)
def get_waterfall_chart():
    return {
        "xAxis":  ['Total', 'Rent', 'Utilities', 'Transportation', 'Meals', 'Other'],
        "series": [2900, 1200, 300, 200, 900, 300]
    }


@router.get(
    "/pie",
    name="",
)
def get_waterfall_chart():
    return {
        "data": [
            {"value": 335, "name": 'Direct'},
            {"value": 310, "name": 'Email'},
            {"value": 274, "name": 'Union Ads'},
            {"value": 235, "name": 'Video Ads'},
            {"value": 400, "name": 'Search Engine'}
        ]
    }
