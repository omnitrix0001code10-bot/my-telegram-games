# -*- coding: utf-8 -*-
from pathlib import Path

root = Path(r"C:\Users\Admin\Desktop\Omni Clash")
html_path = root / "omni_clash_luxury_final.html"
css = (root / "_lux_style.css").read_text(encoding="utf-8")
text = html_path.read_text(encoding="utf-8")

s = text.find("<style>")
e = text.find("</style>")
if s < 0 or e < 0:
    raise SystemExit("style tags not found")
text = text[:s] + "<style>\n" + css + "\n" + text[e:]

replacements = []

old_card = '''function CardVisual({card,enemy=false,small=false,showAssetLabel=false,t}){
  const [imageOk,setImageOk]=useState(true);
  const c=card||{};
  const buff=c.buff||{name:"—",desc:""};
  const debuff=c.debuff||{name:"—",desc:""};
  const safeName=c.name||"Unknown";
  const safeCategory=c.category||"Unknown";
  const safeAvatar=c.avatar||"✦";
  return <div className={`hero-card ${rarityClass(c.rarity)} ${small?"":"p-3"} ${small?"w-full":"battle-card"} ${enemy?"!bg-[#120707]":""}`}>
    <div className={`asset-art ${small?"min-h-[105px]":"min-h-[165px]"} ${enemy?"!bg-[#100707]":""}`}>
      {c.imgAssetSlot && imageOk && <img src={c.imgAssetSlot} alt={safeName} onError={()=>setImageOk(false)}/>}
      {(!c.imgAssetSlot || !imageOk) && <div className="asset-placeholder">{safeAvatar}</div>}
      <div className="absolute inset-x-0 bottom-0 h-20 bg-gradient-to-t from-black/70 to-transparent pointer-events-none"/>
      <div className="absolute left-3 top-3 text-[9px] uppercase font-bold tracking-widest px-2 py-1 rounded-full bg-black/40 border border-white/10">{safeCategory}</div>
      <div className={`absolute right-3 top-3 text-[9px] uppercase font-bold tracking-widest px-2 py-1 rounded-full bg-black/40 border border-white/10 ${normalizeRarity(c.rarity)==="Creator"?"text-[#00ff66]":""}`}>{rarityText(c.rarity,t)}</div>
    </div>
    <div className="p-4">
      <div className="font-cinzel font-bold text-xl leading-tight text-center">{safeName}</div>
      <div className="flex justify-center gap-2 mt-3 text-[10px] font-mono text-slate-400">
        <span>HP {c.hp??"—"}</span><span>DEF {c.def??"—"}</span><span>SPD {c.spd??"—"}</span>
      </div>
      <div className="grid grid-cols-2 gap-2 mt-4">
        <div className="rounded-xl border border-emerald-500/20 bg-emerald-500/5 px-2 py-2">
          <div className="text-[9px] font-bold text-emerald-400 mb-1">{t.buff}</div>
          <div className="text-[9px] text-slate-300 leading-snug">{buff.name||"—"}</div>
        </div>
        <div className="rounded-xl border border-red-500/20 bg-red-500/5 px-2 py-2">
          <div className="text-[9px] font-bold text-red-400 mb-1">{t.debuff}</div>
          <div className="text-[9px] text-slate-300 leading-snug">{debuff.name||"—"}</div>
        </div>
      </div>
      {showAssetLabel && <div className="mt-3 space-y-1 text-[8px] text-slate-500 font-mono"><div>{t.assetSlot}: {c.imgAssetSlot||"—"}</div><div>{t.cardAudio}: {c.cardAudioSlot||"—"}</div></div>}
    </div>
  </div>
}'''

