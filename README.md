# DockerLanguageDetect
Container for py-langid.

Accepts a json get/post on port 5500 on the /language/api path, with the request message format:

## Format

{ "Comment" : "some text in your specific language" }

and returns a json response in the format

{ "Language" : "en", "Probability" : 0.7 }


## Example:

curl --header "Content-Type: application/json" --request POST --data '{"Comment":"This is an example comment."}' http://localhost:5500/language/api
{
  "Language": "en", 
  "Probability": 0.9999998731162608
}
