import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'gspread'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'oauth2client'])

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st


import gspread
from pandas import Categorical
import pandas as pd

gc = gspread.service_account(filename=r'./tugas-latsar-9e9e659bd6d2.json')

sh = gc.open("latsar")
worksheet = sh.get_worksheet(0)


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Cek Permohonan Anda", page_icon=":tada:", layout="wide")

#header
st.subheader("INPUT NOMOR PELAYANAN ANDA")


# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead, th {display: none;}
            .blank {display:none}
            thead, th, td  {width: 100px}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)



def tombolcari(carinomor):

    st.write("---")
    st.write("Rangkuman")
    keterangan = worksheet.row_values(1)
    cell = worksheet.find(carinomor)
    if cell is None:
        st.error('Nomor tidak ditemukan')
    else:
        hasil = worksheet.row_values(cell.row)
        df = pd.DataFrame([ keterangan,hasil])
        keterangan1 = keterangan[21:23]+keterangan[24;34]
        hasil1 = hasil[3:5]+hasil[6:16]
        df1 = pd.DataFrame([keterangan1,hasil1])
        st.table(df[[0,1,2]].T)

        st.write("---")
        st.write("Detail")
        st.table(df1.T)


inputnomor0 ='S-22.'
inputnomor = st.text_input('Contoh: S-22.0001',value="S-22.",max_chars=9)
button = st.button('Cari')


if inputnomor != inputnomor0:
    tombolcari(inputnomor)

