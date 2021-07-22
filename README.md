# FGW
Free Game Works is composed of mainly three parts:
- FGW Core: The core of the ontology and contains all classes and properties.
- FGW Licenses: Contains individuals describing licenses or license validators.
- FGW Formats: Contains individuals describing file formats and types of work.

The files of the ontology are available at:
- fgwcore: http://aspie96.github.io/FGW/fgwcore.owl
- fgwl: http://aspie96.github.io/FGW/fgwl.owl
- fgwf: http://aspie96.github.io/FGW/fgwf.owl

For convenience an additional file is provided which imports the above:
- fgw: http://aspie96.github.io/FGW/fgw.owl

Inferences are available at:
- http://aspie96.githubio/FGW/inferred.owl

In addition to the above, data relative to specific platform is also provided:
- http://aspie96.github.io/FGW/platforms/ambientcg.owl and inferences: http://aspie96.github.io/FGW/platforms/ambientcginferred.owl
- http://aspie96.github.io/FGW/platforms/gamei.owl and inferred: http://aspie96.github.io/FGW/platforms/gameiinferrd.owl
- http://aspie96.github.io/FGW/platforms/oga.owl and inferred: http://aspie96.github.io/FGW/platforms/ogainferred.owl

Note that files of inferred axioms do not import anything, while the original file referring to each platform imports http://aspie96.github.io/FGW/fgw.owl.

See documentation at: http://150.146.207.114/lode/extract?url=http%3A%2F%2Faspie96.github.io%2FFGW%2Fxml%2Ffgw.xml&imported=true&lang=en

Associated documents (in Italian):
- https://docs.google.com/document/d/1g-n6LSMm3gEb2Ucv_uic_h-QvA-Iul2LRV0DRY_EPuo/edit#
- https://docs.google.com/document/d/1yWAbIQGJBIC-bP-5qQUSbEg1GiAEWEObGGIUlXJYMuo/edit#heading=h.c2f5z9mt57v4

The "website" folder contains a website which assumes an instance of Virtuoso with loaded graphs.
