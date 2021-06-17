import streamlit as st
from generate import generate

st.title('Signalist Poetry Generator')

output_len = int(st.radio('Choose poem length in characters: ', ['200', '500', '1000']))
input = st.text_input('Provide poem inspiration:')

if input:
	with st.spinner('Sit tight, generating... :hourglass_flowing_sand:'):
		output = generate(input, output_len)

	st.subheader('Your very own signalist poem :sunglasses::')
	st.write(output)

