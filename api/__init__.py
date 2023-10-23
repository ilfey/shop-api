from .index import router as index_router
from .users import router as users_router
from .products import router as products_router

routers = [
    index_router,
    users_router,
    products_router,
]
