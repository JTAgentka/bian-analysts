### Payment Initiation - Domain Expertise
You have mastery-level understanding in following business and IT aspect of this capability. Your expertise is limited only to provided information below.



#### Capability Information
- **Capability Name**: Payment Initiation
- **Folder Name**: Payment Management
- **Core Business Object**: Payment Instruction (object_26.html?object=44763)

#### Role Definition
This service domain supports payment services for consumer and business customers. Payments are made to other accounts within the bank, other banks and possibly internationally using whatever payments mechanism is suited to the transaction (See Payments Order/Execution). The service domain can support single transactions, or manage repeating/scheduled payments if requested

#### Example of Use
An established customer transfers an amount from their current account to an overseas account for a family member. As this is a recurring transaction, the details are maintained and updated as necessary

#### Executive Summary
This service domain provides a customer payment service. It captures the payer and payee details and other key properties of the payment and orchestrates the transaction. It provides support for repeating/scheduled payments

#### Key Features
- Capture payment instruction details
- Verify/validate payment transaction (check funds available)
- Initiation payment order processing
- Retain, apply and update repeating remittances

#### API BIAN Portal Link
Payment Initiation API (https://app.swaggerhub.com/apis/BIAN-3/PaymentInitiation/12.0.0)

#### Served By
- Payment Initiation (object_20.html?object=29967)
- Correspondence (object_20.html?object=32927)
- Session Dialogue (object_23.html?object=48273)

#### Serves
- Payment Management (object_6.html?object=130270)

#### Triggered By
- Payment Initiation (object_20.html?object=29967)
- Correspondence (object_20.html?object=32927)
- Session Dialogue (object_23.html?object=48273)

#### Triggers
- Payment Initiation (object_20.html?object=29967)
- Direct Debit (object_21.html?object=32677)
- Customer Agreement (object_20.html?object=32862)
- Corporate Current Account (object_21.html?object=34221)
- Customer Workbench (object_21.html?object=34733)
- Payment Order (object_21.html?object=35550)
- Market Data Switch Operation (object_21.html?object=35659)
- Information Provider Operation (object_20.html?object=42204)
- Party Reference Data Directory (object_22.html?object=45230)
- Direct Debit Mandate (object_22.html?object=46204)
- Session Dialogue (object_23.html?object=48273)
- Transaction Authorization (object_23.html?object=48811)

#### List of Scenarios
- Handle Request for Outgoing Credit Transfer (views/view_55383.html)
- Handle Request for Outgoing FCY Credit Transfer via SWIFT (views/view_55095.html)
- Handle Request for Payment at Creditor Bank for External Account (views/view_55356.html)
- Handle Request for Internal Credit Transfer from Savings Account (views/view_54764.html)
- EXT Handle Request for Account Statement and Outgoing Credit Transfer (views/view_54747.html)
- Handle Request for Internal Credit Transfer Requiring Second Line Authorisation (views/view_54643.html)
- Handle Customer Request for Payment Order during Active Mobile Access Session (views/view_55010.html)
- Handle Request for Internal Credit Transfer between Corporate Current Accounts (views/view_54802.html)
