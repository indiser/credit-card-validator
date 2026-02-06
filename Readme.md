# Credit Card Validator & Generator

A robust Flask-based web application for validating and generating valid credit card numbers using the Luhn algorithm. This tool is designed for testing and educational purposes.

## Overview

This application provides a user-friendly interface to validate credit card numbers against the Luhn checksum algorithm and generate valid test credit card numbers. The backend implements rate limiting to prevent abuse and maintain security.

## Features

- ✅ **Credit Card Validation** – Validate credit card numbers using the Luhn algorithm
- ✅ **Card Generation** – Generate valid test credit card numbers on demand
- ✅ **Rate Limiting** – Built-in security with request rate limiting per IP address
- ✅ **Modern UI** – Responsive dark-themed interface using DaisyUI and Tailwind CSS
- ✅ **REST API** – Clean JSON-based API endpoints for programmatic access
- ✅ **Input Validation** – Robust error handling and validation

## Technology Stack

- **Backend:** Python, Flask, Flask-Limiter
- **Frontend:** HTML5, Tailwind CSS, DaisyUI
- **Algorithm:** Luhn Checksum Algorithm

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/indiser/credit-card-validator
   cd "credit-card-validator"
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or: source venv/bin/activate  # On macOS/Linux
   ```

3. Install required dependencies:
   ```bash
   pip install flask flask-limiter
   ```

## Usage

### Running the Application

Start the Flask development server:

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Web Interface

1. **Validate a Card:** Enter a 16-digit card number and click "Check" to validate
2. **Generate a Card:** Click "Generate Valid Number" to create a random valid test card number

### API Endpoints

#### Validate Card
```
POST /api/validate
Content-Type: application/json

{
  "number": "5632016887467943"
}

Response:
{
  "number": "5632016887467943",
  "valid": true,
  "message": "Passes Luhn Check"
}
```

**Rate Limit:** 10 requests per minute per IP address

#### Generate Card
```
GET /api/generate?count=1

Response:
{
  "cards": ["4532123456789012"]
}
```

**Parameters:**
- `count`: Number of cards to generate (1-10, default: 1)

**Rate Limit:** 5 requests per minute per IP address

## Security Features

- **Rate Limiting:** Prevents abuse with configurable limits
  - Default: 200 requests per day, 50 per hour per IP
  - Strict endpoint limits: 10 req/min for validation, 5 req/min for generation
- **Input Validation:** Strict validation of all inputs
- **Error Handling:** Graceful handling of invalid requests with helpful messages

## Project Structure

```
Credit Card Generator/
├── app.py              # Main Flask application with API routes
├── luhn.py             # Luhn algorithm implementation (alternative version)
├── luhn2.py            # Luhn algorithm implementation (alternative version)
├── templates/
│   └── index.html      # Web interface
└── Readme.md           # This file
```

## Luhn Algorithm

The Luhn algorithm is a checksum formula used to validate credit card numbers and detect simple errors in typing or transmission. It works by:

1. Starting from the rightmost digit, double every second digit
2. If the result is greater than 9, subtract 9
3. Sum all the digits
4. If the sum is divisible by 10, the number is valid

## Important Notes

⚠️ **Educational Purpose Only:** This tool is intended for educational purposes and testing environments only. Do not use generated card numbers for any unauthorized transactions.

⚠️ **Test Data:** All generated card numbers are test numbers that pass the Luhn checksum but are not associated with any real financial institutions.

⚠️ **Production Deployment:** Before deploying to production:
- Set `debug=False` in `app.py`
- Configure proper rate limiting storage (Redis recommended instead of memory)
- Implement HTTPS/SSL
- Add authentication if needed
- Review and adjust rate limiting thresholds

## Error Handling

The application returns HTTP 429 (Too Many Requests) when rate limits are exceeded:

```json
{
  "error": "ratelimit exceeded",
  "message": "You are clicking too fast. Relax."
}
```

## Future Enhancements

- Support for multiple card formats (Visa, Mastercard, Amex detection)
- Batch validation/generation
- Persistent rate limiting with Redis
- API key authentication
- Request logging and analytics

## License

This project is provided as-is for educational purposes.

## Contact & Support

For issues, questions, or contributions, please refer to the repository maintainer.

---

**Last Updated:** February 2026

