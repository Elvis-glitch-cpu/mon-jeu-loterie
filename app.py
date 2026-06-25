import streamlit as st
import random 

# Titre du site web
st.title("🎯 Mon Grand Jeu de Loterie en Ligne")

# Choix du nombre secret caché
if 'secret' not in st.session_state:
    st.session_state.secret = random.randint(1, 10)

st.write("L'ordinateur a choisi un nombre entre 1 et 10. À toi de deviner !")

# Case pour taper le nombre
devinette = st.number_input("Entre un nombre :", min_value=1, max_value=10, step=1)

# Bouton de validation
if st.button("Tenter ma chance 🎰"):
    if devinette == st.session_state.secret:
        st.success("🎉 BRAVO ! Tu as gagné la loterie !")
        # Recommencer avec un nouveau nombre secret
        st.session_state.secret = random.randint(1, 10)
    else:
        st.error("❌ Dommage... Ce n'est pas le bon nombre. Réessaye !")
