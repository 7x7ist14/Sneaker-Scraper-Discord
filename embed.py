import discord
import main
import datetime
from discord.ext import commands
from config import TOKEN, CHANNEL_NAME, COMMAND_PREFIX_ALL, COMMAND_PREFIX_RESTOCKS, COMMAND_PREFIX_HYPEBOOST, COMMAND_PREFIX_SNEAKIT, COMMAND_PREFIX_RESTOCKS_PAYOUT, COMMAND_PREFIX_HYPEBOOST_PAYOUT, COMMAND_PREFIX_PAYOUT_ALL

restocks_product_url = main.restocks_product_url
stockx_product_url = main.stockx_product_url
sneakit_product_url = main.sneakit_product_url
hypeboost_product_url = main.hypeboost_product_url
goat_url = main.goat_url
product_title = main.product_title
product_img = main.restocks_product_img
restocks_stock = main.restocks_stock
hypeboost_stock = main.hypeboost_stock
sneakit_stock = main.sneakit_stock
restocks_stock_payout = main.restocks_stock_payout
hypeboost_prices_payout = main.hypeboost_prices_payout


if not TOKEN:
    raise ValueError("The Bot-Token was not included in the config.py file")

if not CHANNEL_NAME:
    raise ValueError("The Channel-Name was not included in the config.py file")

if not COMMAND_PREFIX_ALL:
    raise ValueError("The Command-Prefix for AIO Scraper was not included in the config.py file")

if not COMMAND_PREFIX_RESTOCKS:
    raise ValueError("The Command-Prefix for Restocks Scraper was not included in the config.py file")

if not COMMAND_PREFIX_HYPEBOOST:
    raise ValueError("The Command-Prefix for Hypeboost Scraper was not included in the config.py file")

if not COMMAND_PREFIX_SNEAKIT:
    raise ValueError("The Command-Prefix for Sneakit Scraper was not included in the config.py file")

if not COMMAND_PREFIX_RESTOCKS_PAYOUT:
    raise ValueError("The Command-Prefix for Restocks Payout Scraper was not included in the config.py file")

if not COMMAND_PREFIX_HYPEBOOST_PAYOUT:
    raise ValueError("The Command-Prefix for Hypeboost Payout Scraper was not included in the config.py file")

if not COMMAND_PREFIX_PAYOUT_ALL:
    raise ValueError("The Command-Prefix for AIO Payout Scraper was not included in the config.py file")

