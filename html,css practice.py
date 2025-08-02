# html and css with streamlit
# streamlit run "html,css practice.py"

import streamlit as st
st.markdown("<p>This is a paragraph</p>", unsafe_allow_html=True)
st.markdown("Line one <br> Line two", unsafe_allow_html=True)
st.markdown("<b>Bold Text</b>", unsafe_allow_html=True)
st.markdown("<i>Italic Text</i>", unsafe_allow_html=True)
st.markdown("<u>Underlined Text</u>", unsafe_allow_html=True)

st.markdown("""
<ul>
<li> item 1 </li>
<li> item 2 </li>
</ul>
""",unsafe_allow_html=True
            )

st.markdown("""
<ol>
<li> item 1 </li>
<li> item 2 </li>
</ol>
""",unsafe_allow_html=True
            )