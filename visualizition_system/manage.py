from application import init_app,db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from application.apps.index.models import Student


app = init_app("dev")

# 使用终端脚本工具启动和管理flask
manager = Manager(app)

# 启用数据迁移工具
Migrate(app, db)
# 添加数据迁移的命令到终端脚本工具中
manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    manager.run()