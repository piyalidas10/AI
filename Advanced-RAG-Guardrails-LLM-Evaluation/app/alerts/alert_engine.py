from alerts.email_alert import send_email_alert


def trigger_email_alert(metrics, question):

    issues = []

    if metrics.get("injection_detected"):
        issues.append("Prompt Injection")

    if metrics.get("hallucination_score", 0) > 0.5:
        issues.append("High Hallucination")

    if metrics.get("trust_score", 1) < 0.4:
        issues.append("Low Trust")

    if metrics.get("blocked_reason"):
        issues.append(f"Blocked: {metrics['blocked_reason']}")

    if not issues:
        return

    subject = f"🚨 RAG Alert: {' | '.join(issues)}"

    send_email_alert(subject, metrics, question)