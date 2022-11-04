import csv
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Dome9 Converter for DefectDojo')
    parser.add_argument('--input', help="Dome9 Filename", required=True)
    parser.add_argument('--output', help="Generic Findings output filename", required=True)

    # Parse out arguments
    args = vars(parser.parse_args())
    inFileName = args["input"]
    outFileName = args["output"]

# Initialize output file and populate output file headers (Single Run)
with open(outFileName, 'w', newline='') as outFile:
    fieldnames = ['Date', 'Title', 'CweId', 'Url', 'Severity', 'Description', 'Mitigation', 'Impact',
                  'References',
                  'Active', 'Verified', 'FalsePositive', 'Duplicate']
    outWriter = csv.DictWriter(outFile, fieldnames=fieldnames)
    outWriter.writeheader()

# Open Input File
with open(inFileName, newline='') as inFile:
    inReader = csv.DictReader(inFile)
    for row in inReader:
        rowHasData = row.get('Cloud Account ID')
        if rowHasData is not None:
            Date = row.get('Created Time', 'N/A')
            Title = row.get('Rule Name', 'N/A') + " : " + row.get('Entity ID', 'N/A')
            CweId = '0'
            Severity = row.get('Severity', 'N/A')
            Description = row.get('Description', 'N/A')
            Mitigation = row.get('Remediation', 'N/A')
            Impact = ''
            BundleName = row.get('Bundle Name', 'N/A')
            RuleId = row.get('Rule ID', 'N/A')
            CloudAccountName = row.get('Cloud Account Name', 'N/A')
            CloudAccountId = row.get('Cloud Account ID', 'N/A')
            Region = row.get('Region', 'N/A')
            Network = row.get('Network', 'N/A')
            EntityId = row.get('Entity ID', 'N/A')
            Url = "http://" + CloudAccountName + "/" + EntityId + "/" + Region + "/" + Network
            References = "See CloudGuard Bundle: " + BundleName + "\n" + \
                         "Dome9 Rule ID: " + RuleId + "\n" + \
                         "Account ID: " + CloudAccountId + "\n\n" + \
                         "Resource Location: (AccountName \ Region \ Network \ EntityId)\n" + \
                         "                    " + \
                         CloudAccountName + " \ " + Region + " \ " + Network + " \ " + EntityId
            # Open file with append and write new values
            # May want to find a graceful way of opening file for output once and writing lines.
            with open(outFileName, 'a', newline='') as outFile:
                fieldnames = ['Date', 'Title', 'CweId', 'Url', 'Severity', 'Description', 'Mitigation', 'Impact',
                              'References',
                              'Active', 'Verified', 'FalsePositive', 'Duplicate']
                outWriter = csv.DictWriter(outFile, fieldnames=fieldnames)
                outWriter.writerow({'Date': Date,
                                    'Title': Title,
                                    'CweId': CweId,
                                    'Url': Url,
                                    'Severity': Severity,
                                    'Description': Description,
                                    'Mitigation': Mitigation,
                                    'Impact': Impact,
                                    'References': References})
        else:
            break
