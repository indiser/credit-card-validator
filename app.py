from flask import Flask, render_template, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import random

app = Flask(__name__)

# SECURITY: Setup Rate Limiter
# This tracks users by IP address to prevent spam
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

# --- Business Logic (Same as before) ---
def check_luhn(card_no: str) -> bool:
    if not card_no.isdigit():
        return False
    digits = [int(d) for d in card_no]
    checksum = 0
    is_second = False
    for digit in reversed(digits):
        d = digit
        if is_second:
            d = d * 2
            if d > 9: d -= 9
        checksum += d
        is_second = not is_second
    return checksum % 10 == 0

def generate_luhn_card() -> str:
    payload = [random.randint(0, 9) for _ in range(15)]
    current_sum = 0
    is_second = True 
    for digit in reversed(payload):
        d = digit
        if is_second:
            d = d * 2
            if d > 9: d -= 9
        current_sum += d
        is_second = not is_second
    check_digit = (10 - (current_sum % 10)) % 10
    payload.append(check_digit)
    return "".join(map(str, payload))

# --- Routes ---

@app.route("/")
def index():
    # Flask looks for this file inside the 'templates' folder
    return render_template("index.html")

@app.route("/api/validate", methods=["POST"])
@limiter.limit("10 per minute") # STRICT LIMIT
def validate():
    data = request.get_json()
    card_number = data.get("number", "")
    
    is_valid = check_luhn(card_number)
    
    return jsonify({
        "number": card_number,
        "valid": is_valid,
        "message": "Passes Luhn Check" if is_valid else "Fails Luhn Check"
    })

@app.route("/api/generate", methods=["GET"])
@limiter.limit("5 per minute")
def generate():
    try:
        count = int(request.args.get("count", 1))
        if count > 10: count = 10 # Hard cap at 10
    except ValueError:
        count = 1
        
    cards = [generate_luhn_card() for _ in range(count)]
    return jsonify({"cards": cards})

# --- Error Handlers (Polite messages for spammers) ---
@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify(error="ratelimit exceeded", message="You are clicking too fast. Relax."), 429

if __name__ == "__main__":
    # Debug=True is for you. Set to False before you show a client.

    app.run()
