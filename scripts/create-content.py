import json,pathlib
root=pathlib.Path(__file__).resolve().parents[1]
rows=[
('earth','Terra','Nossa casa azul','planetas','#63dbc1','count','🌍','Sou a Terra, a casa do Tomás! Vamos explorar juntos?',[
('Um planeta cheio de vida','Aqui vivem pessoas, animais e plantas. É nosso lar!','leaf'),('Azul de água','Os oceanos cobrem grande parte da Terra. Quanta água!','water'),('Dia e noite','A Terra gira. O lado iluminado pelo Sol tem dia.','day'),('Nossa companheira','A Lua acompanha a Terra pelo espaço. Ela reflete luz solar.','orbit'),('Uma volta por ano','A Terra leva cerca de um ano para contornar o Sol.','orbit')]),
('moon','Lua','Uma vizinha cheia de crateras','universo','#d6dcec','jump','🌙','Oi, Tomás! Venha conhecer minha superfície cheia de crateras!',[
('Pulos bem altos','A gravidade lunar é menor. Podemos pular mais alto aqui!','jump'),('Luz emprestada','A Lua não produz luz própria. Ela reflete a luz solar.','light'),('Marquinhas espaciais','Rochas espaciais fizeram muitas crateras. São marcas de impactos.','crater'),('Mudando de carinha','Vemos partes diferentes da metade iluminada. São as fases lunares.','phase'),('Pegadas na Lua','Astronautas já caminharam na Lua. Usaram trajes especiais!','suit')]),
('sun','Sol','A estrela da nossa turma','universo','#ffbe50','hot','☀️','Olá, Tomás! Sou o Sol, a estrela do nosso sistema!',[
('Luz e calor','A luz e o calor do Sol ajudam a vida terrestre.','light'),('Uma estrela de perto','O Sol é uma estrela. As outras ficam muito longe!','star'),('Muito maior','O Sol é muito maior que a Terra. Que grandão!','size'),('Uma viagem de luz','A luz solar demora cerca de oito minutos para chegar aqui.','light'),('Olhinhos protegidos','Nunca olhe diretamente para o Sol. Proteja seus olhinhos!','safe')]),
('mercury','Mercúrio','Pequeno e apressadinho','planetas','#b5ac9f','craters','⚪','Sou Mercúrio! Sou pequeno e fico pertinho do Sol!',[
('O primeiro da fila','Mercúrio é o primeiro planeta a partir do Sol.','order'),('O menor planeta','Entre os oito planetas, Mercúrio é o menor.','size'),('Ano rapidinho','Minha volta ao Sol dura cerca de oitenta e oito dias!','orbit'),('Cheio de crateras','Minha superfície é rochosa e tem muitas crateras.','crater'),('Quente e frio','Aqui faz muito calor durante o dia. À noite, muito frio!','hot')]),
('venus','Vênus','Um mundo coberto de nuvens','planetas','#eeac70','hot','🟠','Oi, Tomás! Eu sou Vênus, um planeta cheio de nuvens!',[
('O segundo planeta','Sou o segundo planeta a partir do Sol.','order'),('Mais quente de todos','Minhas nuvens e atmosfera prendem muito calor. Sou muito quente!','hot'),('Quase do mesmo tamanho','Vênus e Terra têm tamanhos parecidos. Mas são muito diferentes!','size'),('Giro diferente','Giro no sentido contrário ao da maioria dos planetas.','spin'),('Brilhante no céu','Posso brilhar bastante no céu. Mas não sou uma estrela!','star')]),
('mars','Marte','Nosso vizinho vermelho','planetas','#f98262','moons','🔴','Olá, Tomás! Sou Marte. Minha poeira tem cor avermelhada!',[
('Vermelho de ferrugem','Minha poeira tem minerais com ferro oxidado. Lembra ferrugem!','color'),('Duas pequenas luas','Tenho duas luas: Fobos e Deimos. Vamos contar até dois?','count'),('Robôs exploradores','Robôs com rodas exploram Marte. Eles enviam descobertas à Terra!','rover'),('Montanha gigante','O Monte Olimpo é um vulcão enorme. Maior que montanhas terrestres!','mountain'),('Um mundo frio','Apesar da cor quentinha, Marte é um planeta frio.','cold')]),
('jupiter','Júpiter','O gigante do Sistema Solar','planetas','#e4b98a','biggest','🟤','Oi, Tomás! Eu sou Júpiter, o maior dos planetas!',[
('Gigante de gás','Sou formado principalmente por gases. Não tenho chão para caminhar!','gas'),('Uma tempestade enorme','Minha Grande Mancha Vermelha é uma tempestade gigantesca.','storm'),('Faixas coloridas','As faixas que você vê são nuvens na minha atmosfera.','cloud'),('Muitas companheiras','Muitas luas giram ao meu redor. Uma delas chama-se Europa!','orbit'),('Giro rapidinho','Um dia em Júpiter dura cerca de dez horas.','spin')]),
('saturn','Saturno','Um planeta com muitos anéis','planetas','#f3d090','rings','🪐','Olá, Tomás! Sou Saturno. Venha conhecer meus anéis!',[
('Anéis de pedacinhos','Meus anéis têm incontáveis pedacinhos de gelo e rocha.','ring'),('Segundo grandalhão','Só Júpiter é maior que eu entre os planetas.','size'),('Sem chão para pisar','Também sou um gigante gasoso. Observamos de dentro da nave.','gas'),('Uma lua com atmosfera','Titã, uma das minhas luas, tem uma atmosfera espessa.','cloud'),('Anéis para outros','Júpiter, Urano e Netuno também têm anéis. São menos visíveis!','ring')]),
('uranus','Urano','O planeta que gira de ladinho','planetas','#a3e8ea','tilt','🔵','Oi, Tomás! Eu sou Urano. Veja como giro de ladinho!',[
('Quase deitado','Meu eixo é muito inclinado. Por isso, giro de ladinho!','tilt'),('Azul esverdeado','O gás metano na atmosfera ajuda a dar minha cor.','color'),('Gigante gelado','Sou chamado gigante de gelo. Minha atmosfera é muito fria!','cold'),('O sétimo planeta','Sou o sétimo planeta a partir do Sol.','order'),('Anéis discretos','Também tenho anéis. São escuros e difíceis de enxergar.','ring')]),
('neptune','Netuno','Azul, distante e ventoso','planetas','#6a99ef','wind','🔵','Oi, Tomás! Eu sou Netuno, o planeta mais distante do Sol!',[
('Último dos oito','Sou o oitavo planeta na ordem a partir do Sol.','order'),('Ventos muito fortes','Minha atmosfera tem ventos muito velozes. Que ventania!','wind'),('Muito longe do Sol','A luz solar chega fraquinha aqui. É muito frio!','cold'),('Uma volta demorada','Um ano aqui dura cerca de 165 anos terrestres.','orbit'),('Lua ao contrário','Minha lua Tritão gira no sentido contrário à minha rotação.','orbit')]),
('rockets','Foguetes','Três, dois, um… vamos!','aventuras','#9af0ce','rocket','🚀','Preparado, comandante Tomás? Vamos descobrir como um foguete voa!',[
('Um empurrão poderoso','O foguete joga gases para trás. Isso o empurra para frente!','thrust'),('Funciona no espaço','Foguetes também funcionam onde quase não existe ar.','thrust'),('Cada peça tem função','Motores empurram. Tanques guardam combustível. A cápsula leva astronautas.','build'),('Viagem em etapas','Alguns foguetes soltam partes usadas. Assim, carregam menos peso!','build'),('Exploradores robóticos','Foguetes também levam satélites e robôs exploradores ao espaço.','rover')]),
('blackhole','Buracos negros','Um mistério para descobrir','universo','#b899ff','boost','🌀','Tomás, vamos observar um buraco negro. Nossa nave está segura!',[
('Gravidade muito forte','Muito perto, sua gravidade impede até a luz de escapar.','pull'),('Não é um aspirador','De longe, ele atrai como outros objetos com mesma massa.','orbit'),('Um limite especial','O horizonte de eventos é um limite sem caminho de volta.','ring'),('Como conseguimos estudar?','Cientistas observam seus efeitos na luz e nos objetos vizinhos.','light'),('Estamos bem seguros','Não existe buraco negro perto o suficiente para engolir a Terra.','safe')]),
('galaxy','Galáxias','Uma imensidão de estrelas','universo','#dba6f5','draw','🌌','Bem-vindo, Tomás! Vamos passear entre muitas, muitas estrelas!',[
('Nossa casa gigante','O Sol pertence à Via Láctea. Ela é nossa galáxia!','star'),('Braços de estrelas','A Via Láctea tem braços em espiral e uma barra central.','spiral'),('Muitas formas','Existem galáxias espirais, elípticas e irregulares. Quanta variedade!','shape'),('Outras estrelas, outros mundos','Muitas estrelas têm planetas. Chamamos esses mundos de exoplanetas.','orbit'),('Um céu muito antigo','Luz leva tempo para viajar. Vemos estrelas como eram antes.','light')]),
('comets','Cometas e asteroides','Viajantes de gelo e rocha','universo','#81e5eb','sum','☄️','Tomás, veja esses viajantes espaciais! Vamos contar juntos?',[
('Cometas têm gelo','Cometas contêm gelo, poeira e rochas.','ice'),('Uma cauda aparece','Perto do Sol, cometas liberam gases e poeira, formando caudas.','tail'),('Asteroides são diferentes','Asteroides são principalmente rochosos ou metálicos.','rock'),('Entre Marte e Júpiter','Muitos asteroides ficam num cinturão entre Marte e Júpiter.','orbit'),('Estrela cadente?','É um meteoro brilhando na atmosfera. Não é uma estrela!','light')]),
('astronaut','Vida no espaço','Um dia de astronauta','aventuras','#ffb5bc','dress','🧑‍🚀','Vamos preparar seu traje, Tomás! Hoje você é o astronauta!',[
('Um traje especial','O traje fornece oxigênio e ajuda a proteger o astronauta.','suit'),('Por que flutuamos?','Na estação, tudo cai junto ao redor da Terra. Parece flutuar!','float'),('Ainda existe gravidade','A gravidade continua agindo na estação espacial.','pull'),('Comidinhas organizadas','Pacotes ajudam a segurar a comida. Assim, ela não sai flutuando!','food'),('Corpo em movimento','Astronautas fazem exercícios para cuidar dos músculos e dos ossos.','jump')]),
('numbers','Números espaciais','Contar é uma aventura','brincadeiras','#fbdc75','numbers','🔢','Um, dois, três! Vamos brincar com os números, Tomás!',[
('Cada coisa, um número','Tocamos cada estrela uma vez para contar direitinho.','count'),('Do pequeno ao grande','Um, dois, três, quatro, cinco. Os números seguem uma ordem!','order'),('Juntar é somar','Uma estrela e mais uma estrela são duas estrelas.','count'),('Quem vem depois?','Depois do cinco, vem o seis. Vamos continuar contando?','order'),('Até dez','Seis, sete, oito, nove, dez. Dez dedos ajudam a contar!','count')]),
('shapes','Cores e formas','Uma paleta de descobertas','brincadeiras','#b6a2f4','shapes','🎨','Olhe as cores e as formas, Tomás! Vamos encontrar pares?',[
('Uma forma redondinha','Planetas são quase esféricos. No desenho, parecem círculos.','shape'),('Estrelas de verdade','Estrelas são enormes bolas de gás. Pontinhas são nosso desenho!','star'),('Caminho em espiral','Uma espiral dá voltas, chegando perto ou longe do centro.','spiral'),('As cores dos mundos','A Terra parece azul. Marte parece avermelhado.','color'),('Encontrando pares','Podemos juntar objetos pela cor ou pela forma.','shape')]),
('light','Luz e velocidade','Rápido, devagar e brilhante','brincadeiras','#fce492','race','💡','Tomás, vamos descobrir quem viaja mais rápido!',[
('A luz viaja','A luz precisa de tempo para chegar de um lugar.','light'),('Muito, muito rápida','No vácuo, nada transporta informação mais rápido que a luz.','light'),('Foguetes são rápidos','Foguetes são rápidos para nós. A luz é muito mais rápida!','thrust'),('Devagar também é legal','A tartaruga anda devagar. Cada um tem seu jeito!','slow'),('Luz para enxergar','Vemos objetos quando a luz deles chega aos nossos olhos.','light')]),
('order','Sistema Solar','Oito planetas, uma estrela','brincadeiras','#78d9e6','order','🪐','Vamos montar o Sistema Solar! O Sol fica no centro!',[
('Os primeiros quatro','Mercúrio, Vênus, Terra e Marte são planetas rochosos.','order'),('Os próximos quatro','Júpiter, Saturno, Urano e Netuno ficam mais longe do Sol.','order'),('Caminhos chamados órbitas','Os planetas seguem caminhos ao redor do Sol: suas órbitas.','orbit'),('E o pequeno Plutão?','Plutão é um planeta anão. Continua fazendo parte dessa turma!','size'),('Um modelo para brincar','Aqui tamanhos e distâncias foram ajustados para caber na tela.','size')])]
data=[]
for idx,(id,name,tag,cat,color,game,emoji,intro,facts) in enumerate(rows):
 data.append(dict(id=id,name=name,tagline=tag,category=cat,color=color,game=game,emoji=emoji,intro=intro,facts=[dict(title=t,text=x,visual=v) for t,x,v in facts]))
