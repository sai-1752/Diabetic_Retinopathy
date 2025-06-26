from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model(r'C:\Users\bijiv\Music\DIABETIC_RETINOPATHY\FRONTEND\model.h5')

# Define your class names
class_names = np.array(['Mild', 'Moderate', 'No_DR', 'Proliferate_DR', 'Severe'])

def validate_image(img):
    """Ensure the uploaded file is an image."""
    try:
        Image.open(img).verify()
    except Exception:
        raise ValidationError("Uploaded file is not a valid image.")

def preprocess_image(image):
    """Preprocess the image to match the model's input."""
    img = Image.open(image)
    img = img.resize((124, 124))  # Resize to match your model's input size
    img_array = np.array(img).astype(np.float32)
    img_array = img_array / 255.0  # Normalize to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Home page view
def home(request):
    return render(request, 'index.html')

# Input page view for login
def input(request):
    file_name = 'account.txt'
    name = request.POST.get('name')
    password = request.POST.get('password')
    with open(file_name, 'r') as file:
        account_list = [line.split() for line in file]
    for account in account_list:
        if account[0] == name and account[1] == password:
            return render(request, 'input.html')
    return HttpResponse('Wrong Password or Name', content_type='text/plain')

# Output page view for prediction
def output(request):
    img = request.FILES['file']
    
    # Validate the uploaded image
    try:
        validate_image(img)
    except ValidationError as e:
        return HttpResponse(str(e), content_type="text/plain")
    
    # Preprocess the image
    preprocessed_img = preprocess_image(img)
    
    # Predict the class
    predictions = model.predict(preprocessed_img)
    predicted_class_index = np.argmax(predictions)
    predicted_class = class_names[predicted_class_index]
    
    print(f"Predicted class index: {predicted_class_index}")
    print(f"Predicted class name: {predicted_class}")
    
    return render(request, 'output.html', {'out': predicted_class})