from django import forms

class MoviesCreateForm(forms.Form):
    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded-4 glass","placeholder":"Enter Movie Title"}),label="Movie Title")

    language_choices=(
        ("Malayalam","Malayalam"),
        ("Tamil","Tamil"),
        ("Hindi","Hindi"),
        ("Kannada","Kannada"),
        ("English","English"),
        ("Korean","Korean"),
    )

    language=forms.ChoiceField(choices=language_choices,widget=forms.Select(attrs={"class":"form-control rounded-4 form-select","placeholder":"Enter Movie language"}),label="Movie Language")
    year=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control rounded-4","placeholder":"Enter Year"}),label="Released Year")
    review=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control rounded-4","placeholder":"Give Review","rows":5}),label="Movie Review")


class TheatreForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Theatre Name"}),label='Theatre Name')
    location=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Theatre Location"}),label="Theatre Location")
    screen_choices=(
        ("3D",'3D'),
        ('2D','2D'),
        ('IMAX','IMAX'),
        ('4K','4K')
    )
    screen_type=forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control form-select"}),label="Screen Type",choices=screen_choices)
    sound_choices=(
        ("Dolby","Dolby"),
        ("Dolby Atmos","Dolby Atmos"),
        ("JBL","JBL"),
    )
    sound_system=forms.ChoiceField(choices=sound_choices,widget=forms.Select(attrs={"class":"form-control form-select"}),label="Sound System")

    seating=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}),label="Seating")