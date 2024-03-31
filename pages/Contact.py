import streamlit as st

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjZO826WSLKEyy9AC_97AJoI89f_GejTw9eA&usqp=CAU");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

# set_bg_hack_url()

st.title("Contact")

st.title("Project Team")

st.title("1.Abhay Lawande")
st.info(
    f' Email ID: abhaylawande2002@gmail.com Mobile No:8010877540 '
)

st.title("2.Shrikant Labade ")
st.info(
    f' Email ID: shrikantlabade123@gmail.com Mobile No.9810877540 '
)

st.title("3.Mrudula Todmal")
st.info(
    f' Email ID:mrudulatodmal03@gmail.com Mobile No.9960388950   '
)

st.title("4.Anshu Kasar ")
st.info(
    f' Email ID:anshukasar@gmail.com Mobile No.8960388950   '
)




