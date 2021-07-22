import requests
import rdflib
from rdflib.namespace import RDF, OWL, RDFS, XSD

url = "https://ambientcg.com/api/v2/full_json?limit=100&include=tagData,relationshipData&offset="

i = 0

c = True

assets = []
categories = []
types = {
	"PhotoTexturePBR": {
		"workType": "Texture",
		"formats": [ "Image-PNG", "Image-JPEG" ]
	},
	"DecalPBR": {
		"workType": "Texture",
		"formats": [ "Image-PNG", "Image-JPEG" ]
	},
	"AtlasPBR": {
		"workType": "Texture",
		"formats": [ "Image-PNG", "Image-JPEG" ]
	},
	"PhotoTexturePlain": {
		"workType": "Texture",
		"formats": [ "Image-PNG", "Image-JPEG" ]
	},
	"SBSAR": {
		"workType": "Texture",
		"formats": [ "SBSAR" ]
	},
	"3DModel": {
		"workType": "3DModel",
		"formats": [ "OBJ" ]
	},
	"Terrain": {
		"workType": "3DModel",
		"formats": [ "EXR", "OBJ" ]
	}
}

while c:
	r = requests.get(url + str(i * 100), headers={
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
	})
	data = r.json()
	foundAssets = data["foundAssets"]
	for asset in foundAssets:
		if asset["dataType"] in types:
			assets.append({
				"assetId": asset["assetId"],
				"category": asset["category"],
				"createdUsing": asset["createdUsing"],
				"tags": asset["tags"],
				"createdUsing": asset["createdUsing"],
				"dataType": asset["dataType"]
			})
			if asset["category"] not in categories:
				categories.append(asset["category"])
	if len(foundAssets) == 0:
		c = False
	else:
		i += 1

