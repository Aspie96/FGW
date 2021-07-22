var fetch = require("node-fetch");
var rdfParser = require("rdf-parse").default;
var rdf = require("rdf");
var fs = require("fs");

var ns = rdf.ns("http://www.fgw.net/core#");
var ns1 = rdf.ns("http://www.fgw.net/licenses#");
var owl = rdf.ns("http://www.w3.org/2002/07/owl#");

var gnuIds = [
	"GPL-",
	"LGPL-",
	"AGPL-",
	"GFDL-"
];

var odIds = [
	/^CC0-1.0$/,
	/^CC-BY-/,
	/^CC-BY-SA/,
	/^LAL-/,
	/^GFDL/,
	/^PDDL-1.0$/,
	/^CC-BY-4.0$/,
	/^ODC-By-1.0$/,
	/^CC-BY-SA-4.0$/,
	/^ODbL-1.0$/,
	/^MirOS$/,
	/^OGL-Canada-2.0$/,
	/^OGDL-Taiwan-1.0$/,
	/^OGL-UK/,
	/^O-UDA-1.0$/
]

var fdIds = [
	/^FreeBSD-DOC$/,
	/^GFDL-/,
	/^LGPL-/,
	/^GPL-/,
	/^MirOS$/,
	/^MIT$/
]

