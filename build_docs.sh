export PRODUCT=total

git submodule update --init --recursive
git submodule foreach git pull origin master
mkdir -p common/content/$PRODUCT/java && cp -r java common/content/$PRODUCT/
mkdir -p common/content/$PRODUCT/net && cp -r net common/content/$PRODUCT/
cp -r _index.md common/content/$PRODUCT
cd common
hugo server, show-feedback-config.toml