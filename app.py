import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Eliminador de Duplicados en CSV")
st.markdown("""
    Suba un archivo **CSV** y la aplicación eliminará las filas duplicadas basándose en todas las columnas.
""")

# Subir archivo CSV
uploaded_file = st.file_uploader("Suba un archivo CSV", type=["csv"])

if uploaded_file is not None:
    try:
        # Cargar CSV en un DataFrame
        df = pd.read_csv(uploaded_file)

        # Mostrar DataFrame original
        st.subheader("📌 Datos Originales")
        st.write(df)

        # Eliminar duplicados
        df_cleaned = df.drop_duplicates()

        # Mostrar DataFrame procesado
        st.subheader("✅ Datos sin Duplicados")
        st.write(df_cleaned)

        # Descargar CSV limpio
        csv = df_cleaned.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Descargar CSV limpio", csv, "datos_sin_duplicados.csv", "text/csv")

    except Exception as e:
        st.error(f"❌ Error al procesar el archivo: {e}")
