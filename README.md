# Panoramiq

Panoramiq is a web application that creates stunning panoramic images by seamlessly stitching together multiple photos. Leveraging the power of Python, Flask, and OpenCV, this project processes uploaded images to detect features, calculate image transformations, and blend them seamlessly. The result is a high-resolution panoramic image that captures the full breadth of a scene.

## Features

- **Image Upload**: Users can upload multiple photos directly through the web interface.
- **Automatic Feature Detection**: Uses OpenCV to detect key points and features in the images.
- **Image Stitching**: Automatically calculates transformations and aligns the images to create a seamless panorama.
- **High-Resolution Output**: Produces high-quality panoramic images that preserve detail and clarity.
- **Web-Based Interface**: Built with Flask, allowing for an interactive and user-friendly experience.

## Technologies Used

- **Python**: Core programming language for the backend processing and image stitching logic.
- **Flask**: Web framework used to create the user interface and handle server-side operations.
- **OpenCV**: Computer vision library used for image processing, feature detection, and stitching.

## Installation

To run Panoramiq locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/panoramiq.git
   cd panoramiq
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   flask run
   ```

5. **Open your browser** and navigate to `http://127.0.0.1:5000` to use Panoramiq.

## Usage

1. **Upload Images**: Click on the "Upload" button to select multiple images from your computer.
2. **Create Panorama**: Once the images are uploaded, click "Stitch Images" to start the panorama creation process.
3. **Download Output**: After processing, the panoramic image will be displayed. You can download it directly from the interface.

## Contributors

- **Shamanth Shetty**
- **Anoop V Acharya**

*If you'd like to contribute, please reach out or submit a pull request!*

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs or feature requests.

## License

This project is yet to be licensed.

## Acknowledgments

We would like to thank the open-source community for providing valuable resources and libraries that made this project possible.

---

Enjoy creating beautiful panoramic images with Panoramiq!
