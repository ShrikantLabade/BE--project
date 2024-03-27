import time
import urllib
import numpy as np
from PIL import Image
import streamlit as st
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img
from flask import Flask
from flask_mail import Mail, Message


# @st.cache(allow_output_mutation=True, suppress_st_warning=True)

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
             background: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5OIBTJnszk9fPrvfZWIrxM9kMVN9mxA6Ivw&usqp=CAU");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )



st.set_page_config(
    page_title="Grape Leaf Disease Detection",
    page_icon="👋",
)


html_temp = """
    <div style =  padding-bottom: 20px; padding-top: 20px; padding-left: 5px; padding-right: 5px">
    <center><h1>Grape Leaf Disease Detection Using  Machine Learning</h1></center>
    
    </div>
    """

st.markdown(html_temp, unsafe_allow_html=True)
html_temp = """
    <div>
    <h2></h2>
    <center><h3>Please upload any Grape Leaf Image from the given list</h3></center>
    </div>
    """
#this is the line
#<center><h3> [Black_rot, Esca_(Black_Measles), Healthy, Leaf_blight_(Isariopsis_Leaf_Spot) ] </h3></center>

st.set_option("deprecation.showfileUploaderEncoding", False)
st.markdown(html_temp, unsafe_allow_html=True)

opt = st.selectbox(
    "How do you want to upload the image for Grape Leaf Disease Detection?\n",
    ("Please Select", "Upload image via link", "Upload image from device"),
)
if opt == "Upload image from device":
    file = st.file_uploader("Select", type=["jpg", "png", "jpeg"])
    st.set_option("deprecation.showfileUploaderEncoding", False)
    if file is not None:
        image = Image.open(file)

elif opt == "Upload image via link":

    try:
        img = st.text_input("Enter the Image Address")
        image = Image.open(urllib.request.urlopen(img))

    except:
        if st.button("Submit"):
            show = st.error("Please Enter a valid Image Address!")
            time.sleep(4)
            show.empty()

