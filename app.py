import streamlit as st
from count_apples import detect_count_apples

st.title("Web App for counting red apples in real world images")
st.write("By: Shrishail Gajbhar, PhD")
# add_bg_from_local('pic2.png')
upload = st.file_uploader("Upload image", type=['png', 'jpg'])

c1, c2 = st.columns(2)

inp_img = c1.button("View input image")
out_img = c2.button("Count apples")

if upload is not None and inp_img == True:
    st.subheader("You uploaded following image")
    st.image(upload)
elif upload is not None and out_img == True:
    num_apples, result = detect_count_apples(upload)
    if num_apples > 1:
        st.subheader(f"The total number of detected apples are {num_apples}!")
        st.image(image=result)
    else:
        st.subheader("It seems the input image doesn't have apples!!")
else:
    st.subheader("You have not uploaded any image yet!!")
