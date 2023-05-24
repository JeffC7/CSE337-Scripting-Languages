# Read in process name as command line arg
$process_name = $args[0]
$all_processes = Get-Process -Name $process_name -ErrorAction SilentlyContinue

# List all currently running processes
Write-Host "Currently running processes:"
Get-Process

if (!$all_processes) {
    Write-Host "No such process is running."
    exit 
}

# Kill all running instances of the process
$all_processes | ForEach-Object { $_.Kill() }

# List all currently running processes to confirm that the specified process is absent
Write-Host "Currently running processes:"
Get-Process