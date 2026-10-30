import os
from google import genai
from google.colab import userdata

# 1. حل مشكلة الحروف العربية
os.environ["PYTHONIOENCODING"] = "utf-8"

# 2. جلب المفتاح بأمان
api_key = userdata.get('GEMINI_API_KEY').strip().split()[0]
client = genai.Client(api_key=api_key)

# 3. قاعدة المعرفة (المستند)
my_document = """
شركة "الذكاء الخارق" هي شركة عراقية تأسست عام 2024.
المؤسس والمدير التنفيذي هو المهندس محمد.
المنتج الرئيسي للشركة هو تطبيق "مساعدي" الذي يعمل بالذكاء الاصطناعي.
سياسة الشركة: العمل 4 أيام في الأسبوع، واليوم الخامس مخصص للتعلم والتطوير.
"""

print("📄 تم تحميل المستند بنجاح!")
print("🤖 أنا الروبوت القارئ. اسألني أي شيء عن الشركة (اكتب 'خروج' للإنهاء).\n")

while True:
    question = input("سؤالك: ")
    
    if question == "خروج" or question == "exit":
        print("إلى اللقاء! 👋")
        break

    # 4. تمرير المستند مع السؤال للنموذج
    prompt = f"""
    أنت مساعد ذكي. أجب على السؤال بناءً على النص التالي فقط.
    إذا لم تكن الإجابة موجودة في النص، فقل "عذراً، هذه المعلومة غير موجودة في المستند".
    
    النص:
    {my_document}
    
    السؤال: {question}
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )
        print("🤖:", response.text, "\n")
    except Exception as e:
        print(f"عذراً، حدث خطأ: {e}\n")
