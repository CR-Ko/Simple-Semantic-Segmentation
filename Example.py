from semantic_segmentation import semantic_segmentation

'''
Train Model from scratch
Model name: S0 (S1 - S7)
Data path: "./Data"
save path: "./Models"
img_ext=".jpg" (Default)
mask_ext=".png" (Default)
'''

# Create model
segmenter = semantic_segmentation("S0", "./Data/", save_path="./Models/")
# Train model
segmenter.train(10)
# Predict using model
segmenter.predict("Data/Test/Images/", "./Output/")

'''
Using a pretrained model
Path to model: "./Models/"
'''
# Load pretrained model
segmenter = semantic_segmentation("./Models/")

# Predict using pretrained model
segmenter.predict("Data/Test/Images/", "./Output/")
