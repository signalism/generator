import streamlit as st
from generate import STYLES, generate

st.set_page_config(page_title='Signalist Poetry Generator', page_icon=':boom:')

st.title('Signalist Poetry Generator')

style = st.selectbox('Choose poetic style:', [ *STYLES.keys() ])
output_len = int(st.radio('Choose poem length in characters: ', ['200', '500', '1000']))
input = st.text_input('Provide poem inspiration:')

if input:
	with st.spinner('Sit tight, generating... :hourglass_flowing_sand:'):
		output = generate(style, input, output_len)

	st.subheader('Your very own signalist poem :sunglasses::')
	st.write(output)

