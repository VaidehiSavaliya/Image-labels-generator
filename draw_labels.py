import json
import cv2
import matplotlib.pyplot as plt

# Define the images and corresponding JSON files
images = [
    ("rose.jpg", "rose_output.json"),
    ("human.jpg", "human_output.json"),
    ("elephant.jpg", "elephant_output.json"),
    ("temple.jpg", "temple_output.json")
]

# Function to draw bounding boxes with improved styling
def draw_bounding_boxes(image, data):
    for label in data['Labels']:
        for instance in label.get('Instances', []):
            box = instance['BoundingBox']

            height, width, _ = image.shape
            left = int(box['Left'] * width)
            top = int(box['Top'] * height)
            box_width = int(box['Width'] * width)
            box_height = int(box['Height'] * height)

            # Customize box color and thickness
            color = (255, 0, 0)  # Red color
            thickness = 3

            # Draw rectangle
            cv2.rectangle(image, (left, top), (left + box_width, top + box_height), color, thickness)

            # Customize label text
            confidence = instance['Confidence']
            label_text = f"{label['Name']} ({confidence:.1f}%)"

            # Draw label background for better visibility
            (text_width, text_height), _ = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
            cv2.rectangle(image, (left, top - text_height - 10), (left + text_width, top), color, -1)

            # Draw label text
            cv2.putText(image, label_text, (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

            # Draw parent labels (if any)
            parent_labels = ", ".join(parent['Name'] for parent in label.get('Parents', []))
            if parent_labels:
                parent_text = f"Parents: {parent_labels}"
                cv2.putText(image, parent_text, (left, top + box_height + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    return image

# Process each image
for image_path, json_path in images:
    # Load Rekognition output
    with open(json_path) as f:
        data = json.load(f)

    # Load the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Draw the improved bounding boxes
    image_with_boxes = draw_bounding_boxes(image, data)

    # Display the image
    plt.figure(figsize=(12, 8))
    plt.imshow(image_with_boxes)
    plt.axis('off')
    plt.title(f"Detected Objects - {image_path}")
    plt.show()

    # Save the output image
    output_filename = f"output_with_boxes_{image_path}"
    cv2.imwrite(output_filename, cv2.cvtColor(image_with_boxes, cv2.COLOR_RGB2BGR))

    print(f"Saved output image as {output_filename}")
