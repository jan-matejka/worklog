.DEFAULT_GOAL := build

DRAM_OPTS    ?= -s zsh -t rst $(DRAM_OPTS_EXTRA)

# common definitions
build_dir     = _build
src_dir       = src

prefix       ?= /usr/local

## installation targets
i_bin_dir     = $(DESTDIR)$(prefix)/bin
i_man_dir     = $(DESTDIR)$(prefix)/man/man1

## build targets
b_bin_dir     = $(build_dir)/bin
b_man_dir     = $(build_dir)/man/man1


install_bin   = install -m755
install_data  = install -m644

bash_comp_dir = $(DESTDIR)$(prefix)/share/bash-completion/completions
zsh_comp_dir  = $(DESTDIR)$(prefix)/share/zsh/vendor-completions

# common program specific definitions
sources   = GNUmakefile $(src_dir) README.rst

cmds      = $(patsubst $(src_dir)/%.zsh,%,$(wildcard $(src_dir)/*.zsh))
cmds     += $(patsubst $(src_dir)/%,%,$(wildcard $(src_dir)/*.py))
mans      = $(patsubst Documentation/man/man1/%.rst,%.1,$(wildcard Documentation/man/man1/*.rst))

dirs      =
dirs     += $(b_bin_dir) $(i_bin_dir)
dirs     += $(b_man_dir) $(i_man_dir)
dirs     += $(bash_comp_dir) $(zsh_comp_dir)

## build dependencies
b_deps    =
b_deps   += $(b_bin_dir)
b_deps   += $(b_man_dir)
b_deps   += $(addprefix $(b_bin_dir)/,$(cmds))
b_deps   += $(addprefix $(b_man_dir)/,$(mans))

## install dependencies
i_deps    =
i_deps   += $(i_bin_dir)
i_deps   += $(i_man_dir)
i_deps   += $(bash_comp_dir) $(zsh_comp_dir)
i_deps   += $(addprefix $(i_bin_dir)/,$(cmds))
i_deps   += $(addprefix $(i_man_dir)/,$(mans))
i_deps   += $(shell find -path ./$(bash_comp_dir)/wl -or -path ./$(zsh_comp_dir)/_wl)

.PHONY: all
all: build

# build
.PHONY: build
build: $(b_deps)

# install
.PHONY: install
install: $(i_deps)

.PHONY: install-home
install-home:

	$(MAKE) install prefix=$(HOME)/.local

# build binaries
$(b_bin_dir)/%: $(src_dir)/%.zsh

	$(install_bin) $< $@

$(b_bin_dir)/%.py: $(src_dir)/%.py

	$(install_bin) $< $@

# build man pages
$(b_man_dir)/%.1: Documentation/man/man1/%.rst

	rst2man $< $@

# install binaries
$(i_bin_dir)/%: $(b_bin_dir)/%

	$(install_bin) $< $@

# install man pages
$(i_man_dir)/%: $(b_man_dir)/%

	$(install_data) $< $@

# install completions
$(bash_comp_dir)/wl: completion/wl.bash

	$(install_data) $< $@

$(zsh_comp_dir)/_wl: completion/wl.bash

	$(install_data) $< $@

# create directories
$(dirs):

	install -m755 -d $@

# tests
.PHONY: test
test: check

.PHONY: check
check: build

	PATH=$$PWD/$(build_dir)/bin:$$PATH dram $(DRAM_OPTS) dram/*

# clean build/tests artefacts
.PHONY: clean
clean:

	$(RM) -r $(build_dir)
