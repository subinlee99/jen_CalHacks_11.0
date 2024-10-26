# pylint: disable=C0415
"""
Functions required for running application
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from os import environ
import asyncio

import os
from supabase import create_client, Client

from .commons.error_handling.base_error import BaseError
from .commons.error_handling.domain_violation_error import (
    DomainViolationError,
)
from .commons.error_handling.http_error import HttpError
from .commons.error_handling.repository_error import RepositoryError
from .commons.utils.env_config import EnvConfig
import logging


class Server:
    _supabase_client: Client | None = None

    _app = FastAPI()
    _logger = logging.getLogger(__name__)

    _instance = None

    ## Make it an singleton class
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_app(self):
        """
        Returns the current app instance
        """
        return self._app

    # TODO: Add supabase client

    def get_supabase_client():
        return create_client(
            os.environ["SUPABASE_URL"],
            os.environ["SUPABASE_KEY"],
        )

    def get_supabase_client(self):
        """
        Returns the current database instance
        """
        if self._supabase_client is None:
            self._supabase_client = create_client(
                os.environ["SUPABASE_URL"],
                os.environ["SUPABASE_KEY"],
            )
            return self._supabase_client
        return self._supabase_client
    
    
    def create_server(self) -> FastAPI:
        """
        Create a great FastAPI server
        """
        self._app.supabase_client = self.get_supabase_client()
        # Cors Middleware
        self._add_middlewares()
        self._add_default_routes()
        # Include routes
        self._add_routes()
        # Register Error handlers
        self._add_error_handlers()

        # Helper logs
        port = int(environ.get("PORT", 8080))
        self._logger.info(f"Swagger docs at http://0.0.0.0:{port}/docs")

        return self._app

    def _add_middlewares(self):
        env_to_origins = {
            "test": ["http://localhost:3000", "http://localhost:4000"],
            "local": ["http://localhost:3000", "http://localhost:4000"],
            "dev": [
                "https://luna-staging-ebon.vercel.app",
                "https://www.staging.jouvire.com/",
            ],
            "prod": ["https://jouvire.com", "https://www.jouvire.com"],
        }

        # Get the allowed origins based on the DATABASE_URL environment variable
        fast_api_env = environ["FAST_API_ENV"]
        if fast_api_env not in env_to_origins:
            self._logger.error(f"Unknown environment {fast_api_env}")
            self._logger.error("Defaulting to local")
            fast_api_env = "local"
        self._logger.info(f"Running in {fast_api_env} environment")
        self._logger.info(f"Allowed origins: {env_to_origins[fast_api_env]}")
        allowed_origins = env_to_origins[fast_api_env]

        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=allowed_origins,
            allow_credentials=True,
            allow_methods=["*"],  # Allows all methods # type: ignore
            allow_headers=["*"],  # Allows all headers
        )

    def _add_default_routes(self):
        # Health route

        @self._app.get("/")
        async def health_route():
            """
            Health check route
            """

            return {"status": "ok", "env": environ["FAST_API_ENV"]}

        # Sentry debug route
        @self._app.get("/sentry-debug")
        async def trigger_error():
            division_by_zero = 1 / 0

    def _add_routes(self):
        pass
        # from .ai_service.entry_points.ai_routes import ai_router
        # from .vendors_service.entry_points.vendors_routes import vendor_router
        # from .user_service.entry_points.user_routes import user_router
        # from .help_service.entry_points.help_routes import help_router
        from .ai_routes.data_access.repository import router as ai_router
        
        from .memory_service.routes import memory_router
        from .search_service.search_routes import search_router

        self._app.include_router(ai_router)
        self._app.include_router(memory_router)
        self._app.include_router(search_router)
        # self._app.include_router(vendor_router)
        # self._app.include_router(user_router)
        # self._app.include_router(help_router)

    def _add_error_handlers(self):
        self._app.add_exception_handler(BaseError, lambda req, ex: ex.respond())  # type: ignore
        self._app.add_exception_handler(DomainViolationError, lambda req, ex: ex.respond())  # type: ignore
        self._app.add_exception_handler(HttpError, lambda req, ex: ex.respond())  # type: ignore
        self._app.add_exception_handler(RepositoryError, lambda req, ex: ex.respond())  # type: ignore

    # TODO: Add supabase client

    # async def _check_mongodb_status(self, timeout=5):
    #     self._logger.info("Checking MongoDB connection, please wait...")
    #     try:
    #         await asyncio.wait_for(
    #             self._app.mongodb.command("serverStatus"), timeout=timeout  # type: ignore
    #         )
    #         self._logger.info(
    #             "MongoDB Connection successful, the database url is: "
    #             + environ["DATABASE_URL"]
    #         )
    #     except asyncio.TimeoutError:
    #         self._logger.error(
    #             f"Checking MongoDB connection timed out after {timeout} seconds."
    #         )
    #         raise ConnectionError(
    #             "Failed to connect to MongoDB, terminating Application"
    #         )
    #     except Exception as e:
    #         self._logger.error("Failed to connect to MongoDB, terminating Application")
    #         raise ConnectionError(
    #             "Failed to connect to MongoDB, terminating Application"
    #         )


server = Server()
