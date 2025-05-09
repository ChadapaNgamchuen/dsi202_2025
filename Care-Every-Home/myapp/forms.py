# myapp/forms.py

from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donor_name', 'email', 'phone', 'equipment_name', 'quantity', 'description']
        # widgets = {
        #     'donor_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control'}),
        #     'equipment_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        # }
        # labels = {
        #     'donor_name': 'ชื่อผู้บริจาค',
        #     'email': 'อีเมล',
        #     'phone': 'เบอร์โทรศัพท์',
        #     'equipment_name': 'ชื่ออุปกรณ์',
        #     'quantity': 'จำนวน',
        #     'description': 'รายละเอียดเพิ่มเติม',
        # }
        # help_texts = {
        #     'donor_name': 'กรุณากรอกชื่อของคุณ',
        #     'email': 'กรุณากรอกอีเมลที่ถูกต้อง',
        #     'phone': 'กรุณากรอกเบอร์โทรศัพท์',
        #     'equipment_name': 'กรุณากรอกชื่ออุปกรณ์ที่ต้องการบริจาค',
        #     'quantity': 'กรุณากรอกจำนวนที่ต้องการบริจาค',
        #     'description': 'กรุณาใส่รายละเอียดเพิ่มเติมเกี่ยวกับอุปกรณ์',
        # }
        # error_messages = {
        #     'donor_name': {
        #         'required': 'กรุณากรอกชื่อของคุณ',
        #     },
        #     'email': {
        #         'required': 'กรุณากรอกอีเมลที่ถูกต้อง',
        #         'invalid': 'กรุณากรอกอีเมลที่ถูกต้อง',
        #     },
        #     'phone': {
        #         'required': 'กรุณากรอกเบอร์โทรศัพท์',
        #     },
        #     'equipment_name': {
        #         'required': 'กรุณากรอกชื่ออุปกรณ์ที่ต้องการบริจาค',
        #     },
        #     'quantity': {
        #         'required': 'กรุณากรอกจำนวนที่ต้องการบริจาค',
        #         'invalid': 'กรุณากรอกจำนวนที่ถูกต้อง',
        #     },
        # }
