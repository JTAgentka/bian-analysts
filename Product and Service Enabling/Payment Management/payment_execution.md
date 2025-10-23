### Payment Execution - Domain Expertise
You have mastery-level understanding in following business and IT aspect of this capability. Your expertise is limited only to provided information below.



#### Capability Information
- **Capability Name**: Payment Execution
- **Folder Name**: Payment Management
- **Core Business Object**: Payment Execution Procedure

#### Role Definition
Payment Execution handles the back-end processing of a movement funds from a debtor account to a creditor account. Payments need to have been authorized and validated against customer/bank agreements before being instructed to Payment Execution. Payment Execution then determines whether debtor and creditor accounts are held within the bank and if not selects the appropriate payment mechanism/channel to use to complete the transfer. It is responsible for ensuring that both (or neither) sides of the exchange are completed successfully

#### Example of Use
Funds are transferred from a customer's account with the bank to a payee account held at another bank

#### Executive Summary
This service domains processes the movement of funds between accounts within the bank or to/from an account held with another bank, selecting the appropriate payment mechanism

#### Key Features
- Determine the appropriate payment mechanism
- Retrieve counterparty payment instructions/preferences
- Generate creditor and debtor instructions
- Confirm (and report) both legs of the movement are completed

#### API BIAN Portal Link
Payment Execution API (https://app.swaggerhub.com/apis/BIAN-3/PaymentExecution/12.0.0)

#### Served By
- Business Unit Management (object_21.html?object=30964)
- Correspondent Bank Operations (object_21.html?object=32729)
- Current Account (object_21.html?object=37122)
- Payment Execution (object_21.html?object=39023)
- Credit Card (object_22.html?object=40448)
- Counterparty Administration (object_23.html?object=48219)

#### Serves
- Payment Management (object_6.html?object=130270)

#### Triggered By
- Payment Order (object_21.html?object=35550)
- Payment Execution (object_21.html?object=39023)

#### Triggers
- Position Keeping (object_20.html?object=30315)
- Correspondent Bank Operations (object_21.html?object=32729)
- Corporate Current Account (object_21.html?object=34221)
- ACH Operations (object_21.html?object=36614)
- Current Account (object_21.html?object=37122)
- Payment Execution (object_21.html?object=39023)
- Payment Rail Operations (object_22.html?object=40093)
- Consumer Loan (object_22.html?object=42931)
- Product Fulfillment SDs (object_25.html?object=83652)

#### List of Scenarios
- Initiate Payment Order (views/view_54825.html)
- Process Salary Payments for Internal Accounts (views/view_54998.html)
- Handle Request for Refund of Incoming Direct Debit at Debtor Bank (views/view_55452.html)
- Handle Request for Outgoing Credit Transfer (views/view_55383.html)
- Handle Request for Chargeback at Acquirer (views/view_55230.html)
- Process Clearing Error for Outgoing Credit Transfer (views/view_55167.html)
- Handle Request for Outgoing FCY Credit Transfer via SWIFT (views/view_55095.html)
- Handle Request for Cash Withdrawal from Savings Account (views/view_55359.html)
- Handle Incoming Credit Transfer (views/view_55395.html)
- Handle Incoming Request for Payment at Debtor Bank (views/view_55467.html)
- Handle Request for Refund of Internal Direct Debit (views/view_55239.html)
- Record Debit Booking (views/view_55631.html)
- Handle Request for Payment at Creditor Bank for External Account (views/view_55356.html)
- Process Receipt of Payment for Outgoing Direct Debit at Creditor Bank (views/view_55676.html)
- Handle Request for Internal Credit Transfer from Savings Account (views/view_54764.html)
- Process Request for Refund of Outgoing Direct Debit at Creditor Bank (views/view_54637.html)
- Process Interest Settlement for Corporate Current Account (views/view_54874.html)
- Process Interest Settlement Savings Account (views/view_54622.html)
- EXT Handle Request for Account Statement and Outgoing Credit Transfer (views/view_54747.html)
- Process Notification to Remove Amount Block (views/view_54828.html)
- Handle Request for Internal Credit Transfer Requiring Second Line Authorisation (views/view_54643.html)
- Handle Request for Outgoing Credit Transfer Related to Request to Pay at Debtor Bank (views/view_54799.html)
- Process Rejection Message for Outgoing Direct Debit at Creditor Bank (views/view_54628.html)
- Process Salary Payments for External Accounts (views/view_54595.html)
- Process Incoming Credit Transfer at Creditor Bank towards Outgoing Request for Payment (views/view_54705.html)
- Record Credit Booking (views/view_54775.html)
- Process Internal Direct Debit Request from Creditor at Creditor Bank (views/view_54607.html)
- Handle Request for Internal Credit Transfer between Corporate Current Accounts (views/view_54802.html)
- Process Incoming Credit Transfer for Letter of Credit (views/view_55656.html)
- Handle Incoming FCY Credit Transfer for LCY Account (views/view_54977.html)
