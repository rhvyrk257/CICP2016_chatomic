from django import forms

SPEAKER_NUM = (
    ('0','0人'),
    ('1','1人'),
    ('2','2人'),
    ('3','3人'),
    ('4','4人以上'),
)

BUBBLE_NUM = (
    ('0','0こ'),
    ('1','1こ'),
    ('2','2こ'),
    ('3','3こ以上'),
)

USE = (
    ('0','0人'),
    ('1','1人'),
    ('2','2人以上')
)

PONE = (
    ('0','ポジティブ'),
    ('1','ネガティブ'),
    ('2','ニュートラル')
)

class UseForm(forms.Form):
    flag = forms.ChoiceField(
        label = "喋っている人",
        required=True,
        widget=forms.RadioSelect(),
        choices=USE,
    )


class PositiveForm(forms.Form):
    pn = forms.ChoiceField(
        label = "ポジネガ判定",
        required=False,
        widget=forms.RadioSelect(),
        choices=PONE,
    )

class UtterForm1(forms.Form):
    utter1 = forms.CharField(
        label = "セリフ1",
        max_length=1000,
        required=False,
        widget=forms.TextInput(attrs={'size':'100'})
)

class UtterForm2(forms.Form):
    utter2 = forms.CharField(
        label = "セリフ2",
        max_length=1000,
        required=False,
        widget=forms.TextInput(attrs={'size':'100'})
)

class SpeakerForm(forms.Form):
    bubble = forms.ChoiceField(
        label = "吹き出し数",
        required=True,
        widget=forms.RadioSelect(),
        choices=BUBBLE_NUM,
    )
