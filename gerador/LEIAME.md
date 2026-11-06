# Gerador de artes do @launchcod

- `render.py` gera slides 1080x1350 (JPG) a partir de um módulo de posts.
  Uso: `cd gerador && POSTS_MODULE=semanaN_posts OUT_DIR=../semanaN python3 render.py`
- Requer Chrome headless, ImageMagick (`convert`) e fontes Inter Display + DejaVu Sans Mono.
- Tipos de slide: cover, point, list, compare, big, cta, poll, chat (ver `semana1_posts.py`).
- Identidade: fundo navy #0A1A33, azul #2F7BFF, claro #F3F6FB. Wordmark "Launch" + "code" em azul.
- Sem emojis nas artes (fonte não suporta); emojis só na legenda.
