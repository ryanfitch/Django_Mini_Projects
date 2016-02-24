from django import forms

class AnswerForms(forms.ModelForm):
    # class Meta:
    #     model = Answers

    def answers(answer):
        if request.method == 'POST':
            # form1 =
            newAnswers = request.POST.get('value')
            print(newAnswers)
            return render(request, 'answers.html', {'newAnswers': newAnswers})

