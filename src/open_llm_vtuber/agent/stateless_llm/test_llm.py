from typing import AsyncIterator
from loguru import logger

from .stateless_llm_interface import StatelessLLMInterface


class TestLLM(StatelessLLMInterface):
    def __init__(
            self,
            model: str = "test-model",
            base_url: str = None,
            llm_api_key: str = None,
            system: str = None,
    ):
        """
        Initialize Test LLM.

        Args:
            model (str): Model name
            base_url (str): Base URL for Test API
            llm_api_key (str): Test API key
            system (str): System prompt
        """
        self.model = model
        self.system = system

        # Initialize Test client
        self.client = None
        logger.info(f"Initialized Test LLM with model: {self.model}")

    async def chat_completion(self, messages, system=None) -> AsyncIterator[str]:
        yield "Hello, this is a test response from TestLLM."
