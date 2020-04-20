from typing import Union
from inspect import Parameter, Signature

from ..primitives import Str, Float, Int, Bool, NoneType
from ..array import Array, MaskedArray, Scalar, DType
from ..containers import List, Tuple, Slice


EMPTY = Parameter.empty
VAR_P = Parameter.VAR_POSITIONAL
VAR_KW = Parameter.VAR_KEYWORD
KW_ONLY = Parameter.KEYWORD_ONLY

Param = lambda name, annotation=None, default=EMPTY, kind=Parameter.POSITIONAL_OR_KEYWORD: Parameter(  # noqa: E731
    name, kind=kind, default=default, annotation=annotation
)
Sig = lambda parameters, return_annotation: Signature(  # noqa: E731
    parameters=parameters, return_annotation=return_annotation
)

# TODO: Once interpret-time compute is available, change Scalar return types to
#   more specific types, if possible

NUMPY_SIGNATURES = {
    "all": [
        Sig([Param("a", Array), Param("axis", Union[Int, List[Int]], None)], Array),
        Sig(
            [Param("a", Union[Array, MaskedArray]), Param("axis", NoneType, None)],
            Scalar,  # TODO: Bool
        ),
        Sig(
            [Param("a", MaskedArray), Param("axis", Union[Int, List[Int]], None)],
            MaskedArray,
        ),
    ],
    "allclose": Sig(
        [
            Param("a", Union[Array, MaskedArray, Scalar]),
            Param("b", Union[Array, MaskedArray, Scalar]),
            Param("rtol", Union[Int, Float], 1e-05),
            Param("atol", Union[Int, Float], 1e-08),
            Param("equal_nan", Bool, False),
        ],
        Scalar,  # TODO: Bool
    ),
    "angle": [
        Sig([Param("z", Array), Param("deg", Bool, False)], Array),
        Sig([Param("z", MaskedArray), Param("deg", Bool, False)], Array),
    ],
    "any": [
        Sig([Param("a", Array), Param("axis", Union[Int, List[Int]], None)], Array),
        Sig(
            [Param("a", Union[Array, MaskedArray]), Param("axis", NoneType, None)],
            Scalar,  # TODO: Bool
        ),
        Sig(
            [Param("a", MaskedArray), Param("axis", Union[Int, List[Int]], None)],
            MaskedArray,
        ),
    ],
    "arange": [
        Sig([Param("stop", Union[Int, Float, Scalar])], Array),
        Sig(
            [
                Param("start", Union[Int, Float, Scalar]),
                Param("stop", Union[Int, Float, Scalar]),
                Param("step", Union[Int, Float, Scalar]),
            ],
            Array,
        ),
    ],
    "argmax": [
        Sig([Param("a", Union[Array, MaskedArray]), Param("axis", Int, None)], Array),
        Sig(
            [Param("a", Union[Array, MaskedArray]), Param("axis", NoneType, None)],
            Scalar,  # TODO: Int
        ),
    ],
    "argmin": [
        Sig([Param("a", Union[Array, MaskedArray]), Param("axis", Int, None)], Array),
        Sig(
            [Param("a", Union[Array, MaskedArray]), Param("axis", NoneType, None)],
            Scalar,  # TODO: Int
        ),
    ],
    "argwhere": Sig([Param("a", Union[Array, MaskedArray])], Array),
    "around": [
        Sig([Param("a", Array), Param("decimals", Int, 0)], Array),
        Sig([Param("a", MaskedArray), Param("decimals", Int, 0)], MaskedArray),
        Sig([Param("a", Scalar), Param("decimals", Int, 0)], Scalar),
    ],
    "atleast_1d": [
        Sig([Param("arys", Union[Array, Scalar])], Array),
        Sig([Param("arys", MaskedArray)], MaskedArray),
        Sig([Param("arys", Union[Array, Scalar], kind=VAR_P)], List[Array]),
        Sig([Param("arys", MaskedArray, kind=VAR_P)], List[MaskedArray]),
    ],
    "atleast_2d": [
        Sig([Param("arys", Union[Array, Scalar])], Array),
        Sig([Param("arys", MaskedArray)], MaskedArray),
        Sig([Param("arys", Union[Array, Scalar], kind=VAR_P)], List[Array]),
        Sig([Param("arys", MaskedArray, kind=VAR_P)], List[MaskedArray]),
    ],
    "atleast_3d": [
        Sig([Param("arys", Union[Array, Scalar])], Array),
        Sig([Param("arys", MaskedArray)], MaskedArray),
        Sig([Param("arys", Union[Array, Scalar], kind=VAR_P)], List[Array]),
        Sig([Param("arys", MaskedArray, kind=VAR_P)], List[MaskedArray]),
    ],
    "average": [
        Sig(
            [
                Param("a", Array),
                Param("axis", Union[Int, List[Int]], None),
                Param("weights", Union[Array, MaskedArray, Scalar], None),
            ],
            Array,
        ),
        Sig(
            [
                Param("a", MaskedArray),
                Param("axis", Union[Int, List[Int]], None),
                Param("weights", Union[Array, MaskedArray, Scalar], None),
            ],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", Union[Array, MaskedArray, Scalar]),
                Param("axis", NoneType, None),
                Param("weights", Union[Array, MaskedArray, Scalar], None),
            ],
            Scalar,  # TODO: Float
        ),
    ],
    "bincount": Sig(
        [
            Param("x", Union[Array, MaskedArray]),
            Param("weights", Union[Array, MaskedArray, NoneType], None),
            Param("minlength", Int, 0),
        ],
        Array,
    ),
    "broadcast_arrays": [
        Sig([Param("args", Array, kind=VAR_P)], List[Array]),
        Sig([Param("args", MaskedArray, kind=VAR_P)], List[MaskedArray]),
    ],
    "broadcast_to": [
        Sig([Param("array", Array), Param("shape", List[Int])], Array),
        Sig([Param("array", MaskedArray), Param("shape", List[Int])], MaskedArray),
    ],
    "clip": [
        Sig(
            [
                Param("a", Array),
                Param("a_min", Union[Int, Float, Scalar, Array]),
                Param("a_max", Union[Int, Float, Scalar, Array]),
            ],
            Array,
        ),
        Sig(
            [
                Param("a", Array),
                Param("a_min", MaskedArray),
                Param("a_max", MaskedArray),
            ],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", MaskedArray),
                Param("a_min", Union[Int, Float, Scalar, Array, MaskedArray]),
                Param("a_max", Union[Int, Float, Scalar, Array, MaskedArray]),
            ],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", Scalar),
                Param("a_min", Union[Int, Float, Scalar]),
                Param("a_max", Union[Int, Float, Scalar]),
            ],
            Scalar,
        ),
        Sig([Param("a", Scalar), Param("a_min", Array), Param("a_max", Array)], Array),
        Sig(
            [
                Param("a", Scalar),
                Param("a_min", MaskedArray),
                Param("a_max", MaskedArray),
            ],
            MaskedArray,
        ),
    ],
    "compress": [
        Sig(
            [
                Param("condition", Union[Array, MaskedArray]),
                Param("a", Array),
                Param("axis", Union[Int, NoneType], None),
            ],
            Array,
        ),
        Sig(
            [
                Param("condition", Union[Array, MaskedArray]),
                Param("a", MaskedArray),
                Param("axis", Union[Int, NoneType], None),
            ],
            MaskedArray,
        ),
    ],
    "concatenate": [
        Sig([Param("arrays", List[Array]), Param("axis", Int, 0)], Array),
        Sig([Param("arrays", List[MaskedArray]), Param("axis", Int, 0)], MaskedArray),
    ],
    "corrcoef": [
        Sig(
            [
                Param("x", Array),
                Param("y", Union[Array, NoneType], None),
                Param("rowvar", Bool, True),
            ],
            Array,
        ),
        Sig(
            [
                Param("x", Array),
                Param("y", MaskedArray, None),
                Param("rowvar", Bool, True),
            ],
            MaskedArray,
        ),
        Sig(
            [
                Param("x", MaskedArray),
                Param("y", Union[Array, MaskedArray, NoneType], None),
                Param("rowvar", Bool, True),
            ],
            MaskedArray,
        ),
    ],
    "count_nonzero": [
        Sig([Param("a", Array), Param("axis", Int, None)], Array),
        Sig([Param("a", MaskedArray), Param("axis", Int, None)], MaskedArray),
        Sig(
            [
                Param("a", Union[Array, MaskedArray, Scalar]),
                Param("axis", NoneType, None),
            ],
            Scalar,
        ),
    ],
    "cov": [
        Sig(
            [
                Param("m", Array),
                Param("y", Union[Array, NoneType], None),
                Param("rowvar", Bool, True),
                Param("bias", Bool, False),
                Param("ddof", Union[Int, NoneType], None),
                Param("fweights", Union[Array, Int, NoneType], None),
                Param("aweights", Union[Array, NoneType], None),
            ],
            Array,
        ),
        Sig(
            [
                Param("m", Array),
                Param("y", MaskedArray, None),
                Param("rowvar", Bool, True),
                Param("bias", Bool, False),
                Param("ddof", Union[Int, NoneType], None),
                Param("fweights", Union[Array, Int, NoneType], None),
                Param("aweights", Union[Array, NoneType], None),
            ],
            MaskedArray,
        ),
        Sig(
            [
                Param("m", MaskedArray),
                Param("y", Union[Array, MaskedArray, NoneType], None),
                Param("rowvar", Bool, True),
                Param("bias", Bool, False),
                Param("ddof", Union[Int, NoneType], None),
                Param("fweights", Union[Array, Int, NoneType], None),
                Param("aweights", Union[Array, NoneType], None),
            ],
            MaskedArray,
        ),
    ],
    "cumprod": [
        Sig(
            [
                Param("a", Union[Array, Scalar]),
                Param("axis", Union[Int, NoneType], None),
                Param("dtype", Union[DType, NoneType], None),
            ],
            Array,
        ),
        Sig(
            [
                Param("a", MaskedArray),
                Param("axis", Union[Int, NoneType], None),
                Param("dtype", Union[DType, NoneType], None),
            ],
            MaskedArray,
        ),
    ],
    "cumsum": [
        Sig(
            [
                Param("a", Union[Array, Scalar]),
                Param("axis", Union[Int, NoneType], None),
                Param("dtype", Union[DType, NoneType], None),
            ],
            Array,
        ),
        Sig(
            [
                Param("a", MaskedArray),
                Param("axis", Union[Int, NoneType], None),
                Param("dtype", Union[DType, NoneType], None),
            ],
            MaskedArray,
        ),
    ],
    "diag": Sig([Param("v", Union[Array, MaskedArray])], Array),
    "diagonal": [
        Sig(
            [
                Param("a", Array),
                Param("offset", Int, 0),
                Param("axis1", Int, 0),
                Param("axis2", Int, 1),
            ],
            Array,
        ),
        Sig(
            [
                Param("a", MaskedArray),
                Param("offset", Int, 0),
                Param("axis1", Int, 0),
                Param("axis2", Int, 1),
            ],
            MaskedArray,
        ),
    ],
    "diff": [
        Sig([Param("a", Array), Param("n", Int, 1), Param("axis", Int, -1)], Array),
        Sig(
            [Param("a", MaskedArray), Param("n", Int, 1), Param("axis", Int, -1)],
            MaskedArray,
        ),
    ],
    "digitize": [
        Sig(
            [
                Param("x", Union[Array, MaskedArray]),
                Param("bins", Union[Array, MaskedArray]),
                Param("right", Bool, False),
            ],
            Array,
        ),
        Sig(
            [
                Param("x", Scalar),
                Param("bins", Union[Array, MaskedArray]),
                Param("right", Bool, False),
            ],
            Scalar,
        ),
    ],
    "dot": Sig(
        [Param("a", Union[Array, MaskedArray]), Param("b", Union[Array, MaskedArray])],
        Scalar,
    ),
    "dstack": [
        Sig([Param("arrays", List[Array])], Array),
        Sig([Param("arrays", List[MaskedArray])], MaskedArray),
    ],
    "ediff1d": [
        Sig(
            [
                Param("ary", Union[Array, Scalar]),
                Param("to_end", Union[Array, Scalar, NoneType], None),
                Param("to_begin", Union[Array, Scalar, NoneType], None),
            ],
            Array,
        ),
        Sig(
            [
                Param("ary", Union[Array, Scalar]),
                Param("to_end", Union[Array, Scalar, NoneType], None),
                Param("to_begin", MaskedArray, None),
            ],
            MaskedArray,
        ),
        Sig(
            [
                Param("ary", Union[Array, Scalar]),
                Param("to_end", MaskedArray, None),
                Param("to_begin", Union[Array, Scalar, NoneType], None),
            ],
            MaskedArray,
        ),
        Sig(
            [
                Param("ary", Union[Array, Scalar]),
                Param("to_end", MaskedArray, None),
                Param("to_begin", MaskedArray, None),
            ],
            MaskedArray,
        ),
        Sig(
            [
                Param("ary", MaskedArray),
                Param("to_end", Union[Array, MaskedArray, Scalar, NoneType], None),
                Param("to_begin", Union[Array, MaskedArray, Scalar, NoneType], None),
            ],
            MaskedArray,
        ),
    ],
    "einsum": Sig(
        [
            Param("subscripts", Str),
            Param("operands", Union[Array, List[Array]]),
            Param("dtype", Union[DType, NoneType], None),
        ],
        Array,
    ),
    "eye": Sig(
        [
            Param("N", Int),
            Param("M", Union[Int, NoneType], None),
            Param("k", Int, 0),
            Param("dtype", DType, DType(float)),
        ],
        Array,
    ),
    "fix": [
        Sig([Param("x", Array)], Array),
        Sig([Param("x", MaskedArray)], MaskedArray),
        Sig([Param("x", Scalar)], Scalar),
    ],
    "flatnonzero": Sig([Param("a", Union[Array, MaskedArray, Scalar])], Array),
    "full": Sig(
        [
            Param("shape", Union[Int, List[Int]]),
            Param("fill_value", Union[Array, MaskedArray, Scalar, Int, Float, Bool]),
            Param("dtype", Union[DType, NoneType], None),
        ],
        Array,
    ),
    "full_like": Sig(
        [
            Param("a", Union[Array, MaskedArray, Scalar]),
            Param("fill_value", Union[Array, MaskedArray, Scalar, Int, Float, Bool]),
            Param("dtype", Union[DType, NoneType], None),
        ],
        Array,
    ),
    "gradient": [
        Sig(
            [
                Param("f", Array),
                Param("varargs", Union[Int, List[Int], Array], kind=VAR_P),
                Param("edge_order", Int, 1, kind=KW_ONLY),
                Param("axis", Union[Int, NoneType], None, kind=KW_ONLY),
            ],
            List[Array],
        ),
        Sig(
            [
                Param("f", MaskedArray),
                Param("varargs", Union[Int, List[Int], Array], kind=VAR_P),
                Param("edge_order", Int, 1, kind=KW_ONLY),
                Param("axis", Union[Int, NoneType], None, kind=KW_ONLY),
            ],
            List[MaskedArray],
        ),
    ],
    "histogram": Sig(
        [
            Param("a", Array),
            Param("bins", Union[List[Int], List[Float], Int], 10),
            Param("range", Union[Tuple[Int, Int], Tuple[Float, Float], NoneType], None),
            Param("weights", Union[Array, NoneType], None),
            Param("density", Union[Bool, NoneType], None),
        ],
        Tuple[Array, Array],
    ),
    "hstack": [
        Sig([Param("arrays", List[Array])], Array),
        Sig([Param("arrays", List[MaskedArray])], MaskedArray),
    ],
    "imag": [
        Sig([Param("val", Union[Array, Scalar])], Array),
        Sig([Param("val", MaskedArray)], MaskedArray),
    ],
    "indices": Sig(
        [
            Param("dimensions", Union[List[Int], List[Float], List[Bool]]),
            Param("dtype", DType, DType(int)),
        ],
        Array,
    ),
    "insert": [
        Sig(
            [
                Param("arr", Array),
                Param("obj", Union[Int, List[Int], Slice]),
                Param("values", Union[Array, MaskedArray, Scalar]),
                Param("axis", Int),
            ],
            Array,
        ),
        Sig(
            [
                Param("arr", MaskedArray),
                Param("obj", Union[Int, List[Int], Slice]),
                Param("values", Union[Array, MaskedArray, Scalar]),
                Param("axis", Int),
            ],
            MaskedArray,
        ),
    ],
    "isclose": [
        Sig(
            [
                Param("a", Array),
                Param("b", Union[Array, Scalar]),
                Param("rtol", Union[Int, Float], 1e-05),
                Param("atol", Union[Int, Float], 1e-08),
                Param("equal_nan", Bool, False),
            ],
            Array,
        ),
        Sig(
            [
                Param("a", Array),
                Param("b", MaskedArray),
                Param("rtol", Union[Int, Float], 1e-05),
                Param("atol", Union[Int, Float], 1e-08),
                Param("equal_nan", Bool, False),
            ],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", MaskedArray),
                Param("b", Union[Array, MaskedArray, Scalar]),
                Param("rtol", Union[Int, Float], 1e-05),
                Param("atol", Union[Int, Float], 1e-08),
                Param("equal_nan", Bool, False),
            ],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", Scalar),
                Param("b", Array),
                Param("rtol", Union[Int, Float], 1e-05),
                Param("atol", Union[Int, Float], 1e-08),
                Param("equal_nan", Bool, False),
            ],
            Array,
        ),
        Sig(
            [
                Param("a", Scalar),
                Param("b", Scalar),
                Param("rtol", Union[Int, Float], 1e-05),
                Param("atol", Union[Int, Float], 1e-08),
                Param("equal_nan", Bool, False),
            ],
            Scalar,
        ),
    ],
    "isin": [
        Sig(
            [
                Param("element", Union[Array, MaskedArray]),
                Param("test_elements", Union[Array, MaskedArray, Scalar]),
                Param("assume_unique", Bool, False),
                Param("invert", Bool, False),
            ],
            Array,
        ),
        Sig(
            [
                Param("element", Scalar),
                Param("test_elements", Union[Array, MaskedArray]),
                Param("assume_unique", Bool, False),
                Param("invert", Bool, False),
            ],
            Array,
        ),
        Sig(
            [
                Param("element", Scalar),
                Param("test_elements", Scalar),
                Param("assume_unique", Bool, False),
                Param("invert", Bool, False),
            ],
            Scalar,
        ),
    ],
    "isreal": [
        Sig([Param("x", Array)], Array),
        Sig([Param("x", MaskedArray)], MaskedArray),
        Sig([Param("x", Scalar)], Scalar),
    ],
    "linspace": [
        Sig(
            [
                Param("start", Union[Int, Float]),
                Param("stop", Union[Int, Float]),
                Param("num", Int, 50),
                Param("endpoint", Bool, True),
                Param("retstep", Bool, False),
                Param("dtype", Union[DType, NoneType], None),
                Param("axis", Int, 0),
            ],
            Array,
        )
    ],
    "max": [
        Sig([Param("a", Array), Param("axis", Union[Int, List[Int]], None)], Array),
        Sig(
            [Param("a", MaskedArray), Param("axis", Union[Int, List[Int]], None)],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", Union[Array, MaskedArray, Scalar]),
                Param("axis", NoneType, None),
            ],
            Scalar,
        ),
    ],
    "mean": [
        Sig([Param("a", Array), Param("axis", Union[Int, List[Int]], None)], Array),
        Sig(
            [Param("a", MaskedArray), Param("axis", Union[Int, List[Int]], None)],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", Union[Array, MaskedArray, Scalar]),
                Param("axis", NoneType, None),
            ],
            Scalar,  # TODO: Float
        ),
    ],
    "meshgrid": Sig(
        [
            Param("xi", Union[Array, MaskedArray, Scalar], kind=VAR_P),
            Param("indexing", Str, "xy", kind=KW_ONLY),
            Param("sparse", Bool, False, kind=KW_ONLY),
        ],
        List[Array],
    ),
    "min": [
        Sig([Param("a", Array), Param("axis", Union[Int, List[Int]], None)], Array),
        Sig(
            [Param("a", MaskedArray), Param("axis", Union[Int, List[Int]], None)],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", Union[Array, MaskedArray, Scalar]),
                Param("axis", NoneType, None),
            ],
            Scalar,
        ),
    ],
    "moveaxis": [
        Sig(
            [
                Param("a", Array),
                Param("source", Union[Int, List[Int]]),
                Param("destination", Union[Int, List[Int]]),
            ],
            Array,
        ),
        Sig(
            [
                Param("a", MaskedArray),
                Param("source", Union[Int, List[Int]]),
                Param("destination", Union[Int, List[Int]]),
            ],
            MaskedArray,
        ),
    ],
    "nanargmax": [
        Sig([Param("a", Union[Array, MaskedArray]), Param("axis", Int, None)], Array),
        Sig(
            [Param("a", Union[Array, MaskedArray]), Param("axis", NoneType, None)],
            Scalar,  # TODO: Int
        ),
    ],
    "nanargmin": [
        Sig([Param("a", Union[Array, MaskedArray]), Param("axis", Int, None)], Array),
        Sig(
            [Param("a", Union[Array, MaskedArray]), Param("axis", NoneType, None)],
            Scalar,  # TODO: Int
        ),
    ],
    "nancumprod": [
        Sig(
            [
                Param("a", Union[Array, Scalar]),
                Param("axis", Union[Int, NoneType], None),
                Param("dtype", Union[DType, NoneType], None),
            ],
            Array,
        ),
        Sig(
            [
                Param("a", MaskedArray),
                Param("axis", Union[Int, NoneType], None),
                Param("dtype", Union[DType, NoneType], None),
            ],
            MaskedArray,
        ),
    ],
    "nancumsum": [
        Sig(
            [
                Param("a", Union[Array, Scalar]),
                Param("axis", Union[Int, NoneType], None),
                Param("dtype", Union[DType, NoneType], None),
            ],
            Array,
        ),
        Sig(
            [
                Param("a", MaskedArray),
                Param("axis", Union[Int, NoneType], None),
                Param("dtype", Union[DType, NoneType], None),
            ],
            MaskedArray,
        ),
    ],
    "nanmax": [
        Sig([Param("a", Array), Param("axis", Union[Int, List[Int]], None)], Array),
        Sig(
            [Param("a", MaskedArray), Param("axis", Union[Int, List[Int]], None)],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", Union[Array, MaskedArray, Scalar]),
                Param("axis", NoneType, None),
            ],
            Scalar,
        ),
    ],
    "nanmean": [
        Sig([Param("a", Array), Param("axis", Union[Int, List[Int]], None)], Array),
        Sig(
            [Param("a", MaskedArray), Param("axis", Union[Int, List[Int]], None)],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", Union[Array, MaskedArray, Scalar]),
                Param("axis", NoneType, None),
            ],
            Scalar,  # TODO: Float
        ),
    ],
    "nanmin": [
        Sig([Param("a", Array), Param("axis", Union[Int, List[Int]], None)], Array),
        Sig(
            [Param("a", MaskedArray), Param("axis", Union[Int, List[Int]], None)],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", Union[Array, MaskedArray, Scalar]),
                Param("axis", NoneType, None),
            ],
            Scalar,
        ),
    ],
    "nanprod": [
        Sig([Param("a", Scalar), Param("axis", NoneType, None)], Scalar),
        Sig([Param("a", Array), Param("axis", Union[Int, List[Int]], None)], Array),
        Sig(
            [Param("a", MaskedArray), Param("axis", Union[Int, List[Int]], None)],
            MaskedArray,
        ),
    ],
    "nanstd": [
        Sig([Param("a", Array), Param("axis", Union[Int, List[Int]], None)], Array),
        Sig(
            [Param("a", MaskedArray), Param("axis", Union[Int, List[Int]], None)],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", Union[Array, MaskedArray, Scalar]),
                Param("axis", NoneType, None),
            ],
            Scalar,  # TODO: Float
        ),
    ],
    "nansum": [
        Sig([Param("a", Array), Param("axis", Union[Int, List[Int]], None)], Array),
        Sig(
            [Param("a", MaskedArray), Param("axis", Union[Int, List[Int]], None)],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", Union[Array, MaskedArray, Scalar]),
                Param("axis", NoneType, None),
            ],
            Scalar,
        ),
    ],
    "nanvar": [
        Sig(
            [
                Param("a", Union[Array, MaskedArray]),
                Param("axis", NoneType, None),
                Param("ddof", Int, 0),
            ],
            Scalar,
        ),  # TODO: Float
        Sig(
            [
                Param("a", Union[Array, MaskedArray]),
                Param("axis", Union[Int, List[Int]], None),
                Param("ddof", Int, 0),
            ],
            Array,
        ),
    ],
    "nan_to_num": [
        Sig([Param("x", Array)], Array),
        Sig([Param("x", MaskedArray)], MaskedArray),
        Sig([Param("x", Scalar)], Scalar),
    ],
    "nonzero": Sig([Param("a", Union[Array, MaskedArray, Scalar])], List[Array]),
    "ones": Sig(
        [Param("shape", Union[Int, List[Int]]), Param("dtype", DType, DType(float))],
        Array,
    ),
    "ones_like": Sig(
        [
            Param("a", Union[Array, MaskedArray, Scalar]),
            Param("dtype", Union[DType, NoneType], None),
        ],
        Array,
    ),
    "outer": Sig(
        [
            Param("a", Union[Array, MaskedArray, Scalar]),
            Param("b", Union[Array, MaskedArray, Scalar]),
        ],
        Array,
    ),
    "pad": [
        Sig(
            [
                Param("array", Union[Array, Scalar]),
                Param("pad_width", Union[Int, List[Int]]),
                Param("mode", Str, "constant"),
            ],
            Array,
        ),
        Sig(
            [
                Param("array", MaskedArray),
                Param("pad_width", Union[Int, List[Int]]),
                Param("mode", Str, "constant"),
            ],
            MaskedArray,
        ),
    ],
    "percentile": Sig(
        [
            Param("a", Union[Array, MaskedArray]),
            Param("q", Union[Array, MaskedArray]),
            Param("axis", Union[Int, List[Int], NoneType], None),
            Param("interpolation", Str, "linear"),
        ],
        Array,
    ),
    "ptp": [
        Sig([Param("a", Array), Param("axis", Union[Int, List[Int]], None)], Array),
        Sig(
            [Param("a", MaskedArray), Param("axis", Union[Int, List[Int]], None)],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", Union[Array, MaskedArray, Scalar]),
                Param("axis", NoneType, None),
            ],
            Scalar,
        ),
    ],
    "reshape": [
        Sig([Param("a", Array), Param("newshape", List[Int])], Array),
        Sig([Param("a", MaskedArray), Param("newshape", List[Int])], MaskedArray),
    ],
    "stack": [
        Sig([Param("arrays", List[Array]), Param("axis", Int, 0)], Array),
        Sig([Param("arrays", List[MaskedArray]), Param("axis", Int, 0)], MaskedArray),
    ],
    "std": [
        Sig([Param("a", Array), Param("axis", Union[Int, List[Int]], None)], Array),
        Sig(
            [Param("a", MaskedArray), Param("axis", Union[Int, List[Int]], None)],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", Union[Array, MaskedArray, Scalar]),
                Param("axis", NoneType, None),
            ],
            Scalar,  # TODO: Float
        ),
    ],
    "sum": [
        Sig([Param("a", Array), Param("axis", Union[Int, List[Int]], None)], Array),
        Sig(
            [Param("a", MaskedArray), Param("axis", Union[Int, List[Int]], None)],
            MaskedArray,
        ),
        Sig(
            [
                Param("a", Union[Array, MaskedArray, Scalar]),
                Param("axis", NoneType, None),
            ],
            Scalar,
        ),
    ],
    "transpose": [
        Sig(
            [Param("a", Array), Param("axes", Union[List[Int], NoneType], None)], Array
        ),
        Sig(
            [Param("a", MaskedArray), Param("axes", Union[List[Int], NoneType], None)],
            MaskedArray,
        ),
    ],
    "var": [
        Sig(
            [
                Param("a", Union[Array, MaskedArray]),
                Param("axis", NoneType, None),
                Param("ddof", Int, 0),
            ],
            Scalar,
        ),  # TODO: Float
        Sig(
            [
                Param("a", Union[Array, MaskedArray]),
                Param("axis", Union[Int, List[Int]], None),
                Param("ddof", Int, 0),
            ],
            Array,
        ),
    ],
    "vstack": [
        Sig([Param("arrays", List[Array])], Array),
        Sig([Param("arrays", List[MaskedArray])], MaskedArray),
    ],
    "zeros": Sig(
        [Param("shape", Union[Int, List[Int]]), Param("dtype", DType, DType(float))],
        Array,
    ),
}


DISPLAY_SIGNATURE_OVERRIDES = {
    "arange": Sig(
        [
            Param("start", Union[Int, Float, Scalar], 0),
            Param("stop", Union[Int, Float, Scalar], None),
            Param("step", Union[Int, Float, Scalar], 1),
        ],
        Array,
    ),
    "atleast_1d": Sig(
        [Param("arys", Union[Array, MaskedArray, Scalar], kind=VAR_P)],
        Union[Array, MaskedArray, List[Array], List[MaskedArray]],
    ),
    "atleast_2d": Sig(
        [Param("arys", Union[Array, MaskedArray, Scalar], kind=VAR_P)],
        Union[Array, MaskedArray, List[Array], List[MaskedArray]],
    ),
    "atleast_3d": Sig(
        [Param("arys", Union[Array, MaskedArray, Scalar], kind=VAR_P)],
        Union[Array, MaskedArray, List[Array], List[MaskedArray]],
    ),
}


SKIP_NP_TESTING = ["arange", "eye", "full", "indices", "ones", "zeros"]
# ^ Skip testing the NumPy versions of certain functions that don't
# work because of validation NumPy does that requires operations
# that proxy types don't support (conditionals)