new_card = '''function CardVisual({card,enemy=false,small=false,showAssetLabel=false,t}){
  const [imageOk,setImageOk]=useState(true);
  const c=card||{};
  const buff=c.buff||{name:"—",desc:""};
  const debuff=c.debuff||{name:"—",desc:""};
  const safeName=c.name||"Unknown";
  const safeCategory=c.category||"Unknown";
  const safeAvatar=c.avatar||"✦";
  return <div className={`lux-card ${rarityClass(c.rarity)} ${small?"w-full":"battle-card"} ${enemy?"lux-card-enemy":""}`}>
    <div className="lux-card-glow"/><div className="lux-card-sweep"/>
    <div className="lux-card-frame">
    <div className={`asset-art ${small?"min-h-[105px]":"min-h-[165px]"} ${enemy?"!bg-[#100707]":""}`}>
      {c.imgAssetSlot && imageOk && <img src={c.imgAssetSlot} alt={safeName} onError={()=>setImageOk(false)}/>}
      {(!c.imgAssetSlot || !imageOk) && <div className="asset-placeholder">{safeAvatar}</div>}
      <div className="absolute inset-x-0 bottom-0 h-20 bg-gradient-to-t from-black/70 to-transparent pointer-events-none"/>
      <div className="absolute left-3 top-3 text-[9px] uppercase font-bold tracking-widest px-2 py-1 rounded-full bg-black/40 border border-white/10">{safeCategory}</div>
      <div className={`absolute right-3 top-3 text-[9px] uppercase font-bold tracking-widest px-2 py-1 rounded-full bg-black/40 border border-white/10 ${normalizeRarity(c.rarity)==="Creator"?"text-[#00ff66]":""}`}>{rarityText(c.rarity,t)}</div>
    </div>
    <div className="p-4">
      <div className="font-cinzel font-bold text-xl leading-tight text-center">{safeName}</div>
      <div className="flex justify-center gap-2 mt-3 text-[10px] font-mono text-slate-400">
        <span>HP {c.hp??"—"}</span><span>DEF {c.def??"—"}</span><span>SPD {c.spd??"—"}</span>
      </div>
      <div className="grid grid-cols-2 gap-2 mt-4">
        <div className="rounded-xl border border-emerald-500/20 bg-emerald-500/5 px-2 py-2">
          <div className="text-[9px] font-bold text-emerald-400 mb-1">{t.buff}</div>
          <div className="text-[9px] text-slate-300 leading-snug">{buff.name||"—"}</div>
        </div>
        <div className="rounded-xl border border-red-500/20 bg-red-500/5 px-2 py-2">
          <div className="text-[9px] font-bold text-red-400 mb-1">{t.debuff}</div>
          <div className="text-[9px] text-slate-300 leading-snug">{debuff.name||"—"}</div>
        </div>
      </div>
      {showAssetLabel && <div className="mt-3 space-y-1 text-[8px] text-slate-500 font-mono"><div>{t.assetSlot}: {c.imgAssetSlot||"—"}</div><div>{t.cardAudio}: {c.cardAudioSlot||"—"}</div></div>}
    </div>
    </div>
  </div>
}'''

old_ab = '''function AbilityButton({ab,energy,disabled,onClick,index,t}){
  const safe = ab || {id:`fallback_${index}`,name:"Unknown Skill",power:0,isUlt:false,energyGain:26};
  return <button onClick={onClick} disabled={disabled || !ab} className={`relative group text-left rounded-2xl p-3 border transition-all duration-500 ${safe.isUlt?"border-purple-400/40 bg-purple-500/10":"border-white/8 bg-white/[.035]"} ${disabled||!ab?"opacity-40 cursor-not-allowed grayscale":"hover:-translate-y-1 hover:border-white/20 hover:bg-white/[.06]"}`}>
    <div className="text-[9px] uppercase tracking-widest text-slate-500 mb-1">0{index+1} • {safe.isUlt?"ULTIMATE":"SKILL"}</div>
    <div className="font-semibold text-sm leading-tight">{safe.name || "Unknown Skill"}</div>
    <div className="mt-2 flex items-center justify-between text-[10px]">
      <span className="text-red-300">DMG {Number(safe.power)||0}</span>
      <span className={safe.isUlt?"text-purple-300":"text-cyan-300"}>{safe.isUlt?`100% ${t.energy}`:`+${safe.energyGain||26}% ${t.energy}`}</span>
    </div>
    {safe.isUlt && energy<100 && <div className="mt-2 text-[9px] text-purple-300/70">{t.noEnergy}</div>}
  </button>
}'''

