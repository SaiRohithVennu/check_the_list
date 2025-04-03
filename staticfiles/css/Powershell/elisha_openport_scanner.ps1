# Prompt the user for the Target IP
$TargetIP = Read-Host "Enter the target IP address"

# Check if the Target IP is provided
if (-not $TargetIP) {
    Write-Host "No IP address entered. Exiting..."
    exit
}

# List of common ports to scan
$Ports = @(21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389)

Write-Host "Scanning Target: $TargetIP"
Write-Host "------------------------------"

# Scan each port
foreach ($Port in $Ports) {
    Write-Host "Trying Port $Port..."
    try {
        $connection = New-Object System.Net.Sockets.TCPClient($TargetIP, $Port)
        if ($connection.Connected) {
            Write-Host "Port $Port is open"
            $connection.Close()
        }
    } catch {
        Write-Host "Port $Port is closed"
    }
}

Write-Host "Scan complete."

pause