# Task Overview
You are tasked with ensuring proper access control for the product management API. The POST and PUT operations for products must be strictly protected using OAuth2 bearer token authentication so that only authorized clients can modify product data. Currently, these restrictions are not enforced, allowing unauthenticated access.

# Guidance
- Review the router setup and authentication dependency usage in the API code.
- Focus on the authentication mechanism applied to the POST and PUT endpoints.
- Address only the specific security issue without changing unrelated application logic or structure.

# Objectives
- Enforce OAuth2 bearer token authentication strictly for POST and PUT product endpoints.
- Ensure that unauthorized requests are rejected with appropriate error codes.
- Make only the necessary changes required to restore the expected security posture.

# How to Verify
- Attempt to create or update a product without providing a bearer token and confirm that the server responds with a 401 Unauthorized error.
- Retry the same operations with the valid token and verify that access is granted and the action succeeds.
