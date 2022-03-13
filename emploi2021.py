import pandas as pd
import json
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as stc
import plotly.express as px
import seaborn as sns
from streamlit_option_menu import option_menu

sns.set()
logo = "https://www.ville-creteil.fr/img/Une-logo-pole-emploi.jpg"
logo2 = "data:image/jpeg;base64,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"

st.set_page_config(page_icon = logo2,
				   page_title ="Bonsoir !", layout = "wide")

df = pd.read_csv("df_clean2.csv")
departement_geo = json.load(open("departements.geojson", "r"))

liste_dep = sorted(df.NomDept.unique().tolist())
liste_famille = df.famille.unique().tolist()
liste_metier = list(df.metier.unique())


dico_map = {}
for feature in departement_geo["features"]:
    feature['id']=feature['properties']['code']
    dico_map[feature['properties']['nom']] = feature['id']


def heatmap(dep):
    departement = df[df.NomDept == dep]

    dep_tail = departement.groupby(["metier"]).agg({"Nbr_demande":"sum"}).sort_values(by="Nbr_demande", ascending = True).head(10)
    labels_tail = dep_tail.index.values.tolist()

    dep_head = departement.groupby(["metier"]).agg({"Nbr_demande":"sum"}).sort_values(by="Nbr_demande", ascending = True).tail(10)
    labels_head = dep_head.index.values.tolist()


    sns.set()
    dep_head.reset_index(inplace=True)
    dep_head = dep_head.sort_values("Nbr_demande", ascending = False)
    dep_head.columns = ["metier", "nbr_demande"]

    dep_tail.reset_index(inplace=True)
    dep_tail = dep_tail.sort_values("Nbr_demande", ascending = False)
    dep_tail.columns = ["metier", "nbr_demande"]


    fig1= plt.figure()
    sns.barplot(y= "metier", x= "nbr_demande", data = dep_head,
				orient="h", palette ="Reds_r")
    plt.xlabel("")
    plt.title("Les métier les plus demandés", fontsize= 18)
    plt.ylabel("")

    st.pyplot(fig1)

    fig2= plt.figure()
    sns.barplot(y= "metier", x= "nbr_demande", data = dep_tail, orient="h", palette ="Blues")
    plt.xlabel("")
    plt.title("Les métier les moins demandés", fontsize= 18)
    plt.ylabel("")
    plt.xlim(0,50)

    st.pyplot(fig2)

def demande_metier(metier):

    df_metier = df[df.metier == metier]
    choro = df_metier.groupby(by=["NomDept"]).agg({"Nbr_demande":"sum"})
    choro = choro.reset_index()
    choro['id']=choro['NomDept'].apply(lambda x: dico_map[x])


    fig = px.choropleth_mapbox(choro, width = 900, height =100, locations="id", geojson = departement_geo, color = "Nbr_demande", hover_name = "NomDept",
                mapbox_style = "open-street-map",
				center = {"lat":46.80, "lon":3.02}, zoom = 5, opacity = 0.5,
                title = metier)

    fig.update_geos(fitbounds = "locations", visible = False)
    fig.update_layout(height=800, title_font_size = 25)

    st.plotly_chart(fig)

def departement_page():

	dep = st.selectbox("Choisir un département",liste_dep)
	heatmap(dep)



def metier_page():


	famille = st.selectbox("Famille de métier",liste_famille)
	liste_metier = df[df.famille == famille]["metier"].unique().tolist()
	metier = st.selectbox("Choisir un métier", liste_metier)

	demande_metier(metier)


def contact_message():
    st.header(":mailbox: Let's Get In Touch !")

    name, message = st.columns((1,2))
    with name:
        contact_form = """<form action="https://formsubmit.co/maxime.letutour@gmail.com" method="POST">
     <input type="text" name="name" placeholder = "Ton Nom" required>
     <input type="email" name="email" placeholder = "Ton E-mail" required>
     </form>"""
        st.markdown(contact_form, unsafe_allow_html=True)

    with message :
        contact_form2 = """<form action="https://formsubmit.co/maxime.letutour@gmail.com" method="POST">
        <textarea name="message" placeholder="Ecris moi !"></textarea>
        <button type="submit">Send</button>
    """
        st.markdown(contact_form2, unsafe_allow_html=True)

    with open("style.txt") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)





def main():
    st.title("Tendances de l'emploi en 2021")

    with st.sidebar:
        st.image(logo, width = 300)
        st.markdown("#")
        st.markdown("####")

        choice = option_menu(
            menu_title = "Analyses",
            options = ["Par département", "Par métier", "Envoie Moi Un Message"],
            icons=["house","hammer","envelope"],
            menu_icon="search"
        )
        
        

    if choice == "Par département":
        departement_page()
    elif choice == "Par métier":
        metier_page()
    elif choice == "Envoie Moi Un Message":
        contact_message()


    st.sidebar.markdown("####")
    st.sidebar.markdown("####")
    st.sidebar.subheader(":notebook_with_decorative_cover: Par Maxime Le Tutour :relieved: ")

    st.sidebar.write(" :blue_book: [**LinkedIn**](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)", unsafe_allow_html =True)

   


    
if __name__ == '__main__':
	main()