
from collections import OrderedDict
import telebot
from telebot import types


TOKEN = ''

bot = telebot.TeleBot(TOKEN)

def listener(messages):
  for m in messages:
    cid = m.chat.id
    uid= m.from_user.id
    usm = m.from_user.username
    if m.content_type == 'text':
      print ("[" + "@" + str(usm) + " " + str(uid) + " in " + str(cid) + "]: " + m.text)
       
bot.set_update_listener(listener)


@bot.message_handler(commands=['commands'])
def command_commands(m):
  cid = m.chat.id
  nds = '/3ds - .cia, GBATemp, 3dsISO, emunand... all in one here.'
  icl = '/icl - ICLadders!'
  pokemon = '/pokemon - All about Pokémon games'
  optc = '/optc - Do you even Zephyr?'
  heroes = '/heroes - Hotslogs, HeroGG, BanChamps...'
  bot.reply_to(m,'{}\n{}\n{}\n{}\n{}\n'.format(nds, icl, pokemon, optc, heroes), disable_web_page_preview=True)
  
  
  



@bot.message_handler(commands=['3ds'])
def command_3ds(m):
  cid = m.chat.id
  nds1 = '<a href="https://gbatemp.net/threads/release-yet-another-theme-application-plus-yata-3ds-theme-editor.393355/">Custom Theme Creator (Yata+)</a>'
  nds2 = '<a href="https://3dsthem.es/">3DSThem</a>'
  nds3 = '<a href="http://www.3dsiso.com/">3DS ISO</a>'
  nds4 = '<a href="https://www.reddit.com/r/3dshacks/">The 3DS Hacks Subreddit</a>'
  nds5 = '<a href="https://gbatemp.net/threads/release-howling-theme-tool-create-your-own-cia-theme-packages-with-custom-and-official-themes.401081/">Howling Theme Tool (.cia theme\'s pack)</a>'
  nds6 = '<a href="http://www.3dsdb.com/">3DS Database</a>'
  nds7 = '<a href="https://github.com/Plailect/Guide/wiki">ARM9</a>'
  nds8 = '<a href="https://gbatemp.net/threads/menuhax-2-0-custom-main-screen-images.401528/">MenuHax 2.0 Custom Main-Screen Images</a>'
  nds9 = '<a href="https://gbatemp.net/threads/wip-phbank-pok%C3%A9mon-homebrew-bank.398718">Pokémon Homebrew Bank</a>'
  nds10 = '<a href="https://mega.nz/#F!BNBFCZyA!9NSm2MDyxpbUqeBXIuooEQ">EUR Themes (286)</a>'
  nds11 = '<a href="http://www.3dsiso.com/cia-downloads/262774-multiup-games-hackroms-legits-cia-eur-usa-jap-rf-02-26-2016-a.html">Asia81 CIA</a>'
  nds12 = '<a href="http://www.3dsiso.com/cia-downloads/262818-multi-moodys-cia-downloads-pokemon-picross-added-3-12-2015-a.html">Moody CIA</a>'
  nds13 = '<a href="http://www.3dsiso.com/cia-downloads/271578-megathread-3ds-eshop-roms-converted-cia-format-1fichier.html">AlvRo CIA</a>'
  nds14 = '<a href="http://www.3dsiso.com/cia-format-gba-nes-gbc-gb-snes-virtual-console-games/263172-3ds-custom-virtual-console-nes-gb-gbc-gba-gen-md-games-595-games.html">3DS Custom VC (NES, GB, GBC, GBA, GEN/MD)</a>'
  nds15 = '<a href="http://gbatemp.net/threads/r4-stage2-twl-flashcart-launcher-and-perhaps-other-cards-soon%E2%84%A2.416434/">R4 Stage2 TWL Flashcart Launcher</a>'
  nds16 = '<a href="http://gbatemp.net/threads/release-a9lh-bootanim9-custom-boot-animations.420202/">Custom boot animation /w A9LH</a>'
  #nds7 = '<a href="URL">Texto</a>'
  bot.reply_to(m,'{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(nds1, nds2, nds3, nds4, nds5, nds6, nds7, nds8, nds9, nds10,nds11,nds12,nds13,nds14,nds15,nds16), parse_mode="HTML", disable_web_page_preview=True)

@bot.message_handler(commands=['icl'])
def command_icl(m):
  cid = m.chat.id
  icl1 = '<a href="https://www.icladders.com/">ICL Home Page</a>'
  #nds3 = '<a href="URL">Texto</a>'
  bot.reply_to(m,'{}'.format(icl1), parse_mode="HTML", disable_web_page_preview=True)

@bot.message_handler(commands=['pokemon'])
def command_pokemon(m):
  cid = m.chat.id
  pkmn1 = '<a href="http://www.smogon.com/">Smogon University</a>'
  pkmn2 = '<a href="http://www.forocoches.com/foro/showthread.php?p=221965540">Plataforma Pokémon - Séptima Generación - VOL LXVII [Pokémon Sol y Pokémon Luna]</a>'
  pkmn3 = '<a href="http://www.forocoches.com/foro/showthread.php?p=223364230">Liga Pokémon Forocoches</a>'
  #nds3 = '<a href="URL">Texto</a>'
  bot.reply_to(m,'{}\n{}\n{}'.format(pkmn1,pkmn2,pkmn3), parse_mode="HTML", disable_web_page_preview=True)

@bot.message_handler(commands=['optc'])
def command_optc(m):
  cid = m.chat.id
  optc1 = '<a href="http://optc-db.github.io/">OPTC Database Stuff</a>'
  #nds3 = '<a href="URL">Texto</a>'
  bot.reply_to(m,'{}'.format(optc1), parse_mode="HTML", disable_web_page_preview=True)

@bot.message_handler(commands=['heroes'])
def command_heroes(m):
  cid = m.chat.id
  heroes1 = '<a href="http://www.hotslogs.com/">Hotslogs</a>'
  heroes2 = '<a href="http://www.hero.gg/">HeroGG</a>'
  #nds3 = '<a href="URL">Texto</a>'
  bot.reply_to(m,'{}\n{}'.format(heroes1, heroes2), parse_mode="HTML", disable_web_page_preview=True)
  

#############################################

#<a href="URL">inlineURL</a>\n
 
bot.skip_pending = True	
bot.polling(none_stop=True)