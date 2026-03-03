def hero_banner() -> str:
    return """
    <div class="hero-container">
        <div class="hero-title">🍊 Swiggy Annual Report : FY 2024–25</div>
        <div class="hero-subtitle">
            Ask any factual question about <strong>Swiggy Limited</strong> 
        </div>
    </div>
    """

def metric_pills() -> str:
    return """
    <div class="metric-row">
        <div class="metric-pill">📦 GMV <span>₹1,24,111 Cr</span></div>
        <div class="metric-pill">💰 Revenue <span>₹7,444.6 Cr</span></div>
        <div class="metric-pill">🛵 Orders <span>1,245.8 M</span></div>
        <div class="metric-pill">🏪 Restaurants <span>3,43,000</span></div>
    </div>
    """

def section_header(icon: str, title: str, badge: str) -> str:
    return f"""
    <div class="section-header">
        {icon} {title} <span class="badge">{badge}</span>
    </div>
    """

def answer_card(content: str) -> str:
    return f'<div class="answer-card">{content}</div>'

def fancy_divider() -> str:
    return '<hr class="fancy-divider">'

def empty_state() -> str:
    return """
    <div style="
        background: #1a1a2e; border: 1px dashed #3a3a5c;
        border-radius: 14px; padding: 28px; text-align: center;
        color: #6060a0; font-size: 0.95rem; margin-top: 10px;
    ">
        💬 Type a question above and hit <strong style="color:#ff8c60">✦ Ask</strong>
        to get an answer from the report.
    </div>
    """
