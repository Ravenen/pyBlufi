
# UUID / gatt services
BLUFI_SERVICE_UUID = "0000ffff-0000-1000-8000-00805f9b34fb"
BLUFI_WRITE_CHAR_UUID = "0000ff01-0000-1000-8000-00805f9b34fb"
BLUFI_NOTIF_CHAR_UUID = "0000ff02-0000-1000-8000-00805f9b34fb"
BLUFI_NOTIF_DESC_UUID = "00002902-0000-1000-8000-00805f9b34fb"

# Frame CTRL
FRAME_CTRL_POSITION_ENCRYPTED = 0
FRAME_CTRL_POSITION_CHECKSUM  = 1
FRAME_CTRL_POSITION_DATA_DIRECTION = 2
FRAME_CTRL_POSITION_REQUIRE_ACK = 3
FRAME_CTRL_POSITION_FRAG        = 4

DEFAULT_PACKAGE_LENGTH = 20
PACKAGE_HEADER_LENGTH = 4
MIN_PACKAGE_LENGTH = 20
NEG_SECURITY_SET_TOTAL_LENGTH = 0x00
NEG_SECURITY_SET_ALL_DATA = 0x01

# Blufi CTRL / DATA enums
class CTRL(object):
    PACKAGE_VALUE = 0x00

    SUBTYPE_ACK = 0x00
    SUBTYPE_SET_SEC_MODE = 0x01
    SUBTYPE_SET_OP_MODE = 0x02
    SUBTYPE_CONNECT_WIFI = 0x03
    SUBTYPE_DISCONNECT_WIFI = 0x04
    SUBTYPE_GET_WIFI_STATUS = 0x05
    SUBTYPE_DEAUTHENTICATE = 0x06
    SUBTYPE_GET_VERSION = 0x07
    SUBTYPE_CLOSE_CONNECTION = 0x08
    SUBTYPE_GET_WIFI_LIST = 0x09

class DATA(object):
    PACKAGE_VALUE = 0x01

    SUBTYPE_NEG = 0x00
    SUBTYPE_STA_WIFI_BSSID = 0x01
    SUBTYPE_STA_WIFI_SSID = 0x02
    SUBTYPE_STA_WIFI_PASSWORD = 0x03
    SUBTYPE_SOFTAP_WIFI_SSID = 0x04
    SUBTYPE_SOFTAP_WIFI_PASSWORD = 0x05
    SUBTYPE_SOFTAP_MAX_CONNECTION_COUNT = 0x06
    SUBTYPE_SOFTAP_AUTH_MODE = 0x07
    SUBTYPE_SOFTAP_CHANNEL = 0x08
    SUBTYPE_USERNAME = 0x09
    SUBTYPE_CA_CERTIFICATION = 0x0a
    SUBTYPE_CLIENT_CERTIFICATION = 0x0b
    SUBTYPE_SERVER_CERTIFICATION = 0x0c
    SUBTYPE_CLIENT_PRIVATE_KEY = 0x0d
    SUBTYPE_SERVER_PRIVATE_KEY = 0x0e
    SUBTYPE_WIFI_CONNECTION_STATE = 0x0f
    SUBTYPE_VERSION = 0x10
    SUBTYPE_WIFI_LIST = 0x11
    SUBTYPE_ERROR = 0x12
    SUBTYPE_CUSTOM_DATA = 0x13
    SUBTYPE_WIFI_STA_MAX_CONN_RETRY = 0x14
    SUBTYPE_WIFI_STA_CONN_END_REASON = 0x15
    SUBTYPE_WIFI_STA_CONN_RSSI = 0x16


DIRECTION_OUTPUT = 0
DIRECTION_INPUT = 1

OP_MODE_NULL = 0x00
OP_MODE_STA = 0x01
OP_MODE_SOFTAP = 0x02
OP_MODE_STASOFTAP = 0x03

SOFTAP_SECURITY_OPEN = 0x00
SOFTAP_SECURITY_WEP = 0x01
SOFTAP_SECURITY_WPA = 0x02
SOFTAP_SECURITY_WPA2 = 0x03
SOFTAP_SECURITY_WPA_WPA2 = 0x04

STA_CONN_SUCCESS = 0x00
STA_CONN_FAIL = 0x01
STA_CONN_CONNECTING = 0X02
STA_CONN_NO_IP = 0x03

WIFI_REASON_4WAY_HANDSHAKE_TIMEOUT = 15
WIFI_REASON_NO_AP_FOUND = 201
WIFI_REASON_HANDSHAKE_TIMEOUT = 204
WIFI_REASON_CONNECTION_FAIL = 205