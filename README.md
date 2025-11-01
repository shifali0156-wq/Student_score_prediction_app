<h1>Student Score Prediction App 🎓</h1>

<h2>A STREAMLIT DEPLOYED WEB APP</h2>

<div style="text-align: center; margin-top: 20px;">
  <a href="https://shifali0156-wq-student-score-prediction-app-app-5ozle7.streamlit.app/" target="_blank"
     style="background: #166d3b; color: #fff; padding: 12px 22px; border-radius: 6px; text-decoration: none; font-size: 1.25em;">
    🔗 Launch Student Score Prediction App
  </a>
</div>

<p style="text-align: center; font-size: 1.2em;">Predict student exam scores from habits and lifestyle, powered by Machine Learning with confidence intervals for every prediction.</p>

<div class="section features">
  <h2>🚀 Features</h2>
  <ul>
    <li><b>Easy-to-use interface:</b> Enter a student’s daily habits and ratings.</li>
    <li><b>Machine learning backend:</b> Robust predictions using Random Forest &amp; XGBoost.</li>
    <li><b>Confidence interval:</b> Get clear confidence ratings for predicted scores.</li>
    <li><b>Live evaluation:</b> Instant feedback on exam score and confidence.</li>
    <li><b>Modern UI:</b> Responsive, clean, and intuitive design.</li>
  </ul>
</div>

<div class="section models">
  <h2>📊 Models Used</h2>
  <ul>
    <li><b>Random Forest Regressor</b></li>
    <li><b>XGBoost Regressor</b></li>
    <li>Both models estimate uncertainty using bootstrapping techniques.</li>
  </ul>
</div>

<div class="section instructions">
  <h2>📦 Installation</h2>
  <b>Requirements:</b>
  <ul>
    <li>Python 3.7+</li>
    <li>Install dependencies listed in <code>requirements.txt</code></li>
  </ul>
  <b>Setup:</b>
  <pre>
git clone https://github.com/&lt;your-username&gt;/Student_score_prediction_app.git
cd Student_score_prediction_app
python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate
pip install -r requirements.txt
  </pre>
</div>

<div class="section usage">
  <h2>🖥️ Usage</h2>
  <pre>streamlit run app.py</pre>
  <p>Then open the displayed localhost address in your browser.</p>
</div>

<div class="section howworks">
  <h2>🎯 How it Works</h2>
  <ul>
    <li><b>Input:</b> Fill in study hours, attendance, sleep, mental health, activities, and media hours.</li>
    <li><b>Prediction:</b> Exam score predicted from trained ML models.</li>
    <li><b>Confidence:</b> The app provides "HIGH", "MODERATE" or "LOW" confidence based on the prediction interval width.</li>
  </ul>
</div>

<div class="section structure">
  <h2>⚙️ Project Structure</h2>
  <pre>
Student_score_prediction_app/
├── app.py                   <!-- Streamlit frontend -->
├── student_score_prediction.py <!-- ML backend and confidence logic -->
├── requirements.txt
├── README.md
  </pre>
</div>

<div class="section models">
  <h2>📊 Models Used</h2>
  <ul>
    <li><b>Random Forest Regressor</b></li>
    <li><b>XGBoost Regressor</b></li>
    <li>Both models estimate uncertainty using bootstrapping techniques.</li>
  </ul>
</div>

