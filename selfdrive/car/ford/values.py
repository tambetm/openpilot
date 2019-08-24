from selfdrive.car import dbc_dict

MAX_ANGLE = 87.  # make sure we never command the extremes (0xfff) which cause latching fault

class CAR:
  FUSION = "FORD FUSION 2018"
  MONDEO = "FORD MONDEO 2016"

FINGERPRINTS = {
  CAR.FUSION: [{
    71: 8, 74: 8, 75: 8, 76: 8, 90: 8, 92: 8, 93: 8, 118: 8, 119: 8, 120: 8, 125: 8, 129: 8, 130: 8, 131: 8, 132: 8, 133: 8, 145: 8, 146: 8, 357: 8, 359: 8, 360: 8, 361: 8, 376: 8, 390: 8, 391: 8, 392: 8, 394: 8, 512: 8, 514: 8, 516: 8, 531: 8, 532: 8, 534: 8, 535: 8, 560: 8, 578: 8, 604: 8, 613: 8, 673: 8, 827: 8, 848: 8, 934: 8, 935: 8, 936: 8, 947: 8, 963: 8, 970: 8, 972: 8, 973: 8, 984: 8, 992: 8, 994: 8, 997: 8, 998: 8, 1003: 8, 1034: 8, 1045: 8, 1046: 8, 1053: 8, 1054: 8, 1058: 8, 1059: 8, 1068: 8, 1072: 8, 1073: 8, 1082: 8, 1107: 8, 1108: 8, 1109: 8, 1110: 8, 1200: 8, 1427: 8, 1430: 8, 1438: 8, 1459: 8
  }],
  CAR.MONDEO: [{
    65: 8, 66: 8, 71: 8, 73: 8, 74: 8, 75: 8, 76: 8, 118: 8, 119: 8, 125: 8, 130: 8, 131: 8, 132: 8, 133: 8, 145: 8, 146: 8, 330: 8, 342: 8, 355: 8, 357: 8, 358: 8, 359: 8, 368: 8, 369: 8, 370: 8, 371: 8, 372: 8, 373: 8, 376: 8, 377: 8, 378: 8, 379: 8, 380: 8, 381: 8, 383: 8, 384: 8, 512: 8, 514: 8, 516: 8, 531: 8, 532: 8, 534: 8, 535: 8, 560: 8, 561: 8, 572: 8, 573: 8, 578: 8, 609: 8, 610: 8, 753: 8, 806: 8, 817: 8, 818: 8, 819: 8, 822: 8, 862: 8, 891: 8, 902: 8, 909: 8, 936: 8, 938: 8, 939: 8, 947: 8, 948: 8, 949: 8, 950: 8, 951: 8, 952: 8, 963: 8, 967: 8, 986: 8, 992: 8, 993: 8, 994: 8, 995: 8, 1002: 8, 1003: 8, 1034: 8, 1045: 8, 1046: 8, 1057: 8, 1068: 8, 1069: 8, 1071: 8, 1072: 8, 1076: 8, 1077: 8, 1078: 8, 1081: 8, 1084: 8, 1085: 8, 1086: 8, 1095: 8, 1109: 8, 1125: 8, 1126: 8, 1127: 8, 1200: 8, 1409: 8, 1438: 8, 1440: 8, 1506: 8
  }],
}

class ECU:
  CAM = 0

ECU_FINGERPRINT = {
  ECU.CAM: [970, 973, 984]
}

DBC = {
  CAR.FUSION: dbc_dict('ford_fusion_2018_pt', 'ford_fusion_2018_adas'),
  CAR.MONDEO: dbc_dict('ford_mondeo_2016_pt', 'ford_fusion_2018_adas'),
}
