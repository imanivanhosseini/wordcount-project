from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    # return HttpResponse('Hello')
    return render(request, 'home.html')
    #_NOTE_: We need to append 'templates' in dir list in the TEMPLATE section in setting.py file,


def count(request):
    fulltext = request.GET['fulltext']
    txtmostcommon = request.GET['txtmostcommon']
    cnt_words = count_words(fulltext)
    most_common = mostcommon(fulltext, txtmostcommon)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': cnt_words, 'most_common': most_common, 'txtmostcommon': txtmostcommon})


def about(request):
    return render(request, 'about.html')


def count_words(fulltext: str) -> int:
    wordlist = fulltext.split()
    return len(wordlist)


def mostcommon(fulltext: str, n_common: str) -> list:

    worddictionary = {}
    for word in fulltext.split():
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    popular_words = sorted(
        worddictionary, key=worddictionary.get, reverse=True)

    return popular_words[:int(n_common)]
