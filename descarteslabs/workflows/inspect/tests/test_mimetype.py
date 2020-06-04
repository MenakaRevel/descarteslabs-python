import pytest

from collections import OrderedDict

from ..mimetype import format_to_mimetype


@pytest.mark.parametrize(
    "format, expected",
    [
        ({"type": "pyarrow"}, "application/vnd.pyarrow"),
        ({"type": "json"}, "application/json"),
        ({"type": "geotiff"}, "image/tiff"),
    ],
)
def test_format_to_mimetype_no_options(format, expected):
    mimetype = format_to_mimetype(format)
    assert mimetype == expected


def test_format_to_mimetype_with_options():
    mimetype = format_to_mimetype(
        OrderedDict([("type", "pyarrow"), ("compression", "lz4"), ("other_param", 1)])
    )
    # TODO: Remove OrderedDict from this test once we drop support for py3.5
    assert mimetype == "application/vnd.pyarrow; compression=lz4; other_param=1"


def test_format_to_mimetype_with_not_options():
    mimetype = format_to_mimetype(
        OrderedDict([("type", "geotiff"), ("overviews", False)])
    )
    # TODO: Remove OrderedDict from this test once we drop support for py3.5
    assert mimetype == "image/tiff; overviews=False"


def test_format_to_mimetype_invalid():
    with pytest.raises(
        ValueError, match="The format dictionary must include a serialization type"
    ):
        format_to_mimetype({"foo": "bar"})
    with pytest.raises(ValueError, match="Output format for inspect"):
        format_to_mimetype({"type": "foo"})

    with pytest.raises(AssertionError, match="Format options keys must be"):
        format_to_mimetype({"type": "pyarrow", 1: "lz4"})

    with pytest.raises(AssertionError, match="Format options values must be"):
        format_to_mimetype({"type": "pyarrow", "compression": [1, 2, 3]})
