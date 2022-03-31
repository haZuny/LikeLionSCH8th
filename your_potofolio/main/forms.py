#모델폼을 사용하기 위한 공간

#모델폼을 사용하기 위해 임포트
from django import forms

from .models import Card


#모델폼 클래스는 forms.ModelForm 상속
class CardForm(forms.ModelForm):

    #어떤 모델의, 어느 필드를 사용할지 정의
    class Meta:
        model = Card    #모델 정의
        fields = ('title', 'describe', 'img', ) #어느 필드를 폼으로 만들지 정의

        #생성자 정의
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            #폼에 어떤 영역인지 표시를 달아줌
            self.fields['title'].label = "제목"
            self.fields['describe'].label = "설명"
            self.fields['img'].label = "대표사진"


            # self.fields['img'].widget.attrs.update({
            #     'class': 'jss_title', 
            #     'placeholder': '제목',
            # })
            # self.fields['content'].widget.attrs.update({
            #     'class': 'jss_content_form', 
            # })
