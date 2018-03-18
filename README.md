# Overview
Communicate with the gAssistant in written and spoken form.
This is a simplified version of google's [gRPC assistant service](https://developers.google.com/assistant/sdk/guides/service/python/).

# SetUp
Do the following steps to setup the enviroment:
1. [Configure a Developer Project and Account Settings](https://developers.google.com/assistant/sdk/guides/service/python/embed/config-dev-project-and-account)
2. [Register the Device Model](https://developers.google.com/assistant/sdk/guides/service/python/embed/register-device)
3. Clone/ Download this repo and cd into it.
4. Install local dependencies
```bash
sudo apt-get install portaudio19-dev libffi-dev libssl-dev
pip install -r requirements.txt
```
 > If you don't want to mess up your python configurations, I would recommend a [virtual enviroment](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv).

# Run
In order to run the script, you first have to set up the ./config.py file. The values can be overwritten temporarily by adding arguments when calling the script (see below).
Just open the ./config.py and you see which values you will have to change.

# Start
As soon as you changed ./config.py, you can start talking with your google assistant!
## Written
`python writeWithAssistant.py`
Show all (optional) options with `python writeWithAssistant.py --help`

## Spoken
`python talkWithAssistant.py`
Show all (optional) options with `python talkWithAssistant.py --help`


# Device Overview (via REST calls)
If you want to communicate with the google assistant, you always have to specify a device you are talking over with.
More information regarding that can be found here: [here](https://developers.google.com/assistant/sdk/reference/device-registration/register-device-manual)
If you are a fan REST calls, check the below out:
An example device_model.json can be found in ./configs.
In order to get the authorization accesstoken, do Setup, step 1, but leave out  "--save", so you get the token.
Remember to substitute the $PARAMETERS in the URL below.

## Register
```bash
curl -s -k -X POST -H "Content-Type: application/json" \
-H "Authorization: Bearer $ACCESSTOKEN" -d @$DEVICE_MODEL_ID.json \
https://embeddedassistant.googleapis.com/v1alpha2/projects/$PROJECT_ID/deviceModels/
```

## Get
```bash
curl -s -k -X GET -H "Content-Type: application/json" \
-H "Authorization: Bearer $ACCESSTOKEN" \
https://embeddedassistant.googleapis.com/v1alpha2/projects/$PROJECT_ID/deviceModels/$DEVICE_MODEL_ID
```

## List
```bash
curl -s -k -X GET -H "Content-Type: application/json" \
-H "Authorization: Bearer $ACCESSTOKEN" \
https://embeddedassistant.googleapis.com/v1alpha2/projects/$PROJECT_ID/deviceModels/
```
