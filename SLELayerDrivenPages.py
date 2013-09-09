import arcpy, os
mxd = arcpy.mapping.MapDocument("CURRENT")
inGrpLayer = arcpy.GetParameterAsText(0)
groupLayer = arcpy.mapping.ListLayers(mxd, inGrpLayer)
outputPath = arcpy.GetParameterAsText(1)
mptxtone = arcpy.GetParameterAsText(2)
lyrfldone = arcpy.GetParameterAsText(3)
mptxttwo = arcpy.GetParameterAsText(4)
lyrfldtwo = arcpy.GetParameterAsText(5)
mptxtthree = arcpy.GetParameterAsText(6)
lyrfldthree = arcpy.GetParameterAsText(7)

try:
	if groupLayer[0].isGroupLayer:
		layerList = []
		layerList = arcpy.mapping.ListLayers(mxd)
		sublayerList = []
		arcpy.AddMessage(str(groupLayer[0].name)+" is a group layer.")
		groupLayer[0].visible = True
		for layer in layerList:
			if layer.longName.startswith(groupLayer[0].name + "\\") and layer.longName.count("\\") == 1:
				sublayerList.append(layer)
				layer.visible = False
		for sublayer in sublayerList:
			if sublayer.name and sublayer.description and sublayer.credits:
				sublayer.visible = True
				arcpy.AddMessage(str(sublayer.name)+" turned on and exporting.")
				if mptxtone and lyrfldone:
					txtelm = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", mptxtone)
					if lyrfldone == "name":
						txtelm[0].text = sublayer.name
					if lyrfldone == "description":
						txtelm[0].text = sublayer.description
					if lyrfldone == "credits":
						txtelm[0].text = sublayer.credits
				if mptxttwo and lyrfldtwo:
					txtelmtwo = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", mptxttwo)
					if lyrfldtwo == "name":
						txtelmtwo[0].text = sublayer.name
					if lyrfldtwo == "description":
						txtelmtwo[0].text = sublayer.description
					if lyrfldtwo == "credits":
						txtelmtwo[0].text = sublayer.credits
				if mptxtthree and lyrfldthree:
					txtelmthree = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", mptxtthree)
					if lyrfldthree == "name":
						txtelmthree[0].text = sublayer.name
					if lyrfldthree == "description":
						txtelmthree[0].text = sublayer.description
					if lyrfldthree == "credits":
						txtelmthree[0].text = sublayer.credits
				arcpy.mapping.ExportToPDF(mxd, os.path.join(outputPath, sublayer.credits +"-"+ sublayer.name + ".pdf"))
				arcpy.AddMessage("Exported "+str(sublayer.name))
				sublayer.visible = False
			else:
				arcpy.AddMessage(str(sublayer.name)+" is missing a sublayer value, credits, description or name.")
except Exception, e:
    import traceback
    map(arcpy.AddError, traceback.format_exc().split("\n"))
    arcpy.AddError(str(e))