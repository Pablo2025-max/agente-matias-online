from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Agente Matias Online activo"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    mensaje = data.get("mensaje", "")

    if "deuda" in mensaje.lower():
        return jsonify({"respuesta": "Decime monto y cuotas."})

    return jsonify({"respuesta": "Soy tu agente IA online."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
