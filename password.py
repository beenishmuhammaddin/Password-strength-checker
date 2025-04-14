import streamlit as st
import re

# 🇵🇰 BEENISH'S PAKISTANI-STYLE DESIGN
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');
    
    /* Mehndi-inspired header */
    .beenish-header {{
        background: linear-gradient(to right, #8B814C, #FD0E35);
        font-family: 'Noto Nastaliq Urdu', serif;
        color: white;
        font-size: 42px;
        text-align: center;
        padding: 20px;
        border: 3px dashed #FFC324;
        border-radius: 0 30px 0 30px;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(139,129,76,0.3);
    }}
    
    /* Truck art-inspired card */
    .beenish-card {{
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><path fill="%234B0082" fill-opacity="0.05" d="M30,10 Q50,5 70,10 T90,30 Q95,50 90,70 T70,90 Q50,95 30,90 T10,70 Q5,50 10,30 T30,10"/></svg>');
        border: 2px solid #1E90FF;
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 5px 15px rgba(30,144,255,0.2);
    }}
    
    /* Basant kite button */
    .stButton>button {{
        background: linear-gradient(45deg, #FD0E35, #FFC324) !important;
        color: #4B0082 !important;
        font-weight: 800 !important;
        font-size: 20px !important;
        border-radius: 5px 20px 5px 20px !important;
        transform: rotate(-2deg);
        transition: all 0.3s !important;
    }}
    .stButton>button:hover {{
        transform: rotate(2deg) scale(1.05) !important;
    }}
    
    /* Strength meter like truck speedometer */
    .strength-meter {{
        height: 30px;
        background: linear-gradient(to right, 
            #FD0E35, #FFC324, #1E90FF, #8B814C);
        border-radius: 15px;
        position: relative;
        overflow: hidden;
    }}
    .strength-meter::after {{
        content: "";
        position: absolute;
        left: calc(var(--strength)*20%);
        top: 0;
        bottom: 0;
        width: 5px;
        background: white;
        box-shadow: 0 0 10px white;
    }}
</style>
""", unsafe_allow_html=True)

# 🎪 PAKISTANI-STYLE HEADER
st.markdown(f"""
<div class="beenish-header">
    <div>🪁 BEENISH KA <span style="color:#FFC324">PASSWORD</span> MAHAL 🪁</div>
    <div style="font-size:18px; margin-top:10px">Chai se strong, Lahore Fort se secure!</div>
</div>
""", unsafe_allow_html=True)

# 🏗️ MAIN CARD WITH TRUCK ART FLAIR
with st.container():
    st.markdown("""
    <div class="beenish-card">
        <div style="text-align:center; font-size:24px; color:#4B0082; margin-bottom:20px">
        <b>🛡️ Apka password check karwain!</b>
        </div>
        <div style="text-align:center; color:#1E90FF">
        <i>"Kamyabi ka raaz: mazboot password!"</i>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 🔑 PASSWORD INPUT WITH MEHNDI BORDERS
password = st.text_input(
    "🔐 Apna secret password daalen:", 
    type="password",
    help="BEENISH TIP: Password mein shadi ka mehndi jitna complex rakhen!",
    key="desi_password"
)

# 💪 STRENGTH CHECK FUNCTION WITH PAKISTANI FLAVOR
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        score += 2
        feedback.append("🟢 Wah! yeh hota hy password (12+ characters)")
    elif len(password) >= 8:
        score += 1
        feedback.append("🟡 Theek hai, lekin awesome nahi (8+ characters)")
    else:
        feedback.append("🔴 Too short! Chai cup se zyada lamba karo")
    
    # Complexity checks
    checks = [
        (r"[A-Z]", "🔵 Upar wala case add karen (A-Z)"),
        (r"[a-z]", "🔵 Neechay wala case add karen (a-z)"),
        (r"\d", "🔵 Kuch numbers dalen (0-9)"),
        (r"[!@#$%^&*]", "🔵 Special characters like biryani masala"),
        (r".{16,}", "🏆 Bonus! Motorway jitna lamba password")
    ]
    
    for pattern, message in checks:
        if re.search(pattern, password):
            score += 1
        else:
            feedback.append(message)
    
    return min(score, 5), feedback

# 🚀 CHECK BUTTON
if st.button("🪁 Password check karo!", key="desi_button"):
    if password:
        score, feedback = check_password_strength(password)
        
        # Visual meter
        st.markdown(f"""
        <div style="margin: 20px 0;">
            <div class="strength-meter" style="--strength:{score};"></div>
            <div style="text-align:center; font-weight:bold; color:#4B0082; margin-top:10px">
                {['❌ Nakhray Wala', '⚠️ Patakha', '👍 Theek Thaak', '💪 Khaas', '🏆 King/Queen of Passwords'][score]}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Feedback
        with st.container():
            st.markdown('<div class="beenish-card">', unsafe_allow_html=True)
            if score == 5:
                st.success("""
                🌟 **BEENISH APPROVED!**  
                Yeh password hai Khyber Pass jitna mazboot!
                """)
            elif score >= 3:
                st.warning("""
                ⚠️ **Chalega...**  
                Lekin Ami ke purse jitna secure nahi hai!
                """)
            else:
                st.error("""
                💥 **Nahi Chalega!**  
                Yeh to Pakistani hukumat jitna kamzor hai!
                """)
            
            if feedback:
                st.markdown("### 💡 BEENISH KE TOTKAY:")
                for tip in feedback:
                    st.write(f"- {tip}")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("""
        🚨 **Arrey Bhai!**  
        Password to dalo pehle!
        """)

# 🌸 FOOTER WITH PAKISTANI CHARM
st.markdown(f"""
<div style="text-align:center; color:#8B814C; margin-top:40px; font-family:'Noto Nastaliq Urdu'">
    <b>~ Bana diya BEENISH ne ~</b><br>
    <div style="font-size:14px; margin-top:10px">
    Lahore se Karachi tak secure passwords ka wada!
    </div>
</div>
""", unsafe_allow_html=True)