import streamlit as st
import helper
import plots as pl
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

df = helper.df
cats = helper.cats
nums = helper.nums


def eda():

    uni_variate, bi_variate, multi_variate = st.tabs(
        ['Univariate', 'Bivariate', 'Multivariate'])

    with uni_variate:
        st.subheader('Descriptive statistics for Categorical Features')
        st.dataframe(df.describe(include='O'))

        st.subheader('Distribution')
        cat_feature = st.selectbox('Select a categorical feature', cats, key=1)
        if cat_feature != 'native-country':
            st.plotly_chart(pl.create_pie_chart(df, cat_feature))
        else: 
            st.plotly_chart(px.histogram(df, x=cat_feature, title=f"Distribution of native-country",text_auto='.2f',histnorm='percent'))
        st.subheader('Descriptive statistics for Numerical Features')
        st.dataframe(df.describe())

        st.subheader('Distribution')
        num_feature = st.selectbox('Select a numerical feature', nums, key=2)
        st.plotly_chart(pl.create_histogram_with_boxplot(df, num_feature))

    with bi_variate:
   
        st.subheader('Numerical vs Numerical Analysis')
        
        st.plotly_chart(px.imshow(df[nums+['income']].corr(numeric_only=True),text_auto='.2f',width=1000, height=800))
        
        
        # fig = px.scatter(df, x='age', y='hours-per-week', trendline='ols', title='Relationship between Age and Hours Worked Per Week')
        # fig.update_traces(marker=dict(size=8, opacity=0.5))
        # st.plotly_chart(fig)
  
            
        st.subheader('Categorical vs Numerical Analysis')
        
        st.subheader('Distribution of income levels among different age groups')
        dff = df.groupby('income')[['age']].mean().reset_index()
        fig = px.bar(dff, x='income', y='age', title='Mean Age by Income',
             labels={'income': 'Income', 'age': 'Mean Age'})
        fig.update_layout(xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig)
        st.text('''Individuals with incomes exceeding $50,000 typically have higher average ages
compared to those with incomes below this threshold.''')
        
        st.subheader('Trends in income levels based on the native country of individuals')
        dff = df[['income','native-country']]
        dff['native-country'] = dff['native-country'].apply(lambda x:x if x=='United-States' else 'other')
        income_by_country = dff.groupby('native-country')['income'].value_counts(normalize=True).unstack().reset_index()
        income_by_country_melted = income_by_country.melt(id_vars='native-country', var_name='income', value_name='proportion')
        fig = px.bar(income_by_country_melted, x='native-country', y='proportion', color='income', barmode='group', text_auto = '.2f',
             title='Distribution of Income by native country')
        st.plotly_chart(fig)
        
        st.subheader('Distribution of income levels across different races')
        income_by_race = df.groupby('race')['income'].value_counts(normalize=True).unstack().reset_index()
        income_by_race_melted = income_by_race.melt(id_vars='race', var_name='income', value_name='proportion')
        fig = px.bar(income_by_race_melted, x='race', y='proportion', color='income', barmode='group', text_auto = '.2f',
             title='Distribution of Income by Race')
        st.plotly_chart(fig)
        
        st.subheader('Difference in income levels between males and females')
        income_by_sex = df.groupby('sex')['income'].value_counts(normalize=True).unstack().reset_index()
        income_by_sex_melted = income_by_sex.melt(id_vars='sex', var_name='income', value_name='proportion')
        fig = px.bar(income_by_sex_melted, x='sex', y='proportion', color='income', barmode='group',text_auto='.2f' ,
             title='Distribution of Income by Gender', labels={'sex': 'Gender', 'proportion': 'Proportion', 'income': 'Income'})
        st.plotly_chart(fig)
        
        st.subheader('Average number of hours worked per week for individuals with income >50K compared to <=50K')
        average_hours_worked = df.groupby('income')[['hours-per-week']].mean().reset_index()
        fig = px.bar(average_hours_worked, x='income', y='hours-per-week', title='Mean hours-per-week by Income',
             labels={'income': 'Income', 'hours-per-week': 'Mean hours per week'})
        fig.update_layout(xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig)
        st.markdown('`People earning more than $50,000 usually work more hours per week than those earning less.`')       
         
        st.subheader('Most common relationships among individuals with income >50K')
        income_by_relationship = df.groupby('relationship')['income'].value_counts(normalize=True).unstack().reset_index()
        income_by_relationship_melted = income_by_relationship.melt(id_vars='relationship', var_name='income', value_name='proportion')
        fig = px.bar(income_by_relationship_melted, x='relationship', y='proportion', color='income', barmode='group', text_auto = '.2f',
             title='Distribution of Income by relationship')
        st.plotly_chart(fig)
        st.markdown('''`Husband: Approximately 44.87% of husbands earn incomes exceeding $50K.
Wife: About 46.89% of wives earn incomes greater than $50K.`''')
        
        st.subheader('Most common occupations among individuals with income >50K')
        income_by_occupation = df.groupby('occupation')['income'].value_counts(normalize=True).unstack().reset_index()
        income_by_occupation_melted = income_by_occupation.melt(id_vars='occupation', var_name='income', value_name='proportion')
        fig = px.bar(income_by_occupation_melted, x='occupation', y='proportion', color='income', barmode='group', text_auto = '.2f',
             title='Distribution of Income by occupation')
        st.plotly_chart(fig)
        st.markdown('''`Exec-managerial: Approximately 47.78% of individuals in executive or managerial roles earn incomes exceeding $50K.
Prof-specialty: About 45.11% of individuals in professional specialty occupations earn incomes greater than $50K.`''')
        
        
        st.subheader('Impact of marital status on income level')
        income_by_marital_status = df.groupby('marital-status')['income'].value_counts(normalize=True).unstack().reset_index()
        income_by_marital_status_melted = income_by_marital_status.melt(id_vars='marital-status', var_name='income', value_name='proportion')
        fig = px.bar(income_by_marital_status_melted, x='marital-status', y='proportion', color='income', barmode='group', text_auto = '.2f',
             title='Distribution of Income by marital status')
        st.plotly_chart(fig)
        
        st.markdown('''`Married-AF-spouse: Approximately 37.84% of individuals who are married to someone from the Armed Forces (AF) earn incomes exceeding $50K.
Married-civ-spouse: About 44.61% of individuals who are married to a civilian spouse earn incomes greater than $50K.`''')
        
        st.subheader('education level and income level')
        income_by_education = df.groupby('education')['income'].value_counts(normalize=True).unstack().reset_index()
        income_by_education_melted = income_by_education.melt(id_vars='education', var_name='income', value_name='proportion')
        fig = px.bar(income_by_education_melted, x='education', y='proportion', color='income', barmode='group', text_auto = '.2f',
             title='Distribution of Income by education')
        st.plotly_chart(fig)
        st.markdown('''`Prof-school: Approximately 73.98% of individuals who attended professional school earn incomes exceeding $50K, with a mean proportion of 73.98%.
Doctorate: About 72.56% of individuals with doctoral degrees earn incomes greater than $50K, with a mean proportion of 72.56%.
Masters: Roughly 54.91% of individuals with master's degrees earn incomes surpassing $50K, with a mean proportion of 54.91%.`''')
        
        st.subheader('Relationship between workclass categories and income levels')
        income_by_workclass = df.groupby('workclass')['income'].value_counts(normalize=True).unstack().reset_index()
        income_by_workclass_melted = income_by_workclass.melt(id_vars='workclass', var_name='income', value_name='proportion')
        fig = px.bar(income_by_workclass_melted, x='workclass', y='proportion', color='income', barmode='group', text_auto = '.2f',
             title='Distribution of Income by workclass')
        st.plotly_chart(fig)
        st.markdown('''- **Self-Employed Incorporated (Self-emp-inc)**: About 55.34% of self-employed individuals with incorporated businesses earn incomes surpassing $50,000.

- **Federal Government (Federal-gov)**: Approximately 39.18% of individuals working in the federal government sector earn incomes exceeding $50,000.
  
- **Local Government (Local-gov)**: Around 29.56% of individuals employed in local government roles earn incomes greater than $50,000.

- **State Government (State-gov)**: Roughly 26.75% of individuals working in state government positions earn incomes exceeding $50,000.
''')
        
    with multi_variate:
        st.subheader('Age of Individuals by Average Hours of Work in the Income')
        data = df.groupby(['age', 'income']).apply(lambda x: x['hours-per-week'].mean()).reset_index(name='Hours')
        fig = px.line(data, x='age', y='Hours', color='income', title='Age of Individuals by Average Hours of Work in the Income Category')
        st.plotly_chart(fig)
        
        st.subheader('Average Age by Income and Gender')
        fig, ax = plt.subplots(figsize=(6, 8))
        sns.barplot(x='income', y='age', hue='sex', data=df, ci=False, ax=ax)
        ax.set_ylabel('Average age')
        st.pyplot(fig)
        st.markdown('''`In terms of income exceeding $50,000, males with a higher average age
tend to outperform females with a higher average age. Conversely, females with a lower average age are more likely to achieve an income surpassing $50,000 compared to males in the same age group.`''')
        

   

