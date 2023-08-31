import streamlit as st

st.write('''
# This is an streamlit App
## Created by: Manish Khatri
## Roll no. : 21f3002258
 
This app will Find the largest number amoung given three numbers
''')

def Find_largest(n1,n2,m3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3

n1=st.number_input('First Number')
n2=st.number_input('Second Number')
n3=st.number_input('Third Number')

max=Find_largest(n1,n2,n3)

st.write(f'Largest number is {max}')


