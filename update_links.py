import requests

# إعدادات السيرفر
SERVER = "http://vipwettbornwet.top:8080"
# معلومات القنوات (ID القناة)
CHANNELS = ["37642", "37643", "37644"]
TOKEN_SECRET = "1260f37e4c58"

# قائمة يوزرات (هنا تضع يوزرات تجدها بالـ Dorking أو اشتراكات أخرى)
ACCOUNTS = [
    "VIP016471744476160385",
    "VIP016471744476160386",
    "NEW_USER_HERE" 
]

def check_link(user):
    url = f"{SERVER}/{user}/{TOKEN_SECRET}/{CHANNELS[0]}.ts"
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except:
        return False

def update_file():
    working_user = None
    for user in ACCOUNTS:
        if check_link(user):
            working_user = user
            break
    
    if working_user:
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            for ch in CHANNELS:
                name = "AFGHAN TV" if ch == "37644" else "AFG CHANNEL"
                f.write(f'#EXTINF:-1 tvg-name="{name}", {name}\n')
                f.write(f"{SERVER}/{working_user}/{TOKEN_SECRET}/{ch}.ts\n")
        print(f"✅ Updated with working user: {working_user}")
    else:
        print("❌ No working accounts found!")

if __name__ == "__main__":
    update_file()
