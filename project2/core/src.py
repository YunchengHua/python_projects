from conf import settings
from lib import common
import time

logger = common.get_logger(__name__)

current_user = {'user': None, 'login_time': None, 'timeout': int(settings.LOGIN_TIMEOUT)}

def log_in(func):

    def wrapper(*args, **kwargs):
        if current_user['user']:
            interval = time.time() - current_user['login_time']
            if interval < current_user['timeout']:
                return func(*args, **kwargs)
        name = input('name>>: ')
        db = common.conn_db()

        if db.get(name):  # log in
            if db.get(name).get('locked'):
                logger.warning('Try to log in locked %s'%current_user['user'])
            else:
                logging_error_times = 0

                while True:
                    if logging_error_times >= 3:
                        logger.warning('%s locked'%(current_user['user']))
                        db[name]['locked'] = 1
                        common.save_db(db)
                        break
                    password = input('password>>:')
                    if password == db.get(name).get('password'):
                        logger.info('%s log in successfully.'%(current_user['user']))
                        current_user['user'] = name
                        current_user['login_time'] = time.time()
                        break
                    else:
                        logging_error_times += 1
                        logger.warning('%s %dth incorrect password.'%(current_user['user'],logging_error_times))
            return func(*args, **kwargs)
        else:  # register
            is_register = input('Register？ （Y/N）')
            if is_register in ['Y', 'y']:
                password = input('password>>')
                db[name] = {"password": password, "money": 0, "locked": 0}
                logger.info("Log in successfully")
                current_user['user'] = name
                current_user['login_time'] = time.time()
                common.save_db(db)
            else:
                logger.info('new user cancelled')
            return func(*args, **kwargs)

    return wrapper


@log_in
def shopping():
    db = common.conn_db()
    money = db.get(current_user['user']).get('money')
    print('You have $%d' % money)
    items_dict = {'book': 1, 'bread': 2}
    for k in items_dict:
        print(k)
    items_bought_dic = {}
    while True:
        item_buy = input('Which do you want to buy?>>').strip()
        item_buy_split = item_buy.split(' ')

        if len(item_buy_split) == 2:
            if item_buy_split[0] in ['q', 'Q']:
                db[current_user['user']]['money'] = money
                common.save_db(db)
                print('You Bought：', items_bought_dic)
                print('Balance：', money)
                break
            elif item_buy_split[0] in items_dict:
                item, item_num = item_buy_split[0], item_buy_split[1]
                item_price = items_dict[item] * int(item_num)
                print(item, ':', item_num, 'spent $%d' % item_price)
                if item_price <= money:
                    money -= item_price
                    logger.info('%s bought %s,and $%d left'%(current_user['user'],item,money))
                    if item in items_bought_dic:
                        items_bought_dic[item] += item_num
                    else:
                        items_bought_dic[item] = item_num
                else:
                    print('Insufficient balance')
            else:
                print('Item does not exit.')
        else:
            print('You should input like (name number),you should seperate by space')

@log_in
def balance_operation(opt):
    #check saving
    db = common.conn_db()
    money = db.get(current_user['user']).get('money')
    print('You have $%d left.' % money)
    num = ''

    #check input
    while not num.isdigit():
        num = input('amount >>: ')
        if num in ['q', 'Q']:
            return
        elif not num.isdigit():
            print('Invalid Input')

    num = int(num)

    # deposit
    if opt == 'in':
        money += num
        db[current_user['user']]['money'] = money
        common.save_db(db)
        logger.info('%s deposits $%d, and $%d left'%(current_user['user'],num,money))
    # spend money
    elif opt == 'out':
        if money > num:
            money -= num
            db[current_user['user']]['money'] = money
            common.save_db(db)
            logger.info('%s spent $%d, and $%d left' % (current_user['user'], num, money))
        else:
            logger.warning('%s fails to spend $%d, and $%d left' % (current_user['user'],num, money))

@log_in
def run():
    while True:
        print('\n1. deposit\n2. withdraw\n3. repay\n4. shopping\nQ. quit\n')
        choice = input('You choice >>: ').strip()
        if not choice: continue
        if choice == '1':
            balance_operation('in')
        if choice in ['2','3']:
            balance_operation('out')
        if choice == '4':
            shopping()
        if choice in ['Q', 'q']:
            quit()
