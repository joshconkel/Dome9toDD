import csv

inFileName = input("Enter full filename of Dome9 .csv file: ")
outFileName = input("Enter full filename of Dome9 GenericFindings .csv file: ")

# Initalize output file and populate output file headers (Single Run)
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
        Date = row.get('Created Time', 'N/A')
        Title = row.get('Rule Name', 'N/A') + " : " + row.get('Entity ID', 'N/A')
        CweId = '0'
        Url = ''
        Severity = row.get('Severity', 'N/A')
        Description = row.get('Description', 'N/A')
        Mitigation = row.get('Remediation', 'N/A')
        Impact = ''
        BundleName = row.get('Bundle Name', 'N/A')
        CloudAccountName = row.get('Cloud Account Name', 'N/A')
        Region = row.get('Region', 'N/A')
        Network = row.get('Network', 'N/A')
        EntityId = row.get('Entity ID', 'N/A')
        References = "See CloudGuard Bundle: " + BundleName + "\n\n" + \
                     "Resource Location: (AccountName \ Region \ Network \ EntityId)\n" + \
                     "                    " + CloudAccountName + " \ " + Region + " \ " + Network + " \ " + EntityId
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
