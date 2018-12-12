import os
import re, subprocess
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from threading import Thread

# Create your views here.
batdir = "F:\\SDK\\Windows\\v2.1.2\\rc1\\"
runbat = batdir + "run64.bat"
outdir = batdir + "output\\"


def sdk_manage(request):
    return render(request, "winsdk_manage.html")


def upload(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        f = open(os.path.join('upload', file_obj.name), 'wb')
        print(file_obj, type(file_obj))
        for chunk in file_obj.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse('OK')


# 工具-修改批处理文件
def modifybat(file, old_str, new_str):
    with open(file, "r", encoding="utf-8") as f1, \
            open("%s.bak" % file, "w", encoding="utf-8") as f2:
        new_str.replace(" ", "", 1)
        for line in f1:
            f2.write(re.sub(old_str, new_str, line))
    os.remove(file)
    os.rename("%s.bak" % file, file)


def sdk_test(request):
    if request.method == "POST":
        interface = request.POST.get("interface", "")
        algversion = request.POST.get("algversion", "")
        sdkversion = request.POST.get("sdkversion", "")

        if interface == "detector":
            modifybat(runbat, "rem call DetectorTest.exe", "call DetectorTest.exe")
            os.system(runbat)
            modifybat(runbat, "call DetectorTest.exe", "rem call DetectorTest.exe")
            file = batdir + "output\\detector_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "extractor":
            modifybat(runbat, "rem call ExtractorTest.exe", "call ExtractorTest.exe")
            os.system(runbat)
            modifybat(runbat, "call ExtractorTest.exe", "rem call ExtractorTest.exe")
            file = batdir + "output\\extractor_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "comparer":
            modifybat(runbat, "rem call ComparerTest.exe", "call ComparerTest.exe")
            os.system(runbat)
            modifybat(runbat, "call ComparerTest.exe", "rem call ComparerTest.exe")
            file = batdir + "output\\comparer_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "searcher":
            modifybat(runbat, "rem call SearcherTest.exe", "call SearcherTest.exe")
            os.system(runbat)
            modifybat(runbat, "call SearcherTest.exe", "rem call SearcherTest.exe")
            file = batdir + "output\\searcher_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "predictor":
            modifybat(runbat, "rem call PredictorTest.exe", "call PredictorTest.exe")
            os.system(runbat)
            modifybat(runbat, "call PredictorTest.exe", "rem call PredictorTest.exe")
            file = batdir + "output\\predictor_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "capturer":
            modifybat(runbat, "rem call CapturerTest.exe", "call CapturerTest.exe")
            os.system(runbat)
            modifybat(runbat, "call CapturerTest.exe", "rem call CapturerTest.exe")
            file = batdir + "output\\capturer_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "tracker":
            modifybat(runbat, "rem call TrackerTest.exe", "call TrackerTest.exe")
            os.system(runbat)
            modifybat(runbat, "call TrackerTest.exe", "rem call TrackerTest.exe")
            file = batdir + "output\\tracker_result\\log.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
        elif interface == "select_all":
            modifybat(runbat, "rem call", "call")
            os.system(runbat)
            os.system(
                "copy " + outdir + "detector_result\\log.txt+" + outdir + "comparer_result\\log.txt+" + outdir + "extractor_result\\log.txt+" + outdir + "tracker_result\\log.txt+" + outdir + "predictor_result\\log.txt+" + outdir + "searcher_result\\log.txt+" + outdir + "capturer_result\\log.txt " + batdir + "all_result.txt 1>nul")
            modifybat(runbat, "call", "rem call")
            file = batdir + "all_result.txt"
            with open(file, "r") as f:
                return HttpResponse(f.read())
    return HttpResponse(algversion)