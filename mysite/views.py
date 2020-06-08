# this file is created by me - vaibhav
# import httpresponse, because it uses this to make request..
from django.http import HttpResponse
# import render to use render template functionality
from django.shortcuts import render
# index url function
def index(request):
    # return HttpResponse('<h1>This is Home Page....</h1>')
    # third argument of render is dictionary of parameters which we will access through html page
    # params = {'name':'vaibhav', 'place':'Dharmshala'}
    # return render(request, 'index.html', params)
    return render(request, 'index.html')

# about url function
def about(request):
    return render(request, 'about.html')
    
# about url function
def contact(request):
    return render(request, 'contact.html')

# analyze url function
def analyze(request):
    dj_text = request.POST.get('text', 'default')  # second parameter is default value
    removepunc = request.POST.get('rempunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newline', 'off')
    spaceremove = request.POST.get('spacerem', 'off')
    count_chars = request.POST.get('count_chars', 'off')

    # remove punctuations
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,./<>?@#$%^&*_~'''
        purpose = 'Remove Punctuations'
        analyzed_text = ""
        for char in dj_text:
            if char not in punctuations:
                analyzed_text += char
        # parameters to be sent in analyze.html page
        params = {'purpose':purpose, 'analyzed_text':analyzed_text}
        # return render(request, 'analyze.html', params)
        dj_text = analyzed_text
    
    # convert to uppercase
    if (uppercase == 'on'):
        analyzed_text = ""
        for char in dj_text:
            analyzed_text += char.upper()
            purpose = 'Conver to UpperCase'
        params = {'purpose':purpose, 'analyzed_text':analyzed_text}
        # return render(request, 'analyze.html', params)
        dj_text = analyzed_text
    
    # new line remover
    if (newlineremover == 'on'):
        analyzed_text = ""
        for char in dj_text:
            if char != '\n': #  and char != '\r' to check carriage retun
                analyzed_text += char
                purpose = 'Remove new line character'
        params = {'purpose':purpose, 'analyzed_text':analyzed_text}
        # return render(request, 'analyze.html', params)
        dj_text = analyzed_text
    
    # extra space remover
    if (spaceremove == 'on'):
        analyzed_text = ""
        for index, char in enumerate(dj_text):
            if dj_text[index] == " ":
                pass
            else:
                analyzed_text += char
                purpose = 'Remove extra spaces'
        params = {'purpose':purpose, 'analyzed_text':analyzed_text}
        # return render(request, 'analyze.html', params)
        dj_text = analyzed_text
    
    # count characters
    if (count_chars == 'on'):
        analyzed_text = ""
        word = []
        for char in dj_text:
            word.append(char)
        analyzed_text += str(len(word))
        purpose = 'Count Words'
        params = {'purpose':purpose, 'analyzed_text':analyzed_text}
        # return render(request, 'analyze.html', params)
        dj_text = analyzed_text

    # check if all button are not on 
    if(removepunc != 'on' and newlineremover != 'on' and spaceremove != 'on' and count_chars != 'on' and uppercase != 'on'):
        params = {'purpose': '', 'analyzed_text':'Error : Please select atleast one operation...'}
        return render(request, 'analyze.html', params)
        # return HttpResponse('Error : Please select atleast one operation...')

    # return all values
    return render(request, 'analyze.html', params)