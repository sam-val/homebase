import requests
from flask import Flask, request, Response

app = Flask(__name__)

express_api_base_url = "http://localhost:3000"


# Create a route to forward requests
@app.route('/api-proxy/<path:path>', methods=["GET"])
def proxy_request(path):
    try:
        api_url = f"{express_api_base_url}/{path}"
        # Forward the request to the Express API
        response = requests.request(
            method=request.method,
            url=api_url,
            params=request.args,
            headers=request.headers,
        )
        data = response.json()
        return {
            "error": None,
            "data": data,
        }
    except Exception as e:
        # let django or a tool like sentry handle errors
        # this needs to be thought further
        return {
            "error": str(e),
            "data": None
        }


if __name__ == '__main__':
    app.run(port=5001, debug=True, host="0.0.0.0")
