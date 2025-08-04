# Malicious URL Detection System

A comprehensive cybersecurity tool that combines machine learning-based URL analysis with real-time web sandboxing for detecting and analyzing malicious URLs. The system features both detection capabilities and malicious URL generation for security research and testing.


## Features

- **ML-Based Detection**: Advanced machine learning model for URL classification
- **Web Sandboxing**: Real-time website screenshot capture and analysis  
- **URL Generation**: Create malicious URLs for testing and research purposes
- **Feature Extraction**: 15+ URL features including domain analysis, character patterns, and regional classification
- **Interactive CLI**: User-friendly command-line interface with menu-driven options
- **Model Evaluation**: Comprehensive model performance analysis and metrics
- **Real-time Processing**: Live URL analysis with instant results

## Project Structure

```
Malicious-URL-Detection/
├── Detection/                 # Core detection module
│   ├── Snapshots/            # Website screenshot storage
│   ├── detect.py             # Main detection engine with ML model
│   ├── evaluate.ipynb        # Model evaluation and metrics
│   ├── geckodriver.log       # Selenium WebDriver logs
│   ├── model.ipynb           # ML model training and development
│   ├── preprocess.ipynb      # Data preprocessing pipeline
│   ├── sandbox.py            # Web sandboxing and screenshot capture
│   └── temp.ipynb            # Temporary analysis and testing
├── MaliciousURLDataset/       # Training dataset and data files
├── Research/                  # Research papers and documentation
├── Resources/                 # Additional resources and documentation
├── CoreX.py                   # Main application core with GUI menu
├── README.md                  # Project documentation
├── Select.py                  # Application entry point and main loop
└── geckodriver.log           # WebDriver execution logs
```

## Getting Started

### Prerequisites

- Python 3.7+
- Firefox browser (for sandboxing)
- GeckoDriver for Selenium
- Required Python packages

### Dependencies

```bash
pip install pandas numpy scikit-learn
pip install selenium pillow matplotlib
pip install tld tldextract pick
pip install pickle-mixin hashlib
```

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/Malicious-URL-Detection.git
cd Malicious-URL-Detection
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **Download and setup GeckoDriver:**
```bash
# Download geckodriver for your OS from:
# https://github.com/mozilla/geckodriver/releases
# Add to PATH or place in project directory
```

4. **Prepare the ML model:**
```bash
# Ensure model.pkl is available in the Detection directory
# Train your own model using model.ipynb or use pre-trained model
```

## Usage

### Running the Application

```bash
python Select.py
```

### Main Menu Options

The application provides an interactive menu with the following options:

#### 1. **Generate Malicious URL**
- Creates malicious URLs for security testing
- Launches multiple terminal windows for comprehensive testing
- Integrates with external tools (CyberTraq, ngrok)

#### 2. **Detect Malicious URL**
- **ML-based Detection**: Analyzes URLs using trained machine learning model
- **Sandboxing Analysis**: Captures real-time screenshots for visual analysis
- **Feature Extraction**: Processes 15+ URL characteristics

#### 3. **Quit**
- Safely exits the application

### URL Detection Features

#### Machine Learning Detection (`detect.py`)

**Extracted Features:**
- URL length and structure analysis
- Hostname and path length
- Special character counts (-, @, ?, %, ., =)
- HTTP/HTTPS protocol analysis
- IP address detection
- URL shortening service detection
- Geographic region classification
- Root domain analysis

#### Web Sandboxing (`sandbox.py`)

**Sandboxing Capabilities:**
- Real-time website screenshot capture
- Multiple snapshot intervals
- Headless browser operation
- Visual comparison analysis
- Automated screenshot organization

### Sandboxing Technology


#### Visual Analysis Pipeline
- Multiple snapshot capture (4 screenshots with 2-second intervals)
- PIL image processing
- Matplotlib visualization
- Side-by-side comparison display

## Performance Metrics

### Model Evaluation

The system includes comprehensive model evaluation in `evaluate.ipynb`:

- **Accuracy**: Overall classification accuracy
- **Precision**: True positive rate for malicious URLs
- **Recall**: Detection rate for actual malicious URLs
- **F1-Score**: Balanced precision-recall metric
- **ROC-AUC**: Area under the receiver operating characteristic curve
- **Confusion Matrix**: Detailed classification results

### Feature Importance Analysis

Key features contributing to detection accuracy:
1. URL length and structure
2. Special character distribution
3. Domain reputation and geographic origin
4. Protocol analysis
5. Shortening service detection

## Development

### Project Architecture

#### Core Components

1. **CoreX.py**: Main application logic and menu system
2. **Select.py**: Entry point and application loop
3. **detect.py**: ML-based detection engine
4. **sandbox.py**: Web analysis and screenshot capture

#### Data Flow

```
User Input → CoreX Menu → Detection/Sandboxing → Results Display
     ↓              ↓                 ↓                ↓
URL Entry → Feature Extraction → ML Prediction → Classification
     ↓              ↓                 ↓                ↓
URL Entry → Selenium Driver → Screenshot → Visual Analysis
```
