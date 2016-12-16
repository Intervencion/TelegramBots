# -*- coding: utf-8 -*-

import os, sys

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


@bot.message_handler(commands=['start'])
def command_start(m): 
  bot.reply_to(m, "Welcome to @D3Builds\_Bot. Here, you'll see the most succesful builds for Diablo 3. Commands in /commands", parse_mode="Markdown")
  
@bot.message_handler(commands=['commands'])
def command_commands(m): 
  bot.reply_to(m,"/help - Do you need help?\n/barb - Check out Barbarian builds\n/crusader - Check out Crusader builds\n/wizard - Do some magic with Wizard builds\n/wd - Summon your pets with these Witch Doctor builds\n/dh - Pew pew pew arrow pew pew pew knife. *KNIFE?* Yes. Knife. Demon Hunter builds.\n/monk - Quins69's fav character. Monk builds Srs.\n/conquest - Builds and tips for S5 conquests", parse_mode="Markdown")
  
@bot.message_handler(commands=['help'])
def command_help(m): 
  bot.reply_to(m,'/start for Start, /commands for commands and /help for this.\nAh, @intervencion developed me.', parse_mode="Markdown")
  
@bot.message_handler(commands=['barb'])
def command_barb(m): 
  bot.reply_to(m,'<a href="http://www.diablofans.com/builds/69882-2-4-gr100-zdps-globe-barb-group">[2.4] [GR100+] zDPS GLOBE [group]</a>\n<a href="http://www.diablofans.com/builds/69851-raekor-barb-solo-grift-86">[2.4] [GR86+] Raekor [solo]</a>\n<a href="http://www.diablofans.com/builds/69910-2-4-gr85-earthquake-solo-group">[2.4] [Startbuild/GR85+] Earthquake [solo/group/TX]</a>\n<a href="http://www.diablofans.com/builds/69865-2-4-gr90-raekor-furious-charge">[2.4] [GR90+] Raekor Furious Charge [solo/group]</a>\n<a href="http://www.diablofans.com/builds/70865-barbarian-gr45-the-thrill-season-5-conquest">[2.4] [GR45+] The Thrill [TX]</a>', parse_mode="HTML")

@bot.message_handler(commands=['crusader'])
def command_crusader(m): 
  bot.reply_to(m,'<a href="http://www.diablofans.com/builds/69853-2-4-gr90-lon-bombardment">[2.4] [GR90+] LoN Bombardment [solo]</a>\n<a href="http://www.diablofans.com/builds/70026-2-4-gr90-lon-blessed-shield-group-solo">[2.4] [GR90+] LoN Blessed Shield [solo/group]</a>\n<a href="http://www.diablofans.com/builds/69887-2-4-gr87-invoker-punish">[2.4] [GR87+] Invoker Punish [solo]</a>\n<a href="http://www.diablofans.com/builds/53898-2-4-the-cannonball-be-your-teams-rift-guardian">[2.4] [GR??+] The Cannonball Pound [group]</a>\n<a href="http://www.diablofans.com/builds/71215-2-4-gr45-with-no-set-items-the-thrill-for">[2.4] [GR45+] The Thrill [TX]</a> <b>-</b> <a href="http://www.diablofans.com/builds/71190-thrill-conquest-thorns-build-recommendation">Variation</a>\n<a href="http://www.diablofans.com/builds/69919-2-4-fast-death-breath-farm">[2.4] [Startbuild] FAST Death Breath Farm [TX]</a>\n<a href="http://www.diablofans.com/builds/70029-2-4-phalanx-bowmen-bounties-t10">[2.4] [GR75+] Phalanx Bowmen [TX]</a>', parse_mode="HTML")

