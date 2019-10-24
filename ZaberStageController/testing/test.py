from labscript import *
from labscript_devices.DummyPseudoclock.labscript_devices import DummyPseudoclock

MOCK = True
labscript_init('test.h5', new=True, overwrite=True)

from labscript_devices.ZaberStageController.labscript_devices import (
    ZaberStageTLS28M,
    ZaberStageController,
)
from labscript import start, stop

DummyPseudoclock()
ZaberStageController('controller', com_port='COM1', mock=MOCK)
ZaberStageTLS28M('stage', controller, 'stage 1')
ZaberStageTLS28M('stage2', controller, 'stage 2')

start()

stage.constant(65465)

stop(1)