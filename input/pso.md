## Your Domain Expertise

## Structure Specification
**Note:** In this document:
- `###` denotes **Domain** level (e.g., Agreement Management, Payment Management)
- `####` denotes **Capability** level (e.g., Payment Initiation, Credit Facility)

---



You have mastery-level understanding following domains:

### Agreement Management (Contract Manager)  with its business capabilities and key functions

#### - **Customer/Product Agreement** – The Customer Agreement service domain captures and maintains the master legal terms of conditions in force for a customer (which as noted can be a complex multinational with many underlying product and service specific agreements).
#### - **Servicing Agreement** – The Servicing Mandate service domain maintains an agreement between the bank and an external party that governs/constrains the allowed access given to the bank's products and services. This access permission can be defined at two levels - overall for the service provider and at a more detailed level as applied to a specific customer..
#### - **Credit Line** – The Credit Facility Service Domain manages the Credit Facilities that a Corporate Customer has with the bank. A Credit Facility is an agreement between the bank and a (corporate) customer to allow the customer to acquire asset products from the bank up to the limit of the credit facility without the need for a full due diligence and underwriting for each of these products. Credit Facilities can have a hierarchy and they come under the overall Credit Limit for the customer, which is the bank-internal maximum credit exposure that the bank is willing to have with the customer.
#### - **Commercial Loan** – The corporate loan product may include different properties/features depending on a bank's preferences and policies. The loan is targeted at corporate customers and may be associated with a type of product and may or may not be secured by collateral..
#### - **Equipment Lease** – The Service Domain provides the financing support to support corporate customers with leasing arrangements for property and equipment. The bank will take a collateral interest in the leased items to underwrite the associated loan(s).

### Collateral Management (Collateral Manager) with its business capabilities and key functions

#### - **Collateral Allocation Management** – Collateral Allocation Management oversees the allocation of a party asset when pledged as collateral to one or more loans. Specific reference details of the asset are maintained in the Party Asset Directory Service Domain. The valuation of an asset is organized by the Party Asset Directory. A valuation can be requested by the Collateral Allocation Management Service Domain. Collateral Allocation Management also determines the portion of an asset value that can be applied or can still be applied as collateral. This will depend on the asset type and specific policies of the bank.
  **Business Object (Owner):** Collateral Asset Allocation
#### - **Collections** – Collateral liquidation for unpaid accounts
  **Business Object (Owner):** Collateral Asset Liquidation Procedure
#### - **Collateral Asset Administration** – This service domain handles the oversight, administration and confirmation of maintenance tasks associated with different types of collateral items. This includes arranging for scheduled and ad-hoc collateral valuations, item status/documentation and title checks and tracking upkeep actions that the item owner is obliged to undertake (such as insuring a house).
  **Business Object (Owner):** Collateral Asset Administrative Plan

### Financial Instrument Management (Financial Instruments Manager) with its business capabilities and key functions

#### - **Corporate Action** – Corporate actions cover a range of activities that directly impact the share price and hence the shareholders of a company. The main types of corporate action include stock splits and reversals, dividend (both cash and stock), rights issues, mergers and acquisitions and spin-offs. This service domain handles the required processing for a customer's securities that are held in custody by the bank
#### - **Currency Exchange** – This is an over the counter service where currency is exchanged and the transaction uses preferential rates and can include transaction fees. Note in some cases travelers checks can be handled as a pseudo currency within this capability. Note that Branch and teller currency inventory tracking and distribution is administered by Branch Currency Management and Branch Currency Distribution service domains
#### - **Custody Administration** – Administer the securities scrip (paper and electronic) holdings for a custodial arrangement. This includes administering the physical movements of securities, safe storage, the processing of associated dividends and interest and securities reporting
  **Business Object (Owner):** Custody Facility
#### - **ECM And DCM** – The service domain provides fulfillment services for the issuance of primary market equity and debt capital market instruments for corporate customers. It supports both private and public (IPO) placements and covers the specification, pricing and placement activities associated with issuance. (it does not include secondary market trading of the instrument)
#### - **Financial Instrument Reference Data Management** – Maintain a central reference directory of market traded asset/instrument details. The details are typically captured from one or more specialist market feeds that publish market asset/instrument details. It can include the result of internal reference data processing.
  **Business Object (Owner):** Financial Instrument Directory Entry
