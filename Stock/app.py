import quart
import quart_cors
from quart import request, render_template
import yfinance as yf

app = quart_cors.cors(quart.Quart(__name__), allow_origin="*")

@app.get("/quote")
async def display_quote():
    symbol = request.args.get('symbol', default="AAPL")
    quote = yf.Ticker(symbol)

    return quote.info

@app.get("/history")
async def display_history():
    symbol = request.args.get('symbol', default="AAPL")
    period = request.args.get('period', default="1y")
    interval = request.args.get('interval', default="1mo")        
    quote = yf.Ticker(symbol)   
    hist = quote.history(period=period, interval=interval)
    data = hist.to_json()
    
    return data



def main():
    app.run(debug=True, host="localhost", port=5002)


if __name__ == "__main__":
    main()