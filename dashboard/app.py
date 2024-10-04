import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from babel.numbers import format_currency
sns.set(style='dark')

# load dataset
bike_sharing = pd.read_csv("dashboard/all_data.csv")
bike_sharing['date'] = pd.to_datetime(bike_sharing['date'])

# set title
st.set_page_config(page_title="Bike-Sharing Dashboard by Akbar Alfaidah",
                   page_icon="bar_chart:",
                   layout="wide")

# Functions for Data Preparation


def create_seasonly_data(bike_sharing):
    seasonly_data = bike_sharing.groupby("season_daily").agg({
        "total_count_hourly": "sum"
    }).reset_index()
    return seasonly_data


def create_membership_data(bike_sharing):
    membership_data = bike_sharing.groupby("year_daily").agg({
        "nonmember_hourly": "sum",
        "member_hourly": "sum"
    }).reset_index()
    return membership_data


# Prepare Filtered Data
min_date = bike_sharing["date"].min()
max_date = bike_sharing["date"].max()

with st.sidebar:
    st.image("dashboard/logo.png")
    start_date, end_date = st.date_input("Filter Tanggal",
                                         min_value=min_date.date(),
                                         max_value=max_date.date(),
                                         value=[min_date.date(), max_date.date()])

# Filter Data
filtered_data = bike_sharing[
    (bike_sharing["date"] >= pd.Timestamp(start_date)) &
    (bike_sharing["date"] <= pd.Timestamp(end_date))
]

# Get the Prepared Data
seasonly_data = create_seasonly_data(filtered_data)
membership_data = create_membership_data(filtered_data)

# Dashboard Title
st.title("Bike-Sharing Dashboard :bar_chart:")
st.markdown("## Analisis Penggunaan Berdasarkan Musim dan Keanggotaan")

# Chart 1: Bike Usage by Season
fig1 = px.bar(seasonly_data,
              x='season_daily',
              y='total_count_hourly',
              color_discrete_sequence=["orange"],
              title='Penggunaan Bike Sharing Berdasarkan Musim')
st.plotly_chart(fig1, use_container_width=True)

# Chart 2: Membership Comparison by Year
fig2 = px.bar(membership_data,
              x='year_daily',
              y=['nonmember_hourly', 'member_hourly'],
              barmode='group',
              color_discrete_sequence=["blue", "red"],
              title='Perbandingan Penggunaan Non-Anggota vs Anggota per Tahun')
st.plotly_chart(fig2, use_container_width=True)

st.caption('Dashboard ini menampilkan bagaimana penggunaan bike-sharing dipengaruhi oleh musim dan perbandingan pengguna berdasarkan keanggotaan.')
st.caption('Copyright © created by Akbar Alfaidah || 2024')
