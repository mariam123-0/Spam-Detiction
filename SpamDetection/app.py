import streamlit as st
import re

# -------- Streamlit Config --------
st.set_page_config(
    page_title="Spam Detection System",
    page_icon="📩",
    layout="wide"
)

# -------- Custom CSS for Styling --------
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        }
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .main-header {
            text-align: center;
            padding: 2rem;
            background: rgba(255,255,255,0.05);
            border-radius: 20px;
            margin-bottom: 2rem;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .main-header h1 {
            font-size: 3rem;
            margin-bottom: 0.5rem;
        }
        .main-header p {
            font-size: 1.2rem;
            opacity: 0.8;
        }
        .spam-warning {
            animation: shake 0.5s;
            text-align: center;
            padding: 2rem;
            background: rgba(255,0,0,0.15);
            border-radius: 10px;
            border: 2px solid #ff4444;
        }
        .ham-success {
            text-align: center;
            padding: 2rem;
            background: rgba(0,255,0,0.1);
            border-radius: 10px;
            border: 2px solid #00ff00;
        }
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-10px); }
            75% { transform: translateX(10px); }
        }
    </style>
""", unsafe_allow_html=True)

# -------- Main Header --------
st.markdown("""
    <div class="main-header">
        <h1>📩 Spam Detection System</h1>
        <p>Protect your inbox from unwanted and malicious messages</p>
    </div>
""", unsafe_allow_html=True)

# -------- Spam Detection Function --------
def predict_spam(text: str) -> bool:
    """
    Detect if a message is spam based on keyword matching
    
    Args:
        text: Input message text
    
    Returns:
        bool: True if spam, False if not spam
    """
    spam_keywords = [
        "free", "win", "cash", "offer", "buy now", "click", "credit",
        "prize", "urgent", "congratulations", "limited time", "guaranteed",
        "earn money", "no risk", "act now", "winner", "claim", "discount",
        "deal", "promotion", "lottery", "million", "dollars", "password",
        "verify", "account", "suspended", "risk"
    ]
    
    text_lower = text.lower()
    
    for keyword in spam_keywords:
        if keyword in text_lower:
            return True
    
    return False

# -------- Main Content Area --------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Message Input
    st.markdown("### ✍️ Enter Your Message")
    user_input = st.text_area(
        "",
        height=150,
        placeholder="Type or paste the message you want to check here...",
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Detect Button
    detect_button = st.button("🔍 Detect Spam", type="primary", use_container_width=True)
    
    # -------- Results Section --------
    if detect_button:
        if not user_input.strip():
            st.warning("⚠️ Please enter a message to analyze.")
        else:
            is_spam = predict_spam(user_input)
            
            # Final Verdict Only
            if is_spam:
                st.markdown("""
                    <div class="spam-warning">
                        <h1 style="color: #ff4444; font-size: 3rem;">🚨 SPAM</h1>
                        <p style="color: #ff8888; font-size: 1.5rem;">This message is SPAM!</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div class="ham-success">
                        <h1 style="color: #00ff00; font-size: 3rem;">✅ NOT SPAM</h1>
                        <p style="color: #88ff88; font-size: 1.5rem;">This message is NOT spam!</p>
                    </div>
                """, unsafe_allow_html=True)

# -------- Footer --------
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: rgba(255,255,255,0.5); padding: 1rem;">
        <p>🔒 Spam Detection System | Powered by Keyword Filtering</p>
    </div>
""", unsafe_allow_html=True)