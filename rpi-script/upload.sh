#!/bin/bash
# script to refresh the huette.html site on my webpage
# It takes two arguments, the fist one is the temperature and the second the file path of the image.
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

echo "starting upload scipt at $(date '+%k:%M')"
echo "The temperature is: $1°C"
echo "Copying the template file"
cp huette-template.md huette.md
sed -i "s/temp /$1/g" huette.md
sed -i "s/thedate/$(date '+%d %B %Y')/g" huette.md
sed -i "s/thetime/$(date '+%k:%M')/g" huette.md

echo "Opening folder in zennercloud"
echo "This might cause an error if the folder already exists"
curl -u rpi-huette:ueberdenwolken -X MKCOL "https://cloud.alexanderkutschera.com/remote.php/dav/files/rpi-huette/RPi_Fotos/$(date '+%Y-%m')"
echo "Uploading image to zennercloud"
curl -u rpi-huette:ueberdenwolken -T $2 "https://cloud.alexanderkutschera.com/remote.php/dav/files/rpi-huette/RPi_Fotos/$(date '+%Y-%m')/$2"
cp $2 ../assets/img/huette.jpg
cp temp_plot.png ../assets/img/temp_plot.png
jpegoptim --size=500k ../assets/img/huette.jpg #reduce the size to reduce traffic for Github
echo "removing original img"
rm $2
echo "Replacing old huette.md file"
cp huette.md ../resources/huette.md
cd ..

echo "Committing changes"
git add *
git commit -m "I'm a bot beep boop"
git push

echo "ending upload scipt at $(date '+%k:%M')"
exit 0
