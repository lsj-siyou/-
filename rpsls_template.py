#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

import random


# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����


def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        number=0
    elif name=="ʷ����":
        number=1
    elif name=="ֽ":
        number=2
    elif name=="����":
        number=3
    elif name=="����":
        number=4
    else:
       print("Error: No Correct Name")
    return number

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        name="ʯͷ"
    elif number==1:
        name="ʷ����"
    elif number==2:
        name="��"
    elif number==3:
        name="����"
    else:
        name="����"
    return name


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    player_choice=choice_name
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randrange(0,4)
    print("�������ѡ��Ϊ:%s"%number_to_name(comp_number))
    if player_choice_number==comp_number:
        print("���ͼ��������һ����")
    elif player_choice_number==0 and comp_number==(3 or 4):
        print("��Ӯ��")
    elif player_choice_number==1 and comp_number==(0 or 4):
        print("��Ӯ��")
    elif player_choice_number==2 and comp_number==(0 or 1):
        print("��Ӯ��")
    elif player_choice_number==3 and comp_number==(1 or 2):
        print("��Ӯ��")
    elif player_choice_number==4 and comp_number==(3 or 2):
        print("��Ӯ��")
    else:
        print("�����Ӯ��")
	
    

    

# ���"-------- "���зָ�
# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

# ����Ļ����ʾ�����ѡ����������

# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

# ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�




# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
while True:
    choice_name=input()
    if choice_name not in ["ʯͷ","ʷ����","��","����","����"]:
        print("Error: No Correct Name")
    else:
        print(rpsls(choice_name))


