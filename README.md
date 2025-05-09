
# Telegram Quiz Bot

بوت تيليجرام يقوم بتحويل الأسئلة النصية إلى اختبارات تفاعلية (Quiz) باستخدام Telegram Polls.

## 🧾 تنسيق الأسئلة:
أرسل للبوت رسالة بالنمط التالي:

```
ما هي طبقة التشفير في OSI؟
A) Application
B) Session
C) Presentation
D) Network
*الصحيح 3
```

## ⚙️ طريقة التشغيل على Render

1. ارفع الملفات إلى GitHub.
2. سجل الدخول في https://render.com.
3. اختر "New Web Service".
4. اربط الخدمة بالريبو.
5. الإعدادات:

- Build Command: `pip install -r requirements.txt`
- Start Command: `python bot.py`

6. في Environment:
- أضف متغير: `BOT_TOKEN` وضع فيه توكن البوت.

7. اضغط Deploy واستمتع!

