from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    #! Zaten Django da clean metodu tanimli sadece biz register formunda overwrite etmistik.


class RegisterForm(forms.Form):
    

    username = forms.CharField(min_length=5,max_length=50,label="Kullanıcı Adı")
    password = forms.CharField(max_length=20,min_length=4,label="Şifre",widget= forms.PasswordInput)
    confirm = forms.CharField(max_length=20,min_length=4,label="Parolayı Doğrula",widget=forms.PasswordInput)
    #* Confim ile Password kismini kiyaslamak icin django bize clean diye bir fonksiyon oneriyor
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password != confirm and (password and confirm):
            raise (forms.ValidationError("Parolalar eşleşmiyor."))
        
        values = {
            "username": username,
            "password" : password,
        }
        return values