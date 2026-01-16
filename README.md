![ice_cream_with_diagonals_Friday_16_January_2026](https://github.com/user-attachments/assets/5711ab2e-1487-42ca-9521-704c1f8fc345)

how to use at the moment
prepare an image
1. add borders
2. invert
3. size
run the following 
poetry run python convert_image_to_wav.py <image_path>

how to clean up SVG
you can open in vim and reference the layers of inkscape to delete the columns you need
to delete the rows you need
something like this :%s/,0.*,220\.0/,220.0/
to delete trailing coords 
something like this... :%s/475\.0.*L/475.0 L
then replace final coordinate before closing quotation mark with new value
:%s/641\.25"/475.0"

do the same for excel?

to delete first x-number of characters `:%s/^.\{56\}//`
In Vim, to delete each occurrence of a comma followed by any characters and then a space (,... ), use this command:
:%s/,[^ ]* //g
In Vim, to delete each occurrence of a comma followed by a space, then any characters, then a period (, ... .), use this command:
:%s/, [^\.]*\.//g



