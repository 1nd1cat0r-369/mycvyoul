import streamlit as st
import os

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(page_title="CV | Information Systems Specialist", page_icon="🖥️", layout="wide")

# --- ESTILOS CSS (Dashboard / Terminal Oscura) ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; font-family: 'Consolas', monospace; }
    h1, h2, h3 { color: #58a6ff; font-family: 'Segoe UI', sans-serif; margin-bottom: 0px; }
    
    /* Tarjetas para la experiencia laboral */
    .exp-card {
        background-color: #161b22;
        border-left: 4px solid #238636;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .cert-box {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
        font-size: 0.9em;
    }
    .highlight { color: #2ea043; font-weight: bold; }
    hr { border-color: #30363d; }
    </style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL (Sidebar) ---
with st.sidebar:
    # 2. SECCIÓN DE FOTOGRAFÍA
    # Si existe el archivo perfil.jpg lo muestra, si no, pone un cuadro gris de prueba
    if os.path.exists("perfil.jpg"):
        st.image("perfil.jpg", width="stretch")
    else:
        st.image("https://dummyimage.com/300x300/161b22/8b949e&text=FOTO+AQUI", width="stretch")
    
    st.title("Joel Hernandez")
    st.subheader("Information Systems Specialist")
    
    # 3. SECCIÓN DE CONTACTO
    st.write("---")
    st.write("### 📞 Contact Info")
    st.write("📍 Zapopan, Jalisco, MX")
    st.write("📧 jhc.soporte@gmail.com") # <-- Reemplaza con tu correo
    st.write("📱 +52 ")    # <-- Reemplaza con tu teléfono
    st.markdown("[🔗 **LinkedIn**](www.linkedin.com/in/joel-hernandez-838ba9271)")
    st.markdown("[🐙 **GitHub**](https://github.com/1nd1cat0r-369)")
    
    # 4. BOTÓN DE DESCARGA PDF
    st.write("---")
    if os.path.exists("cv_joel.pdf"):
        with open("cv_joel.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
            
        st.download_button(
            label="📄 Descargar CV (PDF)",
            data=pdf_bytes,
            file_name="cv_joel.pdf",
            mime="application/pdf"
        )
    else:
        st.info("💡 Coloca tu archivo 'cv_joel.pdf' en la carpeta para activar la descarga.")

    st.write("---")
    
    # 5. STACK TÉCNICO E IDIOMAS (Lo que ya teníamos)
    st.write("### 🛠️ Core Tech Stack")
    st.code("Routing & Switching\nTCP/IP, DHCP, DNS\nWindows Server & Linux\nCybersecurity (CEH)\nPython\nVPN's\nVirtualization VMWARE and Virtual Box", language="text")
    
    st.write("---")
    st.write("### 🌐 Languages")
    st.write("🇪🇸 **Spanish:** Native")
    st.write("🇺🇸 **English:** B1–B2 (In Progress)")
    
    st.write("---")
    st.caption("💡 10 years of IT experience transitioning four years ago into networks  and ethical hacking.")

# --- CABECERA PRINCIPAL ---
st.title("PROFESSIONAL SUMMARY")
st.write("""
Information Systems Specialist with **10 years of experience** in the design, implementation, and maintenance of computer networks. 
Skilled in information security, operating system management (Windows, macOS, Linux, terminal usage), and systems administration. 
Possesses strong problem-solving skills, teamwork abilities, soft skills, and critical thinking.
""")
st.write("---")

# --- CUERPO PRINCIPAL (Columnas) ---
col_exp, col_cert = st.columns([2, 1])

with col_exp:
    st.header("💼 Professional Experience")
    
    st.markdown("""
    <div class="exp-card">
        <h3>Network Infrastructure Technician – IT Support</h3>
        <p style="color:#8b949e; margin-top:5px;"><i>Secretaría de Transporte Jalisco | June 2024 – Present</i></p>
        <ul>
            <li>Participated in multiple network installation projects within and outside the state.</li>
            <li>Provided support for operating systems and resolved LAN and WiFi network issues.</li>
            <li>Applied knowledge of network protocols (<span class="highlight">TCP, IP, DHCP, DNS, SMTP, FTP</span>).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="exp-card">
        <h3>Network Engineer & Technical Support</h3>
        <p style="color:#8b949e; margin-top:5px;"><i>Consulate of Colombia in Guadalajara | June 2018 – May 2024</i></p>
        <ul>
            <li>Designed and implemented network infrastructure.</li>
            <li>Maintained and updated Windows servers and storage systems.</li>
            <li>Provided remote support, configured VPN connections, and monitored WiFi networks.</li>
            <li>Performed incremental backups and disk cloning.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="exp-card">
        <h3>IT Support Technician</h3>
        <p style="color:#8b949e; margin-top:5px;"><i>POSMEX | 2007 – 2017</i></p>
        <ul>
            <li>Delivered technical support for hardware and connectivity issues.</li>
            <li>Configured and maintained network equipment including routers and switches.</li>
            <li>Installed POS systems for major restaurant chains (Outback Steakhouse, Chilis, Wings, etc.).</li>
            <li>Extensive experience in assembling desktops and high-performance/gaming computers.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_cert:
    st.header("🛡️ Certifications")

    st.markdown("""
        <div class="cert-box">
            <strong>Teslag Training (2026)</strong><br>
            <span style="color:#58a6ff;">✅ Advanced Course (CCNA)</span> - <i>40 hours Apr 2026</i>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cert-box">
        <strong>CertJoin (2024)</strong><br>
        <span style="color:#58a6ff;">✅ Certified Ethical Hacker (CEH)</span> - <i>Oct 2024</i>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cert-box">
        <strong>Hacker Mentor Academy (2024)</strong><br>
        • Networking Fundamentals for Pentesters<br>
        • Linux Certification for Pentesters<br>
        • Junior Pentester Specialization (40h)<br>
        • Gamified Ethical Hacking
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cert-box">
        <strong>CISCO Networking Academy (2024)</strong><br>
        • Intro to Cybersecurity<br>
        • Networking & OS Basics<br>
        • Computer Hardware Basics
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.header("🎓 Education")
    st.write("**Bachelor’s Degree in Information Technologies**")
    st.caption("Universidad de Guadalajara Virtual (Incomplete)")