g = rdflib.Graph()
namespace = rdflib.Namespace("http://ambientCG.com/")
categoryNamespace = rdflib.Namespace("http://ambientCG.com/c/")
assetNamespace = rdflib.Namespace("http://ambientCG.com/a/")
fgwcoreNamespace = rdflib.Namespace("http://www.fgw.net/core#")
fgwlNamespace = rdflib.Namespace("http://www.fgw.net/licenses#")
fgwfNamespace = rdflib.Namespace("http://www.fgw.net/formats#")
g.bind("", namespace)
g.bind("owl", OWL)
g.bind("ambientcgc", categoryNamespace)
g.bind("ambientcga", assetNamespace)
g.bind("rdf", RDF)
g.bind("fgwcore", fgwcoreNamespace)
g.bind("fgwl", fgwlNamespace)
g.bind("fgwf", fgwfNamespace)
g.add((
	namespace[""],
	RDF.type,
	OWL.Ontology
))
g.add((
	namespace[""],
	OWL.imports,
	rdflib.URIRef("http://aspie96.github.io/FGW/fgw.owl")
))
g.add((
	namespace["index.php"],
	RDF.type,
	OWL.NamedIndividual
))
g.add((
	namespace["index.php"],
	RDF.type,
	fgwcoreNamespace["Platform"]
))
g.add((
	namespace["index.php"],
	RDFS.label,
	rdflib.Literal("ambientCG", lang="en")
))
g.add((
	namespace["index.php"],
	RDFS.comment,
	rdflib.Literal("Public Domain materials for Physically Based Rendering.", lang="en")
))
g.add((
	namespace["index.php"],
	fgwcoreNamespace["location"],
	rdflib.Literal("http://ambientcg.com/", datatype=XSD.anyURI)
))
g.add((
	namespace[""],
	RDFS.label,
	rdflib.Literal("ambientCG", lang="en")
))
g.add((
	namespace[""],
	RDFS.comment,
	rdflib.Literal("Public Domain materials for Physically Based Rendering.", lang="en")
))
g.add((
	fgwcoreNamespace["PlatformUser"],
	RDF.type,
	OWL.Class
))
g.add((
	fgwcoreNamespace["Platform"],
	RDF.type,
	OWL.Class
))
g.add((
	fgwcoreNamespace["Collection"],
	RDF.type,
	OWL.Class
))
g.add((
	fgwcoreNamespace["Work"],
	RDF.type,
	OWL.Class
))
g.add((
	fgwcoreNamespace["author"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	fgwcoreNamespace["uses"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	fgwcoreNamespace["location"],
	RDF.type,
	OWL.DatatypeProperty
))
g.add((
	fgwcoreNamespace["tag"],
	RDF.type,
	OWL.DatatypeProperty
))
g.add((
	fgwcoreNamespace["workId"],
	RDF.type,
	OWL.DatatypeProperty
))
g.add((
	fgwcoreNamespace["derivedFrom"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	fgwcoreNamespace["notice"],
	RDF.type,
	OWL.DatatypeProperty
))
g.add((
	fgwcoreNamespace["foundIn"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	fgwcoreNamespace["collectsWork"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	fgwcoreNamespace["format"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	fgwcoreNamespace["license"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	fgwcoreNamespace["type"],
	RDF.type,
	OWL.ObjectProperty
))

g.add((
	namespace["legal.php"],
	RDF.type,
	OWL.NamedIndividual
))
g.add((
	namespace["legal.php"],
	RDF.type,
	fgwcoreNamespace["PlatformUser"]
))
g.add((
	namespace["legal.php"],
	RDFS.label,
	rdflib.Literal("Lennart Demes", lang="en")
))
g.add((
	namespace["legal.php"],
	fgwcoreNamespace["location"],
	rdflib.Literal("https://www.artstation.com/struffelproductions", datatype=XSD.anyURI)
))
g.add((
	namespace["legal.php"],
	fgwcoreNamespace["uses"],
	namespace["index.php"]
))

for category in categories:
	g.add((
		categoryNamespace[category],
		RDF.type,
		OWL.NamedIndividual
	))
	g.add((
		categoryNamespace[category],
		RDF.type,
		fgwcoreNamespace["Collection"]
	))
	g.add((
		categoryNamespace[category],
		fgwcoreNamespace["author"],
		namespace["legal.php"]
	))
	g.add((
		categoryNamespace[category],
		fgwcoreNamespace["foundIn"],
		namespace["index.php"]
	))
	g.add((
		categoryNamespace[category],
		RDFS.label,
		rdflib.Literal(category, lang="en")
	))
	g.add((
		categoryNamespace[category],
		RDFS.comment,
		rdflib.Literal(category, lang="en")
	))
	g.add((
		categoryNamespace[category],
		fgwcoreNamespace["location"],
		rdflib.Literal("http://ambientcg.com/c/" + category, datatype=XSD.anyURI)
	))

for type in types:
	if type not in categories:
		g.add((
			categoryNamespace[type],
			RDF.type,
			OWL.NamedIndividual
		))
		g.add((
			categoryNamespace[type],
			RDF.type,
			fgwcoreNamespace["Collection"]
		))
		g.add((
			categoryNamespace[type],
			fgwcoreNamespace["author"],
			namespace["legal.php"]
		))
		g.add((
			categoryNamespace[type],
			fgwcoreNamespace["foundIn"],
			namespace["index.php"]
		))
		g.add((
			categoryNamespace[type],
			RDFS.comment,
			rdflib.Literal(type, lang="en")
		))
		g.add((
			categoryNamespace[type],
			RDFS.label,
			rdflib.Literal(type, lang="en")
		))
		g.add((
			categoryNamespace[type],
			fgwcoreNamespace["location"],
			rdflib.Literal("http://ambientcg.com/c/" + type, datatype=XSD.anyURI)
		))

for asset in assets:
	g.add((
		assetNamespace[asset["assetId"]],
		RDF.type,
		OWL.NamedIndividual
	))
	g.add((
		assetNamespace[asset["assetId"]],
		RDF.type,
		fgwcoreNamespace["Work"]
	))
	g.add((
		assetNamespace[asset["assetId"]],
		fgwcoreNamespace["location"],
		rdflib.Literal("http://ambientcg.com/a/" + asset["assetId"], datatype=XSD.anyURI)
	))
	g.add((
		assetNamespace[asset["assetId"]],
		fgwcoreNamespace["license"],
		fgwlNamespace["CC0-1.0"]
	))
	g.add((
		assetNamespace[asset["assetId"]],
		RDFS.label,
		rdflib.Literal(asset["assetId"], lang="en")
	))
	g.add((
		assetNamespace[asset["assetId"]],
		RDFS.comment,
		rdflib.Literal(asset["assetId"] + " - " + asset["category"] + " - " + asset["dataType"], lang="en")
	))
	g.add((
		assetNamespace[asset["assetId"]],
		fgwcoreNamespace["author"],
		namespace["legal.php"]
	))
	g.add((
		categoryNamespace[asset["category"]],
		fgwcoreNamespace["collectsWork"],
		assetNamespace[asset["assetId"]]
	))
	g.add((
		assetNamespace[asset["assetId"]],
		fgwcoreNamespace["type"],
		fgwfNamespace[types[asset["dataType"]]["workType"]]
	))
	for original in asset["createdUsing"]:
		g.add((
			assetNamespace[asset["assetId"]],
			fgwcoreNamespace["derivedFrom"],
			assetNamespace[original]
		))
	for format in types[asset["dataType"]]["formats"]:
		g.add((
			assetNamespace[asset["assetId"]],
			fgwcoreNamespace["format"],
			fgwfNamespace[format]
		))
	g.add((
		assetNamespace[asset["assetId"]],
		fgwcoreNamespace["workId"],
		rdflib.Literal("ambientcg:" + asset["assetId"], datatype=XSD.token)
	))
	if asset["dataType"] not in categories:
		g.add((
			categoryNamespace[asset["dataType"]],
			fgwcoreNamespace["collectsWork"],
			assetNamespace[asset["assetId"]]
		))
	g.add((
		assetNamespace[asset["assetId"]],
		fgwcoreNamespace["notice"],
		rdflib.Literal("Contains assets from ambientCG.com, licensed under CC0 1.0 Universal.", lang="en")
	))
	for tag in asset["tags"]:
		g.add((
			assetNamespace[asset["assetId"]],
			fgwcoreNamespace["tag"],
			rdflib.Literal(tag.strip(), datatype=XSD.token)
		))

f = open("output.ttl", "wb")
f.write(g.serialize(format="turtle"))
f.close()

