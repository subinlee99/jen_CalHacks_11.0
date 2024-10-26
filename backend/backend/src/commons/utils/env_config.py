"""
Loads the respective env file
"""

import logging
import os
from typing import Optional
from dotenv import load_dotenv, find_dotenv
import logging
from os import environ

logger = logging.getLogger(__name__)


class EnvConfig:
    """
    Loads the respective env file
    """

    REQUIRED_VARS = [
        "PORT",
        "FAST_API_ENV",
        "SUPABASE_URL",
        "SUPABASE_KEY",
    ]

    def __init__(
        self,
        env: Optional[str] = "local",
    ):
        logger.info(f".env.{env}")

        load_dotenv(
            dotenv_path=find_dotenv(filename=f".env.{env}"),
            override=True,
        )

        self._validate_config()

    def _validate_config(self) -> None:
        """Validates and loads all config parameters from files or env vars

        In this method, you can implement loading and validation logic for your
        deployment. The idea to run the validation here is to make sure that a
        faulty configuration is identified when starting the app instead of
        during the runtime through and application crash.
        """
        for f in self.REQUIRED_VARS:
            if f not in os.environ:
                raise ValueError(f"Environment variable {f} is required.")
