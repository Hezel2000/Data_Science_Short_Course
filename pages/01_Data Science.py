#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd

# =============================================================================
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)
# =============================================================================


#---------------------------------#
#------ Einführung ---------------#
#---------------------------------#
    
def einfuehrung():
    st.subheader('Willkommen zur Einführung in Data Sciences')
    st.write('*für Mineralogen, Kosmo-/Geochemiker, Petrologen & den ganzen Rest*')
    
    st.video('https://youtu.be/amJkqAgkris')

#---------------------------------#
#------ Vorlesungen & Übungen ----#
#---------------------------------#
def Vorlesungen_Uebungen():
    import streamlit as st
    st.subheader('Wähle Deine Lerneinheit')

    @st.cache
    def importCourseDatasheet():
        dfSearchAll= pd.read_csv('https://raw.githubusercontent.com/Hezel2000/Data_Science/main/course_material.csv')
        return dfSearchAll
    
    
    def useCourse(dfSearchAll):
        dfSearchAll = dfSearchAll
        gd = GridOptionsBuilder.from_dataframe(dfSearchAll)
        gd.configure_pagination(enabled=True)
        gd.configure_default_column(editable=True,groupable=True)
        gd.configure_selection(selection_mode='single', use_checkbox=True)
        gridoptions = gd.build()
        grid_table = AgGrid(dfSearchAll, gridOptions=gridoptions, update_mode = GridUpdateMode.SELECTION_CHANGED, theme='material')
        sel_row = grid_table['selected_rows']
    
        if len(sel_row) > 0:    
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.video(sel_row[0]['Youtube'])
            with col2:
                st.write('Laufzeit: ' + sel_row[0]['Laufzeit'])
                with st.expander('Jupyter Notebooks', expanded=True):
                    if sel_row[0]['Vorlesung ipynb'] != 'none':
                        vorlesung = "[Vorlesung](https://raw.githubusercontent.com/Hezel2000/Data_Science/main/jupyter_nb/" + sel_row[0]['Vorlesung ipynb'] + ")"
                    else:
                        vorlesung=''
                    if sel_row[0]['Übungen ipynb'] != 'none':
                        uebungen = "[Übungen](https://raw.githubusercontent.com/Hezel2000/Data_Science/main/jupyter_nb/" + sel_row[0]['Übungen ipynb'] + ")"
                    else:
                        uebungen=''
                    if sel_row[0]['Lösungen ipynb'] != 'none':
                        loesungen = "[Lösungen](https://raw.githubusercontent.com/Hezel2000/Data_Science/main/jupyter_nb/" + sel_row[0]['Lösungen ipynb'] + ")"
                    else:
                        loesungen=''
                    if vorlesung=='' and uebungen=='' and loesungen=='':
                        st.write('keine vorhanden')
                    else:
                        st.write(vorlesung,uebungen,loesungen)
                with st.expander('Schlagworte', expanded=True):
                    if sel_row[0]['Schlagworte'] != 'none':
                        st.write(sel_row[0]['Schlagworte'])
                    else:
                        st.write('keine vorhannden')
            
            #st.subheader('Beschreibung')
            st.write(sel_row[0]['Beschreibung'])
    
# =============================================================================
#         else:
#             st.subheader('Wähle eine Einheit aus obiger Liste')
# =============================================================================
            

    dfSearchAll = importCourseDatasheet()

    useCourse(dfSearchAll)
    


#---------------------------------#
#------ Überblick ----------------#
#---------------------------------#

def ueberblick():
    import streamlit as st
    
    st.header('Überblick')
        
    st.write('''**Wie zu schauen ist – oder zumindest: wie geschaut werden kann**\n
Anhalten, nachvollziehen, eventuell zurückspulen und dazu eigen Skizzen oder Mitschriebe anfertigen\n
Einige wenige Videos haben aus rechtlichen Gründen ein Passwort, das erhaltet Ihr von mir''')

    st.write('''
**Die Veranstaltung besteht aus**\n
>ca. 100 Seiten Skript, aufgeteilt in die 3 Teilskripte
>ca. 50 Videos  mit insgesamt über 7 Stunden Material
>über 100 Jupyter Notebooks  mit >100 Fragen, Aufgaben & Beispielen
> 00 Selbstlern-Fragen mit Antworten
>20 Aufgaben zur gemeinsamen Lösung in den Präsenzphasen und den Semester-Projekten
>zahlreiche zusätzlicher Dateien für verschiedene Aufgaben''')

    # =============================================================================
    # **Einordnung der Einheiten für die Abschlussprüfung:**
    # Ich ergänze die Überschriften um die beiden Symbole ◉ (Relevanz) und ▲ (Verständnis). Die Symbole haben eine von 3 Farben,
    # welche anzeigen, wie relevant oder wichtig für das Verständnis ein Thema ist. Die Farben sind: orange: hoch, grün: mittel,
    # blau: weniger.
    # =============================================================================



#---------------------------------#
#------ Inhaltsverzeichnis -------#
#---------------------------------#

