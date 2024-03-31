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
             background: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGIkixQL5xLQNQ-DHJ3wW0TGiOWm8mZkjVuw&usqp=CAU");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

st.title("About Project")

st.title("What is Grapes Leaf disease detection using Machine Learning?")

st.info(f'Data Collection:Gather a diverse dataset of grape leaf images that include healthy leaves as well as leaves affected by various diseases, including Isariopsis Leaf Spot or other common grape leaf diseases.')

st.info(f'Data Preprocessing: Clean and preprocess the images to enhance the quality of the dataset. This may involve resizing, cropping, and normalizing the images.')

st.info(f'Image Feature Extraction: Extract relevant features from the images that can be used as input for machine learning algorithms. Common approaches include using techniques like color histograms, texture analysis, or deep learning-based feature extraction.')

st.info(f'Model Selection:Choose a suitable machine learning model for classification. Convolutional Neural Networks (CNNs) are often used for image classification tasks due to their ability to automatically learn hierarchical features.')

st.info(f'Model Training:Split the dataset into training and testing sets. Train the chosen model on the training set, adjusting the models parameters to minimize the classification error.')

st.info(f'Validation: Validate the trained model using the testing set to assess its performance. This step helps ensure that the model generalizes well to new, unseen data.')

st.info(f'Hyperparameter Tuning: Fine-tune the models hyperparameters to optimize its performance. This may involve adjusting learning rates, regularization parameters, or other model-specific settings.')

st.info(f'Deployment: Once the model achieves satisfactory performance, it can be deployed for real-world use. This may involve integrating it into a web application, mobile app, or other platforms for practical implementation.')

# set_bg_hack_url()


