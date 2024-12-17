import streamlit as st
import pandas as pd
import numpy as np
import pickle # jika Anda memiliki model yang sudah dilatih
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


st.set_page_config(
        page_title="Tugas Akhir Prediksi Dataset",
        page_icon="Logo.png",
)


# Input di sidebar (ganti dengan input yang sesuai untuk model Anda)
st.sidebar.header('Fitur Input Pengguna')

# Contoh input pengguna
def user_input_features():
    # Anda bisa menambahkan lebih banyak input di sini sesuai dengan model Anda
    if page1 == "Dataset Pumpkin Seeds":
        # Judul dan Deskripsi
        st.title("Aplikasi Prediksi Pumpkin Seeds")
        st.write("""
        Aplikasi ini memprediksi **Pumpkin Seeds** berdasarkan fitur input!
        """)
        area = st.number_input('Area', min_value=0, max_value=100000, value=0)
        perimeter = st.number_input('Perimeter', min_value=0.0, max_value=100000.0, value=0.0)
        Major_Axis_Length = st.number_input('Panjang Sumbu Utama', min_value=0.0, max_value=100000.0, value=0.0)
        Minor_Axis_Length = st.number_input('Panjang Sumbu Kecil', min_value=0.0, max_value=100000.0, value=0.0)
        Convex_Area = st.number_input('Convex Area', min_value=0, max_value=100000, value=0)
        Equiv_Diameter = st.number_input('Equiv_Diameter', min_value=0.0, max_value=100000.0, value=0.0)
        Eccentricity = st.number_input('Eccentricity)',min_value=0.0, max_value=10000.0, value=0.0)
        Solidity =st.number_input('Solidity',min_value=0.0, max_value=10000.0, value=0.0)
        Extent = st.number_input('Extent',min_value=0.0, max_value=10000.0, value=0.0)
        Roundness = st.number_input('Roundness',min_value=0.0, max_value=10000.0, value=0.0)
        Aspect_Ration = st.number_input('Aspect_Ration',min_value=0.0, max_value=10000.0, value=0.0)
        Compactness = st.number_input('Compactness',min_value=0.0, max_value=10000.0, value=0.0)

        data = {
            'Area': area,
            'Perimeter': perimeter,
            'Major_Axis_Length': Major_Axis_Length,
            'Minor_Axis_Length': Minor_Axis_Length,
            'Convex_Area': Convex_Area,
            'Equiv_Diameter': Equiv_Diameter,
            'Eccentricity': Eccentricity,
            'Solidity' : Solidity,
            'Extent' : Extent,
            'Roundness' : Roundness,
            'Aspect_Ration' : Aspect_Ration,
            'Compactness' : Compactness
        }

        features = pd.DataFrame(data, index=[0])
        return features
    
    elif page1 == "Dataset Fish":
        # Judul dan Deskripsi
        st.title("Aplikasi Prediksi Jenis Ikan")
        st.write("""
        Aplikasi ini memprediksi **Jenis Ikan** berdasarkan fitur input!
        """)
        length = float(st.number_input('panjang 📏:'))
        weight = float(st.number_input('Bobot :'))
        w_l_ratio = float(st.number_input('Ratio :'))
        

        data = {
            
            'length':length,
            'weight': weight,
            'w_l_ratio':w_l_ratio,
        
        }
    
    elif page1=="Dataset Fruit":
        # Judul dan Deskripsi
        st.title("Aplikasi Prediksi Nama Buah")
        st.write("""
        Aplikasi ini memprediksi **Nama Buah** berdasarkan fitur input!
        """)
        diameter =float(st.number_input('Diameter'))
        weight = float(st.number_input('Berat (weight)'))
        red = int(st.number_input('Merah'))
        green = int(st.number_input('Hijau'))
        blue = int(st.number_input('Biru'))
        
        data = {
            'diameter': diameter,
            'weight': weight,
            'red' : red,
            'green' : green,
            'blue' : blue 
        }

        
    features = pd.DataFrame(data, index=[0])
    return features

    

page1 = st.sidebar.selectbox("Pilih Program", ("Dataset Fruit", "Dataset Fish", "Dataset Pumpkin Seeds"))
page2 = st.sidebar.selectbox("Pilih Algoritma", ("SVM", "Random Forest", "Perceptron"))


input_df = user_input_features()

bt1 = st.button('Prediksi')
if bt1 :
        if page1== "Dataset Fish":
            if page2=="SVM":
                model = pickle.load(open('fish-svm.pkl' , mode='rb'))
            elif page2=="Random Forest":
                model = pickle.load(open('fish_forest.pkl' , mode='rb'))
            elif page2=="Perceptron":
                model = pickle.load(open('fish_perceptron.pkl' , mode='rb'))
            prediksi1 = model.predict(input_df)
            print(prediksi1)
            st.write(f'Ikan nya adalah : {prediksi1}')
                 
        elif page1=="Dataset Fruit":
            if page2=="SVM":
                model = pickle.load(open('fruit_svm.pkl' , mode='rb'))
            elif page2=="Random Forest":
                model = pickle.load(open('fruit_forest.pkl' , mode='rb'))
            elif page2=="Perceptron":
                model = pickle.load(open('fruit_perceptron.pkl' , mode='rb'))
            prediksi1 = model.predict(input_df)
            st.write(f'Buah nya adalah : {prediksi1[0]}')

        elif page1=="Dataset Pumpkin Seeds":
            if page2=="SVM":
                model = pickle.load(open('pumpkin_svm.pkl' , mode='rb'))
            elif page2=="Random Forest":
                model = pickle.load(open('pumpkin_forest.pkl' , mode='rb'))
            elif page2=="Perceptron":
                model = pickle.load(open('pumpkin_perceptron.pkl' , mode='rb'))
            prediksi1 = model.predict(input_df)
            st.write(f'Pumpkin Seeds nya adalah : {prediksi1[0]}')

