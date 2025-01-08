
import inspect


def introspection_info(obj):

    type_obj = type(obj)

    obj_atr = dir(obj)

    obj_methods = (method for method in dir(obj) if callable(method))

    module = inspect.getmodule(introspection_info)

    return (f'Объект: {obj}, тип: {type_obj}, атрибуты: {obj_atr}, методы: {obj_methods}, из модуля: {module}')
    
print(number_info := introspection_info(42))






