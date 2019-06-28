from django.shortcuts import render

def index(request):
    #Get the text
    djtext = request.POST.get('text1', 'default')

    #checking checkboxes value
    rvpunctation=request.POST.get('rvpunct',"off")
    fullcaps = request.POST.get('fulc', "off")
    extraspaceremover = request.POST.get('extraspc', "off")
    newline=request.POST.get('newline','off')
    charcount=request.POST.get('charactercount','off')

    #Operations

    analyzed=""
    purpose=""

    #when text is empty
    if(djtext == ""):
        purpose+="Please enter some text"
        params={'purpose':purpose,'analyzedtxt':'None'}
        return render(request, "text.html", params)

    #Remove punctuation
    if(rvpunctation == "on"):
        purpose += " remove punctuations"
        punct = '''"{}...!__ _- []/(),./?\<>;':^'''
        for i in djtext:
            if i not in punct:
                analyzed += i
        params = {'purpose': purpose, 'analyzedtxt': analyzed}
        djtext=analyzed

    #Capitalize the text
    if(fullcaps == "on"):
        purpose += " capitalize text"
        analyzed=djtext.upper()
        params={'purpose':purpose,'analyzedtxt':analyzed}
        djtext=analyzed

    #Extra-Space Remover
    if(extraspaceremover == "on"):
        purpose +=' extra space remover'
        analyzed=""
        for x in range(len(djtext)):
            if not (djtext[x]==" " and djtext[x+1]==" "):
                analyzed+=djtext[x]
        params={'purpose':purpose,'analyzedtxt':analyzed}
        djtext=analyzed

    #New-Line Remover
    if(newline == "on"):
        purpose +=' new line remover'
        analyzed=""
        for char in djtext:
            if char!="\n" and char!='\r':
                analyzed+=char
        params = {'purpose':purpose, 'analyzedtxt': analyzed}
        djtext=analyzed

    #Character count
    if(charcount=="on"):
        purpose += ' total character'
        analyzed=djtext+" \n Character count = "+str(len(djtext))
        params = {'purpose':purpose, 'analyzedtxt':analyzed }

    #Else case
    if(rvpunctation != 'on' and fullcaps != 'on' and extraspaceremover != 'on' and newline != 'on' and charcount != 'on'):
        params = {'purpose': 'You have not selected any filter', 'analyzedtxt': djtext}

    return render(request,"text.html",params)


def web1(request):
    return render(request,"test.html")