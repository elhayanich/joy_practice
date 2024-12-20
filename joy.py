import streamlit as st
from datetime import date, timedelta

# Fonction pour calculer les croquettes restantes
def calculate_remaining_croquettes(start_date, total_weight, daily_consumption):
    # Date actuelle
    today = date.today()
    
    # Nombre de jours écoulés
    days_elapsed = (today - start_date).days
    
    # Quantité consommée
    consumed = days_elapsed * daily_consumption
    
    # Quantité restante
    remaining = total_weight - consumed
    
    return remaining, days_elapsed

# Interface utilisateur Streamlit
st.title("Gestion des croquettes de mon chat 🐾")

# Entrée des données
st.header("Données de base")
total_weight = st.number_input("Poids initial du paquet (en grammes)", value=1500)
daily_consumption = st.number_input("Consommation quotidienne (en grammes)", value=80 * 3)
start_date = st.date_input("Date de départ", value=date.today().replace(day=1))

# Calcul des croquettes restantes
remaining_croquettes, days_elapsed = calculate_remaining_croquettes(
    start_date, total_weight, daily_consumption
)

# Affichage des résultats
st.header("Résultats")
st.write(f"Nombre de jours écoulés depuis le {start_date}: {days_elapsed} jours.")
st.write(f"Quantité restante de croquettes : {remaining_croquettes:.2f} g")

# Alerte
if remaining_croquettes <= 300:
    st.warning("⚠️ À acheter croquettes !")
elif remaining_croquettes > 0:
    st.success("Tout va bien, les croquettes suffisent pour le moment.")
else:
    st.error("Les croquettes sont épuisées ! 😿")

# Bonus : Suggestion de la prochaine date d'achat
if remaining_croquettes > 0:
    days_left = remaining_croquettes / daily_consumption
    next_purchase_date = date.today() + timedelta(days=int(days_left))
    st.write(f"Date estimée pour acheter un nouveau paquet : {next_purchase_date}")