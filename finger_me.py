import pygatt
import hashlib
from pyfingerbot import XRequest, Coder, TuyaDataPacket, BleReceiver, SecretKeyManager, FingerBot
import time
from struct import unpack
from Crypto.Cipher import AES
from binascii import unhexlify, hexlify

# Use https://github.com/redphx/tuya-local-key-extractor to get these values
#LOCAL_KEY = '`$u|?u.p={7me[:<'
LOCAL_KEY = '5T_SokY+GPk_uhME'
MAC = 'DC:23:52:10:20:74'
UUID = 'uuid819926cef77c'
DEV_ID = 'bf5c9789wbrmcb5w'

fingerbot = FingerBot(MAC, LOCAL_KEY, UUID, DEV_ID)
fingerbot.connect()
