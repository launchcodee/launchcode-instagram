# Conteúdo da semana 3 (21–27/nov/2026) — @launchcod
# Base: semana 2 teve alcance baixo nos posts de feed (10–14 por post, 0 comentários).
# Melhores do período: post-teste interativo (06/11: alcance 261, 4 comentários, 3 compartilhamentos)
# e o Reel de cardápio digital (08/11: alcance 533, 6 compartilhamentos, 5 comentários).
# Ajustes: volta do formato "teste" com CTA de compartilhar, gancho de Black Friday (27/11),
# demonstração de totem e cardápio, todos os posts às 10h (melhor horário no Metricool).

POSTS = [
    {
        "slug": "01-teste-vende-sem-voce",
        "date": "2026-11-21T10:00:00",
        "slides": [
            {"t": "cover", "kicker": "Teste rápido", "title": "Seu negócio vende <b>sem você</b> no balcão?", "sub": "5 perguntas. Responde sim ou não e conta quantos NÃO."},
            {"t": "list", "kicker": "Responda com sinceridade", "title": "Perguntas 1 a 3",
             "items": ["1. O cliente consegue fazer o pedido sem esperar alguém responder?", "2. Se você tirar um dia de folga, os pedidos continuam chegando certo?", "3. Alguém da equipe sabe atualizar um preço sem te ligar?"]},
            {"t": "list", "kicker": "Responda com sinceridade", "title": "Perguntas 4 e 5",
             "items": ["4. Dá para saber quanto vendeu hoje sem abrir o caderno?", "5. O cliente que pediu uma vez tem um jeito fácil de pedir de novo?"]},
            {"t": "point", "n": "3+", "title": "Respondeu NÃO em 3 ou mais?", "body": "O negócio depende demais de você. Dá para mudar isso com tecnologia simples, feita para a sua rotina."},
            {"t": "cta", "title": "Quer saber por onde <b>começar</b>?", "body": "A gente olha sua rotina de pedidos e te mostra o primeiro passo, sem compromisso.", "action": "Comenta TESTE"},
        ],
        "caption": """Seu negócio vende sem você no balcão? 🤔

Faz o teste (sim ou não):

1️⃣ O cliente consegue fazer o pedido sem esperar alguém responder?
2️⃣ Se você tirar um dia de folga, os pedidos continuam chegando certo?
3️⃣ Alguém da equipe sabe atualizar um preço sem te ligar?
4️⃣ Dá pra saber quanto vendeu hoje sem abrir o caderno?
5️⃣ O cliente que pediu uma vez tem um jeito fácil de pedir de novo?

Respondeu NÃO em 3 ou mais? O negócio depende demais de você. E dá pra mudar isso com tecnologia simples, feita pra sua rotina.

💬 Comenta TESTE que a gente olha sua rotina de pedidos e te mostra o primeiro passo.

📲 Manda pra um amigo que vive dizendo que não consegue tirar folga.

#comerciolocal #restaurante #delivery #empreendedorismo #gestao #ubirata #parana #launchcode""",
    },
    {
        "slug": "02-enquete-tirar-da-rotina",
        "date": "2026-11-22T10:00:00",
        "slides": [
            {"t": "poll", "title": "Qual tarefa você tiraria <b>da sua rotina</b> amanhã?",
             "options": [("A", "Anotar pedido no WhatsApp"), ("B", "Responder preço e cardápio"), ("C", "Fechar o caixa à noite"), ("D", "Confirmar horário marcado")],
             "action": "Responde com a letra nos comentários"},
        ],
        "caption": """Se desse pra tirar UMA tarefa da sua rotina amanhã, qual seria? 👇

🅰️ Anotar pedido no WhatsApp
🅱️ Responder preço e cardápio
🅲 Fechar o caixa à noite
🅳 Confirmar horário marcado

Responde só com a letra aqui nos comentários. A mais votada vira um post com o passo a passo de como automatizar. 💡

#empreendedorismo #comerciolocal #restaurante #barbearia #gestao #ubirata #parana #launchcode""",
    },
    {
        "slug": "03-totem-como-funciona",
        "date": "2026-11-23T10:00:00",
        "slides": [
            {"t": "cover", "kicker": "Totem de autoatendimento", "title": "Como funciona um <b>totem</b> no seu balcão", "sub": "Do toque na tela ao pedido na cozinha. Arrasta."},
            {"t": "point", "n": "01", "title": "O cliente escolhe pelas fotos", "body": "Sem fila para falar com o atendente. Ele navega no cardápio no próprio ritmo."},
            {"t": "point", "n": "02", "title": "A tela sugere um adicional", "body": "Batata, bebida, sobremesa. A sugestão aparece na hora certa, sem ninguém precisar lembrar."},
            {"t": "point", "n": "03", "title": "Paga ali mesmo", "body": "Pedido confirmado e pago, sem anotação e sem item trocado no caminho."},
            {"t": "point", "n": "04", "title": "A cozinha recebe e a equipe produz", "body": "O atendente sai do caixa e vai ajudar onde realmente faz diferença."},
            {"t": "cta", "title": "Quer ver o totem <b>funcionando</b>?", "body": "A gente te mostra com um cardápio de exemplo, do jeito que ficaria no seu balcão.", "action": "Comenta TOTEM"},
        ],
        "caption": """Já imaginou seu cliente fazendo o pedido sozinho, sem fila no balcão? 👇

Como funciona o totem de autoatendimento:

1️⃣ O cliente escolhe pelas fotos, no próprio ritmo
2️⃣ A tela sugere um adicional na hora certa (batata, bebida, sobremesa)
3️⃣ Paga ali mesmo, sem anotação e sem item trocado
4️⃣ A cozinha recebe o pedido e a equipe foca na produção

Serve pra lanchonete, hamburgueria, açaí, sorveteria, padaria… qualquer negócio com balcão e fila.

💬 Comenta TOTEM que a gente te mostra funcionando com um cardápio de exemplo.

#totem #autoatendimento #lanchonete #hamburgueria #foodservice #ubirata #parana #launchcode""",
    },
    {
        "slug": "04-black-friday-food-service",
        "date": "2026-11-24T10:00:00",
        "slides": [
            {"t": "cover", "kicker": "Black Friday", "title": "Black Friday não é só para loja. <b>Restaurante também vende.</b>", "sub": "4 ideias para aproveitar a sexta-feira sem queimar sua margem."},
            {"t": "point", "n": "01", "title": "Combo em vez de desconto", "body": "Junte itens que saem juntos. O cliente sente vantagem e o seu ticket sobe."},
            {"t": "point", "n": "02", "title": "Vantagem só no pedido direto", "body": "Brinde ou frete especial para quem pede pelo seu link, não pelo app de delivery."},
            {"t": "point", "n": "03", "title": "Promoção com hora para acabar", "body": "Válida só na sexta, ou só até as 20h. Prazo curto faz o cliente decidir."},
            {"t": "point", "n": "04", "title": "Cardápio atualizado antes", "body": "Nada pior que promoção divulgada e preço antigo no cardápio. Deixe tudo pronto na quinta."},
            {"t": "cta", "title": "Quer o cardápio pronto <b>para sexta</b>?", "body": "A gente te mostra como montar combos e promoções no cardápio digital.", "action": "Comenta BLACK"},
        ],
        "caption": """Quem disse que Black Friday é só pra loja de roupa? 🍔

4 ideias pra restaurante, lanchonete e delivery vender mais na sexta (27/11) sem queimar a margem:

1️⃣ Combo em vez de desconto: junte itens que já saem juntos
2️⃣ Vantagem só no pedido direto: brinde ou frete especial pra quem pede pelo seu link
3️⃣ Promoção com hora pra acabar: só na sexta, ou só até as 20h
4️⃣ Cardápio atualizado antes: nada de promoção divulgada com preço antigo

Salva esse post pra não esquecer na quinta à noite. 📌

💬 Comenta BLACK que a gente te mostra como montar combos e promoções no cardápio digital.

#blackfriday #restaurante #delivery #lanchonete #cardapiodigital #foodservice #ubirata #parana #launchcode""",
    },
    {
        "slug": "05-pedido-errado",
        "date": "2026-11-25T10:00:00",
        "slides": [
            {"t": "cover", "kicker": "Delivery", "title": "Pedido errado não custa um lanche. <b>Custa um cliente.</b>", "sub": "Arrasta e faz a conta."},
            {"t": "big", "kicker": "Exemplo", "pre": "Se sai 1 pedido errado por dia, no fim do mês são", "num": "30", "post": "lanches refeitos e clientes irritados", "note": "Exemplo ilustrativo. A conta muda de negócio para negócio."},
            {"t": "list", "kicker": "De onde vem o erro", "title": "Quase sempre do <b>mesmo lugar</b>.",
             "items": ["Pedido copiado da conversa à mão", "Adicional que ficou só no áudio", "Recado gritado do balcão para a cozinha"]},
            {"t": "list", "kicker": "Como resolver", "title": "O pedido já chega <b>escrito certo</b>.",
             "items": ["O cliente monta o pedido sozinho", "Adicionais e observações no lugar certo", "A cozinha lê, ninguém precisa ditar"]},
            {"t": "cta", "title": "Quer acabar com o <b>pedido trocado</b>?", "body": "Cardápio digital com pedido organizado direto no seu WhatsApp.", "action": "Comenta DELIVERY"},
        ],
        "caption": """Quanto te custa um pedido errado? 🤯

Não é só o lanche refeito. É o motoboy voltando, a cozinha parada e o cliente que talvez não peça de novo.

Exemplo ilustrativo: 1 pedido errado por dia = 30 no fim do mês.

E o erro quase sempre vem do mesmo lugar:
❌ Pedido copiado da conversa à mão
❌ Adicional que ficou só no áudio
❌ Recado gritado do balcão pra cozinha

Com cardápio digital, o pedido já chega escrito certo:
✅ O cliente monta sozinho
✅ Adicionais e observações no lugar certo
✅ A cozinha lê, ninguém precisa ditar

💬 Comenta DELIVERY que a gente te mostra funcionando.

#delivery #restaurante #lanchonete #cardapiodigital #pedidosonline #ubirata #parana #launchcode""",
    },
    {
        "slug": "06-pronto-ou-sob-medida",
        "date": "2026-11-26T10:00:00",
        "slides": [
            {"t": "cover", "kicker": "Opinião", "title": "Sistema pronto ou <b>sob medida</b>?", "sub": "Nem sempre a resposta é a mais cara. Arrasta."},
            {"t": "list", "kicker": "Sistema pronto resolve quando", "title": "Sua rotina é <b>parecida com a de todo mundo</b>.",
             "items": ["Precisa começar rápido", "O processo é simples e padrão", "Você se adapta ao sistema sem sofrer"]},
            {"t": "list", "kicker": "Sob medida faz sentido quando", "title": "O sistema é que precisa <b>se adaptar a você</b>.",
             "items": ["Você usa três sistemas que não conversam", "A equipe vive fazendo gambiarra em planilha", "Seu jeito de vender é o seu diferencial"]},
            {"t": "point", "n": "!", "title": "A pergunta certa não é o preço", "body": "É quanto tempo a sua equipe perde todo dia tentando encaixar o negócio num sistema que não foi feito para ele."},
            {"t": "cta", "title": "Na dúvida, <b>a gente te ajuda a decidir</b>.", "body": "Conversa sem compromisso. Às vezes a resposta é: você nem precisa da gente.", "action": "Chama no direct: PROJETO"},
        ],
        "caption": """Sistema pronto ou sob medida? Nem sempre a resposta é a mais cara. 💭

Sistema pronto resolve quando:
✅ Você precisa começar rápido
✅ O processo é simples e padrão
✅ Dá pra se adaptar ao sistema sem sofrer

Sob medida faz sentido quando:
🔧 Você usa três sistemas que não conversam
🔧 A equipe vive fazendo gambiarra em planilha
🔧 Seu jeito de vender é o seu diferencial

A pergunta certa não é o preço. É quanto tempo sua equipe perde todo dia tentando encaixar o negócio num sistema que não foi feito pra ele.

E você, usa sistema pronto ou já precisou de algo sob medida? Conta aqui.

💬 Na dúvida, chama no direct com a palavra PROJETO. Às vezes a resposta é: você nem precisa da gente.

#softwaresobmedida #sistemas #gestao #comerciolocal #tecnologia #ubirata #parana #launchcode""",
    },
    {
        "slug": "07-black-friday-cardapio",
        "date": "2026-11-27T10:00:00",
        "slides": [
            {"t": "cover", "kicker": "Hoje é Black Friday", "title": "Sua promoção está <b>no cardápio</b> ou só no story?", "sub": "Arrasta e compara."},
            {"t": "compare", "kicker": "Promoção só no story", "bad": True, "items": ["Cliente pergunta o preço no direct", "Cada atendente informa um valor", "Promoção some quando o story expira", "Pedido chega sem o combo certo"]},
            {"t": "compare", "kicker": "Promoção no cardápio digital", "bad": False, "items": ["Combo em destaque logo no topo", "Preço igual para todo mundo", "Fica no ar até a hora que você quiser", "O cliente pede o combo com um toque"]},
            {"t": "cta", "title": "Na próxima data, <b>já esteja pronto</b>.", "body": "Natal e Ano Novo estão aí. A gente monta seu cardápio digital com espaço para promoções.", "action": "Comenta CARDÁPIO"},
        ],
        "caption": """Hoje é Black Friday. Sua promoção está no cardápio ou só no story? 🖤

Promoção só no story:
❌ Cliente pergunta o preço no direct
❌ Cada atendente informa um valor
❌ Promoção some quando o story expira
❌ Pedido chega sem o combo certo

Promoção no cardápio digital:
✅ Combo em destaque logo no topo
✅ Preço igual pra todo mundo
✅ Fica no ar até a hora que você quiser
✅ O cliente pede o combo com um toque

Natal e Ano Novo estão chegando. Bora estar pronto pra próxima?

💬 Comenta CARDÁPIO que a gente te mostra um cardápio digital com promoções funcionando.

#blackfriday #cardapiodigital #delivery #restaurante #promocao #foodservice #ubirata #parana #launchcode""",
    },
]