var graph = new rdf.Graph();
var ontologyClass = owl("Ontology");
var ontology = "http://www.fgwl.net/licenses";
graph.add(new rdf.Triple(
	ontology,
	rdf.rdfns("type"),
	ontologyClass
));
var namedClass = owl("NamedIndividual");
var owlClass = owl("Class");
var licenseClass = ns("LicenseDocument");
graph.add(new rdf.Triple(
	licenseClass,
	rdf.rdfns("type"),
	owl("Class")
));
var licenseValidatorClass = ns("LicenseValidator");
graph.add(new rdf.Triple(
	licenseClass,
	rdf.rdfns("type"),
	owl("Class")
));
var licenseAuthorClass = ns("LicenseAuthor");
graph.add(new rdf.Triple(
	licenseClass,
	rdf.rdfns("type"),
	owl("Class")
));
var osi = ns1("OpenSourceInitiative");
graph.add(new rdf.Triple(
	osi,
	rdf.rdfns("type"),
	namedClass
));
graph.add(new rdf.Triple(
	osi,
	rdf.rdfsns("label"),
	new rdf.Literal("Open Source Initiative", "@en")
));
graph.add(new rdf.Triple(
	osi,
	rdf.rdfsns("comment"),
	new rdf.Literal("OpenSourceInitiative", "@en")
));
graph.add(new rdf.Triple(
	osi,
	ns("location"),
	new rdf.Literal("https://opensource.org/", rdf.xsdns("anyURI"))
));
graph.add(new rdf.Triple(
	osi,
	ns("licenseList"),
	new rdf.Literal("https://opensource.org/licenses", rdf.xsdns("anyURI"))
));
graph.add(new rdf.Triple(
	osi,
	rdf.rdfns("type"),
	licenseValidatorClass
));
var od = ns1("OpenKnowledgeFoundation");
graph.add(new rdf.Triple(
	od,
	rdf.rdfns("type"),
	namedClass
));
graph.add(new rdf.Triple(
	od,
	rdf.rdfsns("label"),
	new rdf.Literal("Open Knwoledge Foundation", "@en")
));
graph.add(new rdf.Triple(
	od,
	rdf.rdfsns("comment"),
	new rdf.Literal("Open Knowledge Foundation", "@en")
));
graph.add(new rdf.Triple(
	od,
	ns("location"),
	new rdf.Literal("https://opendefinition.org/", rdf.xsdns("anyURI"))
));
graph.add(new rdf.Triple(
	od,
	ns("licenseList"),
	new rdf.Literal("https://opendefinition.org/licenses/", rdf.xsdns("anyURI"))
));
graph.add(new rdf.Triple(
	od,
	rdf.rdfns("type"),
	licenseValidatorClass
));
var fsf = ns1("FreeSoftwareFoundation");
graph.add(new rdf.Triple(
	fsf,
	rdf.rdfns("type"),
	namedClass
));
graph.add(new rdf.Triple(
	fsf,
	rdf.rdfsns("label"),
	new rdf.Literal("FreeSoftwareFoundation", "@en")
));
graph.add(new rdf.Triple(
	fsf,
	rdf.rdfsns("comment"),
	new rdf.Literal("FreeSoftwareFoundation", "@en")
));
graph.add(new rdf.Triple(
	fsf,
	ns("location"),
	new rdf.Literal("https://www.fsf.org/", rdf.xsdns("anyURI"))
));
graph.add(new rdf.Triple(
	fsf,
	ns("licenseList"),
	new rdf.Literal("https://www.gnu.org/licenses/license-list.html", rdf.xsdns("anyURI"))
));
graph.add(new rdf.Triple(
	fsf,
	rdf.rdfns("type"),
	licenseValidatorClass
));
graph.add(new rdf.Triple(
	fsf,
	rdf.rdfns("type"),
	licenseAuthorClass
));
var creativeCommons = ns1("CreativeCommons");
graph.add(new rdf.Triple(
	creativeCommons,
	rdf.rdfns("type"),
	namedClass
));
graph.add(new rdf.Triple(
	creativeCommons,
	rdf.rdfsns("label"),
	new rdf.Literal("Creative Commons", "@en")
));
graph.add(new rdf.Triple(
	creativeCommons,
	rdf.rdfsns("comment"),
	new rdf.Literal("Creative Commons", "@en")
));
graph.add(new rdf.Triple(
	creativeCommons,
	ns("location"),
	new rdf.Literal("https://creativecommons.org/", rdf.xsdns("anyURI"))
));
graph.add(new rdf.Triple(
	creativeCommons,
	rdf.rdfns("type"),
	licenseAuthorClass
));
var fd = ns1("DefinitionOfFreeCulturalWorks");
graph.add(new rdf.Triple(
	fd,
	rdf.rdfns("type"),
	namedClass
));
graph.add(new rdf.Triple(
	osi,
	rdf.rdfsns("label"),
	new rdf.Literal("Definition of Free Cultural Works", "@en")
));
graph.add(new rdf.Triple(
	osi,
	rdf.rdfsns("comment"),
	new rdf.Literal("For over 20 years the Open Source Initiative (OSI) has worked to raise awareness and adoption of open source software, and build bridges between open source communities of practice. As a global non-profit, the OSI champions software freedom in society through education, collaboration, and infrastructure, stewarding the Open Source Definition (OSD), and preventing abuse of the ideals and ethos inherent to the open source movement.", "@en")
));
graph.add(new rdf.Triple(
	osi,
	ns("location"),
	new rdf.Literal("https://opensource.org/", rdf.xsdns("anyURI"))
));
graph.add(new rdf.Triple(
	osi,
	ns("licenseList"),
	new rdf.Literal("https://opensource.org/licenses", rdf.xsdns("anyURI"))
));
graph.add(new rdf.Triple(
	fd,
	rdf.rdfns("type"),
	licenseValidatorClass
));
graph.add(new rdf.Triple(
	ns("approved"),
	rdf.rdfns("type"),
	owl("ObjectProperty")
));
graph.add(new rdf.Triple(
	ns("licenseAuthor"),
	rdf.rdfns("type"),
	owl("ObjectProperty")
));
graph.add(new rdf.Triple(
	ns("licenseLevel"),
	rdf.rdfns("type"),
	owl("ObjectProperty")
));
graph.add(new rdf.Triple(
	ns("location"),
	rdf.rdfns("type"),
	owl("DatatypeProperty")
));
graph.add(new rdf.Triple(
	ns("licenseList"),
	rdf.rdfns("type"),
	owl("DatatypeProperty")
));
graph.add(new rdf.Triple(
	ns("licenseSpdx"),
	rdf.rdfns("type"),
	owl("DatatypeProperty")
));
var exceptionClass = ns("LicenseException");
graph.add(new rdf.Triple(
	licenseClass,
	rdf.rdfns("type"),
	owl("Class")
));
graph.add(new rdf.Triple(
	ns("permissive"),
	rdf.rdfns("type"),
	namedClass
));
graph.add(new rdf.Triple(
	ns("strongCopyleft"),
	rdf.rdfns("type"),
	namedClass
));
graph.add(new rdf.Triple(
	ns("weakCopyleft"),
	rdf.rdfns("type"),
	namedClass
));

