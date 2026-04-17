
# Fast Lane Detection using Attention Mechanism
An advanced computer vision web application designed to detect road lanes in real-time from images and videos. By utilizing deep learning architectures enhanced with an **Attention Mechanism**, this system focuses on critical spatial features to improve detection accuracy and speed, even in challenging environments.
## 🌟 Key Features
 * **Attention-Driven Detection:** Implements attention layers to prioritize lane-relevant pixels, reducing noise from surrounding elements like shadows or road textures.
 * **Dual Format Support:** Process both static images and dynamic video files for comprehensive lane analysis.
 * **Web-Based Interface:** A user-friendly dashboard built with Django, allowing users to upload files and view results directly in the browser.
 * **Real-Time Processing:** Optimized for high performance, making it suitable for applications requiring fast inference.
 * **Secure User Management:** Includes a full authentication system for users and administrators.
## 🛠️ Technology Stack
 * **Backend:** Django (Python)
 * **Frontend:** HTML5, CSS3, JavaScript (Bootstrap integration)
 * **Deep Learning:** Python (TensorFlow/Keras or PyTorch)
 * **Computer Vision:** OpenCV
 * **Database:** SQLite3
## 📂 Project Structure
```text
Fast-lane-detection/
│
├── Lane_Detection/    # Core logic for attention-based models
├── users/             # User registration and authentication
├── admins/            # Admin management dashboard
├── assets/            # Project documentation and resources
├── media/             # Storage for uploaded and processed files
├── manage.py          # Django entry point
└── db.sqlite3         # Local database

```
## 🚀 Getting Started
### Prerequisites
 * Python 3.8+
 * pip (Python package manager)
### Installation
 1. **Clone the repository:**
   ```bash
   git clone https://github.com/Iamvijay1/Fast-lane-detection-using-attention-mechanism.git
   cd Fast-lane-detection-using-attention-mechanism
   
   ```
 2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   
   ```
 3. **Install dependencies:**
   ```bash
   pip install django opencv-python numpy tensorflow  # or torch depending on your model
   
   ```
 4. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
   ```
 5. **Launch the server:**
   ```bash
   python manage.py runserver
   
   ```
 6. **View the App:** Navigate to http://127.0.0.1:8000/ in your web browser.
## 📊 Sample Output
The system identifies lane boundaries and overlays them on the original media.
*Original Image vs. Processed Output:*
## 🧠 Why Attention Mechanism?
In lane detection, standard convolutional networks can sometimes struggle with occlusions or poor lighting. The **Attention Mechanism** allows the model to "focus" on specific regions of the frame—such as lane markings—while ignoring irrelevant background information, leading to more robust performance in varied driving conditions.
## 🤝 Contributing
Contributions make the open-source community an amazing place to learn and create.
 1. Fork the Project
 2. Create your Feature Branch (git checkout -b feature/NewFeature)
 3. Commit your Changes (git commit -m 'Add some NewFeature')
 4. Push to the Branch (git push origin feature/NewFeature)
 5. Open a Pull Request
*Created by Vijay*
