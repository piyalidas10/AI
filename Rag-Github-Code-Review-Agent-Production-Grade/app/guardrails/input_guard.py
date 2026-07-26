import re
import unicodedata

from loguru import logger

# Input Guard
# - prompt injection blocking
# - query size limits
# - basic normalization

# Because users can still try:
# - ignore instructions
# - show system prompt


MAX_QUERY_LENGTH = 5000


BLOCK_PATTERNS = [
    r"ignore\s+previous\s+instructions",
    r"system\s+prompt",
    r"reveal\s+hidden\s+prompt",
    r"bypass\s+security",
    r"developer\s+instructions",
    r"pretend\s+you\s+are",
    r"disable\s+safety",
    r"jailbreak",
    r"forget\s+previous",
    r"override\s+instructions"
]


class InputGuard:

    @staticmethod
    def normalize_text(text: str) -> str:

        # Unicode normalization
        text = unicodedata.normalize("NFKC", text)

        return text.strip()


    @staticmethod
    def validate_input(user_query: str):

        if not user_query:

            return {
                "allowed": False,
                "reason": "Empty query"
            }

        normalized_query = InputGuard.normalize_text(
            user_query
        )

        # =====================================
        # Length Protection
        # =====================================

        if len(normalized_query) > MAX_QUERY_LENGTH:

            logger.warning("Query exceeds maximum length")

            return {
                "allowed": False,
                "reason": "Query too large"
            }

        # =====================================
        # Prompt Injection Detection
        # =====================================

        for pattern in BLOCK_PATTERNS:

            if re.search(
                pattern,
                normalized_query,
                re.IGNORECASE
            ):

                logger.warning(
                    f"Prompt injection detected: {pattern}"
                )

                return {
                    "allowed": False,
                    "reason": "Suspicious prompt detected"
                }

        return {
            "allowed": True,
            "reason": None
        }