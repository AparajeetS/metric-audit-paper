$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$kaggle = "C:\Users\apara\AppData\Local\Python\pythoncore-3.14-64\Scripts\kaggle.exe"

@'
{
  "id": "aparajeetshadangi/cei-mbe-large-scale-image",
  "title": "CEI MBE Large Scale Image",
  "code_file": "jmlr_scale_image_kernel.py",
  "language": "python",
  "kernel_type": "script",
  "is_private": "true",
  "enable_gpu": "true",
  "enable_internet": "true",
  "dataset_sources": [],
  "competition_sources": [],
  "kernel_sources": []
}
'@ | Set-Content -LiteralPath (Join-Path $here "kernel-metadata.json") -Encoding UTF8

& $kaggle kernels push -p $here
