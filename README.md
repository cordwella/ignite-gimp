# GIMP Batch templating for IGNITE codes.

This is a gimp plugin (python) for use with [IGNITE](http://www.github.com/cordwella/ignite) QR codes.

It takes a folder filled with QR codes generated from the IGNITE admin site, as well
as a folder with house logos in them, and generates nice sheets of 4 codes with
the name, code and house logo on them.

The output images are A4 side, however we found during our original run of the
game that we tended to print two of these pages on a single A4 sheet if we were
just putting the codes around the school.

## Installation
To install download 'ignite-gimp.py' and place it in the gimp plugins directory. More information available [here](http://blog.meetthegimp.org/how-to-install-python-plugins-under-gimp/).


## Screenshots
![gimp dialog for the plugin](https://cloud.githubusercontent.com/assets/10441829/20198286/b580e9e2-a808-11e6-95f4-9224fcb02f70.png)  
GIMP dialog for the plugin.  
Input image and drawable should both be empty. 
Input and output directories can be the same by this may get confusing when you are printing.

![3](https://cloud.githubusercontent.com/assets/10441829/20198019/44116828-a807-11e6-8a57-71e9f36f7f55.png)  
Sample output

![screenshot from 2016-11-11 12-10-06](https://cloud.githubusercontent.com/assets/10441829/20198290/bafd9ece-a808-11e6-993f-e2b48af122f0.png)  
Input folder should contain these files.

![screenshot from 2016-11-11 12-18-25](https://cloud.githubusercontent.com/assets/10441829/20198371/1487dbe4-a809-11e6-845a-068b94298ff7.png)  
Output in the folder will look like this.

## House logo naming specifications
The names for the house logo files should be the (house name).png . The house name must be exactly the same including capitalization to the house name in your IGNITE database.
For markers with no house the file will be nohouse.png.
The logos shoulf be 760X590 pixels big.
