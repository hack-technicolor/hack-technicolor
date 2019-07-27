if [ -x "$(command -v git)" ]; then
  git pull https://github.com/kevdagoat/hack-technicolor.git
fi
if [ ! -x "$(command -v mkdocs)" ]; then
  pip install --user mkdocs-material
fi
mkdocs serve
