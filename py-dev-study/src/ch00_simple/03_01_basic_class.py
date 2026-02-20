"""
优先使用 @property 而不是直接暴露公有属性，便于未来添加逻辑。
工厂方法用 @classmethod，而不是定义多个 __init__（Python 不支持重载）。
super() 在多继承中至关重要，它按 MRO（方法解析顺序）调用父类。
静态方法慎用：如果函数完全不依赖类/实例，考虑是否应放在模块顶层。
"""
import logging as log
import json
log.basicConfig(level=log.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class Animal:
    species = "未知物种"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age        

    # —————— 从 JSON 字符串创建实例 ——————
    @classmethod
    def from_json(cls, json_str: str):
        """从 JSON 字符串初始化 User 对象"""
        data = json.loads(json_str)
        return cls(
            name=data.get("name"),
            age=data.get("age"),
        )

    # —————— 从字典创建实例（更灵活） ——————
    @classmethod
    def from_dict(cls, data: dict):
        """从字典初始化 User 对象（推荐用于内部逻辑）"""
        return cls(
            name=data.get("name"),
            age=data.get("age"),
        )
    
    # —————— classmethod: 替代构造器 ——————
    @classmethod
    def from_string(cls, animal_str):
        """从 '类型-名字' 字符串创建实例"""
        name = animal_str.split("-")[1]
        age = animal_str.split("-")[2]
        return cls(name, age)

    # —————— 转为字典（便于序列化为 JSON） ——————
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
        }

    # —————— 转为 JSON 字符串 ——————
    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)

    # —————— property: 控制 name 属性访问 ——————
    @property
    def name(self):
        """Getter: 获取名称"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter: 设置名称（带验证）"""
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("名称必须是非空字符串")
        self._name = value

    @name.deleter
    def name(self):
        """Deleter: 删除名称"""
        del self._name

    # —————— staticmethod: 工具函数 ——————
    @staticmethod
    def is_animal_alive(age):
        """判断动物是否可能存活（简单规则）"""
        return age < 50


class Dog(Animal):
    species = "犬科"

    # bread 品种
    def __init__(self, name, age, breed):    
        self.breed = breed
        super().__init__(name, age)  # 调用父类 __init__

    def __dict__(self):
        return {
            "name": self.name,
            "age": self.age,
            "breed": self.breed,
        }
    
    @classmethod
    def from_json(cls, json_str: str):        
        data = json.loads(json_str)
        name=data.get("name")
        age=data.get("age")
        breed=data.get("breed")

        return cls(data['name'], data['age'], data.get('breed'))

    # —————— 从字典创建实例（更灵活） ——————
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name"),
            age=data.get("age"),
            breed=data.get("breed"),
        )
              
    # —————— classmethod: 替代构造器 ——————
    @classmethod
    def from_string(cls, animal_str):
        pass

    def bark(self):
        log.info(f"{self.name} 汪汪叫！")


# ===== 使用示例 =====
if __name__ == "__main__":
    # 1. property: 像访问属性一样调用方法
    dog = Dog("旺财", 4, "金毛")
    log.info(dog.name)        # 旺财（调用 getter）
    dog.name = "小黄"      # 调用 setter（自动验证）
    # dog.name = ""        # 报错：ValueError
    # 3. staticmethod: 直接通过类调用工具函数
    print(Animal.is_animal_alive(30))  # True

    # 4. super(): 子类正确初始化父类
    my_dog = Dog("大黑", 4, "拉布拉多")
    log.info(my_dog.bark())          # 大黑 汪汪叫！

    # 2. classmethod: 通过字符串创建实例
    cat = Animal.from_string("01-猫-2")
    log.info(cat.name)        # 咪咪
    
    my_dog_2 = Dog.from_json('{"name": "小黄", "age": 3, "breed": "秋田犬"}')  
    my_dog_1 = Dog.from_dict({"name": "小黄", "age": 3, "breed": "秋田犬"})

    # 反射
    setattr(my_dog_1, 'name', '大黄')
    log.info(getattr(my_dog_1,'name'))
    log.info(hasattr(my_dog_1, 'name'))
    log.info(type(my_dog_1))
    # 注意： 只有具有 __dict__ 的对象才能用 vars()
    log.info('var: %s', vars(my_dog_1))
    log.info('dir: %s', dir(my_dog_1))
    # 返回对象的唯一标识（通常是内存地址），在对象生命周期内不变。
    log.info('id: %s', id(my_dog_1))
    log.info('id: %s', hash(my_dog_1))
    log.info(isinstance(my_dog_1, Dog)) 
    log.info(isinstance(my_dog_1, Animal)) 
    # 传入参数 判断是否继承关系
    log.info(issubclass(Animal, Dog))

    log.info(isinstance(42, int))        # True
    log.info(isinstance("hello", str))   # True
    log.info(isinstance([1,2], list))    # True
    log.info(isinstance({1,2}, set))     # True
    log.info(isinstance({'a': 1, 'b': 2}, dict))     # True

    # 动态创建类
    MyClass = type('MyClass', (object,), {'x': 10})
    obj = MyClass()
    log.info('obj: %s', obj.x)  # 10






