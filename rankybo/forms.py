from django import forms
from rankybo.models import Question, Answer, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question #사용할 모델
        fields = ['subject', 'content'] # QuestionForm에서 사용할 Question 모델의 속성

        labels = {
            'subject': '글제목',
            'content': '글내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content':'댓글내용',
        }