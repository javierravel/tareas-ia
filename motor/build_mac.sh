#!/bin/bash
# usage: build_mac.sh <dir con p1..p5.wav, texts.json, meta.json> [frames]
set -e
M="$(cd "$(dirname "$0")" && pwd)"; export PATH="$M/bin:$PATH"; export REEL_DIR="$M"
PY=~/fw/bin/python3.11
D="$(cd "$1" && pwd)"; mkdir -p "$D/a"; : > "$D/a/list.txt"
for i in 1 2 3 4 5; do
  ffmpeg -y -loglevel error -i "$D/p$i.wav" -af "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse,apad=pad_dur=0.25" -ar 44100 -ac 1 -c:a pcm_s16le "$D/a/p$i.wav"
  echo "file 'p$i.wav'" >> "$D/a/list.txt"
done
$PY -c "import wave,json,sys; d=sys.argv[1]; print(json.dumps([round(wave.open(f'{d}/a/p{i}.wav').getnframes()/44100,2) for i in range(1,6)]))" "$D" > "$D/durs.json"
cat "$D/durs.json"
if [ "$2" = frames ]; then rm -rf "$D/scenes"; $PY "$M/render_jefe.py" "$D" frames; exit 0; fi
ffmpeg -y -loglevel error -f concat -safe 0 -i "$D/a/list.txt" -af loudnorm=I=-14:TP=-1.5:LRA=11 -ar 44100 "$D/voz.wav"
rm -rf "$D/scenes"; $PY "$M/render_jefe.py" "$D" > /dev/null
cd "$D/scenes" && ls s?.mp4 | sed "s/^/file '/;s/$/'/" > l.txt && ffmpeg -y -loglevel error -f concat -i l.txt -c copy ../video.mp4
cd "$D" && ffmpeg -y -loglevel error -i video.mp4 -i voz.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 160k -shortest "$(basename "$D").mp4"
echo built "$D/$(basename "$D").mp4"
