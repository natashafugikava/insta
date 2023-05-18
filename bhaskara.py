import streamlit as st

st.title('Calculadora de equação do segundo grau')

a = st.number_input('Digite o valor de a:', value=1)
b = st.number_input('Digite o valor de b:', value=-5)
c = st.number_input('Digite o valor de c:', value=6)



delta = b**2 - 4*a*c
try:
  if delta > 0:
    x1 = (-b + delta**(1/2))/(2*a)
    x2 = (-b - delta**(1/2))/(2*a)
    st.write(f'As raízes são {x1:.2f} e {x2:.2f}.')
  elif delta == 0:
    x = -b/(2*a)
    st.write(f'Raiz dupla igual a {x:.2f}.')
  else:
    st.write('A equação não possui raízes reais.')
except:
  st.write('O valor de a não pode ser zero!')