new_ab = '''function AbilityButton({ab,energy,disabled,onClick,index,t,selected=false}){
  const safe = ab || {id:`fallback_${index}`,name:"Unknown Skill",power:0,isUlt:false,energyGain:26};
  return <button onClick={onClick} disabled={disabled || !ab} className={`ability-mod ${safe.isUlt?"is-ult":""} ${selected?"selected":""}`}>
    <div className="text-[9px] uppercase tracking-widest text-slate-500 mb-1">0{index+1} • {safe.isUlt?"ULTIMATE":"SKILL"}</div>
    <div className="font-semibold text-sm leading-tight">{safe.name || "Unknown Skill"}</div>
    <div className="mt-2 flex items-center justify-between text-[10px]">
      <span className="text-red-300">DMG {Number(safe.power)||0}</span>
      <span className={safe.isUlt?"text-purple-300":"text-cyan-300"}>{safe.isUlt?`100% ${t.energy}`:`+${safe.energyGain||26}% ${t.energy}`}</span>
    </div>
    <div className="ability-energy" style={{"--need":(safe.isUlt?100:(safe.energyGain||26))+"%"}}><i/></div>
    {safe.isUlt && energy<100 && <div className="mt-2 text-[9px] text-purple-300/70">{t.noEnergy}</div>}
  </button>
}'''

