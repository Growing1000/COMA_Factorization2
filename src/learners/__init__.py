from .q_learner import QLearner
from .coma_learner import COMALearner
from .qtran_learner import QLearner as QTranLearner
from .comafac_learner import COMAFACLearner
from .facmac_learner import FACMACLearner

REGISTRY = {}

REGISTRY["q_learner"] = QLearner
REGISTRY["coma_learner"] = COMALearner
REGISTRY["qtran_learner"] = QTranLearner
REGISTRY["comafac_learner"] = COMAFACLearner
REGISTRY["facmac_learner"] = FACMACLearner