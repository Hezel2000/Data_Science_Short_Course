import streamlit as st
import pandas as pd

st.subheader('Data Science Short Course 2023 – Online Part')

sel_language = st.radio('',('english', 'german'), horizontal=True)

st.divider()

@st.cache_data
def importCourseDatasheet():
    dfSearchAll= pd.read_csv('course_material_data_science_short_course.csv')
    return dfSearchAll


def useCourse(dfSearchAll):
    col1, col2 = st.columns((20,80))
    with col1:
        chapter_sel = st.radio('Kapitelauswahl', range(1,5), horizontal = True)
    with col2:
        dfSearchAll_tmp = dfSearchAll[dfSearchAll['Kapitel'] == chapter_sel]
        topic_sel = st.selectbox('Auswahl der Einheit', dfSearchAll_tmp['Titel'].tolist())
        sel_row = dfSearchAll.loc[dfSearchAll[dfSearchAll['Titel'] == topic_sel].index[0]]
    
    if len(sel_row) > 0:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.video(sel_row['Youtube'])
        with col2:
            st.write('Laufzeit: ' + sel_row['Laufzeit'])
            with st.expander('Jupyter Notebooks', expanded=True):
                if sel_row['Vorlesung ipynb'] != 'none':
                    vorlesung = "[Vorlesung](https://raw.githubusercontent.com/Hezel2000/Data_Science_Short_Course/main/jupyter_nb/" + sel_row['Vorlesung ipynb'] + ")"
                else:
                    vorlesung=''
                if sel_row['Übungen ipynb'] != 'none':
                    uebungen = "[Übungen](https://raw.githubusercontent.com/Hezel2000/Data_Science_Short_Course/main/jupyter_nb/" + sel_row['Übungen ipynb'] + ")"
                else:
                    uebungen=''
                if sel_row['Lösungen ipynb'] != 'none':
                    loesungen = "[Lösungen](https://raw.githubusercontent.com/Hezel2000/Data_Science_Short_Course/main/jupyter_nb/" + sel_row['Lösungen ipynb'] + ")"
                else:
                    loesungen=''
                if vorlesung=='' and uebungen=='' and loesungen=='':
                    st.write('keine vorhanden')
                else:
                    st.write(vorlesung,uebungen,loesungen)
              
            with st.expander('Schlagworte', expanded=True):
                if sel_row['Schlagworte'] != 'none':
                    st.write(sel_row['Schlagworte'])
                else:
                    st.write('keine vorhanden')

        st.write(sel_row['Beschreibung'])

def useCourse_english(dfSearchAll):
    col1, col2 = st.columns((20,80))
    with col1:
        chapter_sel = st.radio('Select Chapter', range(1,5), horizontal = True)
    with col2:
        dfSearchAll_tmp = dfSearchAll[dfSearchAll['Kapitel'] == chapter_sel]
        topic_sel = st.selectbox('Select Topic', dfSearchAll_tmp['Titel'].tolist())
        sel_row = dfSearchAll.loc[dfSearchAll[dfSearchAll['Titel'] == topic_sel].index[0]]
    
    if len(sel_row) > 0:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.video(sel_row['Youtube'])
        with col2:
            st.write('Duration: ' + sel_row['Laufzeit'])
            with st.expander('Jupyter Notebooks', expanded=True):
                if sel_row['Vorlesung ipynb'] != 'none':
                    vorlesung = "[Vorlesung](https://raw.githubusercontent.com/Hezel2000/Data_Science_Short_Course/main/jupyter_nb/" + sel_row['Vorlesung ipynb'] + ")"
                else:
                    vorlesung=''
                if sel_row['Übungen ipynb'] != 'none':
                    uebungen = "[Übungen](https://raw.githubusercontent.com/Hezel2000/Data_Science_Short_Course/main/jupyter_nb/" + sel_row['Übungen ipynb'] + ")"
                else:
                    uebungen=''
                if sel_row['Lösungen ipynb'] != 'none':
                    loesungen = "[Lösungen](https://raw.githubusercontent.com/Hezel2000/Data_Science_Short_Course/main/jupyter_nb/" + sel_row['Lösungen ipynb'] + ")"
                else:
                    loesungen=''
                if vorlesung=='' and uebungen=='' and loesungen=='':
                    st.write('keine vorhanden')
                else:
                    st.write(vorlesung,uebungen,loesungen)
              
            with st.expander('key words', expanded=True):
                if sel_row['Schlagworte'] != 'none':
                    st.write(sel_row['Schlagworte'])
                else:
                    st.write('none')

        st.write(sel_row['Beschreibung'])
        

dfSearchAll = importCourseDatasheet()
if sel_language == 'german':
    useCourse(dfSearchAll)
else:
    useCourse_english(dfSearchAll)

st.divider()

st.write('Open [Course Webpage](https://hezel2000.quarto.pub/data-science-2023)')

#---------------------------------#
#------ Main Page Sidebar --------#
#---------------------------------#  

# st.sidebar.image('images/goethe-Logo.png', width=150)
# st.sidebar.write("Viele Wege führen zum Erfolg.")