replacements.extend([
    (old_card, new_card),
    (old_ab, new_ab),
    ('creatorPreview:"ОТКРЫТЬ РЕЖИМ СОЗДАТЕЛЯ"', 'creatorPreview:"ОТКРЫТЬ РЕЖИМ СОЗДАТЕЛЯ",\n    noInvites:"Нет активных приглашений"'),
    ('creatorPreview:"OPEN CREATOR MODE"', 'creatorPreview:"OPEN CREATOR MODE",\n    noInvites:"No active invitations"'),
    ('const fogs=useMemo(()=>Array.from({length:14},(_,i)=>({i,left:Math.random()*100,top:Math.random()*90,size:180+Math.random()*260,duration:19+Math.random()*18,delay:-Math.random()*18})),[]);',
     'const fogs=useMemo(()=>Array.from({length:6},(_,i)=>({i,left:Math.random()*100,top:Math.random()*90,size:180+Math.random()*260,duration:19+Math.random()*18,delay:-Math.random()*18})),[]);'),
    ('const particles=useMemo(()=>Array.from({length:54},(_,i)=>({i,left:Math.random()*100,size:1.5+Math.random()*3.8,dur:10+Math.random()*18,delay:-Math.random()*22,dx:(Math.random()-.5)*130})),[]);',
     'const particles=useMemo(()=>Array.from({length:16},(_,i)=>({i,left:Math.random()*100,size:1.5+Math.random()*3.8,dur:10+Math.random()*18,delay:-Math.random()*22,dx:(Math.random()-.5)*130})),[]);'),
    ('''  const scheduleMerge=(onReveal,onHide)=>{
    setMergePhase("active");
    rememberTimer(setTimeout(()=>setMergePhase("flash"),1180));
    rememberTimer(setTimeout(()=>{setMergePhase("result");onReveal?.()},1580));
    rememberTimer(setTimeout(()=>{setMergePhase(null);onHide?.()},2650));
  };''',
     '''  const scheduleMerge=(onReveal,onHide)=>{
    setMergePhase("active");
    rememberTimer(setTimeout(()=>setMergePhase("flash"),1250));
    rememberTimer(setTimeout(()=>{setMergePhase("result");onReveal?.()},1375));
    rememberTimer(setTimeout(()=>{setMergePhase(null);onHide?.()},2500));
  };'''),
    ('''    <div className="page-enter relative z-10 min-h-screen flex flex-col items-center px-4 pt-10 pb-16">
      <div className="text-center mt-7 sm:mt-10">
        <div className="inline-flex items-center gap-2 text-[9px] uppercase tracking-[.35em] text-emerald-300/70 px-3 py-1 rounded-full border border-emerald-400/15 bg-emerald-400/5">LUXURY TACTICAL • v2</div>
        <h1 className="menu-title font-cinzel font-black text-5xl sm:text-7xl md:text-8xl leading-none mt-5 text-transparent bg-clip-text bg-gradient-to-b from-white via-emerald-100 to-emerald-500">{t.title}</h1>''',
     '''    <div className="page-enter relative z-10 min-h-screen flex flex-col items-center px-4 pt-10 pb-16">
      <div className="geo-line geo-vline"/>
      <div className="geo-line" style={{top:"18%",left:"12%",width:"28%"}}/>
      <div className="geo-line" style={{top:"22%",right:"10%",width:"22%"}}/>
      <div className="text-center mt-7 sm:mt-10 relative">
        <div className="hero-kicker uppercase">LUXURY TACTICAL • v2</div>
        <h1 className="menu-title font-cinzel font-black text-5xl sm:text-7xl md:text-8xl leading-none mt-5 text-transparent bg-clip-text bg-gradient-to-b from-white via-emerald-100 to-emerald-500">{t.title}</h1>'''),
    ('<div className="flex flex-wrap justify-center gap-3 max-w-5xl mt-7">{navButton(t.deck,"🃏",()=>setScreenState("deck"),"neon")}{navButton(t.collection,"◫",()=>setScreenState("collection"))}{navButton(t.shop,"◈",()=>setScreenState("shop"),"gold")}{navButton(t.settings,"⚙",()=>setScreenState("settings"))}</div>\n      <div className="flex flex-wrap justify-center gap-3 mt-3">{navButton(t.credits,"✦",()=>setShowCredits(true))}{navButton(t.help,"?",()=>setShowHelp(true))}</div>',
     '<div className="nav-cluster max-w-5xl mt-7">{navButton(t.deck,"🃏",()=>setScreenState("deck"),"neon")}{navButton(t.collection,"◫",()=>setScreenState("collection"))}{navButton(t.shop,"◈",()=>setScreenState("shop"),"gold")}{navButton(t.settings,"⚙",()=>setScreenState("settings"))}</div>\n      <div className="nav-cluster mt-3">{navButton(t.credits,"✦",()=>setShowCredits(true))}{navButton(t.help,"?",()=>setShowHelp(true))}{navButton(t.invites,"✉",()=>{if(incomingInvite)joinPending();else notify(t.noInvites)})}</div>'),
    ('<button onClick={()=>{const c=document.getElementById("joinCode").value.trim();if(c)joinRoom(c,"pvp")}} className="w-full mt-3 rounded-xl bg-white text-black py-2.5 font-bold text-sm">JOIN</button>',
     '<button onClick={()=>{const c=document.getElementById("joinCode").value.trim();if(c)joinRoom(c,"pvp")}} className="lux-btn-primary w-full mt-3 py-2.5 text-sm">JOIN</button>'),
    ('{p&&mergePhase?<CardVisual card={p} t={t} showAssetLabel/>:<div className="lux-panel rounded-[26px] h-[470px] grid place-items-center text-slate-700">{p?t.waiting:t.chooseHero}</div>}',
     '{p?<CardVisual card={p} t={t} showAssetLabel/>:<div className="lux-panel rounded-[26px] h-[470px] grid place-items-center text-slate-700">{t.chooseHero}</div>}'),
    ('{o&&mergePhase?<CardVisual card={o} t={t} enemy showAssetLabel/>:<div className="lux-panel rounded-[26px] h-[470px] grid place-items-center text-slate-700">{t.waiting}</div>}',
     '{o?<CardVisual card={o} t={t} enemy showAssetLabel/>:<div className="lux-panel rounded-[26px] h-[470px] grid place-items-center text-slate-700">{t.waiting}</div>}'),
    ('{abilities.map((ab,i)=><AbilityButton key={ab.id} ab={ab} index={i} energy={game.playerEnergy} disabled={ab.isUlt&&game.playerEnergy<100} onClick={()=>handleSelectAbility(ab)} t={t}/>)}',
     '{abilities.map((ab,i)=><AbilityButton key={ab.id} ab={ab} index={i} energy={game.playerEnergy} disabled={ab.isUlt&&game.playerEnergy<100} selected={game.selectedAbility?.id===ab.id} onClick={()=>handleSelectAbility(ab)} t={t}/>)}'),
])

