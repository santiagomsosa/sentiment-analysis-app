import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

from pysentimiento import SentimentAnalyzer

analyzer = SentimentAnalyzer()

user_input = st.text_input("Ingresa la frase a analizar")

if user_input:
	res = analyzer.predict(user_input)

	if res == "POS":
		st.markdown("<span style='color:green'>La frase ingresada es positiva :+1: (es un comentario positivo)</span>", unsafe_allow_html=True)
	elif res == "NEG":
		st.markdown("<span style='color:red'>La frase ingresada es negativa :thumbsdown: (es un comentario negativo)</span>", unsafe_allow_html=True)
	else:
		st.markdown("La frase es neutra, no es positiva ni negativa")
