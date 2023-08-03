import streamlit as st
from deta import Deta

deta = Deta('d0uu4eawaqg_io7DrMPtNEsoaSMtEAkdjVa6DaUEdfmE')
survey_db = deta.Base('hackathon')


st.set_page_config("The Social Educator",
                   layout="centered")

st.title("Streamlit connection demo")

st.write("You can submit more than 1 question.")


with st.form(key='form',clear_on_submit=True):
    question = st.text_area("What's your view on streamlit connection ? ")


    button = st.form_submit_button('Submit')

    if button:
        survey_db.put({'question':question})
        st.write("Question Submitted!")


st.write(f'Total Question recieved : {len(survey_db.fetch().items)}')
st.write("Data is stored in Base(Deta)")

