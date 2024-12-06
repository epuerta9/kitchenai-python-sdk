# AgentResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** |  | 

## Example

```python
from kitchenai_python_sdk.models.agent_response_schema import AgentResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AgentResponseSchema from a JSON string
agent_response_schema_instance = AgentResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AgentResponseSchema.to_json())

# convert the object into a dict
agent_response_schema_dict = agent_response_schema_instance.to_dict()
# create an instance of AgentResponseSchema from a dict
agent_response_schema_from_dict = AgentResponseSchema.from_dict(agent_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


