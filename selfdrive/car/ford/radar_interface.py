#!/usr/bin/env python3
from cereal import car
from selfdrive.car.interfaces import RadarInterfaceBase
import time


class RadarInterface(RadarInterfaceBase):

  def update(self, can_strings):

    ret = car.RadarData.new_message()
    time.sleep(0.05)  # radard runs on RI updates

    return ret
