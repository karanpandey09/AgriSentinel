from flask import Flask, send_from_directory, request, jsonify
import os

# Flask app setup
app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), "../frontend"),
    static_url_path=""
)

# Serve index.html when user visits root
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Analyze API
@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    # Dummy analysis response (replace with real logic)
    return jsonify({
        "greenness_score": 85,
        "stressed_patches": 3,
        "recommendation": "Irrigate stressed patches within 2 days.",
        "overlay_image_base64": ""  # You can add base64 overlay image here
    })

if __name__ == "__main__":
    app.run(debug=True)