var licensesPromise = fetch("https://raw.githubusercontent.com/spdx/license-list-data/master/json/licenses.json")
	.then(function(res) {
		return res.json();
	})
	.then(function(data) {
		var licenses = data.licenses;
		var promises = [];
		for(license in licenses) {
			promises = promises.concat(function(license) {
				if(!licenses[license].isDeprecatedLicenseId) {
					var individual = ns1(licenses[license].licenseId);
					var addIndividual = function() {
						graph.add(new rdf.Triple(
							individual,
							rdf.rdfns("type"),
							licenseClass
						));
						graph.add(new rdf.Triple(
							individual,
							rdf.rdfns("type"),
							namedClass
						));
						if(licenses[license].isOsiApproved) {
							graph.add(new rdf.Triple(
								individual,
								ns("approved"),
								osi
							));
						}
						var odLicense = false;
						for(odId in odIds) {
							if(odIds[odId].test(licenses[license].licenseId)) {
								odLicense = true;
							}
						}
						if(odLicense) {
							graph.add(new rdf.Triple(
								individual,
								ns("approved"),
								od
							));
						}
						if(licenses[license].isFsfLibre) {
							graph.add(new rdf.Triple(
								individual,
								ns("approved"),
								fsf
							));
						}
						graph.add(new rdf.Triple(
							individual,
							ns("location"),
							new rdf.Literal("http://spdx.org/licenses/" + licenses[license].licenseId + ".html", rdf.xsdns("anyURI"))
						));
						graph.add(new rdf.Triple(
							individual,
							ns("licenseSpdx"),
							new rdf.Literal(licenses[license].licenseId, rdf.xsdns("token"))
						));
						for(seeAlso in licenses[license].seeAlso) {
							graph.add(new rdf.Triple(
								individual,
								ns("location"),
								new rdf.Literal(licenses[license].seeAlso[seeAlso], rdf.xsdns("anyURI"))
							));
						}
					}
					if(licenses[license].licenseId.startsWith("CC-") || licenses[license].licenseId.startsWith("CC0-")) {
						var document;
						if(licenses[license].licenseId != "CC-PDDC") {
							if(licenses[license].licenseId.startsWith("CC0-")) {
								document = "http://creativecommons.org/publicdomain/zero/" + "1.0" + "/rdf"
							} else {
								var subStr = licenses[license].licenseId.substr(3);
								var sub = subStr.split("-");
								var str = "/";
								var aux = false;
								for(item in sub) {
									if(/^[0-9\.]+$/.test(sub[item])) {
										str += "/" + sub[item] + "/";
										aux = false;
									} else {
										if(aux) {
											str += "-";
										}
										str += sub[item];
										aux = true;
									}
								}
								if(aux) {
									str += "/";
								}
								document = "http://creativecommons.org/licenses" + str.toLowerCase() + "rdf";
							}
						} else {
							document = "http://creativecommons.org/licenses/publicdomain/rdf";
						}
						return [new Promise(function(resolve) {
							var equiv;
							var copyleft = false;
							var free = true;
							var deriv = false;
							fetch(document)
								.then(function(res) {
									rdfParser.parse(res.body, {
										contentType: "application/rdf+xml"
									})
										.on("data", function(data) {
											if(!equiv) {
												equiv = data.subject.value.substring(0, data.subject.value.length - 1);
											}
											if(data.predicate.value == "http://creativecommons.org/ns#requires" && data.object.value == "http://creativecommons.org/ns#ShareAlike") {
												copyleft = true;
											}
											if(data.predicate.value == "http://creativecommons.org/ns#permits" && data.object.value == "http://creativecommons.org/ns#DerivativeWorks") {
												deriv = true;
											}
											if(data.predicate.value == "http://purl.org/dc/elements/1.1/title") {
												graph.add(new rdf.Triple(
													individual,
													rdf.rdfsns("label"),
													new rdf.Literal("Creative Commons " + data.object.value, "@" + data.object.language)
												));
												graph.add(new rdf.Triple(
													individual,
													rdf.rdfsns("comment"),
													new rdf.Literal("Creative Commons " + data.object.value, "@" + data.object.language)
												));
											}
											if(data.predicate.value == "http://creativecommons.org/ns#prohibits") {
												free = false;
											}
										})
										.on("end", function() {
											if(free && deriv) {
												addIndividual();
												graph.add(new rdf.Triple(
													individual,
													ns("licenseAuthor"),
													creativeCommons
												));
												graph.add(new rdf.Triple(
													equiv,
													rdf.rdfns("type"),
													namedClass
												));
												graph.add(new rdf.Triple(
													individual,
													owl("sameAs"),
													equiv
												));
												if(copyleft) {
													graph.add(new rdf.Triple(
														individual,
														ns("licenseLevel"),
														ns("strongCopyleft")
													));
												} else {
													graph.add(new rdf.Triple(
														individual,
														ns("licenseLevel"),
														ns("permissive")
													));
												}
												graph.add(new rdf.Triple(
													individual,
													ns("approved"),
													fd
												));
											}
											resolve();
										});
								});
						})];
					}
					var gnuLicense = false;
					for(gnuId in gnuIds) {
						if(licenses[license].licenseId.startsWith(gnuIds[gnuId])) {
							gnuLicense = true;
						}
					}
					if(gnuLicense) {
						if(!licenses[license].licenseId.startsWith("GFDL-") || licenses[license].licenseId.includes("-no-invariants-")) {
							var fsfId;
							if(licenses[license].licenseId.startsWith("GFDL")) {
								fsfId = licenses[license].licenseId.substr(1);
							} else {
								fsfId = licenses[license].licenseId;
							}
							var sub = fsfId.split("-");
							var version = sub[1].split(".");
							var major = parseInt(version[0]);
							var minor = parseInt(version[1]);
							graph.add(new rdf.Triple(
								individual,
								ns("licenseAuthor"),
								fsf
							));
							if((sub[0] == "GPL" && major >= 2) || (sub[0] == "LGPL" && (minor >= 1 || major >= 3)) || (sub[0] == "FDL" && minor >= 3)) {
								return [new Promise(function(resolve) {
									var document = "http://www.gnu.org/licenses/" + sub[0].toLowerCase() + "-" + major + "." + minor + ".rdf";
									var equiv;
									var copyleft = false;
									fetch(document)
										.then(function(res) {
											rdfParser.parse(res.body, {
												contentType: "application/rdf+xml"
											})
												.on("data", function(data) {
													if(!equiv) {
														equiv = data.subject.value;
													}
													if(data.predicate.value == "http://creativecommons.org/ns#requires") {
														if(data.object.value == "http://creativecommons.org/ns#LesserCopyleft") {
															copyleft = "Weak";
														} else if(data.object.value == "http://creativecommons.org/ns#Copyleft") {
															copyleft = "Strong";
														}
													}
												})
												.on("end", function() {
													addIndividual();
													graph.add(new rdf.Triple(
														individual,
														rdf.rdfsns("label"),
														new rdf.Literal(licenses[license].name, "@en")
													));
													graph.add(new rdf.Triple(
														individual,
														rdf.rdfsns("comment"),
														new rdf.Literal(licenses[license].name, "@en")
													));
													if(!licenses[license].isFsfLibre) {
														graph.add(new rdf.Triple(
															individual,
															ns("approved"),
															fsf
														));
													}
													graph.add(new rdf.Triple(
														equiv,
														rdf.rdfns("type"),
														namedClass
													));
													if(sub[0] != "FDL" && licenses[license].licenseId.endsWith("-only")) {
														graph.add(new rdf.Triple(
															individual,
															owl("sameAs"),
															equiv
														));
													} else {
														if(licenses[license].licenseId.endsWith("-or-later")) {
															graph.add(new rdf.Triple(
																individual,
																rdf.rdfsns("seeAlso"),
																ns1(licenses[license].licenseId.replace("-or-later", "-only"))
															));
														} else {
															graph.add(new rdf.Triple(
																individual,
																rdf.rdfsns("seeAlso"),
																equiv
															));
														}
													}
													if(copyleft == "Weak") {
														graph.add(new rdf.Triple(
															individual,
															ns("licenseLevel"),
															ns("weakCopyleft")
														));
													} else if(copyleft == "Strong") {
														graph.add(new rdf.Triple(
															individual,
															ns("licenseLevel"),
															ns("strongCopyleft")
														));
													} else {
														graph.add(new rdf.Triple(
															individual,
															ns("licenseLevel"),
															ns("permissive")
														));
													}
													var fdLicense = false;
													for(fdId in fdIds) {
														if(fdIds[fdId].test(licenses[license].licenseId)) {
															fdLicense = true;
														}
													}
													if(fdLicense) {
														graph.add(new rdf.Triple(
															individual,
															ns("approved"),
															fd
														));
													}
													resolve();
												});
										});
								})];
							} else {
								addIndividual();
								graph.add(new rdf.Triple(
									individual,
									rdf.rdfsns("label"),
									new rdf.Literal(licenses[license].name, "@en")
								));
								graph.add(new rdf.Triple(
									individual,
									rdf.rdfsns("comment"),
									new rdf.Literal(licenses[license].name, "@en")
								));
								if(!licenses[license].isFsfLibre) {
									graph.add(new rdf.Triple(
										individual,
										ns("approved"),
										fsf
									));
								}
								if(!licenses[license].licenseId.startsWith("LGPL-")) {
									graph.add(new rdf.Triple(
										individual,
										ns("licenseLevel"),
										ns("strongCopyleft")
									));
								} else {
									graph.add(new rdf.Triple(
										individual,
										ns("licenseLevel"),
										ns("weakCopyleft")
									));
								}
								if(licenses[license].licenseId.endsWith("-or-later")) {
									graph.add(new rdf.Triple(
										individual,
										rdf.rdfsns("seeAlso"),
										ns1(licenses[license].licenseId.replace("-or-later", "-only"))
									));
								}
								var fdLicense = false;
								for(fdId in fdIds) {
									if(fdIds[fdId].test(licenses[license].licenseId)) {
										fdLicense = true;
									}
								}
								if(fdLicense) {
									graph.add(new rdf.Triple(
										individual,
										ns("approved"),
										fd
									));
								}
							}
						}
					} else if(licenses[license].isOsiApproved || licenses[license].isFsfLibre) {
						addIndividual();
						if(licenses[license].licenseId.startsWith("LAL-")) {
							graph.add(new rdf.Triple(
								individual,
								rdf.rdfsns("label"),
								new rdf.Literal(licenses[license].name, "@fr")
							));
							graph.add(new rdf.Triple(
								individual,
								rdf.rdfsns("comment"),
								new rdf.Literal(licenses[license].name, "@fr")
							));
							graph.add(new rdf.Triple(
								individual,
								rdf.rdfsns("label"),
								new rdf.Literal("Free Art License " + licenses[license].name.split(" ")[-1], "@en")
							));
							graph.add(new rdf.Triple(
								individual,
								rdf.rdfsns("comment"),
								new rdf.Literal("Free Art License " + licenses[license].name.split(" ")[-1], "@en")
							));
						} else {
							graph.add(new rdf.Triple(
								individual,
								rdf.rdfsns("label"),
								new rdf.Literal(licenses[license].name, "@en")
							));
							graph.add(new rdf.Triple(
								individual,
								rdf.rdfsns("comment"),
								new rdf.Literal(licenses[license].name, "@en")
							));
						}
						var fdLicense = false;
						for(fdId in fdIds) {
							if(fdIds[fdId].test(licenses[license].licenseId)) {
								fdLicense = true;
							}
						}
						if(fdLicense) {
							graph.add(new rdf.Triple(
								individual,
								ns("approved"),
								fd
							));
						}
					}
				}
				return [];
			}(license));
		}
		var individual = ns1("OGA-BY-3.0");
		graph.add(new rdf.Triple(
			individual,
			rdf.rdfns("type"),
			licenseClass
		));
		graph.add(new rdf.Triple(
			individual,
			ns("location"),
			new rdf.Literal("https://opengameart.org/content/oga-by-30-faq", rdf.xsdns("anyURI"))
		));
		graph.add(new rdf.Triple(
			individual,
			rdf.rdfns("type"),
			namedClass
		));
		graph.add(new rdf.Triple(
			individual,
			rdf.rdfsns("label"),
			new rdf.Literal("OpenGameArt.org Public License", "@en")
		));
		graph.add(new rdf.Triple(
			individual,
			rdf.rdfsns("comment"),
			new rdf.Literal("OpenGameArt.org Public License", "@en")
		));
		return Promise.allSettled(promises);
	});

