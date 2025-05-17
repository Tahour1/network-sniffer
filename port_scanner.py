import socket  # استيراد مكتبة الشبكات

# 1. طلب عنوان الهدف من المستخدم
target = input("أدخل عنوان الـ IP أو اسم الموقع: ")

# 2. التحقق من أن العنوان صحيح
try:
    socket.gethostbyname(target)
except socket.gaierror:
    print("العنوان غير صالح أو لا يمكن الوصول إليه.")
    exit()

# 3. قائمة بالمنافذ التي سيتم فحصها
ports = [21, 22, 23, 25, 53, 80, 110, 443]

print(f"\nمسح المنافذ المفتوحة في: {target}\n")

# 4. فحص كل منفذ من القائمة
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # إنشاء اتصال TCP
    socket.setdefaulttimeout(1)  # تحديد مهلة الانتظار بـ 1 ثانية
    result = sock.connect_ex((target, port))  # محاولة الاتصال بالمنفذ

    if result == 0:
        print(f"المنفذ {port} مفتوح")

    sock.close()  # إغلاق الاتصال بعد الفحص
