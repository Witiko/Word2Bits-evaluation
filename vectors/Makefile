SHELL=/bin/bash
WORD2BITS_DIR=../Word2Bits
WORD2BITS=$(WORD2BITS_DIR)/word2bits
NAME_REGEX=^([0-9]*)b_([0-9]*)d_vectors_e([0-9]*)$$
NPROC=$(shell nproc)

text8:
	wget http://mattmahoney.net/dc/text8.zip
	unzip text8.zip

%: text8
	make -C $(WORD2BITS_DIR) word2bits
	$(WORD2BITS) \
		-sample 1e-4 \
		-bitlevel $$(sed -r 's/$(NAME_REGEX)/\1/' <<<$@) \
		-size $$(sed -r 's/$(NAME_REGEX)/\2/' <<<$@) \
		-window 10 \
		-negative 24 \
		-threads $(NPROC) \
		-iter $$(sed -r 's/$(NAME_REGEX)/\3/' <<<$@) \
		-min-count 5 \
		-train $< \
		-output $@ \
		-binary 1 \
		&> $@.log
	sed -i 's/\r/\n/g' $@.log
