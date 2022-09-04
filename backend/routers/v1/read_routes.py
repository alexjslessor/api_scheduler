from fastapi import APIRouter


router = APIRouter()

@router.get('/api/route_one')
async def test_route():
    return {'message': 'Hello World'}
