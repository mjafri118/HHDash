#!/usr/bin/python
import os, time

def pdf_to_jpg(link, pdf_output, jpg_output):

    #Downloads the file from the link needed.
    update_command = 'curl -L -o ' + pdf_output + ' "' + link + '"'
    os.system(update_command)

    #Converts file just downloaded into a pic.
    picture_command = "convert -density 300 -trim " + pdf_output + " -quality 100 " + jpg_output
    os.system(picture_command)


pdf_to_jpg(link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT8oxU4BgwJMzvmUSgiNUedV8ve7Htq2KqQzJY9i5-2XLeOkTr-1Uk6Mtk246knBtyb1xtB2sLt_Kcu/pub?gid=529509033&single=true&output=pdf&ndplr=1" , pdf_output = "../Resources/schedule.pdf", jpg_output = "../Resources/schedule.jpg" )

pdf_to_jpg(link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT8oxU4BgwJMzvmUSgiNUedV8ve7Htq2KqQzJY9i5-2XLeOkTr-1Uk6Mtk246knBtyb1xtB2sLt_Kcu/pub?gid=1603161672&single=true&output=pdf" , pdf_output = "../Resources/alert-d.pdf", jpg_output = "../Resources/alert-d.jpg" )
