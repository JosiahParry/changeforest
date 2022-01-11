import numpy as np
import pytest

from changeforest import changeforest


@pytest.mark.parametrize("method", ["knn", "change_in_mean", "random_forest"])
@pytest.mark.parametrize("segmentation_type", ["sbs", "wbs", "bs"])
def test_changeforest(iris_dataset, method, segmentation_type):
    result = changeforest(iris_dataset, method, segmentation_type)
    np.testing.assert_array_equal(result.split_points(), [50, 100])


def test_changeforest_repr(iris_dataset):
    result = changeforest(iris_dataset, "random_forest", "bs")
    assert (
        result.__repr__()
        == """\
                    best_split max_gain p_value
(0, 150]                    50   96.322    0.01
 ¦--(0, 50]                 23   -5.239       1
 °--(50, 150]              100   50.527    0.01
     ¦--(50, 100]           80   -5.557       1
     °--(100, 150]         134   -7.433       1\
"""
    )
