from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from LandPage.models import DefaultUser, StandartEncryptField
from .models import ExtUser
from Account import forms
from Gku import settings
import base64

def changeExtUserInfo(request):
    if 'id' not in request.session:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        errors = list()
        extUserForm = forms.ChangeExtUserInfo(request.POST, request.FILES)
        if extUserForm.is_valid():
            extUser = extUserForm.save(commit=False)
            extUser.user_id = request.session['id']

            if not extUser.chkPhoneNumber():
                errors.append('Неправильный номер телефона!')
            if extUser.total_square < 1:
                errors.append('Некорректное значение площади')
            if extUser.cnt_fiodr < 1:
                errors.append('Некорректное количество проживающих')

            if len(errors) == 0:
                if ExtUser.objects.filter(user_id=extUser.user_id).exists():
                    tmpExtUser = ExtUser.objects.get(user_id=extUser.user_id)
                    if extUser.phone == "":
                        extUser.phone = tmpExtUser.phone
                    if extUser.adress == "":
                        extUser.adress = tmpExtUser.phone
                    if not extUser.ava:
                        extUser.ava = tmpExtUser.ava
                    if extUser.cnt_fiodr == 0:
                        extUser.cnt_fiodr = tmpExtUser.cnt_fiodr
                    if extUser.total_square == 0:
                        extUser.total_square = tmpExtUser.total_square
                    tmpExtUser.delete()

                extUser.save()

                return render(request, 'OK/index.html', {'title': 'Отлично!', 'msg': 'Ваши данные успешно изменены.', 'link': 'account'})

        defaultUserInfoForm = forms.ChangeUserInfo()
        changePassForm = forms.ChangePassword()
        changeMailForm = forms.ChangeMail()
        return render(request, 'AccountSettings/index.html',
                     {'defUserInfo': defaultUserInfoForm, 'extUserInfo': extUserForm,
                     'changePass': changePassForm, 'changeMail': changeMailForm, 'extUserInfoErrors': errors,})
    return HttpResponseRedirect('/account')

def changeStandartUserInfo(request):
    if 'id' not in request.session:
        return HttpResponseRedirect('/account')
    if request.method == "POST":
        errors = list()
        defaultUserInfoForm = forms.ChangeUserInfo(request.POST)
        if defaultUserInfoForm.is_valid():
            userInfo = defaultUserInfoForm.save(commit=False)
            userInfo.user_id = request.session['id']

            user = DefaultUser.objects.get(id=userInfo.user_id)
            if userInfo.name != "":
                user.name = StandartEncryptField(userInfo.name, settings.AES_DEFAULT_KEY)
            if userInfo.surname != "":
                user.surname = StandartEncryptField(userInfo.surname, settings.AES_DEFAULT_KEY)
            if userInfo.patronymic != "":
                user.patronymic = StandartEncryptField(userInfo.patronymic, settings.AES_DEFAULT_KEY)

            user.save()
            return render(request, 'OK/index.html', {'title': 'Отлично!', 'msg': 'Ваши данные успешно изменены.', 'link': 'account'})
        else:
            changePassForm = forms.ChangePassword()
            changeMailForm = forms.ChangeMail()
            extUserForm = forms.ExtUser()
            return render(request, 'AccountSettings/index.html',
                          {'defUserInfo': defaultUserInfoForm, 'extUserInfo': extUserForm,
                           'changePass': changePassForm, 'changeMail': changeMailForm, 'extUserInfoErrors': errors, })
    return HttpResponseRedirect('/account')

def test(request):
    v = 'asd'
    b = base64.b64encode(v)
    print(v)
    return HttpResponse(StandartEncryptField('dfs', settings.AES_DEFAULT_KEY))