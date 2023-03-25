import discord
import main
import datetime
from discord.ext import commands
from config import *

restocks_product_url = main.restocks_product_url
stockx_product_url = main.stockx_product_url
sneakit_product_url = main.sneakit_product_url
hypeboost_product_url = main.hypeboost_product_url
goat_url = main.product_url_goat
product_title = main.product_title
product_img = main.restocks_product_img
restocks_stock = main.restocks_stock
hypeboost_stock = main.hypeboost_stock
sneakit_stock = main.sneakit_stock
restocks_stock_payout = main.restocks_stock_payout
hypeboost_prices_payout = main.hypeboost_prices_payout
paypal_fees_price = main.paypal_fees
paypal_fees_only = main.paypal_fees_2
paypal_fees_to_price = main.paypal_fees_3
goat_product_img = main.product_img_goat
goat_prodcut_title = main.product_title_goat
goat_sizes_prices = main.product_sizes_goat

required_variables = ['TOKEN', 'CHANNEL_NAME', 'COMMAND_PREFIX_ALL', 'COMMAND_PREFIX_RESTOCKS',
                      'COMMAND_PREFIX_HYPEBOOST', 'COMMAND_PREFIX_SNEAKIT', 'COMMAND_PREFIX_RESTOCKS_PAYOUT',
                      'COMMAND_PREFIX_HYPEBOOST_PAYOUT', 'COMMAND_PREFIX_PAYOUT_ALL', 'SIZE_CHART_PREFIX',
                      'PAY_PAL_PREFIX', 'COMMAND_LIST', 'URL_PREFIX', 'COMMAND_PREFIX_GOAT']

