$id = "aparajeetshadangi/cei-mbe-cifar10-grid"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
while ($true) {
    $status = & python -m kaggle kernels status $id
    Write-Host $status
    if ($status -match "complete" -or $status -match "KernelWorkerStatus.COMPLETE") {
        Write-Host "Kernel complete! Downloading output..."
        & python (Join-Path $here "download_kaggle.py")
        break
    }
    if ($status -match "error" -or $status -match "cancel" -or $status -match "KernelWorkerStatus.ERROR") {
        Write-Host "Kernel failed or cancelled."
        exit 1
    }
    Start-Sleep -Seconds 30
}
