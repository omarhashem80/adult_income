import streamlit as st

def conclusion():
    st.title("Income Analysis and Recommendations")
    st.markdown("## Income Analysis")

    st.markdown("### Age")
    st.markdown("Individuals earning over $50,000 typically have higher average ages than those earning less. "
                "This suggests that income tends to increase with age, reflecting career advancement or accumulated experience.")

    st.markdown("### Work Hours per Week")
    st.markdown("Those earning more than $50,000 generally work more hours per week compared to those earning less. "
                "This implies a correlation between higher income and increased dedication to work or higher-paying positions requiring longer hours.")

    st.markdown("### Gender-Based Income Gap")
    st.markdown("There's a higher proportion of females earning <= $50K compared to males.")

    st.markdown("### Work Class")
    st.markdown("- **Upper Income Group**")
    st.markdown("  - *Self-Employed Incorporated (Self-emp-inc)*: About 55.34% of self-employed individuals with incorporated businesses earn incomes surpassing $50,000. "
                "This reflects the potential for entrepreneurship to yield high financial returns.")
    st.markdown("  - *Federal Government (Federal-gov)*: Approximately 39.18% of individuals working in the federal government sector earn incomes exceeding $50,000. "
                "This suggests favorable salary structures or opportunities for advancement within government positions.")
    st.markdown("  - *Local Government (Local-gov)*: Around 29.56% of individuals employed in local government roles earn incomes greater than $50,000. "
                "This may indicate competitive salaries or specialized positions within local governance.")
    st.markdown("  - *State Government (State-gov)*: Roughly 26.75% of individuals working in state government positions earn incomes exceeding $50,000. "
                "Similar to federal and local government roles, state government positions may offer stable income opportunities with potential for growth.")

    st.markdown("### Education")
    st.markdown("- **Lower Income Category**")
    st.markdown("  - *Preschool, 1st-4th*: Higher proportions earn <= $50K. "
                "This suggests that individuals with lower levels of education may face barriers to higher-paying employment opportunities.")
    st.markdown("- **Upper Income Group**")
    st.markdown("  - *Doctorate, Prof-school*: Predominantly earn > $50K. "
                "This underscores the value of advanced education in accessing higher-paying professions and career paths.")

    st.markdown("### Marital Status")
    st.markdown("  - *Never-married, Divorced*: More likely to have incomes <= $50K, "
                "indicating potential financial challenges associated with single or divorced status.")
    st.markdown("  - *Married-civ-spouse*: Higher proportions of incomes > $50K, "
                "possibly reflecting combined household incomes and shared financial responsibilities.")
    st.markdown("  - *Married-AF-spouse*: About 37.84% earn incomes > $50K, "
                "suggesting a potential correlation between military affiliations and higher incomes due to benefits or spousal support.")

    st.markdown("### Occupation")
    st.markdown("  - *Exec-managerial, Prof-specialty*: Higher proportions earn > $50K, "
                "indicating lucrative career paths in management and specialized professions.")
    st.markdown("  - *Handlers-cleaners, Other-service*: Higher proportions earn <= $50K, "
                "reflecting lower-paying service-oriented roles.")

    st.markdown("### Relationship Status")
    st.markdown("  - *Husband, Wife*: Higher proportions earn > $50K, "
                "potentially reflecting shared household incomes and the breadwinner role traditionally associated with husbands.")
    st.markdown("  - *Own-child, Other-relative*: Higher proportions earn <= $50K, "
                "suggesting financial dependence or familial support dynamics.")

    st.markdown("### Native Country")
    st.markdown("  - *United States*: Higher proportions earn <= $50K, "
                "indicating income disparities within the native population.")
    st.markdown("  - *Other countries*: Higher proportions earn > $50K, "
                "suggesting economic opportunities or immigration patterns favoring higher-income earners.")

    st.markdown("### Gender and Age Interaction")
    st.markdown("Among individuals with incomes > $50K, males with higher average ages tend to outperform females with higher average ages, "
                "while females with lower average ages are more likely to achieve incomes > $50K compared to males in the same age group. "
                "This highlights intersecting factors of gender and age in income attainment, potentially influenced by societal biases, career trajectories, and family dynamics.")

    st.markdown("## Recommendations")
    st.markdown("To increase the likelihood of earning over $50,000, adults can consider the following recommendations based on the insights derived from the analysis:")

    st.markdown("1. **Invest in Education**: Pursue higher levels of education such as Doctorate or Professional School degrees, as these are associated with higher proportions of individuals earning >$50K.")

    st.markdown("2. **Explore High-Income Occupations**: Consider careers in fields like Executive Management, Professional Specialties, or roles within the Federal Government, which have demonstrated higher proportions of individuals earning over $50,000.")

    st.markdown("3. **Gain Experience**: Aim to accumulate relevant experience and skills in your chosen field, as higher average ages are associated with higher incomes. This could involve seeking out opportunities for professional growth and advancement.")

    st.markdown("4. **Consider Self-Employment**: Explore opportunities for self-employment, particularly in incorporated businesses, as self-employed individuals in such sectors have a significant proportion earning >$50K.")

    st.markdown("5. **Strive for Work-Life Balance**: While higher-income occupations may require more hours of work per week, it's essential to maintain a healthy work-life balance to avoid burnout and maintain productivity.")

    st.markdown("6. **Explore Opportunities Abroad**: Consider exploring job opportunities in countries other than the United States, as individuals from other countries have shown higher proportions of earning >$50K.")

    st.markdown("7. **Network and Mentorship**: Build a strong professional network and seek out mentorship opportunities to gain insights and guidance from individuals who have achieved success in earning higher incomes.")

    st.markdown("8. **Continuous Learning and Adaptation**: Stay updated with industry trends and advancements, and be open to continuous learning and skill development to remain competitive in the job market.")

    st.markdown("By implementing these recommendations, adults can enhance their prospects of earning over $50,000 and strive towards financial success and stability.")
