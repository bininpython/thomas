# Tomás, o Astronauta

Uma aventura educativa em português brasileiro para crianças de 3 a 5 anos.

## Jogar e desenvolver

Requisitos: Node.js 22 ou superior.

```bash
npm ci
npm run dev
```

Abra a URL exibida pelo Vite. Para a versão final:

```bash
npm run build
npm run preview
```

O resultado fica em `dist/`, pronto para hospedagem estática. Na Vercel, importar este repositório com framework Vite, comando `npm run build` e diretório `dist`. A base relativa permite também hospedar em subdiretórios. O arquivo `index.html` é a entrada do Vite; abrir esse arquivo diretamente não executa o projeto.

## O que está incluído

- React 19, TypeScript, Vite, Three.js e Framer Motion.
- Nova arte do Tomás inspirada na referência fornecida, com traje personalizável.
- 19 destinos: os oito planetas, Lua, Sol, foguetes, buracos negros, galáxias, cometas, vida de astronauta, números, formas, luz e ordem do Sistema Solar.
- 95 curiosidades em cenas individuais, narradas em português do Brasil.
- 161 falas neurais incluídas como MP3: a execução não depende da voz instalada no aparelho, de chaves de API ou de chamadas a serviços de TTS.
- Minijogos com toque, clique e alternativas de arrastar: contagem, somas, montagem, ordem, desenho, comparações e experiências visuais.
- Álbum, três estrelas por aventura concluída, desbloqueio gradual, contagem de lançamento e medalha ao concluir as aventuras.
- Área da família protegida por uma conta, volume, velocidade de reprodução, música suave, redução de movimento, desbloqueio e reinício com confirmação.
- Progresso somente em memória. Nenhum login, anúncio, telemetria ou coleta de dados.

## Organização

- `src/App.tsx`: navegação, histórias, álbum e ajustes.
- `src/components/Planet.tsx`: objetos Three.js e miniaturas dos planetas.
- `src/components/Activities.tsx`: atividades por tema.
- `src/content.json`: explicações e metadados dos destinos.
- `src/narrations.json`: textos de todas as falas.
- `src/audio.ts`: reprodução, cancelamento e música.
- `public/audio/`: narrações prontas.
- `public/art/tomas.webp`: ilustração incorporada ao projeto.
- `scripts/create-content.py`: fonte editável do conteúdo.
- `scripts/generate-audio.py`: geração opcional de novas falas.

Para alterar uma fala, atualize o conteúdo, remova o MP3 correspondente e gere novamente. O gerador requer Python e `edge-tts`; ele utiliza a voz `pt-BR-FranciscaNeural`, com velocidade levemente reduzida. Essa dependência é somente de produção de conteúdo, não do jogo.

## Critérios pedagógicos

Frases curtas, uma curiosidade por vez, repetição a qualquer momento, perguntas faladas e ausência de cronômetro ou punições. Uma resposta diferente recebe incentivo e uma pista visual. Três estrelas são oferecidas por concluir a experiência, independentemente das tentativas. Os textos grandes apoiam a leitura dos adultos.

Modelos visuais não estão em escala. A superfície estilizada da Terra não é um mapa geográfico. Astros gasosos não são apresentados como locais com chão para caminhar. A flutuação orbital é explicada por queda livre conjunta; buracos negros não são descritos como aspiradores universais.

## Referências científicas

- NASA Science — [Sistema Solar](https://science.nasa.gov/solar-system/)
- NASA — [Mercúrio](https://science.nasa.gov/mercury/facts/), [Vênus](https://science.nasa.gov/venus/venus-facts/), [Terra](https://science.nasa.gov/earth/facts/), [Marte](https://science.nasa.gov/mars/facts/)
- NASA — [Júpiter](https://science.nasa.gov/jupiter/jupiter-facts/), [Saturno](https://science.nasa.gov/saturn/facts/), [Urano](https://science.nasa.gov/uranus/facts/), [Netuno](https://science.nasa.gov/neptune/neptune-facts/)
- NASA — [Buracos negros](https://science.nasa.gov/universe/black-holes/)
- NASA Space Place — [Como funcionam foguetes](https://spaceplace.nasa.gov/launching-into-space/en/)

## Compatibilidade

Use um navegador moderno com JavaScript. A narração começa após uma interação do usuário, respeitando as regras de reprodução de áudio dos navegadores. Se WebGL não estiver disponível, a visualização tem uma miniatura alternativa. Cada faixa é carregada somente ao ser usada. As fontes, a arte e os áudios são locais, sem URLs externas no jogo.
