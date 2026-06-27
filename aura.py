
import streamlit as st
import random

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="L'Aura Scanner Hardcore v3.0", page_icon="🤬", layout="centered")

# --- STYLE CHIC & SOMBRE (CSS) ---
st.markdown("""
    <style>
    .main {
        background-color: #05000a;
        color: #f5f5f5;
    }
    .stButton>button {
        background-color: #d4af37;
        color: #05000a;
        border-radius: 12px;
        border: 2px solid #b8860b;
        padding: 12px 25px;
        font-weight: bold;
        width: 100%;
        font-size: 1.1em;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff3366;
        color: #fff;
        box-shadow: 0px 0px 25px #ff3366;
        transform: scale(1.02);
    }
    .question-card {
        background-color: rgba(255, 255, 255, 0.02);
        padding: 35px;
        border-radius: 25px;
        border: 1px solid rgba(212, 175, 55, 0.2);
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.7);
    }
    h1, h2, h3 {
        color: #d4af37 !important;
        font-family: 'Impact', sans-serif;
    }
    .result-aura {
        font-size: 4em;
        font-weight: bold;
        color: #ff3366;
        text-shadow: 0px 0px 30px rgba(255, 51, 102, 0.8);
    }
    </style>
    """, unsafe_allow_html=True)

# --- BANQUE DE QUESTIONS COMPLETEMENT CRUES & PROVOCANTES ---
# 20 questions à gros enjeux de points (Positif max : +5000 / Négatif max : -8000)
all_questions = [
    {
        "q": "Tu te viandes royalement sur les escaliers devant tout le lycée/bureau. Que fais-tu ?",
        "options": [
            ("Je me relève d'un coup sec, je pète un câble et je crie : 'C'EST LE SHOW !'", 4000),
            ("Je chiale par terre en position fœtale comme une grosse merde", -8000),
            ("Je rampe discrètement vers la sortie pour aller mourir ailleurs", -5000),
            ("Je tape un salto arrière pour rattraper le coup (je me repète la gueule)", -2000)
        ]
    },
    {
        "q": "Tu rates le penalty décisif à la dernière minute du match. Tout le monde te regarde.",
        "options": [
            ("Je baisse mon short, je montre mon cul au gardien et je me barre du terrain", 5000),
            ("Je dis que le ballon a une forme de couille et que c'est pas de ma faute", -3000),
            ("Je m'excuse à genoux en bavant sur les crampons du capitaine", -8000),
            ("Je regarde le ciel en mode boss final de manga et je marche lentement vers les vestiaires", 3500)
        ]
    },
    {
        "q": "Ton crush te regarde fixement avec un grand sourire au loin.",
        "options": [
            ("Je lui fais un vieux clin d'œil baveux et je me prends un poteau dans la tronche", -6000),
            ("Je lui sors un doigt d'honneur avec un regard de psychopathe", 3000),
            ("Je panique et je renverse ma boisson chaude sur mon propre entrejambe", -5000),
            ("Je lève un sourcil avec un sourire en coin en mode 'je sais que tu me veux'", 4500)
        ]
    },
    {
        "q": "On te file un cadeau d'anniversaire d'une nullité absolue (un vieux pull moche).",
        "options": [
            ("Je le balance direct à la poubelle devant la personne en disant 'c'est de la merde'", -4000),
            ("Je le mets direct et je dis 'le flow est monstrueux, jalousez pas les crevards'", 4000),
            ("Je souris hypocritement en bégayant 'merki beaucoup' d'une voix de gogol", -3000),
            ("Je le revends sur Vinted en direct sur mon téléphone", 2000)
        ]
    },
    {
        "q": "Tu rentres dans une soirée, mais personne ne calcule ton arrivée.",
        "options": [
            ("Je tape sur une table et je hurle : 'Fermez vos gueules, le roi est là !'", 5000),
            ("Je pars me cacher dans la cuisine pour bouffer des chips tout seul", -4000),
            ("Je squatte le canapé en faisant semblant d'envoyer des messages importants", -2500),
            ("Je commence à éteindre les lumières pour forcer tout le monde à me regarder", 3000)
        ]
    },
    {
        "q": "Un relou essaie de te vanner méchamment en public pour se rendre intéressant.",
        "options": [
            ("Je lui sors un dossier tellement sale sur sa daronne qu'il commence à chialer", 5000),
            ("Je rigole bêtement en disant 'arrête c'est pas gentil'", -5000),
            ("Je le regarde en silence pendant 10 secondes avec un mépris total, puis je l'ignore", 4000),
            ("Je lui propose une bagarre (je me fais démonter par un mec de 50kg)", -7000)
        ]
    },
    {
        "q": "Tu as une tache suspecte de bouffe sur ton jean blanc au niveau de la braguette.",
        "options": [
            ("Je dessine une flèche autour pour assumer mon style de déguisé", 3000),
            ("Je frotte avec de la salive (ça ressemble maintenant à de la pisse)", -6000),
            ("Je marche en me cachant le sexe avec mes deux mains en mode victime", -5000),
            ("Je sors ma bite en disant 'Voilà, au moins c'est clair'", 5000)
        ]
    },
    {
        "q": "Tu te rends compte au bout d'une heure que tu as ton papier toilette collé à la chaussure.",
        "options": [
            ("Je le ramasse, je le renifle et je le jette sur un passant", -5000),
            ("Je dis que c'est une collab exclusive avec Off-White", 4000),
            ("Je l'enlève en speed en faisant semblant de lacer ma chaussure comme un lâche", -1500),
            ("Je m'en fous royalement et je continue de marcher comme un boss", 3000)
        ]
    },
    {
        "q": "On t'accuse à tort d'avoir lâché une caisse monumentale dans l'ascenseur.",
        "options": [
            ("Je dénonce le vieux à côté de moi avec une mauvaise foi légendaire", 2000),
            ("Je prends une grande inspiration et je dis : 'De rien pour le parfum, bande de gueux'", 4500),
            ("Je deviens tout rouge, je bégaie et je m'excuse alors que c'est même pas moi", -6000),
            ("Je lâche un vrai prout encore plus bruyant pour montrer c'est quoi le vrai talent", 5000)
        ]
    },
    {
        "q": "Dernière question de ce test de dégénérés : Pourquoi tu es encore là ?",
        "options": [
            ("Parce que mon aura est divine et que je veux vous pisser dessus", 5000),
            ("Parce que je me fais chier en vacances", 0),
            ("Pour prouver que mes potes sont des grosses victimes sans couilles", 4000),
            ("Je sais pas, je suis juste un pigeon de l'espace", -4000)
        ]
    }
]