(root/'src/content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
common={
 'welcome':'Olá, Tomás! Eu sou a Estrelinha. Vamos descobrir o universo juntos?',
 'explore':'Escolha um mundo para descobrir. Depois, toque no botão de brincar!',
 'missions':'Escolha uma aventura. Cada descoberta abre um novo caminho!',
 'discoveries':'Toque numa curiosidade para escutar. Que mundo você quer conhecer?',
 'album':'Este é seu álbum! Cada aventura traz uma nova figurinha.',
 'good':'Uhuuul! Você conseguiu! Que descoberta linda, Tomás!',
 'try':'Quase, Tomás! Vamos juntos? Olhe a opção que está brilhando.',
 'reward':'Missão cumprida, comandante Tomás! Três estrelas e uma nova figurinha!',
 'final':'Tomás, você explorou todas as aventuras! Sua medalha de astronauta chegou!',
 'locked':'Essa aventura abre depois da anterior. Vamos dar um passinho primeiro?',
 'gate':'Área da família. Peça ajuda a um adulto para entrar.',
 'launch':'Preparar para decolar! Vamos contar juntos?',
 'go':'Decolando! Que aventura incrível nos espera!',
 'ready':'Muito bem! Agora vamos brincar com o que descobrimos.',
 'draw':'Passe o dedo e desenhe uma espiral de estrelas!',
 'boost':'Toque no motor cinco vezes. Vamos seguir nossa rota segura!',
 'rocket':'Monte o foguete: motor, tanque e cápsula. Toque ou arraste!',
 'dress':'Primeiro, o traje. Depois, as botas, luvas e capacete!',
 'pack':'Toque na comida e leve o pacote para a mochila!',
 'jump':'Toque para pular. Na Lua, o pulo é mais alto!',
 'race':'Qual viaja mais rápido? A luz, o foguete ou a tartaruga?',
 'count':'Vamos contar cinco estrelas! Toque em cada uma, sem pressa.',
 'craters':'Vamos descobrir cinco crateras! Toque nas marquinhas da superfície.',
 'moons':'Marte tem duas luas. Toque nas duas para contar!',
 'hot':'Qual parece quentinho? Toque no Sol, nossa estrela!',
 'biggest':'Qual planeta é o maior? Procure o grandalhão Júpiter!',
 'rings':'Leve cada anel até Saturno. Pode tocar ou arrastar!',
 'tilt':'Toque em Urano para inclinar seu eixo. Ele gira de ladinho!',
 'wind':'Toque nas nuvens e veja a ventania de Netuno!',
 'numbers':'Vamos encontrar os números, do um até o dez!',
 'shapes':'Encontre a forma que combina com o modelo!',
 'order':'Monte a fila: Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Urano, Netuno.',
 'sum-0':'Uma pedra, mais uma pedra. Junte duas pedras na cesta!',
 'sum-1':'Duas pedras, mais uma pedra. Junte três pedras na cesta!',
 'sum-2':'Três pedras, mais duas pedras. Junte cinco pedras na cesta!',
 'missing':'Um, dois, e depois? Toque no número três!',
 'home':'Voltamos à nave. Qual será nossa próxima descoberta?'
}
for n in range(1,11): common[f'number-{n}']=[None,'Um!','Dois!','Três!','Quatro!','Cinco!','Seis!','Sete!','Oito!','Nove!','Dez!'][n]
audio=dict(common)
for t in data:
 audio[f"{t['id']}-intro"]=t['intro']
 for i,f in enumerate(t['facts']): audio[f"{t['id']}-{i}"]=f['text']
(root/'src/narrations.json').write_text(json.dumps(audio,ensure_ascii=False,indent=2))
print(len(data),'destinos;',sum(len(t['facts']) for t in data),'curiosidades;',len(audio),'falas')
