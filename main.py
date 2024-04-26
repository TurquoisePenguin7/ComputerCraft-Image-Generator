from PIL import Image
import sys
import numpy
import json
numpy.set_printoptions(threshold=numpy.inf)


"""THOUGHTS:
    - use the values from https://tweaked.cc/module/colors.html and convert them to the 0123456789abcdef values
    - grab the RGB in hex for each row/column combo
    - let numpy do the magic
    """
FNAME = "file.png"
COLORS = {
        "#F0F0F0": 0, 
        "#F2B233": 1, 
        "#E57FD8": 2, 
        "#99B2F2": 3, 
        "#DEDE6C": 4, 
        "#7FCC19": 5, 
        "#F2B2CC": 6, 
        "#4C4C4C": 7, 
        "#999999": 8, 
        "#4C99B2": 9, 
        "#B266E5": "a", 
        "#3366CC": "b", 
        "#7F664C": "c", 
        "#57A64E": "d", 
        "#CC4C4C": "e", 
        "#111111": "f",
    }

# TODO: fix the naming, bruh
def toHex(number: list):
    return f"#{number[0]:02X}{number[1]:02X}{number[2]:02X}"

# TODO: conversion
img = Image.open("mogi.png")
img = img.quantize(colors=16, method=2).save("result.png")
# img.save(FNAME)

converted = Image.open("result.png")
converted = converted.convert("P", palette=Image.ADAPTIVE, colors=16).convert("RGB")
arr = numpy.array(converted.getdata())
print(", ".join(map(toHex, arr)))

# np_img = numpy.array(converted)
# np_img = np_img.flatten()
# # np_img = numpy.array2string(np_img)
# np_img = np_img.tolist()
# print(numpy.asarray(np_img))
# with open("data.txt", "w") as file:
#     # json.dump(np_img.tolist(), file)
#     file.write(", ".join(map(str, np_img)))

# TODO: saving from array, editing it, uploading to pastebin for the silly computercraft mod

# with open("data.txt") as f:
#         ...

# im = Image.fromarray(arr)
# im.save("test2.png")
