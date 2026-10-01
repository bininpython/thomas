import narrations from './narrations.json';
// Voz neural em arquivos locais: nenhuma chamada à nuvem durante o jogo.
const clips=narrations as Record<string,string>;
let active:HTMLAudioElement|null=null;
let last='welcome';
let volume=.85,rate=1,muted=false;
let context:AudioContext|undefined;
let ambient:GainNode|undefined;
let notes:OscillatorNode[]=[];
let onChange:(playing:boolean)=>void=()=>{};
export const voice={
 onChange(fn:(playing:boolean)=>void){onChange=fn},
 configure(v:number,r:number,m:boolean){volume=v;rate=r;muted=m;if(active){active.volume=muted?0:volume;active.playbackRate=rate}if(ambient)ambient.gain.value=muted?0:volume*.018},
 stop(){if(active){active.pause();active.onended=null;active=null}onChange(false)},
 async play(id:string){this.stop();last=id;if(muted)return;const a=new Audio(`${import.meta.env.BASE_URL}audio/${id}.mp3`);active=a;a.volume=volume;a.playbackRate=rate;onChange(true);a.onended=()=>{if(active===a)onChange(false)};a.onerror=()=>{if(active===a)onChange(false)};try{await a.play()}catch{onChange(false)}},
 repeat(){void this.play(last)},
 text(id:string){return clips[id]||''},
 music(enabled:boolean){if(!enabled){notes.forEach(n=>n.stop());notes=[];ambient=undefined;return}if(notes.length)return;context??=new AudioContext();void context.resume();ambient=context.createGain();ambient.gain.value=muted?0:volume*.018;ambient.connect(context.destination);[130.81,196,261.63].forEach(f=>{const o=context!.createOscillator();o.frequency.value=f;o.type='sine';o.connect(ambient!);o.start();notes.push(o)})},
 chime(){if(muted)return;context??=new AudioContext();void context.resume();[523.25,659.25,783.99].forEach((f,i)=>{const o=context!.createOscillator(),g=context!.createGain();o.frequency.value=f;g.gain.setValueAtTime(0,context!.currentTime+i*.09);g.gain.linearRampToValueAtTime(volume*.06,context!.currentTime+i*.09+.02);g.gain.exponentialRampToValueAtTime(.0001,context!.currentTime+i*.09+.5);o.connect(g);g.connect(context!.destination);o.start(context!.currentTime+i*.09);o.stop(context!.currentTime+i*.09+.6)})}
};
