|test| |codecov| |docs|

.. |test| image:: https://github.com/intsystems/ProjectTemplate/workflows/test/badge.svg
    :target: https://github.com/intsystems/ProjectTemplate/tree/master
    :alt: Test status
    
.. |codecov| image:: https://img.shields.io/codecov/c/github/intsystems/ProjectTemplate/master
    :target: https://app.codecov.io/gh/intsystems/ProjectTemplate
    :alt: Test coverage
    
.. |docs| image:: https://github.com/intsystems/ProjectTemplate/workflows/docs/badge.svg
    :target: https://intsystems.github.io/ProjectTemplate/
    :alt: Docs status


.. class:: center

    :Название исследуемой задачи: Классификафия по ОКПД 2 кодам
    :Тип научной работы: M1P
    :Автор: Фирсов Сергей Андреевич
    :Научный руководитель: Старожилец Всеволод Михайлович
    :Научный консультант(при наличии): Вознюк Анастасия 

Abstract
========

Исследование направлено на решение задачи классификации товаров по ОКПД 2 кодам с использованием кратких текстовых описаний. Коды представляют собой детализированную систему категоризации продуктов и услуг по видам экономической деятельности. Основная цель - повышение точности и сокращение ресурсозатратности классификации, анализируя влияние глубины классификатора ОКПД 2. Для достижения этих целей предлагается метод построения текстовых эмбеддингов с использованием нейросетевых технологий, таких как spaCy. Задача усложняется необходимостью предварительной обработки данных для перевода исходных описаний в стандартизированные короткие тексты, адаптированные для анализа. Используются данные государственных закупок по ФЗ 44 за 2022 год, охватывающие около 40% открытых источников, что обеспечивает достаточный объем и разнообразие информации для анализа. Также часть этих данных будет критерием оценки работы программы. Новизна заключается в применении методов машинного обучения к индустриальной задаче, что обещает улучшение в процессах логистики, учёте и анализе в сфере закупок.

(*обсуждалось, что в дальнейшем будем сжимать для достижения лимита по символам*)

*(ENG) The study is aimed at solving the problem of classifying goods according to OKPD 2 codes using short text descriptions. The codes are a detailed system for categorizing products and services by type of economic activity. The main goal is to increase the accuracy and reduce the resource consumption of classification by analyzing the effect of the depth of the OKPD 2 classifier. To achieve these goals, a method for constructing text embeddings using neural network technologies such as spaCy is proposed. The task is complicated by the need for preliminary data processing to translate the original descriptions into standardized short texts adapted for analysis. Public procurement data under Federal Law 44 for 2022 are used, covering about 40% of open sources, which provides a sufficient amount and variety of information for analysis. Also, some of this data will be a criterion for evaluating the work of the program. The novelty lies in the application of machine learning methods to an industrial task, which promises improvement in logistics processes, accounting and analysis in the field of procurement.*

Research publications
===============================
1. 

Presentations at conferences on the topic of research
================================================
1. 

Software modules developed as part of the study
======================================================
1. A python package *mylib* with all implementation `here <https://github.com/intsystems/ProjectTemplate/tree/master/src>`_.
2. A code with all experiment visualisation `here <https://github.comintsystems/ProjectTemplate/blob/master/code/main.ipynb>`_. Can use `colab <http://colab.research.google.com/github/intsystems/ProjectTemplate/blob/master/code/main.ipynb>`_.
