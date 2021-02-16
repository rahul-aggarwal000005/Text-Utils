from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    userText = request.POST.get('text', 'Error')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    if userText == 'Error' or userText == '':
        analyzedText = ''
        usertext = 'Please Enter Some text !!! '
        utilities = ''

    else:
        analyzedText = ''
        usertext = 'Your Text is : ' + userText
        utilities = ''
        if removepunc == 'on':
            utilities = utilities + '- Remove Punctuations \n'
            punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
            for char in userText:
                if char not in punctuations:
                    analyzedText += char

            userText = analyzedText

        if capitalize == 'on':
            utilities = utilities + '- Capitalize \n'
            analyzedText = userText.capitalize()
            userText = analyzedText

        if extraspaceremover == 'on':
            analyzedText = ''
            utilities = utilities + '- Extra Space Remover \n'
            for idx, char in enumerate(userText):
                if not (userText[idx] == ' ' and userText[idx + 1] == ' '):
                    analyzedText = analyzedText + char
            userText = analyzedText

        if newlineremover == 'on':
            analyzedText = ''
            utilities = utilities + '- New Line Remover \n'
            for char in userText:
                if not(char == '\n' or char == '\r'):
                    analyzedText += char

            userText = analyzedText

        if uppercase == 'on':
            utilities = utilities + '- UpperCase \n'
            analyzedText = userText.upper()

    params = {
        'usertext': usertext,
        'analyzed': analyzedText,
        'utilities': utilities
    }
    return render(request, 'analyze.html', params)
