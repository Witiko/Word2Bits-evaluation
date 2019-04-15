SHELL=/bin/bash
WORD2BITS_DIR=../Word2Bits
COMPUTE_ACCURACY=$(WORD2BITS_DIR)/compute_accuracy

%:
	$(COMPUTE_ACCURACY) \
		../vectors/$@ \
		< $(WORD2BITS_DIR)/data/google_analogies_test_set/questions-words.txt \
		&> $@
