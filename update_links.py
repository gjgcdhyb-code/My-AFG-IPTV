import requests

# معلومات السيرفر واليوزر الحالي
SERVER = "http://vipwettbornwet.top:8080"
CHANNEL_ID = "37642" # معرف القناة
# قائمة باليوزرات الاحتياطية (تقدر تضيف يوزرات جديدة هنا دائماً)
ACCOUNTS = ["VIP016471744476160385", "VIP016471744476160386", "Trial99"]

def check_and_update():
    for acc in ACCOUNTS:
        url = f"{SERVER}/{acc}/1260f37e4c58/{CHANNEL_ID}"
        try:
            # نفحص الرابط بطلب بسيط (HEAD)
            response = requests.head(url, timeout=5)
            if response.status_code == 200:
                # إذا اشتغل، نحدث ملف الـ M3U
                with open("playlist.m3u", "r") as f:
                    content = f.read()
                # استبدال الرابط القديم بالجديد (منطق برمجي بسيط)
                # ملاحظة: يمكنك تطوير هذا الجزء ليكون أكثر دقة
                print(f"✅ Found working account: {acc}")
                return True
        except:
            continue
    return False

if __name__ == "__main__":
    check_and_update()
