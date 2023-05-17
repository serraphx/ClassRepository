stock_info = {
  "AAPL": 168.33,
  "GOOG": 106.78,
  "APA": 37.85,
  "OXY": 62.76,
  "USO": 69.25,
  "HAL": 34.47,
  "FANG": 143.49,
  "WMT": 152.76,
  "NFLX": 329.02,
  "META": 212.79,
}

inq = input("Please enter the stock you wish to search:").upper()

req = stock_info.get(
  inq, "Information not available, please enter another symbol.")

print(f"{inq.upper()}:{req}")
