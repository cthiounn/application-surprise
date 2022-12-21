# Pokémon generator

---

## Architecture 

* stable diffusion pipeline - pokemon checkpoint
* rembg for detouring subject image
* streamlit 


## Requirements

* GPU


## Deploy on datalab.sspcloud.fr

* Use helm charts in ./helm-chart/
* helm dependency update
* helm install . --generate-name