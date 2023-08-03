import streamlit as st
import pandas as pd

st.subheader('Data Science Short Course 2023 – Online Part')


#@st.cache_data
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
                if sel_row['Lecture ipynb'] != 'none':
                    vorlesung = "[Vorlesung](https://raw.githubusercontent.com/Hezel2000/Data_Science_Short_Course/main/jupyter_nb/" + sel_row['Lecture ipynb'] + ")"
                else:
                    vorlesung=''
                if sel_row['Exercise ipynb'] != 'none':
                    uebungen = "[Übungen](https://raw.githubusercontent.com/Hezel2000/Data_Science_Short_Course/main/jupyter_nb/" + sel_row['Exercise ipynb'] + ")"
                else:
                    uebungen=''
                if sel_row['Solution ipynb'] != 'none':
                    loesungen = "[Lösungen](https://raw.githubusercontent.com/Hezel2000/Data_Science_Short_Course/main/jupyter_nb/" + sel_row['Solution ipynb'] + ")"
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
            st.video(sel_row['Youtube_eng'])
        with col2:
            st.write('Duration: ' + sel_row['Duration'])
            with st.expander('Jupyter Notebooks', expanded=True):
                if sel_row['Lecture ipynb'] != 'none':
                    vorlesung = "[Lecture](https://raw.githubusercontent.com/Hezel2000/Data_Science_Short_Course/main/jupyter_nb/" + sel_row['Lecture ipynb'] + ")"
                else:
                    vorlesung=''
                if sel_row['Exercise ipynb'] != 'none':
                    uebungen = "[Exercise](https://raw.githubusercontent.com/Hezel2000/Data_Science_Short_Course/main/jupyter_nb/" + sel_row['Exercise ipynb'] + ")"
                else:
                    uebungen=''
                if sel_row['Solution ipynb'] != 'none':
                    loesungen = "[Solution](https://raw.githubusercontent.com/Hezel2000/Data_Science_Short_Course/main/jupyter_nb/" + sel_row['Solution ipynb'] + ")"
                else:
                    loesungen=''
                if vorlesung=='' and uebungen=='' and loesungen=='':
                    st.write('none available')
                else:
                    st.write(vorlesung,uebungen,loesungen)
              
            with st.expander('key words', expanded=True):
                if sel_row['Schlagworte'] != 'none':
                    st.write(sel_row['Schlagworte'])
                else:
                    st.write('none')

        st.write(sel_row['Description'])
        

dfSearchAll = importCourseDatasheet()


tab1, tab2, tab3 = st.tabs(['english', 'german', 'downloads'])
with tab1:
    useCourse_english(dfSearchAll)
with tab2:
    useCourse(dfSearchAll)
with tab3:
    st.write('You can download the online course material as a zip archive here:')
    with open("Exercises & Data2.zip", "rb") as files:
        btn = st.download_button(
            label="Download online material",
            data=files,
            file_name="Data Science online course material.zip",
            mime="application/zip"
        )
    st.markdown(":lightgray[Last updated: 03.08.2023, 8.45 o'clock]")

    st.divider()

st.write('Open [Course Webpage](https://hezel2000.quarto.pub/data-science-2023)')

#---------------------------------#
#------ Main Page Sidebar --------#
#---------------------------------#  

# st.sidebar.image('images/goethe-Logo.png', width=150)
# st.sidebar.write("Viele Wege führen zum Erfolg.")