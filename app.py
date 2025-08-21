import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide",page_title="Startup Analysis")

df = pd.read_csv(r"C:\Users\bhavs\OneDrive\Desktop\streamlit\startup_cleaned_new.csv")
st.sidebar.title("Startup Fandin Analysis")
df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=False)
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

# General Analysis
def perfrom_general():

    with st.container():
        st.title('General Analysis')
        with st.container(vertical_alignment='top'):
            #totel investment in india
            total = round(df['amount'].sum())
        
            #maximum amount which is invested in a startup in india
            max = round(df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0])

            # avg investment amount in startups 
            avg = round(df.groupby('startup')['amount'].sum().mean())

            # totel startup
            startup = df['startup'].nunique()

            #MbM investment graph
        with st.container():
            options = ["Total", "Count"]
            st.subheader('Month On Month Chart')
            selected_option = st.selectbox(
                "select option:", options
            )
            if selected_option == "Total":
                totel = df.groupby(['year','month'])['amount'].sum().reset_index()
                fig, ax = plt.subplots(figsize=(20,10))
                # Plot with year + month as x-axis
                ax.plot(totel.index, totel['amount'], marker='o')

                ax.set_xticks(totel.index)
                ax.set_xticklabels(totel['year'].astype(str) + "-" + totel['month'].astype(str), rotation=45)

                ax.set_xlabel("Year-Month")
                ax.set_ylabel("Total Investment Amount")
                ax.set_title("Month on Month Total Investment")

                st.pyplot(fig)

            elif selected_option == "Count":
                count = df.groupby(['year','month'])['amount'].count().reset_index()
                fig, ax = plt.subplots(figsize=(20,10))
                # Plot with year, month as x-axis
                ax.plot(count.index, count['amount'], marker='o')

                ax.set_xticks(count.index)
                ax.set_xticklabels(count['year'].astype(str) + "-" + count['month'].astype(str), rotation=45)

                ax.set_xlabel("Year-Month")
                ax.set_ylabel("Total Investment Count")
                ax.set_title("Month on Month Investment Count")

                st.pyplot(fig)

    col1, col2 = st.columns(2)

    with col1:
        st.title('General Sector Analysis')
        st.subheader('Top Sector Count')
        verticals_count = df.groupby('vertical')['vertical'].count().sort_values(ascending=False).head()

        fig, ax = plt.subplots(figsize=(10,5))
        ax.pie(verticals_count, labels=verticals_count.index, autopct=lambda p: f'{int(p*sum(verticals_count)/100)}')
        ax.set_title("Top Sector by Count")

        st.pyplot(fig)

    with col2:
        st.title('')

        st.subheader('Top Sector Totel Market Size')
        verticals_sum = df.groupby('vertical')['amount'].sum().sort_values(ascending=False).head()

        fig, ax = plt.subplots(figsize=(10,7))
        ax.pie(verticals_sum, labels=verticals_sum.index, autopct=lambda p: f'{int(p*sum(verticals_sum)/100)} Cr')
        ax.set_title("Top Sector by Marketsize")

        st.pyplot(fig)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader('Top Types of funding')
        temp_df = df.groupby('investment type').size().sort_values(ascending=False).head(5)
        # Create figure
        fig, ax = plt.subplots(figsize=(10,7))
        ax.pie(temp_df, labels=temp_df.index, autopct='%1.1f%%')
        ax.axis("equal")  # Makes it a circle

        # Show in Streamlit
        st.pyplot(fig)

    with col4:
        st.subheader('Top City Investments')
        temp_df = df.groupby('city').size().sort_values(ascending=False).head(5)
        # Create figure
        fig, ax = plt.subplots(figsize=(10,7))
        ax.pie(temp_df, labels=temp_df.index, autopct='%1.1f%%')
        ax.axis("equal")  # Makes it a circle

        # Show in Streamlit
        st.pyplot(fig)    

    with st.container():
        st.header('Top Yearwise Startups')
        selected_op = st.selectbox(
            "Choose your favorite fruit:",("Year wise", "Overall")
        )
        if selected_op == "Year wise":
            st.subheader('Top Yearwise Startups')
            top_yearwise = df.groupby(['year','startup'])['amount'].sum().reset_index().sort_values(['year','amount'],ascending=[True,False]).groupby('year').head(1)
            st.dataframe(top_yearwise,hide_index=True)
        elif selected_op == "Overall":
            st.subheader('Top Overall Startups')
            top_overall = df.groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)
            st.dataframe(top_overall)

        
    with st.container():
        st.header('Top investors')
        top_investors = df.groupby('investors')['amount'].sum().sort_values(ascending=False).head(5)
        st.dataframe(top_investors)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total",str(total) + " Cr")
    with col2:
        st.metric("Max",str(max) + " Cr")
    with col3:
        st.metric("Avg",str(avg) + " Cr")
    with col4:
        st.metric('Totel Starts-Ups ',startup)

