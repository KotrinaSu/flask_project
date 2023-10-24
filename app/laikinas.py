# from app import db
from app.models import Vyras


# viktoras = Vyrai('Vikoras', '118', '175','80')
# jonas = Vyrai('Jonas', '115', '178','80')
#
# db.session.add_all([viktoras, jonas])
# db.session.commit()


one = Vyras.query.get(1)
print(one)
# print(one.meried)

# all= Vyrai.query.all()
# print(all)
#
# one.ugis = '205'
# db.session.add(one)
# db.session.commit()
#
# fiilter = Vyrai.query.filter_by(svoris='80')
# print(filter.all)


