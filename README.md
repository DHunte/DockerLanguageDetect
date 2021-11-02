# DockerLanguageDetect
Container for py-langid.

Accepts a json get/post on port 5500 on the /api path, with the request message format:

{ "Comment" : "some text in your specific language" }

and returns a json response in the format

{ "Language" : "en", "Probability" : 0.7 }
