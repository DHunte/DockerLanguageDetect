# DockerLanguageDetect
Container for py-langid.

Accepts a json get/post request in the format

{ "Comment" : "some text in your specific language" }

and returns a json response in the format

{ "Language" : "en", "Probability" : 0.7 }
