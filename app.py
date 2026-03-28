import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="ذكرى فاجعة البقيع",
    page_icon="🏴",
    layout="wide"
)

# 2. هندسة التصميم (CSS) - يمناوي بالكامل ومتوافق مع الهاتف
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Aref+Ruqaa:wght@400;700&display=swap');

    /* ضبط الاتجاه العام للموقع ليكون من اليمين لليسار */
    .stApp {
        background: radial-gradient(circle, #1a1a1a 0%, #000000 100%);
        color: #fdfdfd;
        direction: rtl; /* يمناوي */
        text-align: right;
    }

    header, footer {visibility: hidden;}

    /* العناوين */
    h1 {
        font-family: 'Aref Ruqaa', serif;
        color: #b08d57 !important;
        text-align: center !important;
        font-size: clamp(2.2rem, 8vw, 4.5rem) !important;
        margin-top: -30px;
    }
    
    h2 {
        font-family: 'Aref Ruqaa', serif;
        color: #b08d57 !important;
        text-align: center !important;
        font-size: clamp(1.6rem, 5vw, 2.8rem) !important;
    }

    /* المحتوى الرئيسي يمناوي */
    .main-content {
        background: rgba(10, 10, 10, 0.95);
        border-right: clamp(5px, 1vw, 10px) solid #b08d57; /* الخط الذهبي على اليمين */
        border-left: none;
        padding: clamp(20px, 4vw, 45px);
        border-radius: 15px;
        line-height: 2;
        font-family: 'Amiri', serif;
        font-size: clamp(1.2rem, 4vw, 1.9rem);
        margin-bottom: 30px;
        text-align: justify;
        direction: rtl;
    }

    /* أزرار الأئمة - يمناوية التصميم */
    .stButton > button {
        width: 100% !important;
        min-height: clamp(90px, 15vh, 130px) !important;
        background: #0d0d0d !important;
        color: #b08d57 !important;
        border: 2px solid #222 !important;
        border-bottom: 5px solid #b08d57 !important;
        border-radius: 15px !important;
        font-family: 'Aref Ruqaa', serif !important;
        font-size: clamp(1.3rem, 4vw, 1.9rem) !important;
        transition: 0.4s !important;
        margin-bottom: 15px !important;
        direction: rtl;
    }
    
    .stButton > button:hover {
        border-color: #b08d57 !important;
        transform: translateY(-5px);
    }

    /* صناديق النبذة - يمناوية */
    .stAlert {
        background-color: rgba(25, 25, 25, 0.98) !important;
        color: #ffffff !important;
        border: 1px solid #b08d57 !important;
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Amiri', serif;
        font-size: clamp(1.1rem, 3.8vw, 1.6rem) !important;
        padding: 25px !important;
    }

    /* ضمان ترتيب الأعمدة من اليمين لليسار في الحاسوب */
    [data-testid="stHorizontalBlock"] {
        direction: rtl !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. المحتوى الرئيسي
st.markdown("<h1>٨ شوال.. هدم القباب الطاهرة</h1>", unsafe_allow_html=True)

# ترتيب الصور يمناوي (من اليمين لليسار)
col_img1, col_img2 = st.columns(2)
with col_img1:
    st.image("https://shiawave.com/ar/wp-content/uploads/2021/05/1-11.jpg", caption="آثار الهدم في بقيع الغرقد", use_container_width=True)
with col_img2:
    st.image("https://alkafeel.net/photos/images/1559868735.jpg", caption="مظلومية القبور المهدومة", use_container_width=True)

st.markdown("""
<div class="main-content">
    لقد كان الثامن من شوال عام 1344هـ فاجعةً كبرى اهتز لها عرش الرحمن، حيث تجرأت معاول الظلم والعدوان على هدم أضرحة أئمة البقيع (عليهم السلام). 
    تلك القباب التي كانت مزاراً للمحبين ومناراتٍ للهدى، أصبحت اليوم قبوراً مهدمة تذرف لها العيون دماً لا دمعاً. 
    نواسي اليوم ولي الله الأعظم الحجة بن الحسن (عجل الله فرجه) بهذا المصاب الجلل.
</div>
""", unsafe_allow_html=True)

# 4. قسم بطاقات الأئمة التفاعلية (مرتبة يمناوي)
st.markdown("<h2>سيرة الأئمة المظلومين في البقيع</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#777; font-size:1.2rem;'>انقر على اسم الإمام لعرض تفاصيل المظلومية والنبذة المختصرة</p>", unsafe_allow_html=True)

# ترتيب الأئمة يبدأ من اليمين (الحسن، السجاد، الباقر، الصادق)
c1, c2, c3, c4 = st.columns([1,1,1,1])

with c1:
    if st.button("الإمام الحسن\nالمجتبى (ع)"):
        st.info("""
        **الإمام الحسن بن علي الزكي (ع):**
        * **كريم أهل البيت:** السبط الأول لرسول الله ﷺ، وُلد في 15 رمضان سنة 3 هـ.
        * **المظلومية:** عانى من خيانة أصحابه، واضطر للصلح حقناً للدماء، ثم سُمّ مسموماً غدراً.
        * **الدفن:** مُنعت جنازته من القرب من جده ﷺ ورُشقت بالسهام، فدُفن مظلوماً في البقيع.
        """)

with c2:
    if st.button("الإمام علي\nالسجاد (ع)"):
        st.info("""
        **الإمام علي بن الحسين (ع):**
        * **زين العابدين:** منبع التقوى، صاحب الصحيفة السجادية ورسالة الحقوق.
        * **المظلومية:** شهد فاجعة كربلاء وهو عليل، وحُمل أسيراً مكبلاً بالأغلال من الكوفة إلى الشام.
        * **الدفن:** قضى حياته بالبكاء على الحسين، ودُفن في البقيع بجوار عمه الحسن.
        """)

with c3:
    if st.button("الإمام محمد\nالباقر (ع)"):
        st.info("""
        **الإمام محمد بن علي الباقر (ع):**
        * **باقر العلم:** لُقب بذلك لعلمه الواسع الذي بقر العلم بقراً واستخرجه.
        * **المظلومية:** حضر واقعة الطف طفلاً، وعاش ضغوط بني أمية حتى استُشهد مسموماً بجين سرج مسموم.
        * **الدفن:** شيد مدرسة علمية كبرى تخرج منها الآلاف، ودُفن في البقيع مع والده وعمه.
        """)

with c4:
    if st.button("الإمام جعفر\nالصادق (ع)"):
        st.info("""
        **الإمام جعفر بن محمد الصادق (ع):**
        * **رئيس المذهب:** تخرج من مدرسته 4000 عالم في مختلف العلوم الشرعية والكونية.
        * **المظلومية:** واجه طغيان المنصور الدوانيقي الذي ضايقه كثيراً حتى استُشهد مسموماً.
        * **الدفن:** هو آخر إمام دُفن في البقيع، لتبقى قبورهم شاهدة على أعظم مظلومية تاريخية.
        """)

# التذييل
st.markdown("<p style='text-align: center; color: #444; margin-top:50px; font-size:1.1rem;'>عظم الله أجورنا وأجوركم | تصميم برمجي سجاد</p>", unsafe_allow_html=True)
