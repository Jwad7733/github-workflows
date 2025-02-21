
name: Run Python Script

     on:
       push:
         branches:
           - main  # تشغيل السكربت عند الدفع إلى الفرع الرئيسي

     jobs:
       generate-codes:
         runs-on: ubuntu-latest
         steps:
           - name: Checkout repository
             uses: actions/checkout@v2

           - name: Set up Python
             uses: actions/setup-python@v2
             with:
               python-version: '3.9'  # تحديد إصدار بايثون

           - name: Run Python script
             run: python generate_codes.py

           - name: Upload output file
             uses: actions/upload-artifact@v2
             with:
               name: random_codes.txt
               path: random_codes.txt
