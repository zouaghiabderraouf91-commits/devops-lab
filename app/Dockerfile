# الصورة الأساسية
FROM python:3.12-slim

# مجلد العمل داخل Container
WORKDIR /app

# نسخ ملفات التطبيق
COPY app.py .

# تثبيت المكتبات
RUN pip install flask gunicorn

# المنفذ الذي يستمع عليه التطبيق
EXPOSE 5000

# أمر التشغيل
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "app:app"]
