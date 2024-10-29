from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import soundfile as sf
from io import BytesIO

# Create your views here.
def index(request):
    return render(request, "index.html",)

def api(request):
    tstamp = float(request.GET.get("t"))
    dur = float(request.GET.get("d"))
    # print(tstamp, dur)
    info = (sf.info("/recs/test.flac"))
    sr = info.samplerate
    print(sr, tstamp, tstamp * sr)
    frame_start, frames_dur = int(tstamp), int(dur)
    # frame_start, frames_dur = int(tstamp * sr), int(dur * sr)
    data, sr = sf.read("/recs/test.flac", start=frame_start, frames=frames_dur)
    f = BytesIO()

    sf.write(f, data, sr, format=info.format)
    return HttpResponse(f.getvalue(), content_type="audio/flac")
