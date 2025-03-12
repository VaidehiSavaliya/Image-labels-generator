📸 Image Labels Generator :

This project uses Amazon Rekognition, S3, and AWS CLI to detect and display labels in images. It also draws bounding boxes around objects and displays confidence scores for accurate visual analysis.

🚀 Features :

~ Detects objects, scenes, and concepts using Amazon Rekognition.
~ Draws bounding boxes on detected objects with labels and confidence scores.
~ Uses AWS S3 for image storage and retrieval.
~ Visualizes image analysis results.

📂 Project Structure :

Image-labels-generator/
├── images/              # Input images for analysis
├── output/              # Processed images with bounding boxes
├── scripts/             # Python scripts for Rekognition and visualization
└── README.md            # Project documentation (this file)

🛠️ Prerequisites :

=> Ensure you have the following installed:

~ Python 3.x
~ AWS CLI (configured with valid credentials)
~ boto3 (AWS SDK for Python)
