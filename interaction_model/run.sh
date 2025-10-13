#!/bin/sh
python3 -u clean_attribute_data.py
python3 -u get_entity_embedding.py
python3 -u get_attributeValue_embedding.py
python3 -u get_neighView_and_desView_interaction_feature.py
python3 -u get_attributeView_interaction_feature.py
python3 -u interaction_model.py