for variable in required_variables:
    if not globals().get(variable):
        raise ValueError(f"The {variable} was not included in the config.py file")

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
        goat_stock_output = goat_sizes_prices(SKU)

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
        embed.add_field(
          name="GOAT Prices:",
          value=goat_stock_output,
          inline=True
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

    elif message.content.startswith(COMMAND_PREFIX_GOAT):
      await message.channel.send("Scraping GOAT...")

      if COMMAND_PREFIX_GOAT in message_content:
        SKU_raw = message_content.replace(COMMAND_PREFIX_GOAT, '')
        SKU = SKU_raw.replace(" ", "")

        product_title_output = goat_prodcut_title(SKU)
        product_img_output = goat_product_img(SKU)
        hypeboost_product_url_output = hypeboost_product_url(SKU)
        restocks_product_url_output = restocks_product_url(SKU)
        stockx_product_url_output = stockx_product_url(SKU)
        sneakit_product_url_output = sneakit_product_url(SKU)
        goat_url_output = goat_url(SKU)
        goat_product_output = goat_sizes_prices(SKU)

        embed = discord.Embed(
          title=product_title_output,
          url=goat_url_output,
          color=0x11806a
        )
        embed.set_author(
          name="GOAT Scraper",
          url="https://twitter.com/jakobaio",
          icon_url= "https://play-lh.googleusercontent.com/XSe2IZfyHjzRL0qSqTOuA4zgr-Ha6oiCMGcOlOvPqcKVaeLIhBNmU3BoUzyIfEISUZQ=w240-h480-rw"
        )
        embed.set_thumbnail(
          url=product_img_output
        )
        embed.add_field(
          name="GOAT Prices:",
          value=goat_product_output,
          inline=True
        )
        embed.add_field(
          name="Open Product on:",
          value=f"[[StockX]]({stockx_product_url_output})      " f"[[GOAT]]({goat_url_output})      " f"[[Restocks]]({restocks_product_url_output})      " f"[[Hypeboost]]({hypeboost_product_url_output})      " f"[[Sneakit]]({sneakit_product_url_output})      ",
          inline=False
        )
        embed.set_footer(
          text=f"Developed by JakobAIO      |      GOAT.com Scraper      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
        )

        await message.channel.send(embed=embed)
        print('GOAT Scraping Successful!')

    elif message.content.startswith(PAY_PAL_PREFIX):
      await message.channel.send("Scraping PayPal fees...")

      if PAY_PAL_PREFIX in message_content:
        price_raw = message_content.replace(PAY_PAL_PREFIX, '')
        price_raw1 = price_raw.replace("€", "")
        price = price_raw1
        paypal_fees_price_output = paypal_fees_price(price)
        paypal_fees_only_output = paypal_fees_only(price)
        paypal_fees_to_price_output = paypal_fees_to_price(price)
        embed = discord.Embed(
          title="PayPal fees",
          url="https://www.paypal.com/de/home",
          color=0x3498db
        )
        embed.set_author(
          name="PayPal",
          url="https://twitter.com/jakobaio",
          icon_url= "https://cdn-icons-png.flaticon.com/512/2504/2504802.png"
          )
        embed.set_thumbnail(
          url="https://cdn-icons-png.flaticon.com/512/888/888871.png"
        )
        embed.add_field(
          name="Your input amount:",
          value=price + "€",
          inline=False
        )
        embed.add_field(
          name="PayPal fees:",
          value=paypal_fees_only_output,
          inline=True
        )
        embed.add_field(
          name="Price after fees:",
          value=paypal_fees_price_output,
          inline=False
        )
        embed.add_field(
          name="PayPal fees added:",
          value=paypal_fees_to_price_output,
          inline=True
        )
        embed.set_footer(
          text=f"Developed by JakobAIO      |      PayPal Fees Calculator      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
        )
        await message.channel.send(embed=embed)
        print('PayPal Fees Scraping Successful!')

    elif message.content.startswith(URL_PREFIX):
      await message.channel.send("Scraping product URL's...")

      if URL_PREFIX in message_content:
        SKU_raw = message_content.replace(URL_PREFIX, '')
        SKU = SKU_raw.replace(" ", "")
        hypeboost_product_url_output = hypeboost_product_url(SKU)
        restocks_product_url_output = restocks_product_url(SKU)
        stockx_product_url_output = stockx_product_url(SKU)
        sneakit_product_url_output = sneakit_product_url(SKU)
        goat_url_output = goat_url(SKU)
        product_title_output = product_title(SKU)
        product_img_output = product_img(SKU,restocks_product_url)
        embed = discord.Embed(
          title=product_title_output,
          url="https://twitter.com/jakobaio",
          color=0x95a5a6
        )
        embed.set_author(
          name="URL Scraper",
          url="https://twitter.com/jakobaio",
          icon_url= "https://cdn.pixabay.com/photo/2016/03/21/23/25/link-1271843_960_720.png"
          )
        embed.set_thumbnail(
          url=product_img_output
        )
        embed.add_field(
          name="",
          value=f"[[StockX]]({stockx_product_url_output})",
          inline=False
        )
        embed.add_field(
          name="",
          value=f"[[Restocks]]({restocks_product_url_output})",
          inline=False
        )
        embed.add_field(
          name="",
          value=f"[[GOAT]]({goat_url_output})",
          inline=False
        )
        embed.add_field(
          name="",
          value=f"[[Hypeboost]]({hypeboost_product_url_output})",
          inline=False
        )
        embed.add_field(
          name="",
          value=f"[[Sneakit]]({sneakit_product_url_output})",
          inline=False
        )
        embed.set_footer(
          text=f"Developed by JakobAIO      |      PayPal Fees Calculator      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
        )
        await message.channel.send(embed=embed)
        print('Scraped URLs')

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

    elif message.content.startswith(SIZE_CHART_PREFIX):
      await message.channel.send("***Size Chart:***")
      with open('nike_size_chart.png', 'rb') as f:
        file = discord.File(f)
        await message.channel.send(file=file)
        print("Size chart send!")

    elif message.content.startswith(COMMAND_LIST):
      if COMMAND_LIST in message_content:
        prefixes = {
            "AIO Scraper": COMMAND_PREFIX_ALL,
            "GOAT Scraper": COMMAND_PREFIX_GOAT,
            "Restocks-Scraper": COMMAND_PREFIX_RESTOCKS,
            "Hypeboost-Scraper": COMMAND_PREFIX_HYPEBOOST,
            "Sneakit-Scraper": COMMAND_PREFIX_SNEAKIT,
            "AIO Payout Scraper": COMMAND_PREFIX_PAYOUT_ALL,
            "Restocks-Payout Scraper": COMMAND_PREFIX_RESTOCKS_PAYOUT,
            "Hypeboost-Payout Scraper": COMMAND_PREFIX_HYPEBOOST_PAYOUT,
            "Size Chart": SIZE_CHART_PREFIX,
            "PayPal Fees Calculator": PAY_PAL_PREFIX,
            "Command list": COMMAND_LIST,
            "All product url's": URL_PREFIX
        }

        commands = "\n".join([f"{key}: {value}" for key, value in prefixes.items()])
        message_text = f"\n{commands}"

        embed = discord.Embed(
            title="Command List",
            url="https://twitter.com/jakobaio",
            color=0x11806a
          )
        embed.set_author(
            name="Scraper commands",
            url="https://twitter.com/jakobaio",
            icon_url= "https://i.imgur.com/mtt9JCN.png"
            )
        embed.set_thumbnail(
            url="https://cdn-icons-png.flaticon.com/512/7546/7546214.png"
          )
        embed.add_field(
            name="Here are the commands:",
            value=message_text,
            inline=True
          )
        embed.add_field(
            name="How to use:",
            value=f"Example: {COMMAND_PREFIX_ALL} DD1503-101",
            inline=False
          )
        embed.set_footer(
            text=f"Developed by JakobAIO      |      Command list      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
          )
        await message.channel.send(embed=embed)
        print("Command list send!")

    elif message.content.startswith("$"):
      await message.channel.send("***Wrong command unfortunatly!***")
      print("False command used!")
      prefixes = {
          "AIO Scraper": COMMAND_PREFIX_ALL,
          "GOAT Scraper": COMMAND_PREFIX_GOAT,
          "Restocks-Scraper": COMMAND_PREFIX_RESTOCKS,
          "Hypeboost-Scraper": COMMAND_PREFIX_HYPEBOOST,
          "Sneakit-Scraper": COMMAND_PREFIX_SNEAKIT,
          "AIO Payout Scraper": COMMAND_PREFIX_PAYOUT_ALL,
          "Restocks-Payout Scraper": COMMAND_PREFIX_RESTOCKS_PAYOUT,
          "Hypeboost-Payout Scraper": COMMAND_PREFIX_HYPEBOOST_PAYOUT,
          "Size Chart": SIZE_CHART_PREFIX,
          "PayPal Fees Calculator": PAY_PAL_PREFIX,
          "Command list": COMMAND_LIST,
          "All product url's": URL_PREFIX
      }

      commands = "\n".join([f"{key}: {value}" for key, value in prefixes.items()])
      message_text = f"\n{commands}"

      embed = discord.Embed(
          title="False command used!",
          url="https://twitter.com/jakobaio",
          color=0xe74c3c
        )
      embed.set_author(
          name="Scraper command error!",
          url="https://twitter.com/jakobaio",
          icon_url= "https://i.imgur.com/mtt9JCN.png"
          )
      embed.set_thumbnail(
          url="https://cdn.pixabay.com/photo/2013/04/01/09/21/attention-98513_960_720.png"
        )
      embed.add_field(
          name="Here is a command list:",
          value=message_text,
          inline=True
        )
      embed.add_field(
          name="How to use:",
          value=f"Example: {COMMAND_PREFIX_ALL} DD1503-101",
          inline=False
        )
      embed.set_footer(
          text=f"Developed by JakobAIO      |      Command list      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
        )
      await message.channel.send(embed=embed)
      print("Command list send!")

bot.run(TOKEN)