@bot.message_handler(commands=['wizard'])
def command_wizard(m): 
  bot.reply_to(m,'<a href="http://www.diablofans.com/builds/69867-2-4-gr100-delsere-energy-twister">[2.4] [GR100+] Delsere Energy Twister [group]</a>\n<a href="http://www.diablofans.com/builds/70097-2-4-gr89-lon-hydra-wizard">[2.4] [GR89+] LoN Hydra [solo/group]</a>\n<a href="http://www.diablofans.com/builds/69933-quin69-gr88-dmo-wizard-solo">[2.4] [GR88+] [Quin69] DMO [solo]</a>\n<a href="http://www.diablofans.com/builds/69890-2-4-gr88-delsere-arcane-orbit">[2.4] [GR88+] Delsere Arcane Orbit [solo]</a>\n<a href="http://www.diablofans.com/builds/70098-2-4-lon-explosive-blast">[2.4] [GR75+] LoN Explosive Blast [TX]</a>\n<a href="http://www.diablofans.com/builds/68417-2-4-t10-rift-and-bounty-farm-wowrasha-revisited">[2.3] [GR75+] Farm Wow\'Rasha Revisited [TX]</a>\n<a href="http://www.diablofans.com/builds/68019-2-4-tal-rasha-6p-disintegrate-meteor-rifts">[2.3] [GR75+] Tal Rasha 6p - Disintegrate Meteor Rifts Grinding [TX]</a>\n<a href="http://www.diablofans.com/builds/70681-flash-fire-wizard-t10-speed">[2.4] [GR??] Speed Flash Fire [TX]</a>\n<a href="http://www.diablofans.com/builds/70620-s5-torment-x-wohrasha-db-farming">[2.4] [GR??] WoH\'Rasha DB Farming [TX]</a>\n<a href="http://www.diablofans.com/builds/70658-2-4-gr45-the-thrill-fire-channeling-wiz">[2.4] [GR45+] The Thrill [TX]</a> <b>-</b> <a href="http://www.diablofans.com/builds/71157-s5-wizard-the-thrill-conquest">Variation</a>\n<a href="http://www.diablofans.com/builds/70102-2-4-t6-firebird-starter-build">[2.4] [Startbuild] Firebird Starter-Build [T6]</a>', parse_mode="HTML")

@bot.message_handler(commands=['wd'])
def command_wd(m): 
  bot.reply_to(m,'<a href="http://www.diablofans.com/builds/69876-2-4-gr100-wd-support-group">[2.4] [GR100+] Support [group]</a>\n<a href="http://www.diablofans.com/builds/69904-2-4-gr90-lon-firebat-gargantuam-group">[2.4] [GR90+] LoN Firebat Gargantuam [group]</a>\n<a href="http://www.diablofans.com/builds/69927-2-4-gr90-lon-dart-wd-group">[2.4] [GR90+] LoN Dart [group]</a>\n<a href="http://www.diablofans.com/builds/69903-2-4-jade-harvester-grift-80-solo">[2.4] [GR80+] Jade Harvester [solo]</a>\n<a href="http://www.diablofans.com/builds/68129-2-4-locust-swarm-pets-lon-fastest-t10-build">[2.4] [GR78+] Locust Swarm/Pets LoN [TX]</a>\n<a href="http://www.diablofans.com/builds/70442-lon-pet-doctor">[2.4] [GR??+] LoN Pet Doctor [solo]</a>\n<a href="http://www.diablofans.com/builds/71725-the-thrill-s5-wd">[2.4] [GR45+] The Thrill [TX]</a>\n<a href="http://www.diablofans.com/builds/70112-2-4-t6-jade-start-build">[2.4] [Startbuild] Jade START-Build [T6]</a>', parse_mode="HTML")

