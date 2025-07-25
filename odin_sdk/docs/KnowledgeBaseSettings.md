# KnowledgeBaseSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**chunking_strategy** | **str** | Chunking strategy to use. Options: sentence (spaCy sentence tokenizer), token (tiktoken), markdown (preserves markdown), json (for JSON data), character (character count based) | 
**embedding_model** | **str** | Embedding model to use. Options: BAAI/bge-small-en-v1.5 (384d), neuralmind/bert-base-portuguese-cased (768d), BAAI/bge-multilingual-gemma2 (3584d), Alibaba-NLP/gte-Qwen2-1.5B-instruct (1536d), Snowflake/snowflake-arctic-embed-m-v1.5, openai-ada (1536d) | [optional] [default to 'BAAI/bge-small-en-v1.5']
**chunk_size** | **int** | Size of chunks in tokens or characters depending on the strategy | [optional] [default to 64]
**chunk_overlap** | **int** | Number of overlapping tokens or characters between chunks | [optional] [default to 6]
**extraction_techniques** | **object** | Extraction techniques for different file types | [optional] 

## Example

```python
from odin_sdk.models.knowledge_base_settings import KnowledgeBaseSettings

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseSettings from a JSON string
knowledge_base_settings_instance = KnowledgeBaseSettings.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBaseSettings.to_json())

# convert the object into a dict
knowledge_base_settings_dict = knowledge_base_settings_instance.to_dict()
# create an instance of KnowledgeBaseSettings from a dict
knowledge_base_settings_from_dict = KnowledgeBaseSettings.from_dict(knowledge_base_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


