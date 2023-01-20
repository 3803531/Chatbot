#!/usr/bin/env python

"""addBoundaries.py: this script automatically adds boundary elements according to punctuation marks in a fml-apml document type."""

from xml.dom.minidom import parse
from xml.dom.minidom import parseString
import re
import fnmatch
import sys, getopt
import os
from os.path import isfile
from os import walk
import codecs

__author__      = "Sabrina Campano"

def usage():
	""" Print script usage."""

	print ('usage: addBoundaries.py [-r] <inputPath> <outputDir> ')

def parseArgs(argv):
	""" Parse script arguments. """

	global replace
	replace = False

	try:
		opts, args = getopt.getopt(argv,"hr",["help", "replaceExistingBoundaries"])
	except getopt.GetoptError:
		#print (str(err))
		usage()
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-r", "--replaceExistingBoundaries"):
			replace = True

	if len(args) < 2:
		print ('Error: wrong number of arguments')
		usage()
		sys.exit(2)

	inputPath = args[0]
	outputDir = args[1]

	if (inputPath == outputDir):
		print ("Error: input path and output directory cannot be the same.")
		sys.exit(2)

	if not os.path.isdir(inputPath) and not os.path.isfile(inputPath):
		print ("Error: directory " + inputPath + " not found")
		sys.exit(2)

	print ('Input path is: ', inputPath)
	print ('Output dir is: ', outputDir)
	print ('Replace existing boundaries: ', "yes" if replace else "no")
	return inputPath, outputDir

def addBoundary(dom, speechElement, punct, nextTimeMarker):

	""" Add a boundary as a child node in a speech element issued from dom data. Boundary attributes are set according
	to a punctuation mark, and to the time marker element that follows the punctuation mark.

	Keyword arguments:
	dom -- dom data
	speechElement -- speech element in which the boundary has to be added
	punct -- punctuation mark
	nextTimeMarker -- that marker element that follows the punctuation mark
	"""

	global boundaryCount

	# Define boundary type.
	boundaryType = ''

	if punct == ',' :
		boundaryType = "LH"
	elif punct == '.' :
		boundaryType = "LL"
	else:
		boundaryType = "HH"

	# Get speech element id.
	speechId = speechElement.getAttribute("id")

	if speechId == None:
		speechId = ""

	# Get time marker id.
	nextTimeMarkerId = nextTimeMarker.getAttribute("id")

	# Create boundary node.
	boundaryNode = dom.createElement("boundary")
	boundaryNode.setAttribute("id", "b" + str(boundaryCount))
	boundaryNode.setAttribute("type", boundaryType)
	boundaryNode.setAttribute("start", speechId +":"+ nextTimeMarkerId)
	boundaryNode.setAttribute("end", speechId +":"+ nextTimeMarkerId + "+0.5")


	# Add boundary node as child to speech element.
	speechElement.appendChild(boundaryNode)
	boundaryCount+=1

def main(argv):

	# Regular expressions to filter files by extension.
	includes = ['*.xml']
	includes = r'|'.join([fnmatch.translate(x) for x in includes])

	inputpath, outputDir = parseArgs(argv)

	if isfile(inputpath) and re.match(includes, inputpath):
		outputPath = os.path.join(outputDir, os.path.basename(inputpath))
		processFile(inputpath, outputPath)
	else:
		for (root, dirs, files) in walk(inputpath):
			files = [f for f in files if re.match(includes, f)]
			for name in files:
				inputFile = os.path.join(root, name) # File to process.
				outputPath = os.path.join(outputDir, os.path.relpath(root, inputpath), name) # File output path.
				processFile(inputFile, outputPath)

def writeDom(dom, outputFile):

	""" Write dom data in a file. """

	if not os.path.exists(os.path.dirname(outputFile)):
		os.makedirs(os.path.dirname(outputFile))

	cleanDom = '\n'.join([line for line in dom.toprettyxml(indent='\t').split('\n') if line.strip()]) # Remove blank lines.

	f = codecs.open(outputFile, "w", encoding='utf-8')
	try:
		f.write(cleanDom)
	finally:
		f.close()

def processFile(inputFile, outputFile):

	""" Add a boundary in the output file when a punctuation mark is found in a speech element of the input file.
	No boundary is added in the speech element when an existing boundary is found and replace option is False. """

	# Counter for the number of boundaries in a single file. Used to set boundary ids.
	global boundaryCount
	# Option for the replacement of existing boundaries.
	global replace

	print ("\nProcessing file: ", inputFile, "...")

	dom = parse(inputFile)
	boundaryCount = 0

	for speech in dom.getElementsByTagName("speech"):

		existingBoundaries = speech.getElementsByTagName("boundary")
		if len(existingBoundaries) > 0:

			if not replace:
				print ("Boundaries found in a speech element from input file. No boundary will be added in this speech element.")
				continue
			else:
				for boundaryElement in existingBoundaries: # Remove existing boundary elements.
					speech.removeChild(boundaryElement)
				print ("Boundaries found in speech element of input file. These boundaries were removed from output file.")

		for child in speech.childNodes:

			if child.nodeType == 3: # If child is a TextNode.
				text = child.nodeValue.strip()
				res = re.findall('[\.\?\!,]', text) # Find punctuation marks in text.
				if len(res) > 0:
					punct = res[len(res)-1] # Get last punctuation mark by default.
					nextSibling = child.nextSibling
					if nextSibling != None and nextSibling.tagName == "tm": # If a time marker element follows punctuation mark.
						addBoundary(dom, speech, punct, nextSibling)

	# Print message with number of boundaries added.
	writeDom(dom, outputFile)
	print ("File ", outputFile," written - ", boundaryCount, "boundaries added.")

if __name__ == "__main__":
	main(sys.argv[1:])