import os
import rdflib
from rdflib.namespace import RDF, OWL, RDFS, XSD

users = os.listdir("icons/ffffff/000000/1x1")

g = rdflib.Graph()

namespace = rdflib.Namespace("http://game-icons.net/")
usersNamespace = rdflib.Namespace("http://game-icons.net/1x1/")
fgwcoreNamespace = rdflib.Namespace("http://www.fgw.net/core#")
licensesNamespace = rdflib.Namespace("http://www.fgw.net/licenses#")
formatsNamespace = rdflib.Namespace("http://www.fgw.net/formats#")
g.bind("", namespace)
g.bind("gameiconsu", usersNamespace)
g.bind("owl", OWL)
g.bind("rdf", RDF)
g.bind("fgwcore", fgwcoreNamespace)
g.bind("fgwa", licensesNamespace)
g.bind("fgwl", formatsNamespace)
g.add((
	namespace[""],
	RDF.type,
	OWL.Ontology
))
g.add((
	namespace["index.html"],
	RDF.type,
	OWL.NamedIndividual
))
g.add((
	namespace[""],
	OWL.imports,
	rdflib.URIRef("http://aspie96.github.io/FGW/fgw.owl")
))
g.add((
	namespace["index.html"],
	RDF.type,
	fgwcoreNamespace["Platform"]
))
g.add((
	namespace["index.html"],
	RDFS.label,
	rdflib.Literal("Game-icons.net", lang="en")
))
g.add((
	namespace["index.html"],
	RDFS.comment,
	rdflib.Literal("An ever growing collection of free game icons.", lang="en")
))
g.add((
	namespace["index.html"],
	fgwcoreNamespace["location"],
	rdflib.Literal("http://game-icons.net/", datatype=XSD.anyURI)
))
g.add((
	namespace[""],
	RDFS.label,
	rdflib.Literal("Game-icons.net", lang="en")
))
g.add((
	namespace[""],
	RDFS.comment,
	rdflib.Literal("An ever growing collection of free game icons.", lang="en")
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
	fgwcoreNamespace["DisjunctiveLicenseSet"],
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
	formatsNamespace["Art2D"],
	RDF.type,
	OWL.NamedIndividual
))
g.add((
	formatsNamespace["Image-SVG"],
	RDF.type,
	OWL.NamedIndividual
))
g.add((
	licensesNamespace["CC-BY-3.0"],
	RDF.type,
	OWL.NamedIndividual
))
g.add((
	licensesNamespace["CC0-1.0"],
	RDF.type,
	OWL.NamedIndividual
))
g.add((
	fgwcoreNamespace["workId"],
	RDF.type,
	OWL.DatatypeProperty
))
for user in users:
	g.add((
		usersNamespace[user],
		RDF.type,
		OWL.NamedIndividual
	))
	g.add((
		usersNamespace[user],
		RDF.type,
		fgwcoreNamespace["PlatformUser"]
	))
	g.add((
		usersNamespace[user],
		RDFS.label,
		rdflib.Literal(user, lang="en")
	))
	g.add((
		usersNamespace[user],
		RDFS.comment,
		rdflib.Literal(user, lang="en")
	))
	g.add((
		usersNamespace[user],
		fgwcoreNamespace["uses"],
		namespace["index.html"]
	))
	icons = os.listdir("icons/ffffff/000000/1x1/" + user)
	for icon in icons:
		work = user + "/" + icon.replace(".svg", "") + ".html"
		g.add((
			usersNamespace[work],
			RDF.type,
			OWL.NamedIndividual
		))
		g.add((
			usersNamespace[work],
			RDF.type,
			fgwcoreNamespace["Work"]
		))
		g.add((
			usersNamespace[work],
			fgwcoreNamespace["foundIn"],
			namespace["index.html"]
		))
		g.add((
			usersNamespace[work],
			fgwcoreNamespace["author"],
			usersNamespace[user]
		))
		g.add((
			usersNamespace[work],
			fgwcoreNamespace["format"],
			formatsNamespace["Image-SVG"]
		))
		g.add((
			usersNamespace[work],
			fgwcoreNamespace["type"],
			formatsNamespace["Art2D"]
		))
		g.add((
			usersNamespace[work],
			RDFS.label,
			rdflib.Literal(icon.replace(".svg", ""), lang="en")
		))
		g.add((
			usersNamespace[work],
			RDFS.comment,
			rdflib.Literal(icon.replace(".svg", ""), lang="en")
		))
		if user in [ "viscious-speed", "zeromancer" ]:
			g.add((
				usersNamespace[work],
				fgwcoreNamespace["license"],
				licensesNamespace["CC0-1.0"]
			))
		else:
			g.add((
				usersNamespace[work],
				fgwcoreNamespace["license"],
				licensesNamespace["CC-BY-3.0"]
			))
		g.add((
			usersNamespace[work],
			fgwcoreNamespace["notice"],
			rdflib.Literal("""

Please, include a mention "Icons made by {author}" in your derivative work.

If you use them in one of your project, don't hesitate to drop a message to delapouite@gmail.com or ping @GameIcons on twitter.

More info and icons available at https://game-icons.net

""", lang="en")
		))
		g.add((
			usersNamespace[work],
			fgwcoreNamespace["workId"],
			rdflib.Literal("ico-" + user + "-" + icon.replace(".svg", ""))
		))


f = open("gamei.owl", "wb")
f.write(g.serialize(format="turtle"))
f.close()
