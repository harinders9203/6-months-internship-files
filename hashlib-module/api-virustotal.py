import requests

API_KEY = "YOUR_API_KEY"

file_hash = "44d88612fea8a8f36de82e1278abb02f"

url = f"https://www.virustotal.com/api/v3/files/{file_hash}"

headers = {
    "x-apikey": API_KEY
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    stats = data["data"]["attributes"]["last_analysis_stats"]
    
    print("Malicious:", stats["malicious"])
    print("Suspicious:", stats["suspicious"])
    print("Undetected:", stats["undetected"])
    
else:
    print("Hash not found or API error")