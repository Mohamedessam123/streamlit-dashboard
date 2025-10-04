import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ============================================
# 📊 البيانات - غير هنا فقط وكل الرسومات هتتحدث تلقائياً!
# ============================================

# إجماليات عامة
summary = {
    'total_offices': 767,
    'total_transactions': 55485,
    'morning_transactions': 47841,
    'evening_transactions': 8932,
    'digital_transactions': 1265,
    'direct_transactions': 54221
}

# توزيع المعاملات حسب المحافظات (أعلى 15)
governorates_data = [
    {'المحافظة': 'القاهرة', 'المعاملات': 8447, 'النسبة': 15},
    {'المحافظة': 'الجيزة', 'المعاملات': 5986, 'النسبة': 11},
    {'المحافظة': 'الشرقية', 'المعاملات': 3763, 'النسبة': 7},
    {'المحافظة': 'الدقهلية', 'المعاملات': 3719, 'النسبة': 7},
    {'المحافظة': 'الإسكندرية', 'المعاملات': 3715, 'النسبة': 7},
    {'المحافظة': 'القليوبية', 'المعاملات': 2770, 'النسبة': 5},
    {'المحافظة': 'البحيرة', 'المعاملات': 2721, 'النسبة': 5},
    {'المحافظة': 'الغربية', 'المعاملات': 2580, 'النسبة': 5},
    {'المحافظة': 'المنوفية', 'المعاملات': 2520, 'النسبة': 5},
    {'المحافظة': 'المنيا', 'المعاملات': 2268, 'النسبة': 4},
    {'المحافظة': 'كفر الشيخ', 'المعاملات': 2017, 'النسبة': 4},
    {'المحافظة': 'سوهاج', 'المعاملات': 2004, 'النسبة': 4},
    {'المحافظة': 'أسيوط', 'المعاملات': 1803, 'النسبة': 3},
    {'المحافظة': 'بني سويف', 'المعاملات': 1586, 'النسبة': 3},
    {'المحافظة': 'قنا', 'المعاملات': 1302, 'النسبة': 2}
]

# معدل الإصدار حسب الساعة
hourly_data = [
    {'الساعة': '8:30-10:00', 'المعاملات': 4260},
    {'الساعة': '10:00-11:00', 'المعاملات': 7312},
    {'الساعة': '11:00-12:00', 'المعاملات': 7731},
    {'الساعة': '12:00-13:00', 'المعاملات': 7325},
    {'الساعة': '13:00-14:00', 'المعاملات': 5860},
    {'الساعة': '14:00-17:00', 'المعاملات': 6414},
    {'الساعة': 'مسائي', 'المعاملات': 9439}
]

# أعلى المكاتب إصداراً
top_offices_data = [
    {'المكتب': 'مكتب توثيق الاهرام', 'صباحي': 485, 'مسائي': 370, 'الإجمالي': 615},
    {'المكتب': 'الخانكة', 'صباحي': 398, 'مسائي': 213, 'الإجمالي': 398},
    {'المكتب': 'الجيزة', 'صباحي': 393, 'مسائي': 140, 'الإجمالي': 393},
    {'المكتب': 'حلوان المطور', 'صباحي': 346, 'مسائي': 174, 'الإجمالي': 348},
    {'المكتب': 'شبرا الخيمة', 'صباحي': 338, 'مسائي': 99, 'الإجمالي': 338},
    {'المكتب': 'السادات', 'صباحي': 331, 'مسائي': 162, 'الإجمالي': 331},
    {'المكتب': 'العاشر من رمضان', 'صباحي': 308, 'مسائي': 123, 'الإجمالي': 308},
    {'المكتب': 'بنى سويف', 'صباحي': 287, 'مسائي': 101, 'الإجمالي': 287},
    {'المكتب': 'كفر الدوار', 'صباحي': 281, 'مسائي': 94, 'الإجمالي': 281},
    {'المكتب': 'الغردقة', 'صباحي': 280, 'مسائي': 84, 'الإجمالي': 280}
]

# ============================================
# إعداد الصفحة
# ============================================

