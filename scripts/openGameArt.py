import requests
import json
from bs4 import BeautifulSoup
import re
import rdflib
from rdflib.namespace import RDF, OWL, RDFS, XSD
from oga import Session

session = Session()

assets = {}

url = "https://opengameart.org/collections?page="

licenses = {
	"CC-BY 4.0": "CC-BY-4.0",
	"CC-BY 3.0": "CC-BY-3.0",
	"CC-BY-SA 4.0": "CC-BY-SA-4.0",
	"CC-BY-SA 3.0": "CC-BY-SA-3.0",
	"GPL 3.0": "GPL-3.0-only",
	"GPL 2.0": "GPL-2.0-only",
	"OGA-BY 3.0": "OGA-BY-3.0",
	"CC0": "CC0-1.0",
	"LGPL 3.0": "LGPL-3.0-only",
	"LGPL 2.1": "LGPL-2.1-only"
}

workTypes = {
	"2D Art": "2DArt",
    "3D Art": "3DArt",
    "Concept Art": "ConceptArt",
    "Texture": "Texture",
    "Music": "Music",
    "Sound Effect": "SoundEffect",
    "Document": "Document"
}

license_sets = []

valid = True
index = 0

users = {}
collections = {}

types = {
	"image/png": "Image-PNG",
	"image/gif": "Image-GIF",
	"audio/ogg": "Audio-OGG",
	"audio/mpeg": "Audio-MPEG",
	"image/svg+xml": "Image-SVG",
	"image/bmp": "Image-BMP"
}

while valid:
	r = requests.get(url + str(index))
	if r.ok:
		document = BeautifulSoup(r.text, features="lxml")
		collectionLinks = document.select("td.views-field-title :first-child")
		collectedElements = document.select(".views-field-field-collected-art")[1:]
		authorLinks = document.findAll(attrs={ "class": "username", "property": "foaf:name" })
		if len(collectionLinks) != 0:
			for collected, collection, user in zip(collectedElements, collectionLinks, authorLinks):
				c = int(collected.text.replace(",", "").replace(" ", ""))
				if c != 0:
					userName = user.text
					userId = user["href"].split("/")[-1]
					collectionName = collection.text
					collectionId = collection["href"].split("/")[-1]
					if userId not in users:
						users[userId] = { "name": userName }
					collections[collectionId] = { "userId": userId, "name": collectionName }
			index += 1
		else:
			valid = False
	else:
		valid = False


print("Collecting collections")

search = session.search(page_limit=5)
async def collect(async_generator):
	results = []
	async for result in async_generator:
		results.append(result)
	return results
results = session.loop.run_until_complete(collect(search))

print("Collecting items")

async def re():
	descrs = (await session.describe_asset(result) for result in results[:20])
	async for descr in descrs:
		assets[descr.id] = {
			"name": descr.name,
			"description": descr.description,
			"authorId": descr.authorId,
			"authorName": descr.authorName,
			"tags": descr.tags,
			"type": descr.type.value,
			"licenses": [ str(license.value) for license in descr.licenses ],
			"notice": descr.attribution,
			"collections": descr.collections,
			"types": descr.types
		}
		if descr.authorId not in users:
			users[descr.authorId] = { "name": descr.authorName }
	await session.close()

session.loop.run_until_complete(re())

