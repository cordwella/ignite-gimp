#!/usr/bin/env python
### Use UBUNTU MONO (font)

from gimpfu import *
import os
import glob

pagewidth = 3508
pageheight = 2480

textsize = 36

def ignite_gimp(nope, death, indirectory, outdirectory, logodirectory, font, fontcolor, backgroundcolor):
    messagebox = pdb.gimp_message_get_handler( )
    pdb.gimp_message_set_handler( 2 ) # send messages in error console
    pos = 0
    CODESPERPAGE = 4
    currentpage = None
    currentpageno = 0
    img = gimp.Image(pagewidth, pagewidth, RGB)
    qrx = 0
    qry = 0
    logox = 0
    logoy = 0
    textx = 0
    texty = 0

    img = None
    layerno = 0
    for filename in glob.iglob(indirectory+'/*.svg'):
        info = filename.split("-")
        imid = info[len(info)-3]
        imname = info[len(info)-2]
        imhouse = info[len(info)-1].split(".")[0]
        #impoints = info[3]
        if pos == 0:
            # create new image, set up details
            img = None
            img = gimp.Image(pagewidth, pagewidth, RGB)
            background = gimp.Layer(img, "Background", pagewidth, pageheight,
                                        RGB_IMAGE, 100, NORMAL_MODE)

            background.fill(BACKGROUND_FILL)
            img.add_layer(background, -1)

            # DRAW A LINE THROUGH MIDDLE OF THE PAGE
            ctrlPoints = [pagewidth/2,0,pagewidth/2,pageheight]
            pdb.gimp_pencil(background,len(ctrlPoints),ctrlPoints)

            ctrlPoints = [0,pageheight/2,pagewidth,pageheight/2]
            pdb.gimp_pencil(background,len(ctrlPoints),ctrlPoints)

            # If you are wanting to modify this here would be your best bet
            # Each defines x and y starting values for each of the codes
            qrx = 2
            qry = 57
            logox = 892
            logoy = 182
            textx = 135
            texty = 1000
        elif pos == 1:
            qrx = 1824
            qry = 57
            logox = 2680
            logoy = 182
            textx = 1910
            texty = 1000
        elif pos == 2:
            qrx = 2
            qry = 1360
            logox = 892
            logoy = 1445
            textx = 75
            texty = 2300
        elif pos == 3:
            qrx = 1824
            qry = 1360
            logox = 2680
            logoy = 1445
            textx = 1910
            texty = 2300

        logofilename = logodirectory+"/"+imhouse+".png"

        pdb.gimp_edit_copy(pdb.gimp_image_merge_visible_layers( pdb.gimp_file_load(logofilename, logofilename), 1))

        logolayer = gimp.Layer(img, str(currentpageno) + "logo" + str(pos), 767, 590, RGB_IMAGE, 100, NORMAL_MODE)
        img.add_layer(logolayer)
        floating = pdb.gimp_edit_paste(logolayer, -1)
        pdb.gimp_floating_sel_anchor(floating)
        logolayer.set_offsets(logox, logoy)

        pdb.gimp_edit_copy(pdb.gimp_image_merge_visible_layers(pdb.gimp_file_load(filename, filename), 1))

        qrlayer = gimp.Layer(img, str(currentpageno) + "qr" + str(pos), 205, 205, RGB_IMAGE, 100, NORMAL_MODE)
        img.add_layer(qrlayer)
        floating = pdb.gimp_edit_paste(qrlayer, -1)
        pdb.gimp_floating_sel_anchor(floating)
        qrlayer.scale(800, 800, 1)
        qrlayer.set_offsets(qrx, qry)

        # TODO: set font size based on text length
        if(len(imname)):
            textlayer = pdb.gimp_text_fontname(img, None, textx, texty, imname, 10, True, 90, POINTS, font)

        pos = pos + 1
        if pos == CODESPERPAGE:
            # Save the current image

            layer = img.merge_visible_layers(1)

            pdb.gimp_file_save(img, layer, outdirectory + "/"+ str(currentpageno) + ".png", outdirectory + "/"+ str(currentpageno) + ".png")
            pdb.gimp_message("Image saved")
            img.resize(pagewidth, pageheight, 0, 0)
            gimp.Display(img)
            pos = 0
            currentpageno = currentpageno + 1

        #pdb.gimp_message("Name:" + imname + "  House:" + imhouse)
    if img != None:
        layer = img.merge_visible_layers(1)

        pdb.gimp_file_save(img, layer, outdirectory + "/"+ str(currentpageno) + ".png", outdirectory + "/"+ str(currentpageno) + ".png")
        pdb.gimp_message("Image saved")
        img.resize(pagewidth, pageheight, 0, 0)
        gimp.Display(img)

    pdb.gimp_message_set_handler( messagebox )


register(
        "ignite_generate",
        "Generates pages of QR Codes with house logos",
        "Generates pages of QR Codes with house logos",
        "Amelia Cordwell",
        "Amelia Cordwell",
        "2016",
        "<Image>/Tools/_Ignite",
        "",
        [
            (PF_DIRNAME, "indirectory", ("Input Directory"), os.getcwd() ),
            (PF_DIRNAME, "outdirectory", ("Output Directory"), os.getcwd() ),
            (PF_DIRNAME, "logodirectory", ("Logo Directory"), os.getcwd() ),
            (PF_FONT, "font", ("Font"), None ),
            (PF_COLOR,  "fontcolor", "Font Color", (0, 0, 0)),
            (PF_COLOR,  "backgroundcolor", "Background Color", (255, 255, 255)),
        ],
        [],
        ignite_gimp)

main()
