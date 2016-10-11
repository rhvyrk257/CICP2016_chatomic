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
    ('3','3こ'),
    ('4','4こ以上'),
)

class UtterForm(forms.Form):
    utter = forms.CharField(
        label = "セリフ",
        max_length=400,
        required=False,
        widget=forms.TextInput()
)

class SpeakerForm(forms.Form):
    bubble = forms.ChoiceField(
        label = "吹き出し数",
        required=False,
        widget=forms.RadioSelect(),
        choices=BUBBLE_NUM,
    )
