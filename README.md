# VadanaOnliner
<div align='center'>
  <br>
  <p>
    <a href='https://github.com/erfannjz/VadanaOnliner'><img src='https://github.com/erfannjz/VadanaOnliner/blob/main/images/vadanaonliner.png' width='256' alt='VadanaOnliner Logo' /></a>
  </p>
    <br>
  <p>
    <img src='https://img.shields.io/badge/License-MIT-blue' alt='' />  <img src='https://img.shields.io/badge/Testing-passing-green?logo=github' alt='' />
    <br>
  </p>
  <p>
  رباتی برای وصل شدن به کلاس آنلاین در سامانه وادانا
  </p>
</div>


# ⚠ توجه!
نتایج استفاده از ربات به خود شخص استفاده کننده مربوط است! لطفا مراقب عواقب آن باشید.

## 🔹طریقه نصب
کافی است بعد از دانلود پروژه و یا Clone کردن آن، در محلی که فایل `requirements.txt` قرار دارد، از دستور زیر استفاده کنید تا کتابخانه های مورد نیاز نصب شوند.  
```bash
pip install -r requirements.txt
```
پس از نصب کتابخانه های مورد نیاز حتما از آپدیت بودن مرورگر خود(کروم/فایرفاکس) اطمینان حاصل فرمایید و با توجه به نسخه مرورگر خود از لینک های زیر، جدید ترین وب درایور را دانلود و در پوشه اصلی جایگزین وب درایور های فعلی کنید.

طریقه مشاهده نسخه مرورگر(کروم/فایرفاکس):
```
Chrome: Menu/Help/About Google Chrome
Firefox: Menu/Help/About Firefox
```

لینک دانلود آخرین نسخه وب درایور(کروم/فایرفاکس):

> https://chromedriver.chromium.org/downloads<br>
> https://github.com/mozilla/geckodriver/releases

پس از انجام تمامی موارد باید فایل `config.json`  را در پوشه `config` بر اساس اطلاعات خود و کلاس مربوطه تغییر دهید.
```json
"username":"محل نام کاربری وادنا",
"password":"محل رمز وادنا",
"vadamap_url":"لینک دانشگاه خود از نقشه وادامپ",
"link_text":"لینک کلاسی که قصد آنلاین شدن با بات را دارید",
"class_time":"ساعت شروع کلاس(مثال:13:30)"
 ```
 توجه: <br>
 - زمان در `class_time` به صورت 24 ساعته میباشد. <br>
 - بهتر است 10 الی 15 دقیقه پس از شروع کلاس ساعت را تنظیم و قرار دهید تا کلاس شروع شود! 


## 🔹مشارکت در پروژه

شما میتوانید در پروژه مشارکت داشته باشید و امکانات بهتر و جدیدتری به آن اضافه کنید؛ فقط کافی است آن را Fork کنید.


## 🔹باگ
اگر باگی در پروژه مشاهده کردید یک `Issue` باز کنید و اطلاع رسانی کنید.

## 🔹لایسنس
این پروژه تحت لایسنس MIT میباشد لطفا به قوانین آن دقت کنید. با تشکر
