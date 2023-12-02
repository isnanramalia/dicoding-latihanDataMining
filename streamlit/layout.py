# BASIC LAYOUT DLM STREAMLIT
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# 1: Sidebar
st.title('Belajar Analisis Data - Streamlit')

with st.sidebar:
    st.text('Ini adl sidebar')

    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=100, value=(0, 100)
    )

    st.write('values:', values)


# 2: Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.header("kolom 1")
    st.image("https://picsum.photos/200/300")

with col2:
    st.header("kolom 2")
    st.image("https://picsum.photos/200/300")

with col3:
    st.header("kolom 3")
    st.image("https://picsum.photos/200/300")


# 3: Tabs
tab1, tab2, tab3 = st.tabs(['tab 1', 'tab 2', 'tab 3'])

with tab1:
    st.text('tab 1')
    st.image("https://static.streamlit.io/examples/cat.jpg")

with tab2:
    st.text('tab 2')
    st.image("https://static.streamlit.io/examples/dog.jpg")

with tab3:
    st.text('tab 3')
    st.image("https://static.streamlit.io/examples/owl.jpg")


# 4: Container
with st.container():
    st.write("Inside the container")

    x = np.random.normal(15, 5, 250)

    fig, ax = plt.subplots()
    ax.hist(x, bins=20)
    st.pyplot(fig)

st.write("Outside the container")


# 5: Expander --> utk menampilkan data yg panjang
x = np.random.normal(15, 5, 250)

fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

with st.expander(label='See explanation'):
    st.write("""
        The histogram of the data is positively skewed, with a skewness of 0.95. 
        This shows that the tail of the distribution is longer on the right hand side than on the left hand side. 
        This means that the data is more spread out towards the right hand side.
    """)
