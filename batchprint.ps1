# C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe
# BatchPrintDuplexBW.ps1

# Specify the default printer name
$defaultPrinterName = "HPFC3052.lan (HP OfficeJet Pro 9020 series)"

# Specify the folder containing the files to be printed
$folderPath = "C:\Users\MSI\Desktop\TINA OFFICE\QUOTE PROPOSALS\NAIL SALONS\2023\OCTOBER\test"
# Get all files in the specified folder
$files = Get-ChildItem $folderPath

# Set printer preferences for black and white and duplex
Set-PrintConfiguration -PrinterName $defaultPrinterName -Color $false -Duplexing "TwoSidedLongEdge"

# Loop through each file and print it with the specified settings
foreach ($file in $files) {
    # Print PDF files using Adobe Acrobat Reader command-line print
    if ($file.Extension -eq ".pdf") {
        Start-Process -FilePath "C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe" -ArgumentList "/t `"$($file.FullName)`" `"$defaultPrinterName`""
    } else {
        Write-Host "File $($file.FullName) is not a PDF and cannot be printed using the script."
    }
}