var exceptionsPromise = fetch("https://raw.githubusercontent.com/spdx/license-list-data/master/json/exceptions.json")
	.then(function(res) {
		return res.json();
	})
	.then(function(data) {
		var exceptions = data.exceptions;
		for(exception in exceptions) {
			var individual = ns1(exceptions[exception].licenseExceptionId);
			graph.add(new rdf.Triple(
				individual,
				rdf.rdfns("type"),
				exceptionClass
			));
			graph.add(new rdf.Triple(
				individual,
				rdf.rdfns("type"),
				namedClass
			));
			graph.add(new rdf.Triple(
				individual,
				ns("location"),
				new rdf.Literal("http://spdx.org/licenses/" + exceptions[exception].licenseExceptionId + ".html", rdf.xsdns("anyURI"))
			));
			graph.add(new rdf.Triple(
				individual,
				rdf.rdfsns("label"),
				new rdf.Literal(exceptions[exception].name, "@en")
			));
			graph.add(new rdf.Triple(
				individual,
				rdf.rdfsns("comment"),
				new rdf.Literal(exceptions[exception].name, "@en")
			));
		}
	});

Promise.allSettled([ licensesPromise, exceptionsPromise ])
	.then(function() {
		var prefix = "@prefix : <http://www.fgw.net/licenses#> .\n\
		@prefix owl: <http://www.w3.org/2002/07/owl#> .\n\
		@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n\
		@prefix xml: <http://www.w3.org/XML/1998/namespace> .\n\
		@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\
		@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n\
		@prefix fgwcore: <http://www.fgw.net/core#> .\n\
		@prefix cc: <http://creativecommons.org/ns#>.\n\
		@prefix dc: <http://purl.org/dc/elements/1.1/> .\n\
		@prefix vann: <http://purl.org/vocab/vann/> .\n\
		<http://www.fgwl.net/licenses> \n\
		dc:creator \"Valentino Giudice\"^^xsd:string ;\n\
		dc:date \"2021-07-14T00:00:00-00:00\"^^xsd:dateTimeStamp ;\n\
		dc:description \"This is the default set of license documents, license exceptions and license validator of the FGW ontology.\"@en ;\n\
		dc:title \"Licenses in the FGW Ontology\"@en ;\n\
		vann:preferredNamespacePrefix \"fgwl\"^^xsd:token ;\n\
		vann:preferredNamespaceUri \"http://www.fgwl.net/licenses#\"^^xsd:anyURI ;\n\
		rdfs:comment \"This is the default set of license documents, license exceptions and license validator of the FGW ontology.\"@en ;\n\
		rdfs:label \"Licenses in the FGW Ontology\"@en .\n";
		fs.writeFile("fgwl.owl", prefix + graph.toArray().join("\n"), function() {
			console.log("Output produced");
		});
	});