def perfrom_startup(startup):
    Startup = startup
    st.title('StartUp Analysis')
    st.header(Startup)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('Industry')
        sector = df[df['startup'] == Startup]['vertical'].iloc[0]
        st.write(sector)

    with col2:
        st.subheader('Sub-Industry')
        sub_sector = df[df['startup'] == Startup]['sub vertical'].iloc[0]
        st.write(sub_sector)

    with col3:
        st.subheader('Location')
        city = df[df['startup'] == Startup]['city'].iloc[0]
        st.write(city)

    with st.container():
        st.subheader('Funding Rounds')
        fundin_rounds = df[df['startup'] == Startup][['date','investment type','investors','amount']]
        st.dataframe(fundin_rounds,hide_index=True)

    with st.container():
        st.subheader("Some Similar Companies")
        vertical = df[df['startup'] == Startup]['vertical'].iloc[0]
        similar_companies = df[(df['vertical'] == vertical) & (df['startup'] != Startup)]['startup'].head(5)

        st.dataframe(similar_companies,hide_index=True)


def perfrom_investers(invester):
    # st.title('Investers Analysis')
    st.title(invester)
    # LOAD RESENT FIVE INVESTMENTS
    last5_df = df[df['investors'].str.contains(invester)].head()[["date","startup","vertical","city","investment type","amount"]]
    st.subheader('Recent Investments')
    st.dataframe(last5_df)

    col1, col2= st.columns(2)

    # LOAD BIGGEST FIVE INVESTMENTS
    with col1:
        st.subheader('Beggest Investments')
        biggest5_series = df[df['investors'].str.contains(invester)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.dataframe(biggest5_series)

    with col2:
        st.subheader('')
        fig, ax= plt.subplots()
        ax.bar(biggest5_series.index,biggest5_series.values)

        st.pyplot(fig)

    # Sector pie graph
    col3, col4, col5= st.columns(3)

    with col3:
        vertical_series = df[df['investors'].str.contains(invester)].groupby('vertical')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Top 5 Sectors invested in')
        fig5, ax5= plt.subplots()
        ax5.pie(vertical_series,labels=vertical_series.index, autopct='%1.1f%%')

        st.pyplot(fig5)

    with col4:
        stage_series = df[df['investors'].str.contains(invester)]['investment type'].value_counts()
        st.subheader('Investments Stage')
        fig2, ax2= plt.subplots()
        ax2.pie(stage_series,labels=stage_series.index,autopct='%1.1f%%')

        st.pyplot(fig2)

    with col5:
        city_series = df[df['investors'].str.contains(invester)]['city'].value_counts()
        st.subheader("Investments City's")
        fig2, ax2= plt.subplots()
        ax2.pie(city_series,labels=city_series.index,autopct='%1.1f%%')

        st.pyplot(fig2)

    col6, col7 = st.columns(2)

    with col6:
        df['year'] = df['date'].dt.year
        year_series = df[df['investors'].str.contains(invester)].groupby('year')['amount'].sum()
        st.subheader("YoY Investments")
        fig2, ax2= plt.subplots()
        ax2.plot(year_series.index,year_series.values)

        st.pyplot(fig2)

    with col7:
        st.subheader("Similar Investors")

        # Create pivot table: investors × verticals (amount invested)
        pivot_df = df.assign(amount=df['amount'].fillna(0)).pivot_table(
            index="investors", 
            columns="vertical", 
            values="amount", 
            aggfunc="sum", 
            fill_value=0
        )

        if invester in pivot_df.index:
            from sklearn.metrics.pairwise import cosine_similarity

            # Compute similarity
            similarity_matrix = cosine_similarity(pivot_df)
            similarity_df = pd.DataFrame(similarity_matrix, 
                                index=pivot_df.index, 
                                columns=pivot_df.index)

        # Get top 5 similar investors (excluding self)
            similar_investors = similarity_df[invester].sort_values(ascending=False).iloc[1:6]

            st.write(similar_investors)
        else:
            st.write("No similar investors found.")


        

choice = st.sidebar.selectbox("Select Option",["General Analysis","Startup Analysis","Invester Analysis"])

if choice == "General Analysis":
        perfrom_general()
elif choice == "Startup Analysis":
    startup_name = st.sidebar.selectbox("Select startup",df['startup'].unique().tolist()
)
    if st.sidebar.button('Analysis'):
        perfrom_startup(startup_name)
elif choice == "Invester Analysis":
    invester = st.sidebar.selectbox("Select Invester",sorted(set(df['investors'].str.split(",").sum()))
)
    if st.sidebar.button('Analysis'):
        perfrom_investers(invester)


