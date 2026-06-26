import streamlit as st
import random

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="L'Aura Scanner Chic v1.0", page_icon="✨", layout="centered")

# --- STYLE CHIC (CSS) ---
st.markdown("""
    <style>
    .main {
        background-color: #0f051a;
        color: #f5f5f5;
    }
    .stButton>button {
        background-color: #d4af37;
        color: #1a0b2e;
        border-radius: 10px;
        border: none;
        padding: 10px 25px;
        font-weight: bold;
        width: 100%;
        font-size: 1.2em;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #f5f5f5;
        color: #d4af37;
        box-shadow: 0px 0px 15px #d4af37;
    }
    .question-card {
        background-color: rgba(255,255,255,0.05);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #d4af37;
        margin-bottom: 25px;
        text-align: center;
    }
    h1, h2, h3 {
        color: #d4af37 !important;
        font-family: 'Serif';
    }
    .result-aura {
        font-size: 3em;
        font-weight: bold;
        color: #d4af37;
        text-shadow: 0px 0px 20px rgba(212, 175, 55, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# --- INITIALISATION DES VARIABLES ---
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.aura_score = 0
    st.session_state.name = ""

# --- QUESTIONS ---
questions = [
    {
        "q": "Tu trébuches lourdement devant tout le monde. Que fais-tu ?",
        "options": [
            ("Je tape un sprint en faisant semblant que c'était fait exprès", 500),
            ("Je reste au sol et je fais l'étoile de mer", -1000),
            ("Je regarde ma chaussure d'un air accusateur", -200),
            ("Je me relève et je fais une révérence royale", 800)
        ]
    },
    {
        "q": "Tu rates un penalty décisif lors d'un match entre potes.",
        "options": [
            ("Je pleure à chaudes larmes", -5000),
            ("Je dis que c'est à cause de la pelouse", -500),
            ("Je reste immobile avec un regard de Sigma", 1000),
            ("Je vais féliciter le gardien", 500)
        ]
    },
    {
        "q": "Ton crush te regarde fixement. Ta réaction ?",
        "options": [
            ("Je lui fais un clin d'œil (je rate et je cligne des deux yeux)", -1000),
            ("Je fais un petit signe de tête nonchalant", 1500),
            ("Je regarde derrière moi pour voir qui il regarde", -500),
            ("Je tombe de ma chaise", -2000)
        ]
    },
    {
        "q": "On te fait un cadeau vraiment nul. Que dis-tu ?",
        "options": [
            ("C'est quoi cette horreur ?", -2000),
            ("C'est... original. Merci !", 200),
            ("C'est exactement ce qu'il me fallait pour ma collection secrète", 1000),
            ("Je le jette immédiatement", -1000)
        ]
    },
    {
        "q": "Tu arrives en retard à un événement chic.",
        "options": [
            ("J'entre en m'excusant 50 fois", -800),
            ("J'entre comme si j'étais le propriétaire des lieux", 2000),
            ("Je reste caché derrière un rideau", -500),
            ("Je dis 'Désolé, ma licorne était en panne'", 500)
        ]
    },
    {
        "q": "Tu t'aperçois que tu as ton sac à dos ouvert depuis 1 heure.",
        "options": [
            ("Je panique et je vérifie tout", -500),
            ("Je dis 'C'est un nouveau style d'aération'", 1000),
            ("Je marche normalement et je le ferme discrètement", 200),
            ("Je demande à un inconnu de me le fermer", -200)
        ]
    },
    {
        "q": "Quelqu'un te salue, tu réponds, mais il saluait la personne derrière toi.",
        "options": [
            ("Je fais semblant de me gratter la tête", -1500),
            ("Je continue de saluer l'air en mode fantôme", -500),
            ("Je salue carrément la personne derrière aussi", 1200),
            ("Je quitte le pays immédiatement", -5000)
        ]
    },
    {
        "q": "Tu gagnes 1 million d'euros à la loterie.",
        "options": [
            ("Je hurle et je saute partout", 200),
            ("Je demande 'C'est tout ?'", 3000),
            ("Je souris calmement en disant 'C'était prévu'", 5000),
            ("Je m'évanouis sur place", -1000)
        ]
    },
    {
        "q": "Tu es en train de manger et un morceau tombe sur ton t-shirt blanc.",
        "options": [
            ("Je lèche la tache", -3000),
            ("Je dis que c'est une pièce de mode conceptuelle", 1000),
            ("Je nettoie avec de l'eau (ça fait une auréole géante)", -500),
            ("Je retire mon t-shirt et je finis en torse nu", 2500)
        ]
    },
    {
        "q": "Dernière question : Pourquoi fais-tu ce test d'Aura ?",
        "options": [
            ("Parce que je suis le Main Character", 2000),
            ("Parce que je m'ennuie en vacances", 0),
            ("Pour prouver que je suis une divinité", 1500),
            ("C'est quoi l'aura ?", -1000)
        ]
    }
]

# --- LOGIQUE DE L'APPLICATION ---
st.title("🌟 L'Aura Scanner Chic v1.0")
st.write("---")

if st.session_state.step == 0:
    st.markdown('<div class="question-card"><h3>Bienvenue dans l\'Elite</h3><p>Entrez votre nom pour commencer le scan mystique.</p></div>', unsafe_allow_html=True)
    name_input = st.text_input("Votre Nom/Pseudo :")
    if st.button("Lancer le Scan"):
        if name_input:
            st.session_state.name = name_input
            st.session_state.step = 1
            st.rerun()
        else:
            st.warning("Veuillez entrer un nom, c'est plus chic.")

elif 1 <= st.session_state.step <= 10:
    idx = st.session_state.step - 1
    st.subheader(f"Question {st.session_state.step} sur 10")
    st.markdown(f'<div class="question-card"><h3>{questions[idx]["q"]}</h3></div>', unsafe_allow_html=True)
    
    for option_text, points in questions[idx]["options"]:
        if st.button(option_text):
            st.session_state.aura_score += points
            st.session_state.step += 1
            st.rerun()

else:
    # --- RESULTATS FINAUX ---
    score = st.session_state.aura_score
    name = st.session_state.name
    
    if score < -5000:
        rank = "LE GIGA-LOOZER 💀"
        desc = "Ta simple existence crée une dette d'aura mondiale. Cache-toi."
    elif score < 0:
        rank = "AURA FRAGILE 🧊"
        desc = "Tu es comme un yaourt périmé : personne ne veut te toucher."
    elif score < 5000:
        rank = "CITOYEN LAMBDA 😐"
        desc = "Tu es sympa, mais tu n'as pas plus de présence qu'un meuble IKEA."
    elif score < 10000:
        rank = "AURA ÉLITE ✨"
        desc = "Le charisme coule dans tes veines. Tu es le Main Character."
    else:
        rank = "DIVINITÉ DE L'OLYMPE 👑"
        desc = "Tu ne marches pas, tu lévites. Les gens s'inclinent sur ton passage."

    st.balloons()
    st.markdown(f"""
        <div class="question-card">
            <h2>Résultat pour {name}</h2>
            <div class="result-aura">{score} Points</div>
            <h3>Rang : {rank}</h3>
            <p>{desc}</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Recommencer le Scan"):
        st.session_state.step = 0
        st.session_state.aura_score = 0
        st.rerun()
