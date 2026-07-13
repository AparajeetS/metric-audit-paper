$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path

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

& python -m kaggle kernels push -p $here