#### - **Financial Instrument Valuation** – Provide securities/asset valuation services. A wide range of valuation approaches can be applied to a range of different instrument/asset types. This Service Domain implements a process by which the most appropriate valuation method is selected and applied in the context of the valuation request and the purpose of the valuation. The fundamental pricing principle is based on an analysis of the present value of expected cash flows. This calculation involves identifying the expected cash flows, determining appropriate (range of)interest rates that might discount future cash flows and calculate the current value of future cash flows applying those interest rates
  **Business Object (Owner):** Market Asset Valuation Procedure
#### - **Financial Instrument Valuation** - Develop and maintain a portfolio of valuation models considering currency, interest rate, instrument quotes, indices, commodity prices and other market, liquidity and credit risk factors. Support the use of these models in trading and pricing activity
  **Business Object (Owner):** Market Asset Valuation Procedure
#### - **Private Placement** - Private placement covers the definition, pricing, placing and all supporting actions involved for a private offering of corporate equity or debt. A private placement avoids many of the more stringent regulatory constraints of a public offering but can only be placed with accredited investors. The associated equity or debt securities issued by the corporate do not need to be registered with the regulatory authorities
#### - **Financial Instrument Valuation** - A public offering involves the specification and packaging of corporate equity or bonds in the public markets to raise capital. This can be the initial public offering (IPO) when a private company is first taken public, and secondary/follow-on offerings to raise further capital. IPO's involve a broad range of financial analysis, auditing and regulatory approval actions. A lead bank and several underwriting banks may coordinate to underwrite the initiative. Secondary offerings can be dilutive (create additional shares) or non-dilutive (redistribute existing shares).
  **Business Object (Owner):** Market Asset Valuation Procedure


### Investment Portfolio Management (Portfolio Manager) with its business capabilities and key functions

#### - **Investment Portfolio Management** – Orchestrate the investment/ rebalancing of an investment portfolio to optimize gains remaining within the terms of the agreement  - Investiční poradenství.
  **Business Object (Owner):** Investment Portfolio
#### - **Investment Portfolio Analysis** – Perform scheduled and ad-hoc performance analysis on a customer's investment portfolio. This can include different types of analysis and performance comparisons.
  **Business Object (Owner):** Investment Portfolio
#### - **Hedge Fund Administration** – Hedge funds group accredited investors as limited partners to the fund with the fund manager as the general partner. As investors are restricted to being accredited a hedge funds is free to make more aggressive investment decisions and can generate higher returns. Fund income combines management and performance fees.
  **Business Object (Owner):** Not explicitly mentioned in the document
#### - **Mutual Fund Administration** – Mutual funds provide an investment vehicle to general investors and as such are highly regulated and tend to focus on lower risk/return investments. Mutual funds are allowed to charge investors a management fee, but unlike hedge funds the mutual fund manager is not permitted to share in the fund's performances.
  **Business Object (Owner):** Not explicitly mentioned in the document
#### - **Investment Portfolio Planning** – Agree the customer investment portfolio governing principles, risk appetite, management/trading guidelines and target portfolio profile. Identify any desired/target and 'out of bounds' securities/sectors. Ensure disclosures and related eligibility, suitability and other regulatory obligations are addressed and reflected in the agreement  - Investiční poradenství.
  **Business Object (Owner):** Investment Portfolio


### Issued Device Administration (Issued Device Manager) with its business capabilities and key functions
#### - **Issued Device Tracking**  This service domain tracks and reports on the state (e.g. suspended, flagged for possible fraud, cancelled) for all issued devices. This covers credit/debit cards and can include other identification devices such as keychain fobs and virtual authentication devices such as electronic signatures, passwords and keys. It may use an external service provider to obtain notifications and is responsible for providing notifications to external services when the bank detects problems with its own issued devices
  **Business Object (Owner):** Device
