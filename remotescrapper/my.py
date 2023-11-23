import csv
from io import StringIO

data = """Abbey	  Abbey	     abbeyjoseph97@gmail.com	
Abdullahi Abdullahi abdullahimuhammad222555@gmail.com			
Abu-hafs  Usman	    usmusa7857@gmail.com			
Adaora	  A.        muokaadaora@gmail.com			
Adebanke	adebanketemiloluwa6@gmail.com			
Adedeji	Shittuadedeji10@gmail.com			
Adronok	oladunlere@yahoo.com			
Avg_Amoz	donjhyde@gmail.com			
Ayobami20	ayobamibabalola20@gmail.com			
Banjiola	banjiolaniyan123@gmail.com			
Beautiest42	beautiestemi@gmail.com			
Believe	dennisonbelievepaul@gmail.com			
Blazer	nyekweblessing23@gmail.com			
Chiazor	chiazordaniel317@gmail.com			
Crowned	adeboye.adesegun@gmail.com			
DAODU	daodutobi@gmail.com			
Dabeluchukwu	dabeluc@gmail.com			
Daniel 0	danielojo051@gmail.com			
Dauda Nazih	flamesk611@gmail.com			
Davies	iyiadedavid.09@gmail.com	Iyiade	David	
Demilade_dev	demmyomoba@gmail.com			
Elibe Emmanuel	elibeemmanuel46@gmail.com			
Emmanuel	emmanuelcharles0302@gmail.com			
F.Timson	timsonfoli@gmail.com			
Fatima	faroukqumar425@gmail.com			
Fist of God	babalolataiwo56@gmail.com			
Fola_Chi	Chijiokefolashade@gmail.com			
Habeeb	alisaannie37@gmail.com			
Hadeabass	abdulganiuabass9@gmail.com			
Hapsun	tolulopefolayemi@gmail.com			
ISABAL	isalabalogun@gmail.com			
Irijahben	irijahben@gmail.com			
Jayfred	chukwuka.frederick@gmail.com			
Jayjay Lee	leejayjay469@gmail.com			
Joshua S	olawalesolesi886@gmail.com			
Kehinde01	kehindeajewole17@gmail.com			
Kiloman	buttyrugged@gmail.com			
Kingsley	gloriousruins58@gmail.com			
Kobaro	kobarorosemary@gmail.com			
Legit Boss	abioyemichael395@gmail.com			
Lil smoke	wonuolaibironke@gmail.com			
Maighana	zmaighana@gmail.com			
Mayorarto	oyebolamayowa2016@gmail.com			
McMaggie	olaojopaul64@gmail.com			
Mercy	Oyekale hoyekemisola00@gmail.com
Mictop011	akinolamicheal303@gmail.com			
New wavr	Japhetidi128@gmail.com			
Oderinde Ayodeji	dreyypapi@gmail.com			
Okafor Franklin	okaforfrank254@gmail.com			
Olajuli	oshoolawale83@gmail.com			
Olalere Ayomide	ayo.olalere12@gmail.com			
Olanrewaju	adebayoolanrewaju85@gmail.com			
Olayinka	joaromasodun@gmail.com			
Olive	akindelebaliqis@gmail.com			
Oluwafemi MIchael	femmikel@gmail.com			
Oluwanisola	oluwasolaadebimpe@gmail.com			
Ovviebankz	forojo572@gmail.com			
Parish	parishsensei@ymail.com			
Rosemary Kowode	kowodebisola@gmail.com	
Rosybisy	Kowode@tecnokrafz.com			
Roxiegen	roxiegen@technokraftz.com			
Rukayat	olaitanrukayat62@gmail.com			
Sadeeq design	isahabubakaralhaji02@gmail.com			
Salaudeen	Salaudeenmumin9@gmail.com			
Samkeymoz	samkeymoz@gmail.com			
Shuaibu shamsu	shamsushuaibuabdullahi1@gmail.com			
Skeepj Ume	skeepj@hotmail.com		
Taiwo		taiwoisrealojomo@gmail.com			
Thales357	thalessalvador15@gmail.com			
Themydee	nifetemiboy@gmail.com			
Timothy	ogundipetimothy960@gmail.com			
Ufid Idris	idrisumar82@gmail.com			
Unique11 Awori aworiwouwu11@gmail.com			
Usman	Musa	uswaib131@gmail.com		
Whalexziano	asooresimeon@gmail.com			
Wiseman	lionelwese618@gmail.com			
Yayara	yayinaomi124@gmail.com			
Yayra	naomifrancis68@gmail.com			
Zahra kamshi	fatimasaidu3626@gmail.com			
Zanny	lawaladekemi06@gmail.com			
abdulazeez	ayobamiaziz95@gmail.com			
agboluajeazeez@gmail.com	agboluajeazeez@gmail.com			
ariregold	omolepaul35@gmail.com			
bolimaj	bolimaj21@gmail.com			
farindewole	farindewole68@gmail.com			
habeeb	Habeebalabi937@gmail.com			
hhhhhh	timsonfoli11@yahoo.com			
kenny	kehindesamuelojomo@gmail.com			
lahdol	lahdol11@gmail.com			
marveking	marveking12@gmail.com			
Adewunmi Adesoji morawunmi@gmail.com		
Salam Ashrof    salaamashroff@gmail.com			
seun oloyede	oloyedeseun35@gmail.com
"""

# Replace extra whitespaces with a single space
data = ' '.join(data.split())

# Create a CSV file in memory
csv_output = StringIO()
csv_writer = csv.writer(csv_output)

# Write header
csv_writer.writerow(["First Name", "Last Name", "Email Address"])

# Process each line of data
for line in data.split('\n'):
    # Split line into words
    words = line.split()

    # Check if line contains an email address
    if any('@' in word for word in words):
        # Extract first name, last name, and email address
        first_name = ' '.join(words[:-1])
        last_name = words[-2] if len(words) > 1 else ''
        email_address = words[-1]

        # Write to CSV
        csv_writer.writerow([first_name, last_name, email_address])
    else:
        # Duplicate data without '@' sign
        csv_writer.writerow([words[0], ' '.join(words[1:]), ''])

# Save CSV to a file
with open('formatted_datas.csv', 'w', newline='') as csv_file:
    csv_file.write(csv_output.getvalue())

print("CSV file 'formatted_datas.csv' created successfully.")
