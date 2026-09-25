# -*- coding: utf-8 -*-
import re
from pathlib import Path

root = Path(r"C:\Users\Admin\Desktop\Omni Clash")
orig = (root / "omni_clash_backup_original.html").read_text(encoding="utf-8")
final = (root / "omni_clash_luxury_final.html").read_text(encoding="utf-8")

def funcs(src):
    names = set(re.findall(r'\bfunction\s+([A-Za-z0-9_]+)', src))
    names |= set(re.findall(r'\bconst\s+([A-Za-z0-9_]+)\s*=\s*(?:\([^)]*\)|[A-Za-z0-9_,\s]+)\s*=>', src))
    names |= set(re.findall(r'\bconst\s+([A-Za-z0-9_]+)\s*=\s*\(', src))
    return names

of, ff = funcs(orig), funcs(final)
missing_fn = sorted(of - ff)
extra_fn = sorted(ff - of)

# function keyword count
ofc = len(re.findall(r'\bfunction\s+', orig))
ffc = len(re.findall(r'\bfunction\s+', final))

const_keys = ["CREATOR_ID","CASE_PRICE","PVE_REWARD","PVP_REWARD","BOSS_REWARD","ONLINE_PAUSE_LIMIT",
              "CARDS_DATABASE","BOSS_DATABASE","TRANSLATIONS","rarityWeights","categoryConfig","APP_TITLE"]
states = ["lang","coins","unlocked","squad","collectionUniverse","shopTab","bossName","showCredits","showHelp",
          "pauseOpen","confirmExit","pauseLeft","incomingInvite","toast","caseState","settings","game","online",
          "screenState","mergePhase"]
net = ["ROOM_INFO","HOST_READY","HERO","HERO_ACK","ABILITY","ROUND_RESULT","RESET_ROUND","SURRENDER","PAUSE",
       "FORFEIT","RAID_READY","RAID_HERO","RAID_ABILITY","RAID_RESULT","BOSS_ABILITY","CREATOR_STATE","JOIN"]
stages = ["CARD_SELECT","ABILITY_SPLIT","RESOLVING","ROUND_RESULT","GAME_OVER"]
handlers = ["handleNet","handleSelectHero","handleSelectAbility","handleNextRound","calculateHit","resolveLocalRound",
            "executeLocalClash","scheduleMerge","resolvePvPRound","hostRoom","joinRoom","buyCard","openCase",
            "shareRoom","createRaid","startPve","AudioEngine","bindConn","destroyNetwork"]

def ru_en_keys(src):
    mru = re.search(r'ru:\{(.*?)\n  \},', src, re.S)
    men = re.search(r'en:\{(.*?)\n  \}', src, re.S)
    def keys(block):
        return set(re.findall(r'^\s*([A-Za-z0-9_]+):', block, re.M))
    return keys(mru.group(1)), keys(men.group(1))

oru, oen = ru_en_keys(orig)
fru, fen = ru_en_keys(final)

shop_ids = set(re.findall(r'\["(b10_|mvl_|dc_|creator_)', orig))
shop_ids_f = set(re.findall(r'\["(b10_|mvl_|dc_|creator_)', final))

checks = {
    "function keyword orig/final": (ofc, ffc),
    "missing functions": missing_fn,
    "missing constants": [k for k in const_keys if k not in final],
    "missing states": [k for k in states if f"[{k}," not in final and f"[{k}]" not in final and f"{k}," not in final],
    "missing net": [k for k in net if f'type:"{k}"' not in final and f'type==="{k}"' not in final],
    "missing stages": [k for k in stages if k not in final],
    "missing handlers": [k for k in handlers if k not in final],
    "ru keys missing": sorted(oru - fru),
    "en keys missing": sorted(oen - fen),
    "telegram": "Telegram" in final and "initDataUnsafe" in final and 'CREATOR_ID = "8358656894"' in final,
    "peerjs": "peerjs" in final.lower() and "new Peer" in final,
    "audio": "class AudioEngine" in final,
    "clash css": "clash-p" in final and "clash-player-anim" in final and "flash-boom" in final,
    "design tokens": all(x in final for x in ["--bg-deep","--emerald-soft","lux-btn-primary","rarity-creator"]),
    "single root": final.count('ReactDOM.createRoot') == 1,
    "card count orig/final": (orig.count('b10_'), final.count('b10_')),
}

print("=== STATIC REPORT ===")
for k,v in checks.items():
    print(f"{k}: {v}")
print("function names orig", len(of), "final", len(ff), "extra", extra_fn[:20])
print("ru keys orig", len(oru), "final", len(fru), "added", sorted(fru-oru))
print("en keys orig", len(oen), "final", len(fen), "added", sorted(fen-oen))
print("file sizes", len(orig), len(final))

# syntax-ish: unmatched braces in script
script = final.split('<script type="text/babel">',1)[1].rsplit('</script>',1)[0]
print("brace delta", script.count("{")-script.count("}"), "paren", script.count("(")-script.count(")"), "jsx ltgt skip")
print("TODO/FIXME/demo", "TODO" in final, "FIXME" in final, "CardShowcase" in final, "DEMO_CARD" in final)
