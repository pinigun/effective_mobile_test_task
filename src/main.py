from fastapi import FastAPI
from products.router import router as products_router
from orders.router import router as orders_router

app = FastAPI()

# Including routers
for router in [
    products_router,
    orders_router
]:
    app.include_router(router)