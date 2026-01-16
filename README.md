<div style="display: flex; gap: 20px; align-items: flex-start; margin-bottom: 30px;">
  <div style="flex: 0 0 300px;">
    <div style="width: 300px; height: 400px; overflow: hidden; border: 1px solid #ccc;">
      <img src="https://github.com/user-attachments/assets/1ab50aba-0adc-4ec6-98ec-1172b405c1a2" width="140%" />
    </div>
  </div>
  <div style="flex: 1;">
    <h1>FFT Thing</h1>
    <p>Image to audio visualization tool</p>
  </div>
</div>

## How to use at the moment
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

