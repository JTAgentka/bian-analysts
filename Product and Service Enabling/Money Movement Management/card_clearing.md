### Card Clearing - Domain Expertise
You have mastery-level understanding in following business and IT aspect of this capability. Your expertise is limited only to provided information below.



#### Role Definition
The behavior varies depending on the role of the participant bank/network. A card acquiring Bank consolidates all incoming transactions from Merchants, determining their routing, and transmitting to the respective Card Networks. For the Card Networks it receives and consolidates the transactions from all Acquiring Banks and to distribute and route them to the respective Card Issuing Banks. For the Card Issuing Banks it receives their cardholder transactions from the Card Networks and routes them to the instance of the Credit/Charge Card service domain which is responsible for the card used in the transaction. The transactions may include charges, refunds, and chargebacks.

#### Folder Name
Money Movement Management

#### Core Business Object
Card Clearing (object_26.html?object=35470)

#### Example of Use
An Acquiring Bank receives charge transactions submitted by Merchants through Point of Sale Terminals or batch submission for recurring billing and forwards these transactions to the respective Card Issuing Banks through the Card Network (e.g. Visa, MC, AMEX, Diners, etc.). This process may take place multiple times during the day.

#### Executive Summary
This service domain orchestrates the capture and consolidation of card financial transactions originating from various sources, such as POS Network, E-Commerce Gateway, ATM Network, or Card Case Management. It also handles the clearing of the transactions from the Acquirers to the Issuers through the Card Networks

#### Key Features
- Card transaction capture and addressing
- FX conversion and fee handling
- Transaction matching and reconciliation
- Transaction routing

#### API BIAN Portal Link
https://app.swaggerhub.com/apis/BIAN-3/CardClearing/12.0.0

#### Service Relationships

### Served By
- Wave 2 (object_25.html?object=153742)
- Clearing And Settlement (object_25.html?object=171759)

### Serves
- Money Movement Management (object_6.html?object=130159)

### Triggered By
- Financial Gateway (object_20.html?object=29241)
- Card Case (object_21.html?object=30796)
- Operational Gateway (object_21.html?object=32276)
- Card Financial Settlement (object_21.html?object=34230)
- Card Clearing (object_21.html?object=36804)

### Triggers
- Financial Gateway (object_20.html?object=29241)
- Card Case (object_21.html?object=30796)
- Operational Gateway (object_21.html?object=32276)
- Product Directory (object_21.html?object=34953)
- Card Transaction Capture (object_21.html?object=35397)
- Payment Order (object_21.html?object=35550)
- Market Data Switch Operation (object_21.html?object=35659)
- Card Clearing (object_21.html?object=36804)
- Corporate Treasury (object_21.html?object=37090)
- Fraud Evaluation (object_22.html?object=39639)
- Credit Card (object_22.html?object=40448)
- Financial Accounting (object_20.html?object=42346)
- Merchant Acquiring Facility (object_20.html?object=42530)
- Card Network Participant Facility (object_22.html?object=42759)
- Card Authorization (object_22.html?object=44578)

#### List of Scenarios
- Process Card Clearing by Issuer (views/view_55194.html)
- Handle Request for Chargeback at Acquirer (views/view_55230.html)
- Process Settlement by Acquirer (views/view_55526.html)
- Process Card Clearing by Acquirer (views/view_55404.html)
- Handle Card Chargeback at Issuer (views/view_55464.html)
- Process Transaction Booking (views/view_55666.html)
- Handle Request for Information for Chargeback at Acquirer (views/view_55149.html)
- Process Card Clearing by Card Network (views/view_55080.html)
- Process Settlement by Issuer (views/view_55004.html)
