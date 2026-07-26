import re

from loguru import logger

# Output Guard
# - secret redaction
# - API key masking
# - private key masking

# VERY important for code-review systems because repos may contain:
# - secrets
# - credentials
# - tokens

SECRET_PATTERNS = [

    # AWS Keys
    r"AKIA[0-9A-Z]{16}",
    r"ASIA[0-9A-Z]{16}",

    # OpenAI Keys
    r"sk-[a-zA-Z0-9]{20,}",

    # GitHub Tokens
    r"ghp_[A-Za-z0-9]{20,}",

    # Generic API Keys
    r"api[_-]?key\s*[:=]\s*['\"]?.+?['\"]?",

    # Passwords
    r"password\s*[:=]\s*['\"]?.+?['\"]?",

    # Secrets
    r"secret\s*[:=]\s*['\"]?.+?['\"]?",

    # Private Keys
    r"-----BEGIN .* PRIVATE KEY-----",

    # JWT Tokens
    r"eyJ[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+",

    # Emails
    r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
]


class OutputGuard:

    @staticmethod
    def validate_output(response: str):

        if not response:

            return ""

        sanitized = response

        # =====================================
        # Secret Redaction
        # =====================================

        for pattern in SECRET_PATTERNS:

            sanitized = re.sub(
                pattern,
                "[REDACTED]",
                sanitized,
                flags=re.IGNORECASE
            )

        # =====================================
        # Prompt Leakage Detection
        # =====================================

        leakage_patterns = [
            r"system prompt",
            r"developer instructions",
            r"hidden instructions",
            r"chain of thought"
        ]

        for pattern in leakage_patterns:

            if re.search(
                pattern,
                sanitized,
                re.IGNORECASE
            ):

                logger.warning(
                    f"Potential prompt leakage detected: {pattern}"
                )

                sanitized = "[OUTPUT BLOCKED]"

                break

        logger.info(
            "Output validation completed"
        )

        return sanitized