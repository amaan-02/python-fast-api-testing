from fastapi import FastAPI

from app.routes import users, roles, auth, admin, system, utils

app = FastAPI(
    title="Scalable FastAPI Project",
    description="A scalable project with 50+ endpoints across multiple features.",
    version="1.0.0",
)

app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(roles.router, prefix="/api/roles", tags=["Roles"])
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin Operations"])
app.include_router(system.router, prefix="/api/system", tags=["System Monitoring"])
app.include_router(utils.router, prefix="/api/utils", tags=["Utilities"])
