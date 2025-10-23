### Transaction Authorization - Domain Expertise
You have mastery-level understanding in following business and IT aspect of this capability. Your expertise is limited only to provided information below.



#### Role Definition
This service domain is used to mitigate transaction risk for interactive product and service access fulfillment and works in collaboration with customer identity authentication services. It analyses recent customer activity in order to detect possible out of pattern/fraudulent behavior and authorizes transactions accordingly. The authorization can be subject to obtaining increased levels of customer authentication by requiring the customer to provide additional proof of identity.

#### Folder Name
Money Movement Management

#### Core Business Object
Not specified in the document

#### Example of Use
A customer payment request from their current account is authorized during an assisted servicing session

#### Executive Summary
This service domain handles risk based authorization for interactive customer transactions. This combines the context (channel) transaction, customer details and recent activity analysis as appropriate. The authorization may require a specific level of party/customer authentication to get approval.

#### Key Features
- Consolidate details of proposed customer transaction
- Analyze recent channel activity for out of pattern customer behavior
- Detect fraud/unwanted activity - raise authentication requirements

#### API BIAN Portal Link
https://app.swaggerhub.com/apis/BIAN-3/TransactionAuthorization/12.0.0

#### Service Relationships

### Served By
- External Access Framework (object_25.html?object=127286)
- Cross Channel (object_25.html?object=130605)
- Wave 1 (object_25.html?object=153747)
- Cross Channel (object_25.html?object=171776)
- TPP Backend (object_25.html?object=83605)
- ASPSP Backend (object_25.html?object=85535)

### Serves
- Money Movement Management (object_6.html?object=130159)

### Triggered By
- Payment Initiation (object_20.html?object=29967)
- Servicing Order (object_21.html?object=32295)
- Processing Order (object_20.html?object=33179)
- Customer Offer (object_22.html?object=39968)
- Contact Handler (object_20.html?object=41839)
- Session Dialogue (object_23.html?object=48273)
- Transaction Authorization (object_23.html?object=48811)

### Triggers
- Party Lifecycle Management (object_20.html?object=29780)
- Customer Access Entitlement (object_20.html?object=30136)
- Servicing Mandate (object_21.html?object=35374)
- Fraud Evaluation (object_22.html?object=39639)
- Transaction Authorization (object_23.html?object=48811)

#### List of Scenarios
- EXT Handle Request for Overdraft Limit on Virtual Account (views/view_55055.html)
- EXT Handle Request to Add Account to Sweep Agreement (views/view_55061.html)
- Initiate Payment Order (views/view_54825.html)
- EXT Handle Request to Move Overdraft Limit between Virtual Accounts (views/view_54989.html)
- EXT Handle Request for High Volume Account Opening (views/view_54681.html)
- EXT Handle Merchandising Loan Application (views/view_55092.html)
- EXT Handle Request to Open Retail Current Account (views/view_55487.html)
- EXT Handle Customer Relationships Case (views/view_55529.html)
- EXT Handle Request to Reactivate Dormant Corporate Current Account (views/view_55347.html)
- EXT Handle Request to Change Corporate Current Account Ownership (views/view_55493.html)
- EXT Handle Request to Pre-Open Corporate Current Account (views/view_55077.html)
- EXT Handle Request to Add Signatory to Corporate Current Account (views/view_55296.html)
- EXT Process B2B Direct Debit Mandate Notice from Creditor Bank at Debtor Bank (views/view_55425.html)
- EXT Handle Bulk Request for Opening Salary Accounts (views/view_55326.html)
- EXT Handle Request to Use Direct Debits as Payment Instrument (views/view_55260.html)
- Get Customer Request and Show Account Balance (views/view_55475.html)
- EXT Handle Request to Terminate Sweep Agreement (views/view_55499.html)
- EXT Handle Instruction to Terminate B2B Direct Debits Service at Creditor Bank (views/view_55440.html)
- EXT Handle Request to Change Virtual Account Ownership (views/view_55562.html)
- EXT Handle Request to Close Virtual Account (views/view_55455.html)
- EXT Handle Request for High Volume Virtual Account Opening (views/view_55266.html)
- Handle Request to Get Customer Account Balance (views/view_55284.html)
- EXT Handle Request to Close Corporate Current Account (views/view_55101.html)
- EXT Handle Request for Combined Account Statement (views/view_55637.html)
- EXT Handle Request for Renewal of Uncollateralised Consumer Loan (views/view_55034.html)
- EXT Handle Request to Detach Account from Corporate Payroll Service Agreement (views/view_54714.html)
- 1 - Initiate Consent (views/view_39366.html)
- 3 - Initiate Consent (views/view_44841.html)
- EXT Handle Request for Preferential Rates for Corporate Current Account (views/view_54889.html)
- EXT Handle Request for Account Statement and Outgoing Credit Transfer (views/view_54747.html)
