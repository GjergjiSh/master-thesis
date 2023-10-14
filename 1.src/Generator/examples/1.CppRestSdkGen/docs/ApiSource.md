```c++
{>licenseInfo}}
{{#operations}}

#include "{{packageName}}/api/{{classname}}.h"
#include "{{packageName}}/IHttpBody.h"
#include "{{packageName}}/JsonBody.h"
#include "{{packageName}}/MultipartFormData.h"

#include <boost/algorithm/string/replace.hpp>

#include <unordered_set>

{{#apiNamespaceDeclarations}}
namespace {{this}} {
{{/apiNamespaceDeclarations}}

using namespace {{modelNamespace}};

{{classname}}::{{classname}}( std::shared_ptr<const ApiClient> apiClient )
    : m_ApiClient(apiClient)
{
}

{{classname}}::~{{classname}}()
{
}

{{#operation}}
pplx::task<{{{returnType}}}{{^returnType}}void{{/returnType}}> {{classname}}::{{operationId}}({{#allParams}}{{^required}}boost::optional<{{/required}}{{{dataType}}}{{^required}}>{{/required}} {{paramName}}{{^-last}}, {{/-last}}{{/allParams}}) const
{
{{#allParams}}{{#required}}{{^isPrimitiveType}}{{^isContainer}}
    // verify the required parameter '{{paramName}}' is set
    if ({{paramName}} == nullptr)
    {
        throw ApiException(400, utility::conversions::to_string_t("Missing required parameter '{{paramName}}' when calling {{classname}}->{{operationId}}"));
    }
{{/isContainer}}{{/isPrimitiveType}}{{/required}}{{/allParams}}

    std::shared_ptr<const ApiConfiguration> localVarApiConfiguration( m_ApiClient->getConfiguration() );
    utility::string_t localVarPath = utility::conversions::to_string_t("{{{path}}}");
    {{#pathParams}}
    boost::replace_all(localVarPath, utility::conversions::to_string_t("{") + utility::conversions::to_string_t("{{baseName}}") + utility::conversions::to_string_t("}"), web::uri::encode_uri(ApiClient::parameterToString({{{paramName}}})));
    {{/pathParams}}

    std::map<utility::string_t, utility::string_t> localVarQueryParams;
    std::map<utility::string_t, utility::string_t> localVarHeaderParams( localVarApiConfiguration->getDefaultHeaders() );
    std::map<utility::string_t, utility::string_t> localVarFormParams;
    std::map<utility::string_t, std::shared_ptr<HttpContent>> localVarFileParams;

    std::unordered_set<utility::string_t> localVarResponseHttpContentTypes;
    {{#produces}}
    localVarResponseHttpContentTypes.insert( utility::conversions::to_string_t("{{{mediaType}}}") );
    {{/produces}}

    utility::string_t localVarResponseHttpContentType;

    // use JSON if possible
    if ( localVarResponseHttpContentTypes.size() == 0 )
    {
        {{#vendorExtensions.x-codegen-response.isString}}
        localVarResponseHttpContentType = utility::conversions::to_string_t("text/plain");
        {{/vendorExtensions.x-codegen-response.isString}}
        {{^vendorExtensions.x-codegen-response.isString}}
        localVarResponseHttpContentType = utility::conversions::to_string_t("application/json");
        {{/vendorExtensions.x-codegen-response.isString}}
    }
    // JSON
    else if ( localVarResponseHttpContentTypes.find(utility::conversions::to_string_t("application/json")) != localVarResponseHttpContentTypes.end() )
    {
        localVarResponseHttpContentType = utility::conversions::to_string_t("application/json");
    }
    // multipart formdata
    else if( localVarResponseHttpContentTypes.find(utility::conversions::to_string_t("multipart/form-data")) != localVarResponseHttpContentTypes.end() )
    {
        localVarResponseHttpContentType = utility::conversions::to_string_t("multipart/form-data");
    }
    {{#vendorExtensions.x-codegen-response.isString}}
    // plain text
    else if( localVarResponseHttpContentTypes.find(utility::conversions::to_string_t("text/plain")) != localVarResponseHttpContentTypes.end() )
    {
        localVarResponseHttpContentType = utility::conversions::to_string_t("text/plain");
    }
    {{/vendorExtensions.x-codegen-response.isString}}
    {{#vendorExtensions.x-codegen-response-ishttpcontent}}
    else
    {
        //It's going to be binary, so just use the first one.
        localVarResponseHttpContentType = *localVarResponseHttpContentTypes.begin();
    }
    {{/vendorExtensions.x-codegen-response-ishttpcontent}}
    {{^vendorExtensions.x-codegen-response-ishttpcontent}}
    else
    {
        throw ApiException(400, utility::conversions::to_string_t("{{classname}}->{{operationId}} does not produce any supported media type"));
    }
    {{/vendorExtensions.x-codegen-response-ishttpcontent}}

    localVarHeaderParams[utility::conversions::to_string_t("Accept")] = localVarResponseHttpContentType;

    std::unordered_set<utility::string_t> localVarConsumeHttpContentTypes;
    {{#consumes}}
    localVarConsumeHttpContentTypes.insert( utility::conversions::to_string_t("{{{mediaType}}}") );
    {{/consumes}}

    {{#allParams}}
    {{^isBodyParam}}
    {{^isPathParam}}
    {{#required}}
        {{^isPrimitiveType}}
        {{^isContainer}}
    if ({{paramName}} != nullptr)
        {{/isContainer}}
        {{/isPrimitiveType}}
    {{/required}}
    {{^required}}
        {{^isPrimitiveType}}
        {{^isContainer}}
    if ({{paramName}} && *{{paramName}} != nullptr)
        {{/isContainer}}
        {{/isPrimitiveType}}
        {{#isPrimitiveType}}
        {{#isFile}}
    if ({{paramName}} && *{{paramName}} != nullptr)
        {{/isFile}}
        {{^isFile}}
    if ({{paramName}})
        {{/isFile}}
        {{/isPrimitiveType}}
        {{#isContainer}}
    if ({{paramName}})
        {{/isContainer}}
    {{/required}}
    {
        {{#isQueryParam}}
        localVarQueryParams[utility::conversions::to_string_t("{{baseName}}")] = ApiClient::parameterToString({{^required}}*{{/required}}{{paramName}});
        {{/isQueryParam}}
        {{#isHeaderParam}}
        localVarHeaderParams[utility::conversions::to_string_t("{{baseName}}")] = ApiClient::parameterToString({{^required}}*{{/required}}{{paramName}});
        {{/isHeaderParam}}
        {{#isFormParam}}
        {{#isFile}}
        localVarFileParams[ utility::conversions::to_string_t("{{baseName}}") ] = {{^required}}*{{/required}}{{paramName}};
        {{/isFile}}
        {{^isFile}}
        localVarFormParams[ utility::conversions::to_string_t("{{baseName}}") ] = ApiClient::parameterToString({{^required}}*{{/required}}{{paramName}});
        {{/isFile}}
        {{/isFormParam}}
    }
    {{/isPathParam}}
    {{/isBodyParam}}
    {{/allParams}}

```