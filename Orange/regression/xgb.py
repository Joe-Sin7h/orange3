# pylint: disable=too-many-arguments
from typing import Tuple
import sys

import numpy as np
import xgboost

from Orange.base import XGBBase
from Orange.data import Variable, ContinuousVariable, Table
from Orange.preprocess.score import LearnerScorer
from Orange.regression import Learner

__all__ = ["XGBRegressor", "XGBRFRegressor"]

# Temporary workaround for https://github.com/dmlc/xgboost/issues/7156
N_JOBS = 1 if sys.platform == "darwin" else None


class _FeatureScorerMixin(LearnerScorer):
    feature_type = Variable
    class_type = ContinuousVariable

    def score(self, data: Table) -> Tuple[np.ndarray, Tuple[Variable]]:
        model: XGBBase = self(data)
        return model.skl_model.feature_importances_, model.domain.attributes


class XGBRegressor(XGBBase, Learner, _FeatureScorerMixin):
    __wraps__ = xgboost.XGBRegressor

    def __init__(self,
                 max_depth=None,
                 learning_rate=None,
                 n_estimators=100,
                 verbosity=None,
                 objective="reg:squarederror",
                 booster=None,
                 tree_method=None,
                 n_jobs=N_JOBS,
                 gamma=None,
                 min_child_weight=None,
                 max_delta_step=None,
                 subsample=None,
                 colsample_bytree=None,
                 colsample_bylevel=None,
                 colsample_bynode=None,
                 reg_alpha=None,
                 reg_lambda=None,
                 scale_pos_weight=None,
                 base_score=None,
                 random_state=None,
                 missing=np.nan,
                 num_parallel_tree=None,
                 monotone_constraints=None,
                 interaction_constraints=None,
                 importance_type="gain",
                 gpu_id=None,
                 validate_parameters=None,
                 preprocessors=None):
        super().__init__(max_depth=max_depth, learning_rate=learning_rate,
                         n_estimators=n_estimators, verbosity=verbosity,
                         objective=objective, booster=booster,
                         tree_method=tree_method, n_jobs=n_jobs, gamma=gamma,
                         min_child_weight=min_child_weight,
                         max_delta_step=max_delta_step, subsample=subsample,
                         colsample_bytree=colsample_bytree,
                         colsample_bylevel=colsample_bylevel,
                         colsample_bynode=colsample_bynode,
                         reg_alpha=reg_alpha, reg_lambda=reg_lambda,
                         scale_pos_weight=scale_pos_weight,
                         base_score=base_score, random_state=random_state,
                         missing=missing, num_parallel_tree=num_parallel_tree,
                         monotone_constraints=monotone_constraints,
                         interaction_constraints=interaction_constraints,
                         importance_type=importance_type, gpu_id=gpu_id,
                         validate_parameters=validate_parameters,
                         preprocessors=preprocessors)


class XGBRFRegressor(XGBBase, Learner, _FeatureScorerMixin):
    __wraps__ = xgboost.XGBRFRegressor

    def __init__(self,
                 max_depth=None,
                 learning_rate=None,
                 n_estimators=100,
                 verbosity=None,
                 objective="reg:squarederror",
                 booster=None,
                 tree_method=None,
                 n_jobs=N_JOBS,
                 gamma=None,
                 min_child_weight=None,
                 max_delta_step=None,
                 subsample=None,
                 colsample_bytree=None,
                 colsample_bylevel=None,
                 colsample_bynode=None,
                 reg_alpha=None,
                 reg_lambda=None,
                 scale_pos_weight=None,
                 base_score=None,
                 random_state=None,
                 missing=np.nan,
                 num_parallel_tree=None,
                 monotone_constraints=None,
                 interaction_constraints=None,
                 importance_type="gain",
                 gpu_id=None,
                 validate_parameters=None,
                 preprocessors=None):
        super().__init__(max_depth=max_depth, learning_rate=learning_rate,
                         n_estimators=n_estimators, verbosity=verbosity,
                         objective=objective, booster=booster,
                         tree_method=tree_method, n_jobs=n_jobs, gamma=gamma,
                         min_child_weight=min_child_weight,
                         max_delta_step=max_delta_step, subsample=subsample,
                         colsample_bytree=colsample_bytree,
                         colsample_bylevel=colsample_bylevel,
                         colsample_bynode=colsample_bynode,
                         reg_alpha=reg_alpha, reg_lambda=reg_lambda,
                         scale_pos_weight=scale_pos_weight,
                         base_score=base_score, random_state=random_state,
                         missing=missing, num_parallel_tree=num_parallel_tree,
                         monotone_constraints=monotone_constraints,
                         interaction_constraints=interaction_constraints,
                         importance_type=importance_type, gpu_id=gpu_id,
                         validate_parameters=validate_parameters,
                         preprocessors=preprocessors)
