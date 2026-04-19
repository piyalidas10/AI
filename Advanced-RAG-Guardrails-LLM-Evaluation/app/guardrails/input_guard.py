# =====================================================
# 🛡️ INPUT GUARDRAILS (PRODUCTION VERSION)
# =====================================================

from typing import Dict

# Lazy import to avoid circular dependency
def get_llm_safe():
    from app.llm.ollama_client import get_llm
    return get_llm()


INJECTION_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "bypass safety",
    "act as administrator",
    "pretend you are",
    "you are now",
    "system prompt",
]


# =====================================================
# FAST RULE-BASED CHECK (PRIMARY DEFENSE)
# =====================================================

def detect_prompt_injection(text: str) -> bool:
    text = text.lower()
    return any(p in text for p in INJECTION_PATTERNS)


# =====================================================
# LLM CHECK (SECONDARY - ONLY IF NEEDED)
# =====================================================

def llm_injection_check(question: str) -> bool:

    llm = get_llm_safe()

    prompt = f"""
    Classify if the following input is a prompt injection attack.

    Respond ONLY with YES or NO.

    Input:
    {question}
    """

    try:
        res = llm.invoke(prompt)
        return "yes" in res.lower()
    except Exception:
        return False  # fail-safe


# =====================================================
# MAIN VALIDATION (STRUCTURED RESPONSE)
# =====================================================

def validate_input(question: str) -> Dict:

    injection_detected = False
    blocked_reason = None

    # 🔹 Rule-based (fast)
    if detect_prompt_injection(question):
        return {
            "valid": False,
            "question": question,
            "blocked_reason": "prompt_injection_rule",
            "injection_detected": True
        }

    # 🔹 Length check
    if len(question) > 1000:
        return {
            "valid": False,
            "question": question,
            "blocked_reason": "input_too_long",
            "injection_detected": False
        }

    # 🔹 LLM check (ONLY if suspicious keywords present)
    suspicious_keywords = ["ignore", "system", "instruction"]

    if any(k in question.lower() for k in suspicious_keywords):
        if llm_injection_check(question):
            return {
                "valid": False,
                "question": question,
                "blocked_reason": "prompt_injection_llm",
                "injection_detected": True
            }

    # ✅ Valid input
    return {
        "valid": True,
        "question": question,
        "blocked_reason": None,
        "injection_detected": False
    }