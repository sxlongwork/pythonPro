"""
创建一个类后，其父类默认是object类的就是新式类，python3.x中创建的类默认是新式类
创建一个类后不指定它的父类为object类的话，就不是object的子类，这种类是旧式类，python2.x不指定父类默认创建的就是旧式类
新式类和旧式类会影响方法的调用顺序

为了兼容性考虑，创建类时若没有父类，建议都指定object父类

"""