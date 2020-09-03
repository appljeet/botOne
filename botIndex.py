import requests
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')


# 156501
def disable():
    URL = 'https://reseller-api.netnut.io/api/aff/customer/156501/disable'

    data = {'loginEmail': 'nunihalawi@outlook.com', 'loginPassword': '25AtHW5q'}

    response = requests.post(url=URL, data=data)

    data = response.json()

    return data


def enable():
    URL = 'https://reseller-api.netnut.io/api/aff/customer/156501/enable'

    data = {'loginEmail': 'nunihalawi@outlook.com', 'loginPassword': '25AtHW5q'}

    response = requests.post(url=URL, data=data)

    data = response.json()

    return data


def getSpecificUsage():
    URL = 'https://reseller-api.netnut.io/api/aff/customers'

    parameters = {'loginEmail': 'nunihalawi@outlook.com', 'loginPassword': '25AtHW5q', 'customer_id': '156501'}

    response = requests.get(url=URL, params=parameters)

    data = response.json()

    return data


# get customers
def allCustomers():
    URL = 'https://reseller-api.netnut.io/api/aff/customers'

    parameters = {'loginEmail': 'nunihalawi@outlook.com', 'loginPassword': '25AtHW5q'}

    response = requests.get(url=URL, params=parameters)

    data = response.json()

    return data


# add customer
def newCustomer():
    URL = 'https://reseller-api.netnut.io/api/aff/customers'

    # ask for input from user for all these values
    data = {'loginEmail': 'nunihalawi@outlook.com',
            'loginPassword': '25AtHW5q',
            'customer_name': 'Abhijit Singh',
            'customer_dashboard_email': 'ironman7564@gmail.com',
            'customer_dashboard_pwd': 'iwantakoenigsegg',
            'customer_login_name': 'abhi',
            'customer_login_pwd': 'iwantagemera',
            'customer_country_code': 'us'}

    response = requests.post(url=URL, data=data)

    returnValue = response.json()

    return returnValue


@client.event
async def on_ready():
    print('Bot ready')


@client.command()
async def getAll(ctx):
    await ctx.send(allCustomers())


@client.command()
async def getMyUsage(ctx):
    await ctx.send(getSpecificUsage())


@client.command()
async def createCustomer(ctx):
    await ctx.send(newCustomer())


@client.command()
async def disableCustomer(ctx):
    await ctx.send(disable())


@client.command()
async def enableCustomer(ctx):
    await ctx.send(enable())


client.run('NzI4NDAzNTMyNzg0NTk5MTcx.Xv58Jg.9YR08XK-w8_Tos17MBhaILP-yUE')

# make an info command that lists all available commands to the user and what they do
