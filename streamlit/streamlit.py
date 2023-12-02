import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# untuk menjalankan streamlit, ketik di terminal: streamlit run streamlit.py

# ini untuk menampilkan teks
st.write(
    """
    # My first app
    Hello *world!*
    """
)

# ini untuk menampilkan dataframe
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# markwdown untuk menampilkan teks
st.markdown(
    """
    ## My first app
    Hello, ini mark down!
    """
)

st.title("Belajar analisis data, ini title!")

st.header("Ini header!")

st.subheader("Ini subheader!")

# code utk menampilkan code
code = '''def hello():
    print("Ini st code!")'''
st.code(code, language='python')

st.text("Ini text!")

# latex utk menampilkan rumus
st.latex(r'''
...     \sum_{k=0}^{n-1} ar^k =
         a\left(\frac{1-r^{n}}{1-r}\right)
            ''')

# ini data display
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.dataframe(data=df, width=300, height=100)

# ini data table
st.table(data=df)

# metric utk menampilkan angka
st.metric(label="Temperature", value="70 F", delta="1.2")

# st json utk menampilkan json
st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

x = np.random.normal(15, 5, 250)
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)
