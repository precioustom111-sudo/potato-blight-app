# Potato Blight Classifier

A CNN-based image classifier that distinguishes Potato Early Blight from Potato Late Blight, built with MobileNetV2 transfer learning and deployed via Streamlit.

## Dataset
Sourced from the PlantVillage dataset (Kaggle), filtered to Potato Early Blight and Late Blight classes.

## How to Use
1. Open the deployed app link.
2. Upload an image of a potato leaf.
3. The app displays the predicted class (Early Blight or Late Blight) with confidence score.

## Model Performance
- Test accuracy: 94.9%
- Precision/Recall balanced across both classes (see confusion matrix)

## Live App
[Try the app here](https://potato-blight-app-sp6k3ucnwqzlqrjfnrra8j.streamlit.app/)

# Potato Early Blight Vs Potato Late Blight

A CNN-based image classifier that distinguishes Potato Early Blight from Potato Late Blight, built with MobileNetV2 transfer learning and deployed via Streamlit.

## Live App
[Try the app here](https://potato-blight-app-sp6k3ucnwqzlqrjfnrra8j.streamlit.app/)

## Dataset
Sourced from the PlantVillage dataset (Kaggle), filtered to Potato Early Blight and Late Blight classes.

## How to Use
1. Open the deployed app link above.
2. Upload an image of a potato leaf.
3. The app displays the predicted class (Early Blight or Late Blight) with a confidence score.

## Model Performance
- Training accuracy: ~97.9%
- Validation accuracy: ~95.9%
- Test accuracy: 94.9%
- Precision/Recall balanced across both classes (see confusion matrix)

## Report
This project uses a CNN (MobileNetV2 transfer learning) to classify potato leaf images as Early Blight or Late Blight. The dataset was sourced from the PlantVillage dataset on Kaggle, filtered to the two target classes. The model was trained for 10 epochs, achieving 94.9% accuracy on a held-out test set. The application was built with Streamlit, allowing users to upload a leaf image and receive an instant prediction with confidence score. It was deployed on Streamlit Community Cloud, with the source code managed on GitHub. The main challenge encountered was a Python/TensorFlow version mismatch between the local training environment and the cloud deployment environment, which caused model-loading errors. This was resolved by pinning the exact TensorFlow version used locally in the requirements file, ensuring compatibility across environments.

## Contributors
- [TOM PRECIOUS VICTOR] — [23/EG/CE/024] — [precioustom111-sudo]
- [ETETE JESSIE BASSEY] -[23/EG/CE/044] - [basseyjessie16-maker]
- [UKO GOD'SWILL DENIS] - [23/EG/CE/034] - [godswilldenis04-collab]
- [UDOIBE IDARESIT FRANCIS] - [23/EG/CE/104] - [udoibe idaresit francis]
- [JOHN ETIUWEM VICTOR] - [23/EG/CE/074] -[Etiuwem]
