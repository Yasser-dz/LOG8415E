from flask import Flask, request
import requests

app = Flask(__name__)
ip_proxy = "172.31.17.7"


@app.route('/endpoint', methods=['GET', 'POST'])
def handle_request():
    # Extract the query from the incoming request
    query = request.form.get('query')
    strategy = request.form.get('strategy')

    allowed_strategies = ["direct", "random", "customized"]
    if strategy not in allowed_strategies:
        return False, "Invalid strategy"
    # Validate the request
    if request.method == 'POST':
        # Forward the request to the Proxy
        response = requests.post(f"http://{ip_proxy}/endpoint", params={"strategy": strategy}, data=query)
    else:
        # Forward the request to the Proxy
        response = requests.get(f"http://{ip_proxy}/endpoint", params={"strategy": strategy}, data=query)

    return response.content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)