bot = commands.Bot(command_prefix=COMMAND_PREFIX_ALL, intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Sneaker Scraper!'))
    print("Bot logged in!")


@bot.event
async def on_message(message):
  if message.author == bot.user:
      return
  message_content = message.content.lower()

  if message.channel.name == CHANNEL_NAME:
    if message.content.startswith(COMMAND_PREFIX_ALL):
      await message.channel.send("Scraping AIO...")

      if COMMAND_PREFIX_ALL in message_content:
        SKU_raw = message_content.replace(COMMAND_PREFIX_ALL, '')
        SKU = SKU_raw.replace(" ", "")

        product_title_output = product_title(SKU)
        product_img_output = product_img(SKU,restocks_product_url)
        hypeboost_product_url_output = hypeboost_product_url(SKU)
        restocks_product_url_output = restocks_product_url(SKU)
        stockx_product_url_output = stockx_product_url(SKU)
        sneakit_product_url_output = sneakit_product_url(SKU)
        goat_url_output = goat_url(SKU)
        restocks_stock_output = restocks_stock(SKU)
        hypeboost_stock_output = hypeboost_stock(SKU)
        sneakit_stock_output = sneakit_stock(SKU)

        embed = discord.Embed(
          title=product_title_output,
          url=hypeboost_product_url_output,
          color=0xf1c40f
        )
        embed.set_author(
          name="AIO Scraper",
          url="https://twitter.com/jakobaio",
          icon_url= "https://i.imgur.com/mtt9JCN.png"
        )
        embed.set_thumbnail(
          url=product_img_output
        )
        embed.add_field(
          name="Hypeboost Prices:",
          value=hypeboost_stock_output,
          inline=True
        )
        embed.add_field(
          name="Restocks Prices:",
          value=restocks_stock_output,
          inline=True
        )
        embed.add_field(
          name="Sneakit Prices:",
          value=sneakit_stock_output,
          inline=True
        )
        embed.set_footer(
          text="Developed by Jakob.AIO"
        )
        embed.add_field(
          name="Open Product on:",
          value=f"[[StockX]]({stockx_product_url_output})      " f"[[Sneakit]]({sneakit_product_url_output})      " f"[[Restocks]]({restocks_product_url_output})      " f"[[Hypeboost]]({hypeboost_product_url_output})      " f"[[GOAT]]({goat_url_output})      ",
          inline=False
        )
        embed.set_footer(
          text=f"Developed by JakobAIO      |      AIO Scraper      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
        )

        await message.channel.send(embed=embed)
        print('AIO Scraping Successful!')

    elif message.content.startswith(COMMAND_PREFIX_RESTOCKS):
      await message.channel.send("Scraping Restocks...")

      if COMMAND_PREFIX_RESTOCKS in message_content:
        SKU_raw = message_content.replace(COMMAND_PREFIX_RESTOCKS, '')
        SKU = SKU_raw.replace(" ", "")
        product_title_output = product_title(SKU)
        product_img_output = product_img(SKU,restocks_product_url)
        hypeboost_product_url_output = hypeboost_product_url(SKU)
        restocks_product_url_output = restocks_product_url(SKU)
        stockx_product_url_output = stockx_product_url(SKU)
        sneakit_product_url_output = sneakit_product_url(SKU)
        goat_url_output = goat_url(SKU)
        restocks_stock_output = restocks_stock(SKU)

        embed = discord.Embed(
          title=product_title_output,
          url=restocks_product_url_output,
          color=0x546e7a
        )
        embed.set_author(
          name="Restocks Scraper",
          url="https://twitter.com/jakobaio",
          icon_url= "https://www.reklamation24.de/img/content/marken/original_6710_1.gif"
          )
        embed.set_thumbnail(
          url=product_img_output
        )
        embed.add_field(
          name="Restocks Prices:",
          value=restocks_stock_output,
          inline=True
        )
        embed.set_footer(
          text="Developed by Jakob.AIO"
        )
        embed.add_field(
          name="Open Product on:",
          value=f"[[StockX]]({stockx_product_url_output})      " f"[[Sneakit]]({sneakit_product_url_output})      " f"[[Restocks]]({restocks_product_url_output})      " f"[[Hypeboost]]({hypeboost_product_url_output})      " f"[[GOAT]]({goat_url_output})      ",
          inline=False
        )
        embed.set_footer(
          text=f"Developed by JakobAIO      |      Restocks.net Scraper      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
        )

        await message.channel.send(embed=embed)
        print('Restocks Scraping Successful!')

    elif message.content.startswith(COMMAND_PREFIX_HYPEBOOST):
      await message.channel.send("Scraping Hypeboost...")

      if COMMAND_PREFIX_HYPEBOOST in message_content:
        SKU_raw = message_content.replace(COMMAND_PREFIX_HYPEBOOST, '')
        SKU = SKU_raw.replace(" ", "")
        product_title_output = product_title(SKU)
        product_img_output = product_img(SKU,restocks_product_url)
        hypeboost_product_url_output = hypeboost_product_url(SKU)
        restocks_product_url_output = restocks_product_url(SKU)
        stockx_product_url_output = stockx_product_url(SKU)
        sneakit_product_url_output = sneakit_product_url(SKU)
        goat_url_output = goat_url(SKU)
        hypeboost_stock_output = hypeboost_stock(SKU)

        embed = discord.Embed(
          title=product_title_output,
          url=hypeboost_product_url_output,
          color=0x206694
        )
        embed.set_author(
          name="Hypeboost Scraper",
          url="https://twitter.com/jakobaio",
          icon_url= "https://consumersiteimages.trustpilot.net/business-units/610a587f2b259a001d8d9b5f-198x149-1x.jpg"
        )
        embed.set_thumbnail(
          url=product_img_output
        )
        embed.add_field(
          name="Hypeboost Prices:",
          value=hypeboost_stock_output,
          inline=True
        )
        embed.set_footer(
          text="Developed by Jakob.AIO"
        )
        embed.add_field(
          name="Open Product on:",
          value=f"[[StockX]]({stockx_product_url_output})      " f"[[Sneakit]]({sneakit_product_url_output})      " f"[[Restocks]]({restocks_product_url_output})      " f"[[Hypeboost]]({hypeboost_product_url_output})      " f"[[GOAT]]({goat_url_output})      ",
          inline=False
        )
        embed.set_footer(
          text=f"Developed by JakobAIO      |      Hypeboost.com Scraper      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
        )

        await message.channel.send(embed=embed)
        print('Hypeboost Scraping Successful!')

    elif message.content.startswith(COMMAND_PREFIX_SNEAKIT):
      await message.channel.send("Scraping Sneakit...")

      if COMMAND_PREFIX_SNEAKIT in message_content:
        SKU_raw = message_content.replace(COMMAND_PREFIX_SNEAKIT, '')
        SKU = SKU_raw.replace(" ", "")
        product_title_output = product_title(SKU)
        product_img_output = product_img(SKU,restocks_product_url)
        hypeboost_product_url_output = hypeboost_product_url(SKU)
        restocks_product_url_output = restocks_product_url(SKU)
        stockx_product_url_output = stockx_product_url(SKU)
        sneakit_product_url_output = sneakit_product_url(SKU)
        goat_url_output = goat_url(SKU)
        sneakit_stock_output = hypeboost_stock(SKU)

        embed = discord.Embed(
          title=product_title_output,
          url=sneakit_product_url_output,
          color=0x95a5a6
        )
        embed.set_author(
          name="Sneakit Scraper",
          url="https://twitter.com/jakobaio",
          icon_url= "https://consumersiteimages.trustpilot.net/business-units/630e4bd7744ce9c5e2e2fc4e-198x149-1x.jpg"
        )
        embed.set_thumbnail(
          url=product_img_output
        )
        embed.add_field(
          name="Sneakit Prices:",
          value=sneakit_stock_output,
          inline=True
        )
        embed.set_footer(
          text="Developed by Jakob.AIO"
        )
        embed.add_field(
          name="Open Product on:",
          value=f"[[StockX]]({stockx_product_url_output})      " f"[[Sneakit]]({sneakit_product_url_output})      " f"[[Restocks]]({restocks_product_url_output})      " f"[[Hypeboost]]({hypeboost_product_url_output})      " f"[[GOAT]]({goat_url_output})      ",
          inline=False
        )
        embed.set_footer(
          text=f"Developed by JakobAIO      |      Sneakit.com Scraper      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
        )

        await message.channel.send(embed=embed)
        print('Sneakit Scraping Successful!')

    elif message.content.startswith(COMMAND_PREFIX_PAYOUT_ALL):
      await message.channel.send("Scraping Payout AIO...")

      if COMMAND_PREFIX_PAYOUT_ALL in message_content:
        SKU_raw = message_content.replace(COMMAND_PREFIX_PAYOUT_ALL, '')
        SKU = SKU_raw.replace(" ", "")

        product_title_output = product_title(SKU)
        product_img_output = product_img(SKU,restocks_product_url)
        hypeboost_product_url_output = hypeboost_product_url(SKU)
        restocks_product_url_output = restocks_product_url(SKU)
        stockx_product_url_output = stockx_product_url(SKU)
        sneakit_product_url_output = sneakit_product_url(SKU)
        goat_url_output = goat_url(SKU)
        hypeboost_prices_payout_output = hypeboost_prices_payout(SKU)
        restocks_prices_payout_output = restocks_stock_payout(SKU)

        embed = discord.Embed(
          title=product_title_output,
          url=hypeboost_product_url_output,
          color=0x7289da
        )
        embed.set_author(
          name="Payout AIO Scraper",
          url="https://twitter.com/jakobaio",
          icon_url= "https://i.imgur.com/mtt9JCN.png"
        )
        embed.set_thumbnail(
          url=product_img_output
        )
        embed.add_field(
          name="Hypeboost Payout Prices:",
          value=hypeboost_prices_payout_output,
          inline=True
        )
        embed.add_field(
          name="Restocks Payout Prices:",
          value=restocks_prices_payout_output,
          inline=True
        )
        embed.set_footer(
          text="Developed by Jakob.AIO"
        )
        embed.add_field(
          name="Open Product on:",
          value=f"[[StockX]]({stockx_product_url_output})      " f"[[Sneakit]]({sneakit_product_url_output})      " f"[[Restocks]]({restocks_product_url_output})      " f"[[Hypeboost]]({hypeboost_product_url_output})      " f"[[GOAT]]({goat_url_output})      ",
          inline=False
        )
        embed.set_footer(
          text=f"Developed by JakobAIO      |      Payout AIO Scraper      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
        )

        await message.channel.send(embed=embed)
        print('Payout AIO Scraping Successful!')

    elif message.content.startswith(COMMAND_PREFIX_RESTOCKS_PAYOUT):
      await message.channel.send("Scraping Restocks Payout...")

      if COMMAND_PREFIX_RESTOCKS_PAYOUT in message_content:
        SKU_raw = message_content.replace(COMMAND_PREFIX_RESTOCKS_PAYOUT, '')
        SKU = SKU_raw.replace(" ", "")
        product_title_output = product_title(SKU)
        product_img_output = product_img(SKU,restocks_product_url)
        hypeboost_product_url_output = hypeboost_product_url(SKU)
        restocks_product_url_output = restocks_product_url(SKU)
        stockx_product_url_output = stockx_product_url(SKU)
        sneakit_product_url_output = sneakit_product_url(SKU)
        goat_url_output = goat_url(SKU)
        restocks_stock_payout_output = restocks_stock_payout(SKU)

        embed = discord.Embed(
          title=product_title_output,
          url=restocks_product_url_output,
          color=0x607d8b
        )
        embed.set_author(
          name="Restocks Payout Scraper",
          url="https://twitter.com/jakobaio",
          icon_url= "https://www.reklamation24.de/img/content/marken/original_6710_1.gif"
        )
        embed.set_thumbnail(
          url=product_img_output
        )
        embed.add_field(
          name="Restocks Payout Prices:",
          value=restocks_stock_payout_output,
          inline=True
        )
        embed.set_footer(
          text="Developed by Jakob.AIO"
        )
        embed.add_field(
          name="Open Product on:",
          value=f"[[StockX]]({stockx_product_url_output})      " f"[[Sneakit]]({sneakit_product_url_output})      " f"[[Restocks]]({restocks_product_url_output})      " f"[[Hypeboost]]({hypeboost_product_url_output})      " f"[[GOAT]]({goat_url_output})      ",
          inline=False
        )
        embed.set_footer(
          text=f"Developed by JakobAIO      |      Restocks Payout Scraper      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
        )

        await message.channel.send(embed=embed)
        print('Restocks Payout Scraping Successful!')

    elif message.content.startswith(COMMAND_PREFIX_HYPEBOOST_PAYOUT):
      await message.channel.send("Scraping Hypeboost Payout...")

      if COMMAND_PREFIX_HYPEBOOST_PAYOUT in message_content:
        SKU_raw = message_content.replace(COMMAND_PREFIX_HYPEBOOST_PAYOUT, '')
        SKU = SKU_raw.replace(" ", "")
        product_title_output = product_title(SKU)
        product_img_output = product_img(SKU,restocks_product_url)
        hypeboost_product_url_output = hypeboost_product_url(SKU)
        restocks_product_url_output = restocks_product_url(SKU)
        stockx_product_url_output = stockx_product_url(SKU)
        sneakit_product_url_output = sneakit_product_url(SKU)
        goat_url_output = goat_url(SKU)
        hypeboost_prices_payout_output = hypeboost_prices_payout(SKU)

        embed = discord.Embed(
          title=product_title_output,
          url=hypeboost_product_url_output,
          color=0x206694
        )
        embed.set_author(
          name="Hypeboost Payout Scraper",
          url="https://twitter.com/jakobaio",
          icon_url= "https://consumersiteimages.trustpilot.net/business-units/610a587f2b259a001d8d9b5f-198x149-1x.jpg"
          )
        embed.set_thumbnail(
          url=product_img_output
        )
        embed.add_field(
          name="Hypeboost Payout Prices:",
          value=hypeboost_prices_payout_output,
          inline=True
        )
        embed.set_footer(
          text="Developed by Jakob.AIO"
        )
        embed.add_field(
          name="Open Product on:",
          value=f"[[StockX]]({stockx_product_url_output})      " f"[[Sneakit]]({sneakit_product_url_output})      " f"[[Restocks]]({restocks_product_url_output})      " f"[[Hypeboost]]({hypeboost_product_url_output})      " f"[[GOAT]]({goat_url_output})      ",
          inline=False
        )
        embed.set_footer(
          text=f"Developed by JakobAIO      |      Hypeboost Payout Scraper      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
        )

        await message.channel.send(embed=embed)
        print('Hypeboost Payout Scraping Successful!')

    elif message.content.startswith("$"):
      await message.channel.send("Wrong command unfortunatly!")
      print("False command used!")

bot.run(TOKEN)