#### - **Issued Device Administration** – This service domain administers the inventory management and allocation/issuance for all issued devices and materials (e.g. cards). This covers credit/debit cards and can include other identification/authentication devices such as keychain fobs. It also handles virtual token inventory such as passwords, secret questions and biometric records (signatures, voice/image).
  **Business Object (Owner):** IssuedDeviceAllocationSystem


### Payment Management (Payment Manager) with its business capabilities and key functions

Payment Initiation → Payment Order → Payment Execution → Accounts Receivable
#### - **Payment Initiation** – This service domain supports payment services for consumer and business customers. Payments are made to other accounts within the bank, other banks and possibly internationally using whatever payments mechanism is suited to the transaction (See Payments Order/Execution). The service domain can support single transactions, or manage repeating/scheduled payments if requested
#### - **Payment Order** – Payment Order handles the internal bank and compliance checks and processing of funds transfers prior to initiating the actual mechanics of transfer which is handled by the service domain Payment Execution. This includes watch-list and other regulatory checks and applying any counterparty specific limits and payment preferences. It may also oversee payment netting arrangements between the bank and other counterparties
#### - **Payment Execution** – The Transaction Processing capability manages various types of account transactions from BISQ (Core Banking System) including card transactions, terminal transactions, loan/credit transactions, fees, and general transactions. This service domain publishes real-time transaction events to Digital Channels for both Czech and Slovak markets through Kafka event streams.
#### - **Direct Debit** – This service domain processes the creditor side of direct debit processing. Typically a creditor will submit a batch of direct debit requests. The process checks the required service mandates are in place and initiates the payment processing. It tracks payment and reports on completion or other processing issues that might arise (such as insufficient funds available).

### Product Management (Product Manager) with its business capabilities and key functions

#### - **Product Deployment** – Plan and administer the deployment activities for new and enhanced products and services, includes employee training, product inventory and solution deployment and coordination with systems production release, IT platform operations, production fulfillment staffing, customer servicing, marketing and sales activities.
#### - **Product Quality Assurance** – The service domain maintain and execute a portfolio of product quality assurance tests and if appropriate certifications to apply to new and updated production applications. These tests can be applied to any specific aspects of product sales, servicing and fulfillment as might be appropriate.
#### - **Brokered Product** – Administer 3rd party coordination for the production delivery of 'brokered' products and services that are offered through the bank, possibly in combination with the bank's own product and service offerings.
#### - **Brokered Product** – The service domains administer the provisioning and distribution of product inventory across the branch network and/or organizing distribution direct to customers (e.g. using mail services) where appropriate. The administration function keeps track of inventory holdings and administers a provisioning schedule to acquire replacement inventory as needed to meet requirements
#### - **Products and Services Direction** – Develop and communicate product and service policies and adapt in response to changing needs and to practical experience
#### - **Product Combination** – The Product Combination service domain allows a bank to assemble a composite product from two or more existing products. The combination framework implements necessary functional constraints on the 'contained products' and handles considerations such as transfer pricing where the profitability of embedded products may be compromised to ensure management analysis is not distorted
#### - **Products and Services Direction** – Maintain a current price list (with ranges and optional terms) by product/customer type for exceptional pricing conditions that override standard pricing as would be derived from the standard product specification
#### - **Discount Pricing** – Maintain a current price list (with ranges and optional terms) by product/customer type for exceptional pricing conditions that override standard pricing as would be derived from the standard product specification
#### - **Product Design** – Design and refine bank product and service specifications. This addresses multiple aspects including the core product specification definition, legal, tax and regulatory compliance, pricing, risk and performance assessments, testing and supporting systems and production requirements definition
#### - **Product Directory** – The product directory service domain provides a central service to reference product specifications 
  **Business Object (Owner):** Yes
#### - **Product Matching** – The service domain implements a decision service (that might be interactive) to isolate the preferred product(s) for which a customer is eligible in a specific servicing situation. The product selection logic will balance factors including customer indicated desired product type/features, customer type/profile, solicitation/retention/enquiry servicing situation, prevailing campaigns/bank preferred products. The decision logic improves product selection to optimize the customer interaction and support business development
#### - **Product Portfolio** – Maintain a portfolio of view of the bank's products with key product performance data and consolidated activity details to support profitability and performance analysis across the product portfolio
  **Business Object (Owner):** Product Analysis
