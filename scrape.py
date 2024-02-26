import requests
import json

# Define headers with Content-Type
# headers = {
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en-US,en;q=0.8',
#     'Content-Type': 'application/json',
#     'Origin': 'https://www.zerogpt.com',
#     'Referer': 'https://www.zerogpt.com/',
#     'Sec-Ch-Ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
#     'Sec-Ch-Ua-Mobile': '?0',
#     'Sec-Ch-Ua-Platform': '"Linux"',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-site',
#     'Sec-Gpc': '1',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
# }


headers = {
    'authority': 'www.semrush.com',
    'method': 'POST',
    'path': '/goodcontent/api/summary-generator/generate-summary/',
    'scheme': 'https',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'Baggage': 'sentry-environment=production,sentry-release=qoXktU2SJB3W2\_6fG8MHH,sentry-public\_key=368d98c4dbab4e3facf002659376bb8f,sentry-trace\_id=378055fdf46d4805847f97b1b1030b7b,sentry-sample\_rate=1,sentry-transaction=POST%20%2Fgoodcontent%2Fapi%2Fsummary-generator%2Fgenerate-summary%2F,sentry-sampled=true',
    'Content-Length': '3391',
    'Content-Type': 'application/json',
    'Cookie': 'PHPSESSID=9cf708443cecec95e8538a5d9af89cd8; SSO-JWT=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI5Y2Y3MDg0NDNjZWNlYzk1ZTg1MzhhNWQ5YWY4OWNkOCIsImlhdCI6MTcwODkzOTk3NiwiaXNzIjoic3NvIn0.dpwn67cxWi5znZJ9FRhkV5nKACQrI7WhXUipqm-BO1ZSjjyXJ9Xwcixg4LU2am4yiy3t4nAzaxa8dTS-ku4DHw; GCLB=COetj7OKsPDDIA',
    'Origin': 'https://www.semrush.com',
    'Referer': 'https://www.semrush.com/goodcontent/summary-generator/',
    'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Gpc': '1',
    'Sentry-Trace': '378055fdf46d4805847f97b1b1030b7b-9ee83a52a84a4380-1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

def summarize(input_text, summary_length=20, bullet_points=False, language="en"):
    url = "https://www.semrush.com/goodcontent/api/summary-generator/generate-summary/"
    # Define the payload as a dictionary
    payload = {
        'text': input_text,
        'length_penalty': -3,
        'format': ('bullets' if bullet_points else 'paragraph')
    }

    # Convert payload to JSON format
    json_payload = json.dumps(payload)

    # Send the POST request with JSON payload and headers
    response = requests.post(url, data=json_payload, headers=headers)

    # Check the response status
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("POST request failed with status code:", response.status_code)
        print(response.text)
        return {'summary': ""}