# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.io import MySQLSink
def test_MySQLSink_inputs():
    input_map = dict(username=dict(),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    database_name=dict(mandatory=True,
    ),
    host=dict(xor=['config'],
    mandatory=True,
    requires=['username', 'password'],
    usedefault=True,
    ),
    table_name=dict(mandatory=True,
    ),
    password=dict(),
    config=dict(mandatory=True,
    xor=['host'],
    ),
    )
    inputs = MySQLSink.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value