import streamlit as st
import helper
from analysis import eda
from model import model
from conclusion import conclusion
st.header('Adult income')

page = st.sidebar.radio('Pages', ['Home', 'Analysis', 'Model', 'Conclusion'])

def home():

    st.subheader('This app is created to analyze the Adult Income dataset and predict income.')
    st.image('./assets/cover.png', caption='Adult income')
    st.text('''
    This dataset contains information on individuals' income, including their age,
    workclass, education, marital status, occupation, race, sex, capital gain,
    capital loss, hours per week,and native country.
    The target variable is the income, categorized as <=50K or >50K.
    The purpose of this app is to provide insights into the dataset through
    data analysis, model building, and conclusion.
    ''')
    st.markdown("""
        <div style='text-align: left; font-size: 18px; font-weight: bold; margin-bottom: 10px;'>
            Column Descriptions:
        </div>
        <ul style='list-style-type: square;'>
            <li><strong>age:</strong> The age of the individual.</li>
            <li><strong>workclass:</strong> The type of workclass, indicating the employment status.</li>
            <li><strong>fnlwgt:</strong> The final weight assigned to the individual's demographic characteristics in the population.</li>
            <li><strong>education:</strong> The highest level of education achieved by the individual.</li>
            <li><strong>education-num:</strong> The numerical representation of education (corresponding to education level).</li>
            <li><strong>marital-status:</strong> The marital status of the individual.</li>
            <li><strong>occupation:</strong> The occupation of the individual.</li>
            <li><strong>relationship:</strong> The relationship status of the individual.</li>
            <li><strong>race:</strong> The race of the individual.</li>
            <li><strong>sex:</strong> The gender of the individual.</li>
            <li><strong>capital-gain:</strong> The capital gains of the individual.</li>
            <li><strong>capital-loss:</strong> The capital losses of the individual.</li>
            <li><strong>hours-per-week:</strong> The number of hours worked per week by the individual.</li>
            <li><strong>native-country:</strong> The native country of the individual.</li>
            <li><strong>income:</strong> The income of the individual, categorized as <=50K or >50K.</li>
        </ul>""", unsafe_allow_html=True)

    # Load data
    df = helper.df

    # Show data
    st.write(df.head())


tabs = {
    'Home': home,
    'Analysis': eda,
    'Model': model,
    'Conclusion': conclusion
}
tabs[page]()