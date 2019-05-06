This repository contains the [evaluation](evaluation.ipynb) of the
[Word2Bits][] algorithm by [Maximilian Lam][agnusmaximus].

 [agnusmaximus]: https://github.com/agnusmaximus
 [Word2Bits]: https://github.com/agnusmaximus/Word2Bits (Quantized word vectors that take 8x-16x less space than regular word vectors)

 <p>
   <a href="figures/accuracy-iter.pdf">
     <img src="figures/accuracy-iter.png"
          width="290"
          alt="Training accuracy (solid line) and loss (dashed line) vs epochs trained (vector dimension = 400) on 100MB of Wikipedia. Trends show that Word2Vec is prone to overfitting with many epochs of training."
          title="Training accuracy (solid line) and loss (dashed line) vs epochs trained (vector dimension = 400) on 100MB of Wikipedia. Trends show that Word2Vec is prone to overfitting with many epochs of training." />
   </a>
   <a href="figures/accuracy-size.pdf">
     <img src="figures/accuracy-size.png"
          width="290"
          alt="Training accuracy (solid line) and loss (dashed line) vs dimension (epochs trained = 10) on 100MB of Wikipedia. Trends show that overfitting may occur with larger vector dimensions."
          title="Training accuracy (solid line) and loss (dashed line) vs dimension (epochs trained = 10) on 100MB of Wikipedia. Trends show that overfitting may occur with larger vector dimensions." />
   </a>
   <a href="figures/speed-size.pdf">
     <img src="figures/speed-size.png"
          width="290"
          title="Duration of computing vector distances (solid line) and performing vector arithmetic (dashed line) in the evaluation of the Google analogy task. Using bitwise vector operations and Hamming distance results in up to 16× speed increase compared to float vectors and cosine similarity." />
   </a>
</p>

To reproduce our results, download the repository and install the required Python packages:

``` sh
git clone --recurse-submodules https://github.com/witiko/Word2Bits-evaluation.git
rm vectors/*.log analogy/!(Makefile) analogy_bitwise/!(Makefile)
pip install -r requirements.txt
```

Then, open the file [`evaluation.ipynb`](evaluation.ipynb) in [Jupyter
notebook][jupyter] and run all cells.

 [jupyter]: https://jupyter.org/ (Project Jupyter | Home)
