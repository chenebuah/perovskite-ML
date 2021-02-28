# perovskite-ML
Title: Comparative Analysis of Machine Learning Approaches on the Prediction of the Electronic Properties of Perovskites: A Case Study of ABX3 and A2BB’X6

# Abstract
Machine learning (ML) methods have recently been widely employed to tackle several problems in quantum mechanics and materials science. Their main objective is to develop surrogate models that can be used to bypass the costly Schrodinger equations and their approximations such as the density functional theory. In this study, twelve ML techniques are described, implemented and compared against each other on the prediction of the formation energy and the energy band gap of two distinctive perovskite crystal configurations: ABX3 and A2BB'X6. The considered perovskite samples are described using well developed features, and cover a diverse mix of oxides and halides occupying the X-anionic sites, alongside finite and infinite bandgap structures. Results obtained show that among the twelve ML models tested, the Support Vector Regression (SVR) model is the top performer whereas the Gaussian Process Regression (GPR) model performs poorest. Moreover, SVR proved significantly superior over its peers in predicting both target electronic properties. For the formation energy, reported error metrics on the combined ABX3 and A2BB’X6 samples are calculated to be 0.055 eV MAE, 0.096 eV RMSE and 99% R2 on the test set while on the energy bandgap, accuracy metrics were evaluated at 0.493 eV MAE, 0.717 eV RMSE, and 81.58% R2 on the test set. All the data and codes implemented in this study are openly available at: github.com/chenebuah/perovskite-ML.

# References
1 - C. Li, H. Hao, B. Xu, G. Zhao, L. Chen, S. Zhang, H. Liu, A progressive learning method for predicting the band gap of ABO3 perovskites using an instrumental variable, J. Mater. Chem. C, 8, (2020), 3127.

2 - Q. Xu, Z. Li, M. Liu, W.J. Yin, Rationalizing Perovskite Data for Machine Learning and Materials Design, J. Phys. Chem. Lett., 9, (2018), 6948−6954.

3 - S. Lu, Q. Zhou, Y. Ouyang, Y. Guo, Q. Li, J. Wang, Accelerated discovery of stable lead-free hybrid organic-inorganic perovskites via machine learning, Nature Comm., 9(1), (2018), 3405.

4 - S. Körbel, M.A.L. Marques, S. Botti, Stability and electronic properties of new inorganic perovskites from high-throughput ab initio calculations, J. Mater. Chem. C, 4(15), (2016), 3157–3167.

5 - H. Lu, et al., Screening stable and metastable ABO3 perovskites using machine learning and the materials project, Comput. Mater Sci., Vol. 177, (2020), 109614
