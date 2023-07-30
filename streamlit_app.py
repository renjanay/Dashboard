
import streamlit as st

def main():
    st.title("Website Visualisasi Data dengan Tableau dan Streamlit")
    st.write("Contoh visualisasi data menggunakan Tableau yang disematkan di Streamlit")

    # Tambahkan URL dari visualisasi Tableau yang telah dipublikasikan
    tableau_url = "https://public.tableau.com/views/AnnualIncome_16905597262340/Sheet1?:language=en-US&:display_count=n&:origin=viz_share_link"
    
    # Tambahkan iframe untuk menyematkan visualisasi Tableau ke dalam halaman Streamlit
    st.write("Visualisasi data menggunakan Tableau:")
    st.components.v1.iframe(tableau_url, height=800)

if __name__ == "__main__":
    main()
