from nsepython import nse_optionchain_scrapper
# from gtts import gTTS
# import pygame

# mytext= 'investment framework!'
# language='en'
# myobj=gTTS(text=mytext,lang=language,slow=False)
# myobj.save("IF.mp3")
# pygame.mixer.init()
# pygame.mixer.music.load("IF.mp3")
# pygame.mixer.music.play() 
data = nse_optionchain_scrapper("NIFTY")

spot_price = data["records"]["underlyingValue"]
# print("NIFTY Spot Price:", spot_price)  

nearest_strike = round(spot_price /50)*50
#print("Nearest Strike Price:", nearest_strike)

strike_range = [nearest_strike + i * 50 for i in range(-5, 6)]
print("Strike Range:", strike_range)

total_ce_volume = 0
total_pe_volume = 0
total_ce_invested = 0
total_pe_invested = 0

 
for entry in data["records"]["data"]: 
    if entry["strikePrice"] in strike_range:
        if "CE" in entry:
            ce_volume = entry["CE"].get("totalTradedVolume", 0)
            total_ce_volume += ce_volume
            total_ce_invested += (ce_volume * 75 * 1.2) / 10000

        if "PE" in entry:
            pe_volume = entry["PE"].get("totalTradedVolume", 0)
            total_pe_volume += pe_volume
            total_pe_invested += (pe_volume * 75 * 1.2) / 10000


print("Spot Price:", spot_price)
print("Nearest Strike:", nearest_strike)
print("Total CE Volume:", total_ce_volume)
print("Total PE Volume:", total_pe_volume)
print("Combined Volume:", total_ce_volume + total_pe_volume)

# Calculate the total invested amount
print("Total CE Invested Amount (in Cr):", total_ce_invested)
print("Total PE Invested Amount (in Cr):", total_pe_invested)