g = rdflib.Graph()
namespace = rdflib.Namespace("http://opengameart.org/")
userNamespace = rdflib.Namespace("http://opengameart.org/users/")
contentNamespace = rdflib.Namespace("http://opengameart.org/content/")
auxNamespace = rdflib.Namespace("http://opengameart.org/aux/")
licens = rdflib.Namespace("http://www.fgw.net/core#")
licensNamespace = rdflib.Namespace("http://www.fgw.net/licenses#")
typesNamespace = rdflib.Namespace("http://www.fgw.net/formats#")
g.bind("", namespace)
g.bind("ogau", userNamespace)
g.bind("ogac", contentNamespace)
g.bind("owl", OWL)
g.bind("rdf", RDF)
g.bind("fgwcore", licens)
g.bind("fgwl", licensNamespace)
g.bind("fgwf", typesNamespace)
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
	licens["Platform"]
))
g.add((
	namespace["index.php"],
	RDFS.label,
	rdflib.Literal("OpenGameArt.org", lang="en")
))
g.add((
	namespace["index.php"],
	RDFS.comment,
	rdflib.Literal("A media repository intended for use with free and open source software game projects, offering open content assets.", lang="en")
))
g.add((
	namespace["index.php"],
	licens["location"],
	rdflib.Literal("http://opengameart.org/", datatype=XSD.anyURI)
))
g.add((
	namespace[""],
	RDFS.label,
	rdflib.Literal("OpenGameArt.org", lang="en")
))
g.add((
	namespace[""],
	RDFS.comment,
	rdflib.Literal("A media repository intended for use with free and open source software game projects, offering open content assets.", lang="en")
))
g.add((
	licens["PlatformUser"],
	RDF.type,
	OWL.Class
))
g.add((
	licens["Platform"],
	RDF.type,
	OWL.Class
))
g.add((
	licens["Collection"],
	RDF.type,
	OWL.Class
))
g.add((
	licens["DisjunctiveLicenseSet"],
	RDF.type,
	OWL.Class
))
g.add((
	licens["Work"],
	RDF.type,
	OWL.Class
))
g.add((
	licens["author"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	licens["uses"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	licens["location"],
	RDF.type,
	OWL.DatatypeProperty
))
g.add((
	licens["tag"],
	RDF.type,
	OWL.DatatypeProperty
))
g.add((
	licens["notice"],
	RDF.type,
	OWL.DatatypeProperty
))
g.add((
	licens["foundIn"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	licens["format"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	licens["memberLicense"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	licens["license"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	licens["type"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	licens["collectsWork"],
	RDF.type,
	OWL.ObjectProperty
))
g.add((
	licens["workId"],
	RDF.type,
	OWL.DatatypeProperty
))
for user in users:
	g.add((
		userNamespace[user],
		RDF.type,
		OWL.NamedIndividual
	))
	g.add((
		userNamespace[user],
		RDF.type,
		licens["PlatformUser"]
	))
	g.add((
		userNamespace[user],
		RDFS.label,
		rdflib.Literal(users[user]["name"], lang="en")
	))
	g.add((
		userNamespace[user],
		RDFS.comment,
		rdflib.Literal(users[user]["name"], lang="en")
	))
	g.add((
		userNamespace[user],
		licens["location"],
		rdflib.Literal("http://opengameart.org/users/" + user, datatype=XSD.anyURI)
	))
	g.add((
		userNamespace[user],
		licens["uses"],
		namespace["index.php"]
	))
for collection in collections:
	g.add((
		contentNamespace[collection],
		RDF.type,
		OWL.NamedIndividual
	))
	g.add((
		contentNamespace[collection],
		RDF.type,
		licens["Collection"]
	))
	g.add((
		contentNamespace[collection],
		licens["author"],
		userNamespace[collections[collection]["userId"]]
	))
	g.add((
		contentNamespace[collection],
		licens["foundIn"],
		namespace["index.php"]
	))
	g.add((
		contentNamespace[collection],
		RDFS.label,
		rdflib.Literal(collections[collection]["name"], lang="en")
	))
	g.add((
		contentNamespace[collection],
		RDFS.comment,
		rdflib.Literal(collections[collection]["name"], lang="en")
	))
	g.add((
		contentNamespace[collection],
		licens["location"],
		rdflib.Literal("http://opengameart.org/content/" + collection, datatype=XSD.anyURI)
	))

for license in licenses:
	g.add((
		licensNamespace[licenses[license]],
		RDF.type,
		OWL.NamedIndividual
	))

for workType in workTypes:
	g.add((
		typesNamespace[workTypes[workType]],
		RDF.type,
		OWL.NamedIndividual
	))

for type in types:
	g.add((
		typesNamespace[types[type]],
		RDF.type,
		OWL.NamedIndividual
	))

for asset in assets:
	g.add((
		contentNamespace[asset],
		RDF.type,
		OWL.NamedIndividual
	))
	g.add((
		contentNamespace[asset],
		RDF.type,
		licens["Work"]
	))
	if len(assets[asset]["licenses"]) > 1:
		assets[asset]["licenses"].sort()
		license_id = "--".join([ licenses[license] for license in assets[asset]["licenses"] ])
		if license_id not in license_sets:
			g.add((
				auxNamespace[license_id],
				RDF.type,
				OWL.NamedIndividual
			))
			g.add((
				auxNamespace[license_id],
				RDF.type,
				licens["DisjunctiveLicenseSet"]
			))
			for license in assets[asset]["licenses"]:
				g.add((
					auxNamespace[license_id],
					licens["memberLicense"],
					licensNamespace[licenses[license]]
				))
			license_sets.append(license_id)
		g.add((
			contentNamespace[asset],
			licens["license"],
			auxNamespace[license_id]
		))
	else:
		g.add((
			contentNamespace[asset],
			licens["license"],
			licensNamespace[licenses[assets[asset]["licenses"][0]]]
		))
	g.add((
		contentNamespace[asset],
		RDFS.comment,
		rdflib.Literal(assets[asset]["description"], lang="en")
	))
	g.add((
		contentNamespace[asset],
		RDFS.label,
		rdflib.Literal(assets[asset]["name"], lang="en")
	))
	g.add((
		contentNamespace[asset],
		licens["author"],
		userNamespace[assets[asset]["authorId"]]
	))
	for collection in assets[asset]["collections"]:
		if collection in collections:
			g.add((
				contentNamespace[collection],
				licens["collectsWork"],
				contentNamespace[asset]
			))
	g.add((
		contentNamespace[asset],
		licens["type"],
		typesNamespace[workTypes[assets[asset]["type"]]]
	))
	g.add((
		contentNamespace[asset],
		licens["workId"],
		rdflib.Literal("oga-" + asset, datatype=XSD.token)
	))
	for type in assets[asset]["types"]:
		if type in types:
			g.add((
				contentNamespace[asset],
				licens["format"],
				typesNamespace[types[type]]
			))
	if assets[asset]["notice"] is not None:
		g.add((
			contentNamespace[asset],
			licens["notice"],
			rdflib.Literal(assets[asset]["notice"], lang="en")
		))
	for tag in assets[asset]["tags"]:
		g.add((
			contentNamespace[asset],
			licens["tag"],
			rdflib.Literal(tag, datatype=XSD.token)
		))

f = open("output.ttl", "wb")
f.write(g.serialize(format="turtle"))
f.close()
