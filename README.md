# 🎨 AI Avatar Generator

Transform any face image into a cartoon-style avatar using AI. This project detects facial features (skin tone, hair, emotion, beard, etc.) and generates a personalized avatar using `py-avataaars`.

---

## 🚀 Features

* 📤 Upload an image via web interface
* 🧠 Face detection using DeepFace (stable, no MediaPipe issues)
* 🎨 Skin & hair color detection using KMeans clustering
* 😀 Emotion-based mouth & eyebrow mapping
* 🧔 Beard detection using edge density
* 🎲 Randomized features (eyes, clothes, accessories)
* 🖼️ Avatar generation (PNG)
* 📥 Download generated avatar

---

## 🏗️ Tech Stack

* Backend: Flask
* AI/ML: DeepFace
* Image Processing: OpenCV, NumPy
* Clustering: Scikit-learn (KMeans)
* Background Removal: rembg (ONNX)
* Avatar Engine: py-avataaars

---

## 📁 Project Structure

```
project/
│
├── app.py                # Flask server
├── avatar_logic.py       # Avatar generation logic
├── uploads/              # Uploaded images
├── outputs/              # Generated avatars
├── templates/
│   └── index.html        # Frontend UI
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone <your-repo-url>
cd project
```

### 2. Create virtual environment

```
python -m venv avatar_env
avatar_env\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

If rembg fails:

```
pip install "rembg[cpu]"
```

If DeepFace throws TensorFlow error:

```
pip install tf-keras
```

---

## ▶️ Running the App

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 📸 How It Works

### Pipeline

```
User Upload
   ↓
Background Removal (rembg)
   ↓
Face Detection (DeepFace)
   ↓
Feature Extraction:
   - Skin color (KMeans + distance)
   - Hair color (KMeans)
   - Beard (edge detection)
   - Emotion (DeepFace)
   - Gender → Hair style
   ↓
Avatar Generation (py-avataaars)
   ↓
Output Image
```

---

## 🧠 Key Logic

### 🎨 Skin Color Detection

* Extract forehead region
* Apply KMeans clustering
* Map closest color using Euclidean distance

### 💇 Hair Color Detection

* Extract top region of face
* Cluster dominant color
* Match with predefined palette

### 😀 Emotion Detection

* Uses DeepFace
* Maps emotion → avatar mouth & eyebrow

### 🧔 Beard Detection

* Uses Canny edge detection
* Density determines beard type

### 🎲 Random Features

* Eyes
* Clothes
* Accessories

---

## ⚠️ Important Notes

* MediaPipe removed due to instability
* DeepFace used for reliable detection
* First run may be slow (model loading)
* Flask reloader disabled for TensorFlow compatibility

---

## 🐞 Error Handling

The app handles:

* Missing file upload
* No face detected
* Image read errors
* Model failures (fallback used)

---

## 🌐 Deployment

Recommended platforms:

* Render (easy setup)
* Railway (better performance)

---

## 🚀 Future Improvements

* Faster processing
* Better feature detection accuracy
* Cloud storage (AWS S3)
* Modern frontend (React / Next.js)
* Async processing (queue system)

---

## 👨‍💻 Author

Surbhit

---

## 📜 License

This project is for educational and development purposes.
