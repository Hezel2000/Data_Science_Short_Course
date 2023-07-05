import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd


st.subheader('Welcome to the Data Science Short Course 2023')

st.write('30 to 50 minutes of videos as preparation, exercises during online meeting')


#---------------------------------#
#------ Vorlesungen & Übungen ----#
#---------------------------------#
st.subheader('Wähle Deine Lerneinheit')

@st.cache_data
def importCourseDatasheet():
    dfSearchAll= pd.read_csv('course_material_data_science_short_course.csv')
    return dfSearchAll


def useCourse(dfSearchAll):
    import pandas as pd

    tab1, tab2 = st.tabs(['Chapters', 'All'])
    
    with tab1:
        col1, col2 = st.columns((20,80))
        with col1:
            chapter_sel = st.radio('Select a Chapter', range(1,5), horizontal = True)
        with col2:
            dfSearchAll_tmp = dfSearchAll[dfSearchAll['Kapitel'] == chapter_sel]
            topic_sel = st.selectbox('Select Unit', dfSearchAll_tmp['Titel'].tolist())
            st.write(topic_sel)
            sel_row = dfSearchAll.loc[dfSearchAll[dfSearchAll['Titel'] == topic_sel].index[0]+1]

    with tab2:
        topic_sel = st.selectbox('Select a Topic', dfSearchAll['Titel'].tolist())
        sel_row_b = dfSearchAll.loc[dfSearchAll[dfSearchAll['Titel'] == topic_sel].index[0]+1]


    # dfSearchAll = dfSearchAll
    # gd = GridOptionsBuilder.from_dataframe(dfSearchAll)
    # gd.configure_pagination(enabled=True, paginationPageSize=5)
    # gd.configure_default_column(editable=True,groupable=True)
    # gd.configure_selection(selection_mode='single', use_checkbox=True)
    # gridoptions = gd.build()
    # grid_table = AgGrid(dfSearchAll, gridOptions=gridoptions, update_mode = GridUpdateMode.SELECTION_CHANGED, theme='material')
    # sel_row = grid_table['selected_rows']
    # st.write(sel_row)
    # st.write(sel_row[0]['Youtube'])


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
                    uebungen = "[Übungen](https://jupyter_nb/" + sel_row['Übungen ipynb'] + ")"
                else:
                    uebungen=''
                if sel_row['Lösungen ipynb'] != 'none':
                    loesungen = "[Lösungen](https://raw.githubusercontent.com/Hezel2000/Data_Science/main/jupyter_nb/" + sel_row['Lösungen ipynb'] + ")"
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
                    st.write('keine vorhannden')
        
        #st.subheader('Beschreibung')
        st.write(sel_row['Beschreibung'])

# =============================================================================
#         else:
#             st.subheader('Wähle eine Einheit aus obiger Liste')
# =============================================================================
        

dfSearchAll = importCourseDatasheet()
useCourse(dfSearchAll)

    
#---------------------------------#
#------ Main Page Sidebar --------#
#---------------------------------#  

st.sidebar.image('images/goethe-Logo.png', width=150)
st.sidebar.write("Viele Wege führen zum Erfolg.")

