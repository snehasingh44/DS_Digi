import streamlit as st

st.title("Demo App")

n1 = st.number_input("Enter Number)")
n2 = st.number_input("Enter Another Number)")
c1, c2, c3, c4, c5, c6 = st.columns(6)
add =  c1.button("add")
subtract = c2.button("subtract")
mul = c3.button("Multiply")
div = c4.button("Divide")
exp = c5.button("Exponent")
mod = c6.button("Modulus")
if add:
    r = int(n1) + int(n2)
    st.success(r)
if subtract:
    r = int(n1)- int(n2)
    st.success(r)
if mul:
    r = int(n1)* int(n2)
    st.success(r)
if div:
    r = int(n1)/ int(n2)
    st.success(r)
if exp:
    r = int(n1)** int(n2)
    st.success(r)
if mod:
    r = int(n1)% int(n2)
    st.success(r)