if image is not None:

    try:
        st.image(image, width=300, caption="Uploaded Image")

        if st.button("DETECT"):
            img_array = np.array(image.resize((128, 128), Image.ANTIALIAS))
            img_array = np.array(img_array, dtype="uint8")
            img_array = np.array(img_array) / 255.0

            model_dir = "Model/model2.h5"
            model = keras.models.load_model(model_dir)

            # Labels
            train_labels = {
                "Black_rot": 0,
                "Esca_(Black_Measles)": 1,
                "healthy": 2,
                "Leaf_blight_(Isariopsis_Leaf_Spot)": 3,

            }
            labels = dict((value, key) for key, value in train_labels.items())

            # Predicting
            predictions = model.predict(img_array[np.newaxis, ...])
            acc = np.max(predictions[0]) * 100
            result = labels[np.argmax(predictions[0], axis=-1)]

            # with open('readme.txt', 'w') as f:
            #     f.write(result)
            # set_bg_hack_url()


            # Displaying output
            st.info(
                f'The uploaded image has been Detected as " {result}"'# with confidence {acc}%.'
            )
            # if result == "Black_rot":
            #     st.info(
            #         f'Where black rot is a problem, apply a fungicide every 14 days after the "New Shoot" spray up to and including the "Before Ripening" spray. During long rainy periods, shorten the interval to 7 to 10 days between sprays.'
            #     )
            if result == "Black_rot":
                st.info(
                    f'To treat black rot in grape leaves, consider the following steps:\n\n'
                    f'1. **Pruning:** Remove and destroy infected plant parts, including leaves, shoots, and canes during the dormant season.\n\n'
                    f'2. **Fungicides:** Apply fungicides labeled for black rot control. Bordeaux mixture or other recommended fungicides can be effective, but follow guidelines and application schedules.\n\n'
                    f'3. **Sanitation:** Keep the vineyard clean by removing fallen leaves and debris, as they can harbor the fungus and contribute to the disease cycle.\n\n'
                    f'4. **Cultural Practices:** Ensure proper spacing between vines for good air circulation, promoting a less favorable environment for the fungus.\n\n'
                    f'5. **Timing:** Apply treatments at the right time, especially during critical growth stages and favorable weather conditions for disease development.'
                )
            #
            # if result == "Esca_(Black_Measles)":
            #         st.info(
            #             f'A preventive/curative treatment of grapevine towards fungal induced esca is proposed. A mixture of antimicrobial molecules inhibit mycelial growth and spore germination. The efficiency of the treatment can be monitored by an immunological assay.'
            #         )

            if result == "Esca_(Black_Measles)":
                st.info(
                    f'Esca disease, also known as "Black Measles," is a complex grapevine trunk disease caused by various fungi. Symptoms include wilting, leaf discoloration, and characteristic tiger-striped patterns. Managing Esca involves several strategies:\n\n'
                    f'1. **Pruning:** Remove and destroy infected wood during pruning to limit the spread of the disease.\n\n'
                    f'2. **Protective Wound Dressings:** Apply protective wound dressings to cuts and wounds on vines to reduce the risk of fungal infection.\n\n'
                    f'3. **Fungicides:** Some fungicides may help protect against Esca, but they are not always fully effective. Consult with local experts for appropriate fungicide recommendations.\n\n'
                    f'4. **Cultural Practices:** Maintain good vineyard hygiene, and avoid excessive pruning during wet periods.\n\n'
                    f'5. **Resistant Varieties:** Consider planting grape varieties that are less susceptible to Esca.\n\n'
                    f'It\'s crucial to monitor vineyards regularly and seek advice from local viticulture experts for the most effective and region-specific management strategies.\n'
                    f'The disease can be monitored by an immunological assay, and a preventive/curative treatment involving a mixture of antimicrobial molecules may be employed to inhibit mycelial growth and spore germination.'
                )

            # if result == "Leaf_blight_(Isariopsis_Leaf_Spot)":
            #         st.info(
            #             f'Proper pruning helps improve air circulation and sunlight penetration, reducing humidity around the grapevines. Ensure proper spacing between grapevines to enhance air circulation.Sanitation: Regularly remove and destroy infected leaves, canes, and debris on the ground to reduce the source of inoculum. Use drip irrigation to keep the foliage dry, as wet conditions can promote the development of leaf diseases.'
            #         )

            if result == "Leaf_blight_(Isariopsis_Leaf_Spot)":
                st.info(
                    f'Leaf blight in grapevines, often caused by fungal pathogens, can be effectively managed through the following steps:\n\n'
                    f'1. **Fungicides:** Apply fungicides labeled for leaf blight control. Copper-based fungicides or those containing other effective ingredients can be used. Follow recommended application schedules.\n\n'
                    f'2. **Pruning:** Remove and destroy infected leaves during routine pruning to reduce the disease load.\n\n'
                    f'3. **Sanitation:** Keep the vineyard clean by regularly removing fallen leaves and debris, as they can harbor fungal spores.\n\n'
                    f'4. **Spacing and Air Circulation:** Ensure proper vine spacing to allow for good air circulation, creating an environment less conducive to fungal growth.\n\n'
                    f'5. **Avoid Overhead Irrigation:** Minimize overhead irrigation, as wet foliage can promote the spread of fungal diseases. Drip irrigation is preferable.\n\n'
                    f'6. **Cultural Practices:** Maintain overall vineyard health through appropriate nutrient management and soil care.\n\n'
                    f'Proper pruning helps improve air circulation and sunlight penetration, reducing humidity around the grapevines. Ensure proper spacing between grapevines to enhance air circulation.\n\n'
                    f'Sanitation is crucial; regularly remove and destroy infected leaves, canes, and debris on the ground to reduce the source of inoculum. Use drip irrigation to keep the foliage dry, as wet conditions can promote the development of leaf diseases.'
                )

            if result == "healthy":
                    st.info(
                        f'Great you Have Healthy Grapes crops Keep Monitoring and checks regularly to prevent any Disease Should not catch '
                    )
                    exec(open("email1.py").read())


    except:
        st.success("Please enter an Input Image of an appropriate format :) ")