@bot.message_handler(commands=['dh'])
def command_dh(m): 
  bot.reply_to(m,'<a href="http://www.diablofans.com/builds/69873-2-4-gr92-dh-shadow-impale">[2.4] [GR92+] Shadow Impale [group]</a>\n<a href="http://www.diablofans.com/builds/69895-2-4-gr91-m6-chakram-aoe-group">[2.4] [GR91+] M6 Chakram AOE [group]</a>\n<a href="http://www.diablofans.com/builds/69834-2-4-gr-75-90-6p-shadow-updated-jan-19-group">[2.4] [GR85+] 6p Shadow Impale [solo/group]</a>\n<a href="http://www.diablofans.com/builds/67802-2-4-gr-75-80-nats-fok">[2.4] [GR85+] Nats FoK [solo/group]</a>\n<a href="http://www.diablofans.com/builds/69831-2-4-gr-75-80-cluster-marauder">[2.4] [GR82-90+] Cluster Marauder [solo/group]</a>\n<a href="http://www.diablofans.com/builds/69836-2-4-gr-75-80-nats-fok-fulminator">[2.4] [GR80+] Nats FoK / Fulminator [solo]</a>\n<a href="http://www.diablofans.com/builds/69833-2-4-gr-75-80-unhallowed-fire">[2.4] [GR80+] Unhallowed Fire [solo]</a>\n<a href="http://www.diablofans.com/builds/68396-2-4-grift-78-multishot-dh">[2.4] [GR78+] Multishot [solo]</a>\n<a href="http://www.diablofans.com/builds/70615-2-4-egf-m6-70-cold-marauder">[2.4] [GR70+] EGF M6. Cold Marauder [solo]</a>\n<a href="http://www.diablofans.com/builds/69830-2-4-fastest-torment-10-build-ue-fire">[2.4] [GR75+] UE Fire [TX]</a> <b>-</b> <a href="http://www.diablofans.com/builds/69843-2-4-bounty-farming-build-up-to-430-movement-speed">Variation for Bounties</a>\n<a href="http://www.diablofans.com/builds/69992-optimized-cold-ue-for-t10-2-3min-run">[2.4] [TX] Optimized Cold UE (2-3min/run) [solo/group]</a>\n<a href="http://www.diablofans.com/builds/70036-2-4-unhallowed-essence-torment-x-speed-farm">[2.4] [TX] UE Speed Farm [solo/group]</a>\n<a href="http://www.diablofans.com/builds/70779-the-thrill-demon-hunter-2-4-season-5">[2.4] [GR45+] The Thrill [TX]</a>\n<a href="http://www.diablofans.com/builds/70115-2-4-t6-impale-start-build">[2.4] [Startbuild] Impale START-Build [T6]</a>', parse_mode="HTML")

@bot.message_handler(commands=['monk'])
def command_monk(m): 
  bot.reply_to(m,'<a href="http://www.diablofans.com/builds/69908-2-4-gr100-loh-heal-monk-group">[2.4] [GR100+] LoH Heal [group]</a>\n<a href="http://www.diablofans.com/builds/69914-2-4-gr85-lon-flurry-ep">[2.4] [GR85+] LoN Flurry/EP [solo]</a>\n<a href="http://www.diablofans.com/builds/57405-quin69-gr71-ulianas-monk">[2.3] [GR78+] Quin69 Uliana\'s [TX]</a>\n<a href="http://www.diablofans.com/builds/68571-davloks-lazy-gong-mode-2-4-gold-sriracha-edition">[2.4] [GR75+] Gong Mode Farm [TX]</a>\n<a href="http://www.diablofans.com/builds/69922-one-punch-monk-t10-speed">[2.4] [GR75+]One Punch Monk [TX]</a>\n<a href="http://www.diablofans.com/builds/71700-the-thrill-s5-monk">[2.4] [GR45+] The Thrill [TX]</a>\n<a href="http://www.diablofans.com/builds/70107-2-4-t6-swk-wol-start-build">[2.4] [Startbuild] SWK WoL START-Build [T6]</a>', parse_mode="HTML")

@bot.message_handler(commands=['conquest'])
def command_conquest(m): 
  bot.reply_to(m,'<a href="http://us.battle.net/d3/en/forum/topic/16410411140">Avarice Conquest (50 Million gold streak)</a>\n<a href="http://eu.battle.net/d3/en/forum/topic/13604830636">Sprinter/Speed Racer Conquest. FAQ/Walkthrough</a> (<a href="http://www.diablofans.com/builds/30956-sprinter-speed-racer-build">Mage Build</a>)\n<a href="https://www.reddit.com/r/Diablo/comments/41ovbl/working_builds_that_cleared_gr45_with_no_set/">The Thrill (GR45 w/out Tier)</a>\n<a href="http://diablocaos.com/mazmorrasconjunto.php">Ubicación Mazmorras de Conjunto</a>', parse_mode="HTML")

#############################################

#<a href="URL">inlineURL</a>\n
 
	
bot.skip_pending = True	
bot.polling(none_stop=True)
