# Garbage Detector

**Garbage Detector** is an advanced deep learning project developed by me using ChatGPT to automatically identify and classify various types of waste (sampah) in images. This project leverages state-of-the-art object detection techniques to facilitate smart waste management, improve environmental monitoring, and support automated sorting systems.

## Features

- Detects multiple categories of waste including Plastic, Paper, Metal, Glass, and Organic materials.
- Real-time detection capabilities for both images and videos.
- Fully customizable to accommodate different datasets and class categories.
- Supports applications in smart waste management and robotic sorting solutions.

## Model Overview

The project uses **YOLOv8**, a cutting-edge object detection framework known for its speed and accuracy. YOLOv8 predicts bounding boxes and class probabilities for multiple objects in a single pass. Key highlights include:

- **High accuracy and speed:** Optimized for real-time inference.
- **Scalability:** Effective on datasets of varying sizes.
- **Flexibility:** Can be fine-tuned for specific waste categories and input resolutions.
- **Confidence scoring:** Provides confidence levels for detected objects to filter low-confidence predictions.

## Dataset Structure

The dataset is structured for object detection workflows:

- **images/train and images/valid:** Training and validation images.
- **labels/train and labels/valid:** YOLO-format label files defining object locations and classes.
- **data.yaml:** Contains dataset paths, number of classes, and class names.

## Usage Notes

- Adjust batch size according to available GPU memory to prevent out-of-memory issues.
- A diverse set of images per waste category improves model generalization and detection performance.
- Smaller YOLO variants can be used if computational resources are limited.

## Acknowledgements

- **ChatGPT:** For guidance and support in developing the project.
- **Ultralytics:** For providing the YOLOv8 framework and documentation.
- **Open-source contributors:** For datasets, tutorials, and tools that aided in building and training the model.
- **Research community:** For advancements in computer vision and deep learning that made this project possible.

## References

- [YOLOv8 Documentation](https://docs.ultralytics.com/)
- [Ultralytics GitHub Repository](https://github.com/ultralytics/ultralytics)

## License

This project is released under the MIT License.