def inhaltsverzeichnis():
    st.header('Inhaltsverzeichnis')
        
    st.subheader('1 Einführung, Installation & ein erstes Programm: 1.1 – 1.4 [11:42]')
    st.write('In der ersten Stunde starten wir gemeinsam mit mit der Installation von Jupyter Notebooks, bzw. Anaconda. Wir lernen das Interface ein wenig kennen und schreiben ein erstes kleines Programm. Außerdem erkläre ich wie dieser Kurs im Flipped Classroom Format abläuft.')
    
    st.subheader('2 Rufe eine selbst geschriebene Mischungs-Funktion auf: 2.1 – 2.5 [39:17]')
    st.write('Zum Programmieren verwenden wir Befehle, das sollte recht einleuchtend sein. Nun hat Python natürlich keine Befehle für die Geochemie, um mit so einem beispielsweise direkt auszurechnen wie die neue Zusammensetzung einer Schmelze ist, nachdem sie sich mit einer anderen gemischt hat. Praktisch wäre es aber schon. Nicht nur in der Geochemie, sondern für sehr vieles. Daher ist es möglich eigenen Befehle zu definieren – etwas zur Mischung von Magmen – um diese anschließend immer wieder zu verwenden. Es ist sogar möglich mehrere Befehle in einer Datei zu speichern, und aus dieser ›Bibliothek‹ immer wieder aufzurufen. Wie das geht lernen wir in dieser Einheit.')
    
    st.subheader('3 Erste Schritte in ›Data Science‹:  3.1 – 3.5 [43:21]')
    st.write('In den vergangenen Jahren werden immer mehr Daten publiziert, deren Menge zukünftig noch schneller anwachsen wird. Es ist nicht leicht, all den Publikationen dieser erfreulich großen Mengen immer neuer Informationen zu folgen. Jupyter Notebooks wurden gerade auch dafür entwickelt, auf große Mengen an Daten zuzugreifen, diese zu visualisieren, analysieren und auf Problemstellungen anzuwenden. Natürlich ist das nur möglich, wenn die Daten in entsprechenden Formaten vorliegen. Oftmals ist daher im ersten Schritt ein ›Daten clean-up‹ notwendig. Seit 2020 gibt es nun endlich mehrere Initiativen, darunter so große wie die Nationale Forschungsdatenbank Initiative (NFDI) der DFG, GWK und anderer, die versuchen gemeinsam mit internationalen Partnern Daten besser verfügbar zu machen. Schon bestehende Datenbanken wie GeoROC, EarthChem oder auch MetBase erlauben schon seit langer Zeit solchen Zugang, und damit Data Science in z.B. der Geo- und Kosmochemie. In dieser Einheit steigen wir in das neue Feld der Data Science in der Mineralogie ein.')
    
    st.subheader('4 Interaktive Elemente & erste Programme:  4.1 – 4.5 [41:42]')
    st.write('Nun fehlt uns nur noch wenig Rüstzeug, um erste, leistungsfähige Programme zu schreiben. Dieses Verbleibende lernen wir in dieser Einheit, um dann tatsächlich 2 Programme zu bauen, welche Datenbank-Daten effektiv darstellen. Vor allem lernen wir hier interaktive Möglichkeiten kennen die es uns ermöglichen, mit den Daten über eine graphische Benutzeroberfläche direkt zu interagieren, diese zu manipulieren und immer wieder neu darzustellen.')
    
    st.subheader('5 Data Science mit API Requests & Daten-Auswertung  5.1 – 5.5 [1:03:22]')
    st.write('Eine besonders effektive und interessante Art auf Daten zuzugreifen ist über ›Application Programming Interfaces‹ – kurz: API. Der Begriff API ist sehr weit verbreitet, und sollte man sich in jedem Fall merken. In einer idealen Welt hätte man gar keine eigenen Datenbanken mehr, sondern würde nur noch über APIs auf Datenbanken zugreifen, sich die gewünschten Daten herunter laden, und diese dann auf dem eigenen Computer auswerten. Ein Großteil des Internets, und viele der erfolgreichsten Apps auf dem Smartphone funktionieren genau so: über ein API werden die gewünschten Daten geladen, und die App macht letztlich nicht mehr als ein Interface zur verfügung zu stellen, um diese Daten entsprechend auszuwählen und darzustellen. Das Interface ist dabei ein Graphical User Interface – kurz GUI. Ebenfalls ein Begriff, den man kennen sollte. Eine GUI ist letztlich nichts anders als das, was wir mit ›Interact‹ kennen gelernt haben. D.h., mit einer API und einer GUI machen wir exakt das, was fast jede unserer App auf dem Smartphone macht. Das hört sich alles großartig an – und ist es auch! Wäre da nicht das eine Problem: viele geowissenschaftliche Datenbanken haben – noch – keine vernünftige API. Glücklicherweise ändert sich daran gerade viel. Fun Fact Wir hier in Frankfurt sind an dieser Änderung recht zentral beteiligt.')
    
    st.subheader('6 Die vielen Möglichkeiten Diagramme zu erstellen  6.1 – 6.4 [55:22]')
    st.write('In dieser letzten Einheit Daten darzustellen zeige ich – ansatzweise – wie vielfältig mit Jupyter Notebooks, bzw. Python geplottet werden kann, bzw. wie enorm flexibel interaktive Elemente genutzt werden können. Mit dem Package ›geopandas‹ lernen wir außerdem die Möglichkeit kennen, Daten auf Karten darzustellen – natürlich geht auch das interaktiv. Die Bedeutung guter, aussagekräftiger, übersichtlicher, und dabei durchaus komplexer Diagramme kann nicht ausreichend unterstrichen werden. Diagramme und Abbildungen bilden fast immer den Kern eines sehr guten papers, Vortrags oder natürlich einer Abschlussarbeit. Das gelingt jedoch nur mit dem entsprechenden Werkzeug. Matplotlib gehört sicherlich zu den besten Werkzeugen, um wissenschaftliche Diagramme und Abbildungen zu erzeugen. Die hohe Flexibilität interaktiver Elemente erlaubt es sehr schnell und übersichtlich Daten zusammen mit anderen Daten unterschiedlichster Quellen und beliebiger Menge zu visualisieren und analysieren. Das ist ein sehr guter, erster Schritt, um Daten zu verstehen, um dann in die Detail-Analyse zu gehen.')
    
    st.subheader('7 Stabile Isotope: Fraktionierung & Darstellung  7.1 – 7.4  [40:29]')
    st.write('Mit dieser Einheit gehen wir weiter zu Modellierungen. Wir haben uns nun eine erste, solide Sicherheit erarbeitet, Python Codes mit Jupyter Notebooks zu erstellen, und dabei die Vorzüge von Jupyter Notebooks für Data Science kennen gelernt. Wir haben gesehen, wie man Daten darstellt, filtert und selektiert, interaktiv verfügbar macht, mit APIs auf Datenbanken zugreift, Daten in großen Mengen analysiert um etwas Anomalien zu studieren, und mehr. Nun werden wir vermehrt anwenden, was wir können – und trotzdem weiter Neues kennen lernen, und diese weiterhin mit dem bislang gelernten verbinden. Dazu schauen wir uns in dieser Einheit an, wie man einfach modelliert. Dazu verwenden wir Funktionen, welche einen Prozess – oder später etwas komplexer – ein Modell beschreiben. Du lernst wie man Funktionen darstellt, welche Funktionen schon eingebaut per Befehl angewendet werden können (hier: lineare Regression), und als Abschluss, wie man leicht Fehlerbalken an Daten bekommt.')
    
    st.subheader('8 Mikroanalytik: Linieninterferenzen charakteristischer Röntgenstrahlung:  8.1 – 8.3 [43:58]')
    st.write('Der Kurs heißt ja Mikroanalytik. Daher soll es nun ein wenig um Mikroanalytik gehen. Außerdem ist es die letzte Einheit von Teil I. Daher soll eine erste Idee vermittelt werden, wie das Semester-Projekt aussehen könnte: nämlich in etwa so wie die Ergebnisse dieser Einheit. Diese sind zwei Programme dazu, wie Linieninterferenzen charakteristischer Röntgenstrahlung identifiziert und visualisiert werden können. Wem das nichts sagt, keine Sorge, im ersten Video gibt es eine kleine Auffrischung/Erklärung, was das ist. Die anschließenden beiden Videos zeigen zwei Programm dazu. Das Thema ist damit aber noch gar nicht vollständig behandelt, sodass sogar das ein Semester-Projekt werden könnte. D.h., ein Semester-Projekt könnte eben so ein Thema durcharbeiten: verschiedene Programme mit einem dann vernünftigen GUI um Interferenzen zu finden, und damit sein Messprogramm an der Mikrosonde, RFA, o.ä. vorzubereiten. Tatsächlich wird eine generelle Idee des Semester-Projekts sein, verwendbare Programme für die Mikroanalytik o.ä. zu erstellen. Dazu dann in der Präsenzphase zu dieser Einheit mehr.')
    
    st.subheader('9 Special Edition: Search the Data Science Script Database: 9.1 [26:14]')
    st.write('Das ist keine wirklich eigenständige oder neue Einheit, sondern die Lösung der Aufgabe zur 8. Präsenzveranstaltung.')
    
    
#---------------------------------#
#------ Main Page Sidebar --------#
#---------------------------------#  

st.sidebar.image('https://raw.githubusercontent.com/Hezel2000/GeoROC/main/images/Goethe-Logo.jpg', width=150)

page_names_to_funcs = {
    'Einführung': einfuehrung,
    'Vorlesungen & Übungen': Vorlesungen_Uebungen,
    'Überblick': ueberblick,
    'Inhaltsverzeichnis': inhaltsverzeichnis
}

demo_name = st.sidebar.radio("Viele Wege führen zum Erfolg", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