st.set_page_config(
    page_title="لوحة تحليل مكاتب التوثيق",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS لتحسين المظهر
st.markdown("""
<style>
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
    }
    h1, h2, h3 {
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# العنوان الرئيسي
# ============================================

st.title("📊 لوحة تحليل مكاتب التوثيق")
st.markdown("### يوم الثلاثاء 30-09-2025")
st.divider()

# ============================================
# البطاقات الإحصائية
# ============================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="🏢 إجمالي المكاتب",
        value=f"{summary['total_offices']:,}"
    )

with col2:
    st.metric(
        label="📝 إجمالي المعاملات",
        value=f"{summary['total_transactions']:,}"
    )

with col3:
    st.metric(
        label="🌅 معاملات صباحية",
        value=f"{summary['morning_transactions']:,}"
    )

with col4:
    st.metric(
        label="🌙 معاملات مسائية",
        value=f"{summary['evening_transactions']:,}"
    )

st.divider()

# ============================================
# التبويبات
# ============================================

tab1, tab2, tab3, tab4 = st.tabs([
    "نظرة عامة",
    "توزيع المحافظات", 
    "الأداء الزمني",
    "أعلى المكاتب"
])

# ============================================
# تبويب 1: نظرة عامة
# ============================================

with tab1:
    col1, col2 = st.columns(2)
    
    # مصر الرقمية vs المباشر
    with col1:
        st.subheader("مصر الرقمية vs المباشر")
        
        digital_direct_df = pd.DataFrame({
            'النوع': ['مصر الرقمية', 'مباشر من المكتب'],
            'العدد': [summary['digital_transactions'], summary['direct_transactions']]
        })
        
        fig1 = px.pie(
            digital_direct_df,
            values='العدد',
            names='النوع',
            color_discrete_sequence=['#10b981', '#3b82f6'],
            hole=0.4
        )
        fig1.update_traces(
            textposition='inside',
            textinfo='percent+label',
            textfont_size=14
        )
        fig1.update_layout(
            height=400,
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.2)
        )
        st.plotly_chart(fig1, use_container_width=True)
        
        # عرض الأرقام
        st.metric("مصر الرقمية", f"{summary['digital_transactions']:,}")
        st.metric("مباشر من المكتب", f"{summary['direct_transactions']:,}")
    
    # صباحي vs مسائي
    with col2:
        st.subheader("الفترة الصباحية vs المسائية")
        
        period_df = pd.DataFrame({
            'الفترة': ['صباحي', 'مسائي'],
            'العدد': [summary['morning_transactions'], summary['evening_transactions']]
        })
        
        fig2 = px.pie(
            period_df,
            values='العدد',
            names='الفترة',
            color_discrete_sequence=['#f59e0b', '#8b5cf6'],
            hole=0.4
        )
        fig2.update_traces(
            textposition='inside',
            textinfo='percent+label',
            textfont_size=14
        )
        fig2.update_layout(
            height=400,
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.2)
        )
        st.plotly_chart(fig2, use_container_width=True)
        
        # عرض الأرقام
        st.metric("صباحي", f"{summary['morning_transactions']:,}")
        st.metric("مسائي", f"{summary['evening_transactions']:,}")

# ============================================
# تبويب 2: المحافظات
# ============================================

with tab2:
    st.subheader("أعلى 15 محافظة في الإصدار")
    
    gov_df = pd.DataFrame(governorates_data)
    
    fig3 = px.bar(
        gov_df,
        y='المحافظة',
        x='المعاملات',
        orientation='h',
        color='المعاملات',
        color_continuous_scale='Blues',
        text='المعاملات'
    )
    fig3.update_traces(
        texttemplate='%{text:,}',
        textposition='outside'
    )
    fig3.update_layout(
        height=600,
        showlegend=False,
        yaxis={'categoryorder':'total ascending'}
    )
    st.plotly_chart(fig3, use_container_width=True)
    
    # عرض الجدول
    st.dataframe(
        gov_df.style.format({'المعاملات': '{:,}', 'النسبة': '{}%'}),
        use_container_width=True,
        hide_index=True
    )

# ============================================
# تبويب 3: الأداء الزمني
# ============================================

with tab3:
    st.subheader("معدل الإصدار خلال ساعات اليوم")
    
    hourly_df = pd.DataFrame(hourly_data)
    
    fig4 = px.line(
        hourly_df,
        x='الساعة',
        y='المعاملات',
        markers=True,
        line_shape='spline'
    )
    fig4.update_traces(
        line_color='#10b981',
        line_width=3,
        marker=dict(size=10, color='#10b981')
    )
    fig4.update_layout(
        height=500,
        hovermode='x unified'
    )
    st.plotly_chart(fig4, use_container_width=True)
    
    # عرض الجدول
    st.dataframe(
        hourly_df.style.format({'المعاملات': '{:,}'}),
        use_container_width=True,
        hide_index=True
    )

# ============================================
# تبويب 4: أعلى المكاتب
# ============================================

with tab4:
    st.subheader("أعلى 10 مكاتب إصداراً")
    
    offices_df = pd.DataFrame(top_offices_data)
    
    fig5 = go.Figure()
    
    fig5.add_trace(go.Bar(
        y=offices_df['المكتب'],
        x=offices_df['صباحي'],
        name='صباحي',
        orientation='h',
        marker=dict(color='#f59e0b')
    ))
    
    fig5.add_trace(go.Bar(
        y=offices_df['المكتب'],
        x=offices_df['مسائي'],
        name='مسائي',
        orientation='h',
        marker=dict(color='#8b5cf6')
    ))
    
    fig5.update_layout(
        barmode='stack',
        height=500,
        yaxis={'categoryorder':'total ascending'},
        legend=dict(orientation="h", yanchor="bottom", y=-0.2)
    )
    
    st.plotly_chart(fig5, use_container_width=True)
    
    # عرض الجدول
    st.dataframe(
        offices_df.style.format({'صباحي': '{:,}', 'مسائي': '{:,}', 'الإجمالي': '{:,}'}),
        use_container_width=True,
        hide_index=True
    )

# ============================================
# Footer
# ============================================

st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>تم إنشاء هذه اللوحة باستخدام Streamlit</p>
    <p>لتحديث البيانات، قم بتعديل المتغيرات في أول الكود</p>
</div>
""", unsafe_allow_html=True)