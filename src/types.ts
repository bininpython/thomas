export interface Fact { title:string; text:string; visual:string }
export interface Topic { id:string;name:string;tagline:string;category:string;color:string;game:string;emoji:string;intro:string;facts:Fact[] }
export type Page='explore'|'missions'|'discoveries'|'album';
export interface Settings { muted:boolean; music:boolean;volume:number;rate:number;reduced:boolean;suit:number }