old_merge = '''      {mergePhase&&p&&o&&<div className={`merge-scene ${mergePhase==="active"?"active":""} ${mergePhase==="flash"||mergePhase==="result"?"active flash":""} ${mergePhase==="result"?"show-result":""}`}>
        <div className="merge-core">
          <div className="merge-fusion-glow"/><div className="merge-fusion-ring"/>
          <div className="merge-card left"><div className="merge-card-inner"><div className="merge-card-label">OPPONENT</div><div className="text-6xl relative z-10">{p.avatar}</div><div className="font-cinzel mt-4 relative z-10">{p.name}</div></div></div>
          <div className="merge-card right"><div className="merge-card-inner"><div className="merge-card-label">YOU</div><div className="text-6xl relative z-10">{o.avatar}</div><div className="font-cinzel mt-4 relative z-10">{o.name}</div></div></div>
          <div className="merge-white"><div className="merge-winner"><div className="merge-fused-icons">{result?.roundWinner==="PLAYER"?p.avatar:result?.roundWinner==="OPPONENT"?o.avatar:"✦"}</div>{mergePhase==="result"&&<><small>{t.round} {game.round}</small><strong>{result?.roundWinner==="PLAYER"?t.roundWin:result?.roundWinner==="OPPONENT"?t.roundLose:t.draw}</strong><em>{result?.roundWinner==="PLAYER"?p.name:result?.roundWinner==="OPPONENT"?o.name:`${p.name} • ${o.name}`}</em></>}</div></div>
        </div>
      </div>}'''

new_merge = '''      {mergePhase&&p&&o&&<div className={`merge-scene ${mergePhase==="active"?"active":""} ${mergePhase==="flash"||mergePhase==="result"?"active flash":""} ${mergePhase==="result"?"show-result":""}`}>
        <div className="merge-flash-boom"/>
        <div className="merge-core">
          <div className="merge-fusion-orb"/><div className="merge-fusion-ring"/>
          <div className="merge-card left clash-player-anim"><div className="merge-card-inner"><div className="merge-card-label">YOU</div><div className="text-6xl relative z-10">{p.avatar}</div><div className="font-cinzel mt-4 relative z-10">{p.name}</div></div></div>
          <div className="merge-card right clash-opponent-anim"><div className="merge-card-inner"><div className="merge-card-label">OPPONENT</div><div className="text-6xl relative z-10">{o.avatar}</div><div className="font-cinzel mt-4 relative z-10">{o.name}</div></div></div>
          <div className="merge-white"><div className="merge-winner"><div className="merge-fused-icons">{result?.roundWinner==="PLAYER"?p.avatar:result?.roundWinner==="OPPONENT"?o.avatar:"✦"}</div>{mergePhase==="result"&&<><small>{t.round} {game.round}</small><strong>{result?.roundWinner==="PLAYER"?t.roundWin:result?.roundWinner==="OPPONENT"?t.roundLose:t.draw}</strong><em>{result?.roundWinner==="PLAYER"?p.name:result?.roundWinner==="OPPONENT"?o.name:`${p.name} • ${o.name}`}</em></>}</div></div>
        </div>
        {mergePhase==="result"&&<div className={`merge-fusion-glow ${result?.roundWinner==="PLAYER"?"glow-win":result?.roundWinner==="OPPONENT"?"glow-loss":"glow-draw"}`}>{result?.roundWinner==="PLAYER"?t.roundWin:result?.roundWinner==="OPPONENT"?t.roundLose:t.draw}</div>}
      </div>}'''

replacements.append((old_merge, new_merge))

missing = []
for a,b in replacements:
    if a not in text:
        missing.append(a[:120].replace("\n"," / "))
    else:
        text = text.replace(a,b,1)

if missing:
    print("MISSING", len(missing))
    for m in missing:
        print("---", m)
    raise SystemExit(1)

html_path.write_text(text, encoding="utf-8")
print("OK patched", html_path, "chars", len(text))
