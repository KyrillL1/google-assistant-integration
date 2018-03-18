#config.py
# Replace everything marked as $VARIABLE
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
pathToCredentials = dir_path+"/configs/credentials.json" # if it's saved in another path, enter this here.
pathToDeviceConfig = dir_path+"/configs/device_config.json" # if it's saved in another path, enter this here.
currentDevice = {
    'device_model_id' : "$MY_MODEL_ID",
    'device_instance_id' : "$MY_DEVICE_INSTANCE_ID",
    'type' : '$MY_TYPES',
    'trait' : ['$MY_TRAITS'],
    'manufacturer' : '$MY_MANUFACTURER',
    'product-name' : '$MY_PRODUCT_NAME',
    'description' : '$MY_DESCRIPTION',
    'nickname' : '$MY_NICKNAME',
    'client-type' : 'Service'
}
writtenAssist = {
    'audio_out_config': {
        'encoding' : 'LINEAR16',
        'sample_rate_hertz' : 16000,
        'volume_percentage' : 0
    },
    'lang' : 'en-UK', # change if you want another language.
    'promptOut' : "", # change if you want a string pre-fixed in front of your output. E.g. promptOut: 'Assistant>'
    'promptIn' : "" # same as promptOut, only that it will pre-fix the prompt (if you are using a terminal e.g.)
}
spokenAssist = {
    'lang' : 'en-UK', # change if you want another language.
    'DEFAULT_AUDIO_SAMPLE_RATE' : 16000,
    'DEFAULT_AUDIO_SAMPLE_WIDTH' : 2,
    'DEFAULT_AUDIO_ITER_SIZE' : 3200,
    'DEFAULT_AUDIO_DEVICE_BLOCK_SIZE': 6400,
    'DEFAULT_AUDIO_DEVICE_FLUSH_SIZE' : 25600
}

ASSISTANT_API_ENDPOINT = 'embeddedassistant.googleapis.com' # don't change
DEFAULT_GRPC_DEADLINE = 60 * 3 + 5 # don't change