# --- INITIALISATION ET MELANGEMENT ---
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.aura_score = 0
    st.session_state.name = ""
    # On pioche 10 questions aléatoires parmi les 10 hyper-hardcore
    st.session_state.selected_questions = random.sample(all_questions, min(len(all_questions), 10))

# --- LOGIQUE DU SCANNER ---
st.title("🤬 L'AURA SCANNER ULTRA-HARDCORE v3.0")
st.write("---")

if st.session_state.step == 0:
    st.markdown('<div class="question-card"><h3>⚠️ ZONE DE HAUTE TOXICITÉ</h3><p>Ici on ne rigole pas avec le charisme. Entrez votre blaze si vous en avez dans le pantalon.</p></div>', unsafe_allow_html=True)
    name_input = st.text_input("Ton Blaze (ou ton pseudo de lâche) :")
    if st.button("DÉMARRER LE MASSACRE"):
        if name_input:
            st.session_state.name = name_input
            st.session_state.step = 1
            st.rerun()
        else:
            st.warning("Écris ton nom espèce de trou du cul, on fait pas un test anonyme.")

elif 1 <= st.session_state.step <= 10:
    idx = st.session_state.step - 1
    current_q = st.session_state.selected_questions[idx]
    
    st.subheader(f"Dilemme de Bâtard {st.session_state.step} sur 10")
    st.markdown(f'<div class="question-card"><h3>{current_q["q"]}</h3></div>', unsafe_allow_html=True)
    
    # Boutons de réponse
    for option_text, points in current_q["options"]:
        if st.button(option_text):
            st.session_state.aura_score += points
            st.session_state.step += 1
            st.rerun()

else:
    # --- RANGS ULTRA CRUS ET GROS ECARTS ---
    score = st.session_state.aura_score
    name = st.session_state.name
    
    if score < -30000:
        rank = "L'AVORTON SANS ÂME 💩"
        desc = "Ta simple existence donne la chiasse à l'univers. Même ton ombre s'est barrée pour ne pas être associée à ta gueule de victime. Arrête de creuser ton trou, t'es déjà au centre de la Terre."
    elif score < -10000:
        rank = "LA GROSSE SERPILLIÈRE HUMAINE 🤡"
        desc = "T'es le genre de mec qui s'excuse quand on lui marche sur les pieds. Ton charisme est aussi plat qu'une bière sans bulles oubliée au soleil. Bref, t'es un paillasson."
    elif score < 0:
        rank = "LE PNJ CHIANT DE SERVICE 😐"
        desc = "Franchement, si tu disparaissais demain, même Siri s'en battrait les couilles. Tu sers de décor. Réveille-toi un peu ou va t'acheter une personnalité."
    elif score < 15000:
        rank = "LE BG DU QUARTIER 🚬"
        desc = "Bon, ça passe. T'as une petite gueule sympa, tu sais aligner deux mots sans bégayer comme un gogol devant ton crush. Mais calme-toi, t'es pas encore le roi."
    elif score < 30000:
        rank = "MONSTRUEUX MAIN CHARACTER ⚡"
        desc = "Là, on parle ! Tu passes les portes de travers tellement t'as des grosses couilles. Ton flow fait rager les mecs et mouiller les meufs. Continue comme ça, sale bête."
    elif score < 45000:
        rank = "LE GRAND PATRON DE LA ZONE 👑"
        desc = "Tu pisses sur la concurrence sans aucune pression. Tu claques des doigts et tout le monde ferme sa gueule. T'as un niveau de charisme presque insultant."
    else:
        rank = "DIEU LE PÈRE (ET VOUS ÊTES TOUS SES PUTES) 🌌"
        desc = "L'univers entier s'agenouille pour te sucer le grand orteil. Tu ne marches pas, tu lévites au-dessus de la plèbe. Fermez tous vos gueules, l'Empereur suprême de l'Aura est dans la place !"

    st.balloons()
    st.markdown(f"""
        <div class="question-card">
            <h2>Rapport d'Aura de {name}</h2>
            <div class="result-aura">{score} PTS</div>
            <h3>Verdict : {rank}</h3>
            <p style="font-size: 1.2em; line-height: 1.5; margin-top: 15px;">{desc}</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Relancer un Nouveau Scan (pour tester tes couilles)"):
        st.session_state.step = 0
        st.session_state.aura_score = 0
        st.session_state.selected_questions = random.sample(all_questions, min(len(all_questions), 10))
        st.rerun()


