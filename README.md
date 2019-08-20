# Purpose
Importing OFX files into financial software from my bank has always been a pain.  Merchants report the transaction data to the bank, and the transaction data is always merchant-centered.  For example, here is an excerpt from an OFX file provided to the bank
```
<STMTTRN>
    <TRNTYPE>DEBIT</TRNTYPE>
    <DTPOSTED>20190325120000</DTPOSTED>
    <DTUSER>20190325120000</DTUSER>
    <TRNAMT>-75.01</TRNAMT>
    <FITID>5348555026201903251</FITID>
    <NAME>DEBIT CARD PURCHASE XXXXX1234</NAME>
    <MEMO>Merchant1</MEMO>
</STMTTRN>
```
As you can see, the transaction name is not the name of the merchant `Merchant1`, but my payment method.  Once imported into my financial softare, I get the amount OK, but I don't know who the Payee is; `DEBIT CARD PURCHASE XXXXX1234` was not who I payed.

This script is meant to rectify this problem by swapping the `NAME` and `MEMO` fields in an OFX file.

# Requirements
* Python 3.x

# Usage
`<path_to_python3_interpreter> ofx_swapper.py <OFX_file_name>`

invokes the script on the specified OFX file, swapping name and memo fields of all transactions.  The transformed data is written to stdout.

`<path_to_python3_interpreter> ofx_swapper.py -o <OFX_file_name>`

overwites the original file with the swapped data

# My (macOS) workflow
I use [Hazel](https://www.noodlesoft.com) to process the OFX file as it is downloaded from my bank.  When the file is detected on disk, Hazel is activated and runs the Shell Script
`/usr/local/bin/python3 ~/bin/ofx_swapper.py -o $1`
This performs the name and memo swap, overwriting the downloaded file.

Hazel then Opens the OFX file in my financial software, which starts the import process.
