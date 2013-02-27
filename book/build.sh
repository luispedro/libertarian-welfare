#!/usr/bin/env zsh

function build() {
    input=$1
    mkdir -p .$input.tex_files
    cd .$input.tex_files
    TEXINPUTS=..:../bioinfo/:.:../../images/:../../figures/: xelatex $input
    BSTINPUTS=:..:../bioinfo/: BIBINPUTS=:..:.: biber $input
    cp $input.pdf ..
    cd ..
}
build libertarian-welfare
