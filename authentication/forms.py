from django import forms

class loginForm(forms.Form):
    email = forms.CharField(label='email', widget=forms.TextInput(
        attrs={'id': 'login-email', 'placeholder': 'Email'}))
    password = forms.CharField(
        label='password', widget=forms.PasswordInput(
            attrs={'id': 'login-password', 'placeholder': 'Password'})
    )

class registerPenggunaForm(forms.Form):
    ROLE_CHOICES = [
        ('podcaster', 'Podcaster'),
        ('artist', 'Artist'),
        ('songwriter', 'Songwriter'),
        ('penggunabiasa', 'Tidak Ketiganya'),
    ]
    GENDER_CHOICES = [
        (1, 'Laki-laki'),
        (0, 'Perempuan'),
    ]
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'id': 'register-pengguna-email', 'placeholder': 'Email'}))
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'id': 'register-pengguna-password', 'placeholder': 'Password'}))
    nama = forms.CharField(
        label='Nama',
        widget=forms.TextInput(attrs={'id': 'register-pengguna-nama', 'placeholder': 'Nama'}))
    tempat_lahir = forms.CharField(
        label='Tempat Lahir',
        widget=forms.TextInput(attrs={'id': 'register-pengguna-tempat-lahir', 'placeholder': 'Tempat Lahir'}))
    tanggal_lahir = forms.DateField(
        label='Tanggal Lahir',
        widget=forms.DateInput(attrs={'type': 'date'}))
    kota_asal = forms.CharField(
        label='Kota Asal',
        widget=forms.TextInput(attrs={'id': 'register-pengguna-kota-asal', 'placeholder': 'Kota Asal'}))
    gender = forms.ChoiceField(
        label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect())
    role = forms.ChoiceField(
        label='Role', choices=ROLE_CHOICES, widget=forms.RadioSelect())

class registerLabelForm(forms.Form):
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={'id': 'register-label-email', 'placeholder': 'Email'}))
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'id': 'register-label-password', 'placeholder': 'Password'}))
    nama = forms.CharField(
        label='Nama',
        widget=forms.TextInput(attrs={'id': 'register-label-nama', 'placeholder': 'Nama'}))
    kontak = forms.CharField(
        label='Kontak',
        widget=forms.TextInput(attrs={'id': 'register-label-kontak', 'placeholder': 'Kontak'}))
