### TensorFlow API层次结构
- **一共可分为三个层次：** 低阶API，中阶API，高阶API
    - **第一层**为python实现的操作符，主要包括各种张量操作算子、计算图、自动微分
    - **第二层**为python实现的模型组件，对低级API进行了函数封装，主要包括各种模型层，损失函数，优化器，数据管道，特征列等等
    - **第三层**为python实现的模型成品，一般为安装OOP方式封装的高级API，主要为tf.karas.models提供的模型的类接口

**低层TensorFlow API**
- **tf.*(低层)**
    - tf.dtypes(数据类型转化)
    - tf.math(数学标量计算)
    - tf.initalizers(初始化操作)
    - tf.random(随机数生成)
    - tf.linalg(线性代数的运算)
    - tf.strings(字符串处理)
    - tf.ragged(张量操作，如切片)
    - tf.audio(声音处理)
    - tf.image(图像处理)
    - tf.io(文件处理)
<br>
- **中层TensorFlow API**
    - tf.data(数据管道)
    - tf.feature_column(特征列)
    - tf.nn(激活函数)
    - tf.keras.layers(模型层，如CNN、RNN)
    - tf.keras.losses(损失函数)
    - tf.keras.metrics(评估函数)
    - tf.keras.optimizers(优化器)
    - tf.keras.callbacks(回调函数)
    - tf.summary(模型可视化)
<br>
- **高层TensorFlow API**
tensorflow.keras.models
建模方式有三种：
    - Sequential方法
    - 函数式API方法
    - Model子类话自定义模型
