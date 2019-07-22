import datetime
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Resumedata

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="メールアドレス", required=True, error_messages={'required': '必須'})
    first_name = forms.CharField(label="名前", required=True, error_messages={'required': '必須'})
    last_name = forms.CharField(label="苗字", required=True, error_messages={'required': '必須'})
    password1 = forms.CharField(widget=forms.PasswordInput, label="パスワード", required=True, error_messages={'required': '必須'})
    password2 = forms.CharField(widget=forms.PasswordInput, label="パスワード(確認)", required=True, error_messages={'required': '必須'})
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
#        user.phone = self.cleaned_data['phone']
        user.email = self.cleaned_data['email']
#        user.set_password(self.cleaned_data["password1"])

#        user = super(RegistrationForm, self).save(commit=False)
#        user.first_name = self.cleaned_data['first_name']
#        user.last_name = self.cleaned_data['last_name']
#        user.phone = self.cleaned_data['phone']
#        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user



class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="メールアドレス", required=True, error_messages={'required': '必須'})
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput, required=True, error_messages={'required': '必須'})
    class Meta:
        model = User




class InputForm1(forms.ModelForm):
    phone = forms.CharField(label="電話番号", required=True, error_messages={'required': '必須'})
    twitter = forms.CharField(label="Twitterアカウント", required=False)
    instagram = forms.CharField(label="Instagramアカウント", max_length=20, required=False)
    facebook = forms.CharField(label="Facebookアカウント", max_length=20, required=False)

    class Meta:
        model = Resumedata
        fields = ('phone', 'twitter', 'instagram', 'facebook',)



Months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
Years = [y for y in range(1968, datetime.date.today().year+1)]

Date_Options = []
Date_Options.append((('Null', '選択してください')))
for year in Years:
    for month in Months:
        Date_Options.append((str(month)+' '+str(year), str(month) + '-' + str(year)))
Date_Options.append((('Present', '現在')))


class InputForm2(forms.ModelForm):
    school1 = forms.CharField(label="学校名", max_length=40)
    major1 = forms.CharField(label="専攻", max_length=40)
    s_start1 = forms.CharField(label="入学月", widget=forms.Select(choices=Date_Options))
    s_end1 = forms.CharField(label="卒業月", widget=forms.Select(choices=Date_Options))
    school2 = forms.CharField(label="学校名", max_length=40)
    major2 = forms.CharField(label="専攻", max_length=40)
    s_start2 = forms.CharField(label="入学月", widget=forms.Select(choices=Date_Options))
    s_end2 = forms.CharField(label="卒業月", widget=forms.Select(choices=Date_Options))
    school3 = forms.CharField(label="学校名", max_length=40)
    major3 = forms.CharField(label="専攻", max_length=40)
    s_start3 = forms.CharField(label="入学月", widget=forms.Select(choices=Date_Options))
    s_end3 = forms.CharField(label="卒業月", widget=forms.Select(choices=Date_Options))

    class Meta:
        model = Resumedata
        fields = ('school1', 'major1', 's_start1', 's_end1',
                  'school2', 'major2', 's_start2', 's_end2',
                  'school3', 'major3', 's_start3', 's_end3',)

Aboutme1_Options= [
    ('waiter', 'ウェイター'),
    ('cook', 'シェフ'),
    ]

Aboutme2_Options= [
    ('English communication', '英会話'),
    ('team working', 'チームワーク'),
    ]
class InputForm3(forms.ModelForm):
    aboutme1 = forms.CharField(label='希望職種', widget=forms.Select(choices=Aboutme1_Options))
    aboutme2 = forms.CharField(label='付けたいスキル', widget=forms.Select(choices=Aboutme2_Options))

    class Meta:
        model = Resumedata
        fields = ('aboutme1', 'aboutme2')

SkillType_Options= [
    ('s1a', 'バリスタ'),
    ('s1b', '接客'),
    ('s1c', 'レジ打ち'),
    ]

SkillLevel_Options= [
    ('l1a', '初心者'),
    ('l1b', '経験者'),
    ('l1c', 'エキスパート'),
]

class InputForm4(forms.ModelForm):
    exp1 = forms.CharField(label='会社名１',max_length=40)
    position1 = forms.CharField(label='ポジション',max_length=40)
    e_start1 = forms.CharField(label='開始月', widget=forms.Select(choices=Date_Options))
    e_end1 = forms.CharField(label='終了月', widget=forms.Select(choices=Date_Options))
    exp2 = forms.CharField(label='会社名２',max_length=40)
    position2 = forms.CharField(label='ポジション',max_length=40)
    e_start2 = forms.CharField(label='開始月', widget=forms.Select(choices=Date_Options))
    e_end2 = forms.CharField(label='終了月', widget=forms.Select(choices=Date_Options))
    exp3 = forms.CharField(label='会社名３', max_length=40)
    position3 = forms.CharField(label='ポジション', max_length=40)
    e_start3 = forms.CharField(label='開始月', widget=forms.Select(choices=Date_Options))
    e_end3 = forms.CharField(label='終了月', widget=forms.Select(choices=Date_Options))
    skill_type1 = forms.CharField(label='スキル１', widget=forms.Select(choices=SkillType_Options))
    skill_level1 = forms.CharField(label='レベル', widget=forms.Select(choices=SkillLevel_Options))
    skill_type2 = forms.CharField(label='スキル２', widget=forms.Select(choices=SkillType_Options))
    skill_level2 = forms.CharField(label='レベル', widget=forms.Select(choices=SkillLevel_Options))
    skill_type3 = forms.CharField(label='スキル３', widget=forms.Select(choices=SkillType_Options))
    skill_level3 = forms.CharField(label='レベル', widget=forms.Select(choices=SkillLevel_Options))

    class Meta:
        model = Resumedata
        fields = ('exp1', 'position1', 'e_start1', 'e_end1',
                  'exp2', 'position2', 'e_start2', 'e_end2',
                  'exp3', 'position3', 'e_start3', 'e_end3',
                  'skill_type1', 'skill_level1','skill_type2', 'skill_level2','skill_type3', 'skill_level3')