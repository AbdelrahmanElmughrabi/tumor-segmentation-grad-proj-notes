Goal:
The user uploads a medical image, the system runs the model, and the prediction is displayed on the screen.
### The application can have 4 main functions

1. **Data upload**
    
    - Upload a single image file
        
    - or upload a small folder
        
    - for the first version, a single image is better
        
2. **Preview**
    
    - Show the uploaded image on the screen
        
    - Display basic file information such as file name, size, and format
        
3. **Prediction**
    
    - When the user clicks **Predict**, the model runs
        
    - The system outputs a prediction such as **benign** or **malignant**
        
    - If available, a segmentation mask can also be shown
        
4. **Result display**
    
    - Predicted class
        
    - Confidence score
        
    - Original image
        
    - Mask overlay or heatmap
        
    - Optional **Save Result** button

Stack:
- **Desktop GUI:** PySide6
- - **Packaging:** PyInstaller