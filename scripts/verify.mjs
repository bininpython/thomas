import {spawn} from 'node:child_process';
import {readFileSync,existsSync} from 'node:fs';
import {chromium} from '@playwright/test';
const port=5187;
const server=spawn(process.execPath,['node_modules/vite/bin/vite.js','--host','127.0.0.1','--port',String(port)],{stdio:'ignore'});
let browser;
try{
 for(let i=0;i<100;i++){try{await fetch(`http://127.0.0.1:${port}`);break}catch{await new Promise(r=>setTimeout(r,100))}}
 browser=await chromium.launch({headless:true,args:['--no-sandbox','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const page=await browser.newPage({viewport:{width:1440,height:1080},reducedMotion:'reduce'});page.setDefaultTimeout(10000);
 await page.addInitScript(()=>{const Original=window.Audio;window.Audio=function(src){const a=new Original(src);window.__lastAudio=a;return a}});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(`http://127.0.0.1:${port}`);await page.evaluate(()=>document.fonts.ready);await page.screenshot({path:'/tmp/tomas-welcome.png'});
 await page.getByRole('button',{name:'Vamos explorar!',exact:true}).click();await page.screenshot({path:'/tmp/tomas-desktop.png',fullPage:true});
 await page.getByRole('button',{name:'Vamos conhecer!',exact:true}).click();await page.screenshot({path:'/tmp/tomas-story.png'});
 for(let i=0;i<4;i++)await page.getByRole('button',{name:'Próxima descoberta',exact:true}).click();
 await page.getByRole('button',{name:'Vamos brincar!',exact:true}).click();
 for(let i=1;i<=5;i++)await page.getByRole('button',{name:`Contar ${i}`,exact:true}).click();
 await page.getByRole('button',{name:'Ganhar figurinha',exact:true}).click();await page.waitForFunction(()=>window.__lastAudio?.src.includes('reward.mp3')&&!window.__lastAudio.paused);await page.getByRole('button',{name:'Mais aventuras',exact:true}).click();
 if(await page.locator('.mission-card.complete').count()!==1)throw Error('Earth reward missing');
 const data=JSON.parse(readFileSync('src/content.json','utf8'));
 const selection=process.env.VERIFY_FROM?data.slice(data.findIndex(t=>t.id===process.env.VERIFY_FROM)):data.slice(1);
 for(const topic of selection){
  await page.getByRole('button',{name:'Descobertas',exact:true}).click();
  const card=page.locator('.discovery-card').filter({has:page.getByRole('heading',{name:topic.name,exact:true})});await card.locator('.fact-row').first().click();
  await page.getByRole('button',{name:'Brincar com essa descoberta',exact:true}).click();
  const game=topic.game;
  if(['craters','moons'].includes(game)){for(let i=1;i<=(game==='moons'?2:5);i++)await page.getByRole('button',{name:`Contar ${i}`,exact:true}).click()}
  else if(game==='jump'){for(let i=0;i<3;i++)await page.getByRole('button',{name:'Vamos pular!',exact:true}).click()}
  else if(game==='hot')await page.getByRole('button',{name:'Quentinho',exact:true}).click();
  else if(game==='biggest'){await page.getByRole('button',{name:'Terra',exact:true}).click();if(!await page.locator('.hint').count())throw Error('No supportive hint');await page.getByRole('button',{name:'Júpiter',exact:true}).click()}
  else if(game==='rings'){for(let i=1;i<=3;i++)await page.getByRole('button',{name:`Adicionar anel ${i}`,exact:true}).click()}
  else if(game==='tilt'){for(let i=0;i<5;i++)await page.getByRole('button',{name:'Girar de ladinho',exact:true}).click()}
  else if(game==='wind'){for(let i=0;i<5;i++)await page.getByRole('button',{name:'Soprar os ventos',exact:true}).click()}
  else if(game==='rocket'){for(const name of ['Motor','Tanque','Cápsula'])await page.getByRole('button',{name,exact:false}).last().click()}
  else if(game==='boost'){for(let i=0;i<5;i++)await page.getByRole('button',{name:'Ligar o motor',exact:true}).click()}
  else if(game==='draw'){const box=await page.locator('.drawing-board').boundingBox();await page.mouse.move(box.x+box.width*.5,box.y+box.height*.5);await page.mouse.down();for(let i=0;i<30;i++)await page.mouse.move(box.x+box.width*.5+Math.cos(i/3)*i*3,box.y+box.height*.5+Math.sin(i/3)*i*2);await page.mouse.up();await page.getByRole('button',{name:'Minha galáxia!',exact:true}).click()}
  else if(game==='sum'){for(const total of [2,3,5]){for(let i=0;i<total;i++)await page.locator('.stone').nth(i).click();if(total<5)await page.getByRole('button',{name:'Mais uma brincadeira',exact:true}).click()}}
  else if(game==='dress'){for(const name of ['Traje','Botas','Luvas','Capacete'])await page.locator('.activity').getByRole('button',{name,exact:false}).click();await page.getByRole('button',{name:'Mais uma brincadeira',exact:true}).click();for(let i=0;i<4;i++)await page.locator('.activity .answer').nth(i).click()}
  else if(game==='numbers'){for(let i=1;i<=10;i++)await page.locator('.activity').getByRole('button',{name:String(i),exact:true}).click();await page.getByRole('button',{name:'Mais uma brincadeira',exact:true}).click();await page.locator('.activity').getByRole('button',{name:'3',exact:true}).click()}
  else if(game==='shapes'){for(const name of ['●','★','🌀'])await page.locator('.activity').getByRole('button',{name,exact:true}).click()}
  else if(game==='race')await page.locator('.activity .answer').filter({hasText:'Luz'}).click();
  else if(game==='order'){for(const name of ['Mercúrio','Vênus','Terra','Marte','Júpiter','Saturno','Urano','Netuno'])await page.getByRole('button',{name:`Colocar ${name}`,exact:true}).click()}
  await page.getByRole('button',{name:'Ganhar figurinha',exact:true}).click();console.log('PASS',topic.name);await page.getByRole('button',{name:'Mais aventuras',exact:true}).click();
 }
 if(await page.locator('.mission-card.complete').count()!==selection.length+1)throw Error('Not all adventures complete');
 await page.getByRole('button',{name:'Meu álbum',exact:true}).click();if(await page.locator('.earned-sticker').count()!==selection.length+1)throw Error('Album count mismatch');
 await page.getByRole('button',{name:'Área da família',exact:true}).first().click();await page.getByRole('button',{name:'18',exact:true}).click();if(await page.getByRole('button',{name:'Reduzir movimento',exact:true}).count())await page.getByRole('button',{name:'Reduzir movimento',exact:true}).click();await page.getByRole('button',{name:'Fechar ajustes',exact:true}).click();
 await page.setViewportSize({width:390,height:844});await page.getByRole('button',{name:'Explorar',exact:true}).first().click();await page.screenshot({path:'/tmp/tomas-mobile.png',fullPage:true});
 if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1))throw Error('Mobile overflow');
 await page.getByRole('button',{name:'Vamos conhecer!',exact:true}).click();await page.screenshot({path:'/tmp/tomas-mobile-story.png',fullPage:true});
 const clips=JSON.parse(readFileSync('src/narrations.json','utf8'));for(const id of Object.keys(clips)){if(!existsSync(`public/audio/${id}.mp3`))throw Error(`Missing audio ${id}`)}
 if(errors.length)throw Error(errors.join('\n'));
 console.log(`PASS: ${selection.length+1} adventures, album, parents, mobile, 161 audio assets; no JS errors.`);
}finally{if(browser)await browser.close();server.kill()}