#### - **Sales Product** – A sales product defines specific constraints and terms that augment the features of the base product it 'wraps'. It is used to support customization or core products to address specific market needs and opportunities with more narrowly targeted products
  **Business Object (Owner):** Yes
#### - **Sales Sales Support** – Administer the allocation of specialist support to advise on specific products and services

### Trust Management (Trust Manager) with its business capabilities and key functions
#### - **Trust Account Maintenance** – Provide trust services for high value customers, including asset maintenance, court administration, tax and expense handling, asset management and estate, inheritance and income tax processing.

### Investment Order Management (Order Manager) with its business capabilities and key functions
#### - **Order Allocation** – Apply appropriate rules to allocate a completed or partially completed block order across the customers placing the constituent market orders.
  **Business Object (Owner):** SecuritiesAllocationTransaction

#### - **Trade Confirmation Matching** – Trade matching and confirmation/affirmation is the process by which the broker dealer and institutional investor involved in a market trade ensure they agree all terms early in the trade process. The matching function is typically performed by a central market facility with both broker dealer and the institutional investor reporting trade details independently. The central system matches reported trades and then seeks confirmation/affirmation from the interested parties. This Service Domain supports the broker or investor role interfacing to that central market service
#### - **Trading Book Oversight** – The bank's trading book tracks the securities held by the bank that are frequently traded and may implement sophisticated risk measures to manage the banks exposure. Trading book oversight is responsible for tracking and analyzing the bank's trading book to manage risk
#### - **Quote Management** – Quote management handles the process by which a trader obtains quotes from multiple market makers in order to select the bank to execute a trade with. Recent trade prices reported to the exchange can be compared with trade activity for the different quoting banks in order to make the selection
  **Business Object (Owner):** QuotationProcedure
#### - **Trade and Price Reporting** – Operate a trade reporting facility as required by applicable trading market participation rules and regulations. Capture and transmit executed trade details to the exchange in compliance with the required timeframes and operating schedules
#### - **Program Trading** – Program trading covers a broad range of market trading activities, where the trading rules policies driving the trading decisions are automated, likely with some level of human monitoring/oversight as appropriate. This generic Service Domain is intended to support any form of program trading. In practice a bank may find it necessary to 'clone and specialize' the service domain to support different type of program trading it may employ as necessary.
  **Business Object (Owner):** ProgramTradingOperatingSession
#### - **Securities Fails Processing** – Market trades of securities may fail at different stages in the clearing and settlement processing. This Service Domain handles the resolution of securities processing failures
#### - **Credit Risk Operations** – This Service Domain monitors the counterparty credit limits (CCL) used to govern trading activity to manage credit exposure. Note there may be regulatory requirements that determine allowed CCLs.
  **Business Object (Owner):** TradingCreditPositionMeasurement
#### - **Consumer Investments** – This supports consumer initiated securities investment and trading activity for their self-managed securities investments. Trades will typically be blocked/netted against the bank's own securities position for subsequent market execution. Quotes/prices are based on the prevailing price at the time of the customer instruction to trade
#### - **Market Order** – Market Order records an instruction from a customer or his or her representative (which could be an account manager in the bank) to buy or sell securities. It follows the order during its lifetime and reports back to the requestor on the execution. In case of a sell order it puts a block on the investment account when the order is placed. This block will be removed when the order is executed or when it expires. A market order may be broken into multiple market trades or combined with other market orders for a block trade at the bank's discretion
#### - **Market Order Execution** – The Market Order Execution Service Domain is responsible for the booking of securities transactions (e.g. resulting from market orders or some types of corporate actions) on investment accounts, so in terms of security name plus quantity. Market Order Execution knows the different transaction types and the related booking sets. It will call Securities Position Keeping to create the debit and the credit bookings of a transaction. It will ensure that the bookings of a securities transaction are executed completely or not at all (the latter in the case of an exception). The execution of a market order may be in parts (trades) or it may be combined with other market orders for a block trade. The Service Connection "Execute Market Order" on this Service Domain handles the execution of (an undivided part of) one Market Order. A securities transaction will have a related money transaction. This will be handled by Payment Order - Payment Execution.
