{
  "typeName" : "AWS::ApiGateway::RestApi",
  "description" : "The ``AWS::ApiGateway::RestApi`` resource creates a REST API. For more information, see [restapi:create](https://docs.aws.amazon.com/apigateway/latest/api/API_CreateRestApi.html) in the *Amazon API Gateway REST API Reference*.\n On January 1, 2016, the Swagger Specification was donated to the [OpenAPI initiative](https://docs.aws.amazon.com/https://www.openapis.org/), becoming the foundation of the OpenAPI Specification.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "additionalProperties" : false,
  "definitions" : {
    "EndpointConfiguration" : {
      "type" : "object",
      "additionalProperties" : false,
      "properties" : {
        "Types" : {
          "type" : "array",
          "uniqueItems" : true,
          "items" : {
            "type" : "string"
          },
          "description" : "A list of endpoint types of an API (RestApi) or its custom domain name (DomainName). For an edge-optimized API and its custom domain name, the endpoint type is ``\"EDGE\"``. For a regional API and its custom domain name, the endpoint type is ``REGIONAL``. For a private API, the endpoint type is ``PRIVATE``."
        },
        "VpcEndpointIds" : {
          "type" : "array",
          "uniqueItems" : true,
          "items" : {
            "type" : "string"
          },
          "description" : "A list of VpcEndpointIds of an API (RestApi) against which to create Route53 ALIASes. It is only supported for ``PRIVATE`` endpoint type."
        }
      },
      "description" : "The ``EndpointConfiguration`` property type specifies the endpoint types of a REST API.\n ``EndpointConfiguration`` is a property of the [AWS::ApiGateway::RestApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html) resource."
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : false,
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "required" : [ "Key", "Value" ],
      "description" : ""
    },
    "S3Location" : {
      "type" : "object",
      "additionalProperties" : false,
      "properties" : {
        "Bucket" : {
          "type" : "string",
          "description" : "The name of the S3 bucket where the OpenAPI file is stored."
        },
        "ETag" : {
          "type" : "string",
          "description" : "The Amazon S3 ETag (a file checksum) of the OpenAPI file. If you don't specify a value, API Gateway skips ETag validation of your OpenAPI file."
        },
        "Version" : {
          "type" : "string",
          "description" : "For versioning-enabled buckets, a specific version of the OpenAPI file."
        },
        "Key" : {
          "type" : "string",
          "description" : "The file name of the OpenAPI file (Amazon S3 object name)."
        }
      },
      "description" : "``S3Location`` is a property of the [AWS::ApiGateway::RestApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html) resource that specifies the Amazon S3 location of a OpenAPI (formerly Swagger) file that defines a set of RESTful APIs in JSON or YAML.\n On January 1, 2016, the Swagger Specification was donated to the [OpenAPI initiative](https://docs.aws.amazon.com/https://www.openapis.org/), becoming the foundation of the OpenAPI Specification."
    }
  },
  "properties" : {
    "RestApiId" : {
      "type" : "string",
      "description" : ""
    },
    "RootResourceId" : {
      "type" : "string",
      "description" : ""
    },
    "ApiKeySourceType" : {
      "type" : "string",
      "description" : "The source of the API key for metering requests according to a usage plan. Valid values are: ``HEADER`` to read the API key from the ``X-API-Key`` header of a request. ``AUTHORIZER`` to read the API key from the ``UsageIdentifierKey`` from a custom authorizer."
    },
    "BinaryMediaTypes" : {
      "type" : "array",
      "uniqueItems" : true,
      "items" : {
        "type" : "string"
      },
      "description" : "The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads."
    },
    "Body" : {
      "type" : [ "object", "string" ],
      "description" : "An OpenAPI specification that defines a set of RESTful APIs in JSON format. For YAML templates, you can also provide the specification in YAML format."
    },
    "BodyS3Location" : {
      "$ref" : "#/definitions/S3Location",
      "description" : "The Amazon Simple Storage Service (Amazon S3) location that points to an OpenAPI file, which defines a set of RESTful APIs in JSON or YAML format."
    },
    "CloneFrom" : {
      "type" : "string",
      "description" : "The ID of the RestApi that you want to clone from."
    },
    "EndpointConfiguration" : {
      "$ref" : "#/definitions/EndpointConfiguration",
      "description" : "A list of the endpoint types of the API. Use this property when creating an API. When importing an existing API, specify the endpoint configuration types using the ``Parameters`` property."
    },
    "Description" : {
      "type" : "string",
      "description" : "The description of the RestApi."
    },
    "DisableExecuteApiEndpoint" : {
      "type" : "boolean",
      "description" : "Specifies whether clients can invoke your API by using the default ``execute-api`` endpoint. By default, clients can invoke your API with the default ``https://{api_id}.execute-api.{region}.amazonaws.com`` endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint"
    },
    "FailOnWarnings" : {
      "type" : "boolean",
      "description" : "A query parameter to indicate whether to rollback the API update (``true``) or not (``false``) when a warning is encountered. The default value is ``false``."
    },
    "Name" : {
      "type" : "string",
      "description" : "The name of the RestApi. A name is required if the REST API is not based on an OpenAPI specification."
    },
    "MinimumCompressionSize" : {
      "type" : "integer",
      "description" : "A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size."
    },
    "Mode" : {
      "type" : "string",
      "description" : "This property applies only when you use OpenAPI to define your REST API. The ``Mode`` determines how API Gateway handles resource updates.\n Valid values are ``overwrite`` or ``merge``. \n For ``overwrite``, the new API definition replaces the existing one. The existing API identifier remains unchanged.\n  For ``merge``, the new API definition is merged with the existing API.\n If you don't specify this property, a default value is chosen. For REST APIs created before March 29, 2021, the default is ``overwrite``. For REST APIs created after March 29, 2021, the new API definition takes precedence, but any container types such as endpoint configurations and binary media types are merged with the existing API. \n Use the default mode to define top-level ``RestApi`` properties in addition to using OpenAPI. Generally, it's preferred to use API Gateway's OpenAPI extensions to model these properties."
    },
    "Policy" : {
      "type" : [ "object", "string" ],
      "description" : "A policy document that contains the permissions for the ``RestApi`` resource. To set the ARN for the policy, use the ``!Join`` intrinsic function with ``\"\"`` as delimiter and values of ``\"execute-api:/\"`` and ``\"*\"``."
    },
    "Parameters" : {
      "type" : [ "object", "string" ],
      "additionalProperties" : false,
      "patternProperties" : {
        "[a-zA-Z0-9]+" : {
          "type" : "string"
        }
      },
      "description" : "Custom header parameters as part of the request. For example, to exclude DocumentationParts from an imported API, set ``ignore=documentation`` as a ``parameters`` value, as in the AWS CLI command of ``aws apigateway import-rest-api --parameters ignore=documentation --body 'file:///path/to/imported-api-body.json'``."
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : false,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "description" : "The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with ``aws:``. The tag value can be up to 256 characters."
    }
  },
  "tagging" : {
    "taggable" : true,
    "tagOnCreate" : true,
    "tagUpdatable" : true,
    "cloudFormationSystemTags" : true,
    "tagProperty" : "/properties/Tags"
  },
  "primaryIdentifier" : [ "/properties/RestApiId" ],
  "readOnlyProperties" : [ "/properties/RestApiId", "/properties/RootResourceId" ],
  "writeOnlyProperties" : [ "/properties/Body", "/properties/BodyS3Location", "/properties/CloneFrom", "/properties/FailOnWarnings", "/properties/Mode", "/properties/Parameters" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "apigateway:GET", "apigateway:POST", "apigateway:PUT", "apigateway:PATCH", "apigateway:UpdateRestApiPolicy", "s3:GetObject", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "apigateway:GET" ]
    },
    "update" : {
      "permissions" : [ "apigateway:GET", "apigateway:DELETE", "apigateway:PATCH", "apigateway:PUT", "apigateway:UpdateRestApiPolicy", "s3:GetObject", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "apigateway:DELETE" ]
    },
    "list" : {
      "permissions" : [ "apigateway:GET" ]
    }
  }
}
