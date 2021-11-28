import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import joblib
import streamlit as st


st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("diabetes Prediction")
st.text("Provide URL of bean Image for image classification")

@st.cache(allow_output_mutation=True)
def load_model():
  model = joblib.load('/app/model/pima_model.joblib')
  return model

with st.spinner('Loading Model Into Memory....'):
  model = load_model()

classes=['angular_leaf_spot','bean_rust','healthy']

path = st.text_input('Enter numbers to classify.. ','6,148,72,35,0,33.6,0.627,50')
if path is not None:
    content = list(map(float, string.split(',')))


    st.write("Predicted Class :")
    with st.spinner('classifying.....'):
      label =model.predict([content])
      st.write(label)
    st.write("")

