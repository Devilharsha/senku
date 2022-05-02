on_string = """
══════✭✭✭✭✭═══════

𝘾𝙊𝙉𝙉𝙀𝘾𝙏𝙀𝘿 𝙏𝙊 𝙇𝙊𝙑𝙀𝙇𝙔 𝙎𝙔𝙎𝙏𝙀𝙈 

══════✭✭✭✭✭═══════

     「♡ 𝙐𝙎𝙀𝙍 𝙄𝙉𝙁𝙊 ♡」

♡ 𝙉𝘼𝙈𝙀 -   {name}

♡ 𝙍𝘼𝙉𝙆 -  {Enforcer} 

♡ 𝙑𝙀𝙍𝙄𝙁𝙄𝙀𝘿 𝙐𝙎𝙀𝙍 ✓
"""

# Make sure not to change these too much
# If you still wanna change it change the regex too
scan_request_string = """
╒═══「 $SCAN 」
Lovely X Scan request!
**♡ Enforcer:** {enforcer} 
**♡ User scanned:** {spammer}
**♡ Reason:** `{reason}`
**♡ Scan Source:** {chat}
**♡ Target Message:** `{message}`
"""
forced_scan_string = """
╒═══「 $FORCED 」
**♡ Inspector:** {ins}
**♡ Target:** {spammer}
**♡ Reason:** `{reason}`
**♡ Scan Source:** {chat}
**♡ Target Message:** `{message}`
"""

reject_string = """
╒═══「 $REJECTED 」
**Crime Coefficient:** `Under 100`
Not a target for enforcement action. 
The trigger will be locked.
"""

proof_string = """
**Case file for** - {proof_id} :
┣━**Reason**: {reason}
┗━**Message**
         ┣━[Nekobin]({paste})
         ┗━[DelDog]({url})"""

scan_approved_string = """
╒═══「 #LethalEliminator 」
**♡ Target User:** {scam}
**♡ Crime Coefficient:** `Over 300`
**♡ Reason:** `{reason}`
**♡ Enforcer:** `{enforcer}`
**♡ Case Number:** `{proof_id}`
"""

bot_gban_string = """
╒═══「 #DestroyDecomposer 」
**♡ Enforcer:** `{enforcer}`
**♡ Target User:** {scam}
**♡ Reason:** `{reason}`
"""

# https://psychopass.fandom.com/wiki/Crime_Coefficient_(Index)
# https://psychopass.fandom.com/wiki/The_Dominator
