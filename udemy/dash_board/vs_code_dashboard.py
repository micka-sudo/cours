import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import numpy as np

df_auto = pd.read_csv(r"E:\Cours_udemy\dash_board\auto.csv", dtype = "unicode")
df_candidats = pd.read_csv(r"E:\Cours_udemy\dash_board\candidats_2019.csv", dtype = "unicode")
df_chomage = pd.read_csv(r"E:\Cours_udemy\dash_board\chomage.csv", dtype = "unicode")
df_csp = pd.read_csv(r"E:\Cours_udemy\dash_board\csp.csv", dtype = "unicode")
df_delinquance = pd.read_csv(r"E:\Cours_udemy\dash_board\delinquance.csv", dtype = "unicode")
df_demographie = pd.read_csv(r"E:\Cours_udemy\dash_board\demographie.csv", dtype = "unicode")
df_election = pd.read_csv(r"E:\Cours_udemy\dash_board\election.csv", dtype = "unicode")
df_emploi = pd.read_csv(r"E:\Cours_udemy\dash_board\emploi.csv", dtype = "unicode")
df_entreprises = pd.read_csv(r"E:\Cours_udemy\dash_board\entreprises.csv", dtype = "unicode")
df_immobilier = pd.read_csv(r"E:\Cours_udemy\dash_board\immobilier.csv", dtype = "unicode")
df_infos = pd.read_csv(r"E:\Cours_udemy\dash_board\infos.csv", dtype = "unicode")
df_liensVilles = pd.read_csv(r"E:\Cours_udemy\dash_board\liensVilles.csv", dtype = "unicode")
df_salaires = pd.read_csv(r"E:\Cours_udemy\dash_board\salaires.csv", dtype = "unicode")
df_santeSocial = pd.read_csv(r"E:\Cours_udemy\dash_board\santeSocial.csv", dtype = "unicode")

# unique pour éviter les doublons
villes = [{'label' : ville, "value": ville} for ville in df_liensVilles["ville"].unique()]

# fonction dash de la class dash
app = dash.Dash(__name__)
# on creer un layout /
app.layout = html.Div([
    html.Div([
        # Creation selecteur de ville
        html.H4("Choisissez une ville :"),
        dcc.Dropdown(
            id='ville-picker',
            # pour le menu deroulant pour les villes
            options=villes,
            #pour avoir une ville par defaut
            value= "Paris (75000)"
            
        )
    ], style={
        # taille
        'width':'25%',
        # bordure 1px taille, solid type, eee couleur
        'border':'1px solid #eee',
        # espace autour de la box top, right, down, bot
        'padding':'30px 30px 30px 120px',
        # ombre de la box 
        'box-shadow': '0 2px 2px #ccc',
        # pour eviter les div a coter de notre drowp down
        'display':'inline-block',
        # pour l'alignement vertical
        'verticalAlign': 'top'
    }),
    html.Div([
        # creation tabs
        dcc.Tabs(id = 'tabs', value = 'tab-1', children =[
            # onglet infos generales
            dcc.Tab(label = "Info Générales", children =[
                # 1er Div
                html.Div([
                    # titre de taille h3
                    html.H3("info Générale")
                ], style = {'background': 'blue', 'color' : 'white', 'textAlign': 'center','padding':'10px 0px 10px 0px'}),
                # 2eme div dash table
                html.Div([
                    # création dash table
                    dash_table.DataTable(
                        id = 'Table_infos',
                        
                    )
                ], style = {}),
                # 3eme div Map
                html.Div(id = "Map", style = {}),
                
            ]),
            # onglet demographie
            dcc.Tab(label = " Demographie"),
            # onglet Santé social
            dcc.Tab(label = " Santé et Social"),
            # onglet immobilier
            dcc.Tab(label = " Immobilier"),
            # onglet Entreprises
            dcc.Tab(label = " Entreprises"),
            # onglet Emploi
            dcc.Tab(label = " Emploi"),
            # onglet Salaires
            dcc.Tab(label = " Salaires"),
            # onglet CSP
            dcc.Tab(label = " CSP"),
            # onglet Automobiles
            dcc.Tab(label = " Automobiles"),
            # onglet Délinquance
            dcc.Tab(label = " Délinquance"),
            # onglet Européennes
            dcc.Tab(label = " Européennes"),
            # onglet CHOMAGE EN FRANCE
            dcc.Tab(label = " CHOMAGE EN FRANCE")
            
        ])
    ])
])

@app.callback([Output('table_info','data'), Output('table_info', 'columns')],
             [Input('ville-picker','value')])
def update_generale(ville_choisie):
    # var columns du data set infos
    colonnes = df_infos.columns
    # columns drop
    colonnes_off = ['Taux de chômage (2015)','Etablissement public de coopération intercommunale (EPCI)','lien',
                    'Unnamed: 0',"Pavillon bleu", "Ville d'art et d'histoire", 
                    "Ville fleurie", "Ville internet",'ville']
    # recupération des infos qui nous interesse / pas presente dans colonnes_of
    listeInfos = [info for info in colonnes if info not in colonnes_off]
    
    # recuperation intitulé columns et donnée du df
    infos = {
        'intitule': listeInfos,
        'donnee' : [df_infos[df_infos['ville'] == ville_choisie][col].iloc[0] for col in listeInfos]
    }
    # convertion infos en data_frame
    table = pd.DataFrame(infos)
    # choix colonne
    data = table.to_dict("rows")
    # creation de l'entetet
    entete = {'id': 'intitule', 'name': "   "}, {'id': 'donnee', 'name': ville_choisie}

    return data, entete

server = app.server
if __name__ == "__main__":
    # pour lancer le serveur dash debug = True pour effectuer les changement en direct
    # debug=True ne fonctionne pas a revoir
    app.run_server(debug=True)  