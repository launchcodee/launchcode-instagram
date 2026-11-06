#!/usr/bin/env bash
# Gera um Reel vertical (1080x1920) a partir dos slides de um post.
# Uso: REEL=1 POSTS_MODULE=semanaN_posts OUT_DIR=/tmp/src python3 render.py   (slides sem "Arrasta")
#      ./reel.sh /tmp/src/<slug> "TEXTO DO TOPO" "Texto do rodapé" saida.mp4
# Tempo por slide: capa 3s, slides de lista 5s, demais 4s.
set -e
PREFIX="$1"; TOP="$2"; BOTTOM="$3"; OUT="$4"
FONT=$(fc-match -f '%{file}' 'Inter Display:bold')
W=$(mktemp -d); n=0; inputs=(); durs=()
for f in "$PREFIX"-*.jpg; do
  n=$((n+1))
  convert -size 1080x1920 xc:'#0A1A33' "$f" -geometry +0+285 -composite -font "$FONT" \
    -fill '#2F7BFF' -pointsize 40 -gravity north -annotate +0+150 "$TOP" \
    -fill white -pointsize 44 -gravity south -annotate +0+130 "$BOTTOM" "$W/f$n.png"
  if [ $n -eq 1 ]; then d=3.0; else d=4.5; fi
  inputs+=(-loop 1 -t $d -i "$W/f$n.png"); durs+=($d)
done
F=0.4; zp="zoompan=z='min(zoom+0.0005,1.035)':d=300:s=1080x1920:fps=30"; fc=""; off=0
for ((i=0;i<n;i++)); do fc+="[$i]$zp,trim=duration=${durs[$i]}[v$i];"; done
prev="v0"
for ((i=1;i<n;i++)); do off=$(echo "$off+${durs[$((i-1))]}-$F"|bc); fc+="[$prev][v$i]xfade=transition=slideleft:duration=$F:offset=$off[x$i];"; prev="x$i"; done
fc+="[$prev]format=yuv420p[out]"
ffmpeg -y -loglevel error "${inputs[@]}" -filter_complex "$fc" -map "[out]" -c:v libx264 -preset veryfast -crf 20 -r 30 -movflags +faststart "$OUT"
rm -rf "$W"
