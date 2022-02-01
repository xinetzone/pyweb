from sanic import Sanic
from sanic.response import text

app = Sanic("proxied_example")
app.config.FORWARDED_SECRET = "YOUR SECRET"

@app.get("/")
def index(request):
    # 此处将会显示公网IP
    return text(
        f"{request.remote_addr} connected to {request.url_for('index')}\n"
        f"Forwarded: {request.forwarded}\n"
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, workers=8, access_log=False)