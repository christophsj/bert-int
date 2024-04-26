from interaction_model.clean_attribute_data import run_clean_attribute_data
from interaction_model.get_attributeValue_embedding import get_attribute_value_embedding
from interaction_model.get_entity_embedding import get_entity_embedding
from interaction_model.get_neighView_and_desView_interaction_feature import get_neighView_and_desView_interaction_feature
from interaction_model.get_attributeView_interaction_feature import get_attributeView_interaction_feature
from interaction_model.interaction_model import run_interaction_model



if __name__ == '__main__':
    run_clean_attribute_data()
    get_entity_embedding()
    get_attribute_value_embedding()
    get_neighView_and_desView_interaction_feature()
    get_attributeView_interaction_feature()
    run_interaction_model()
# python -u clean_attribute_data.py
# python -u get_entity_embedding.py
# python -u get_attributeValue_embedding.py
# python -u get_neighView_and_desView_interaction_feature.py
# python -u get_attributeView_interaction_feature.py
# python -u interaction_model.py