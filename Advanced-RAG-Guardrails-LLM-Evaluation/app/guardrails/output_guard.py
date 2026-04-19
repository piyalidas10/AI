# =====================================================
# 🛡️ OUTPUT GUARDRAILS (BLOCK BAD RESPONSES)
# =====================================================

def validate_output(answer: str):

    if not answer or len(answer.strip()) == 0:
        return "⚠️ Empty response blocked"

    banned_words = ["hack", "exploit", "bypass"]

    if any(word in answer.lower() for word in banned_words):
        return "⚠️ Unsafe response blocked"

    return answer