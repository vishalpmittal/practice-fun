"""
    tag: design ds, db, stack, list

    Create a very simple in-memory database, which has a very limited command set. 
    All of the commands are going to be fed to you one line at a time via
    stdin, and your job is to process the commands and to perform whatever operation
    the command dictates.

    Data commands:
    Your database should accept the following commands:
    - SET [name] [value]: Set a variable [name] to the value [value]. 
    Neither variable names nor values will ever contain spaces.
    - GET (name): Print out the value stored under the variable (name]. 
    Print NULL if that variable name hasn't been set.
    - DELETE (name): Delete the variable (name)
    - COUNT [value): Return the number of variables equal to (value). 
    If no values are equal, this should output 0.
    - END: Exit the program

    Transaction commands:
    In addition to the data commands, your database should support transactions,
    accepting the following commands:
    - BEGIN: Open a transactional block
    - ROLLBACK: Rollback all of the commands from the most recent transactional block.
    - COMMIT: Permanently store all of the operations from aff presently open transactional blocks.

    Both ROLLBACK and COMMIT cause the program to print 'NO TRANSACTION’ if
    there are no open transaction blocks. Your database needs to support nested transactions. 
    ROLLBACK only applies to the most recent transaction block, but COMMIT applies to all 
    transaction blocks. (Any data command run outside of a transaction is committed immediately.)

    Performance considerations:
    When thinking about the structure of your database, assume that the most common
    operations are GET, SET, DELETE, and COUNT, all of which are equally common.
    All these commands should have an expected worst-case of O(log(N)) or better,
    where N is the total number of variables stored in the database.

    Additionally, you should assume that only a small number of values will be changed
    in a transaction. Your solution should be efficient about how much memory is used
    by a transaction (i.e. it should not nearly double your program's memory usage).
"""
import copy


class InMemDB:
    def __init__(self):
        self.db = dict()
        self.db["__count"] = dict()
        self.__xtion_stack__ = []

    def __str__(self):
        return "-------------\n-> DB : {}\n-> __xtion_stack__ : {}".format(
            self.db, self.__xtion_stack__
        )

    def __is_xtion(self):
        return len(self.__xtion_stack__) != 0

    def GET(self, key):
        if self.__is_xtion() and key in self.__xtion_stack__[-1]:
            return self.__xtion_stack__[-1][key]

        return self.db.get(key, None)

    def COUNT(self, val):
        if self.__is_xtion() and val in self.__xtion_stack__[-1]["__count"]:
            return self.__xtion_stack__[-1]["__count"][val]

        return self.db["__count"].get(val, 0)

    def SET(self, key, new_val):
        old_val = self.GET(key)
        old_val_cnt = self.COUNT(old_val)
        new_val_cnt = self.COUNT(new_val)

        set_db = self.db

        if self.__is_xtion():
            set_db = self.__xtion_stack__[-1]

        set_db[key] = new_val
        set_db["__count"][new_val] = new_val_cnt + 1
        if old_val:
            set_db["__count"][old_val] = old_val_cnt - 1

    def DELETE(self, key):
        curr_val = self.GET(key)
        if not curr_val:
            return

        curr_count = self.COUNT(curr_val)

        if self.__is_xtion():
            self.__xtion_stack__[-1][key] = None
            self.__xtion_stack__[-1]["__count"][curr_val] = curr_count - 1
        elif key in self.db:
            del self.db[key]
            self.db["__count"][curr_val] = curr_count - 1

    def END(self):
        """
            END resets the db to base. It doesn't matter if called between 
            transactions or not.
        """
        self.__init__()

    def BEGIN(self):
        if self.__is_xtion():
            self.__xtion_stack__.append(copy.deepcopy(self.__xtion_stack__[-1]))
        else:
            temp_dict = dict()
            temp_dict["__count"] = dict()
            self.__xtion_stack__.append(temp_dict)

    def ROLLBACK(self):
        if not self.__is_xtion():
            return "NO TRANSACTION"

        # remove the last operation dict from the stack
        self.__xtion_stack__.pop(len(self.__xtion_stack__) - 1)

    def COMMIT(self):
        if not self.__is_xtion():
            return "NO TRANSACTION"

        db_updates = self.__xtion_stack__[-1]

        # update count
        for value, cnt in db_updates["__count"].items():
            self.db["__count"][value] = cnt
        del db_updates["__count"]

        # update key values
        for key, val in db_updates.items():
            if val == None:
                del self.db[key]
            else:
                self.db[key] = val

        self.__xtion_stack__ = []


db = InMemDB()


def test1():
    """
        SET a 10
        GET a          -> 10
        DELETE a
        GET a          -> NULL
        END
    """
    db.SET("a", 10)
    assert db.GET("a") == 10
    db.DELETE("a")
    assert db.GET("a") == None
    db.END()
    assert db.GET("a") == None
    print("test1 passed!")


def test2():
    """
        SET a 10
        SET b 10
        COUNT 10      -> 2
        COUNT 20      -> 0
        DELETE a
        COUNT 10      -> 1
        SET b 30
        COUNT 10      -> 0
        END
    """
    db.SET("a", 10)
    db.SET("b", 10)
    assert db.COUNT(10) == 2
    assert db.COUNT(20) == 0
    db.DELETE("a")
    assert db.COUNT(10) == 1
    db.SET("b", 30)
    assert db.COUNT(10) == 0
    db.END()
    print("test2 passed!")


def test3():
    """
        BEGIN
        SET a 10
        GET a      -> 10
        BEGIN
        SET a 20
        GET a      -> 20
        ROLLBACK
        GET a      -> 10
        ROLLBACK
        GET a      -> NULL
        END
    """
    db.BEGIN()
    db.SET("a", 10)
    assert db.GET("a") == 10
    db.BEGIN()
    db.SET("a", 20)
    assert db.GET("a") == 20
    db.ROLLBACK()
    assert db.GET("a") == 10
    db.ROLLBACK()
    assert db.GET("a") == None
    db.END()
    print("test3 passed!")


def test4():
    """
        BEGIN
        SET a 30
        BEGIN
        SET a 40
        COMMIT
        GET a   -> 40
        ROLLBACK -> NO TRANSACTION
        END
    """
    db.BEGIN()
    db.SET("a", 30)
    db.BEGIN()
    db.SET("a", 40)
    db.COMMIT()
    assert db.GET("a") == 40
    assert db.ROLLBACK() == "NO TRANSACTION"
    db.END()
    print("test4 passed!")


def test5():
    """
        SET a 50
        BEGIN
        GET a   ->   50
        SET a 60
        BEGIN
        DELETE a
        GET a  ->    NULL
        ROLLBACK
        GET a  ->    60
        COMMIT
        GET a  ->    60
        END
    """
    db.SET("a", 50)
    db.BEGIN()
    assert db.GET("a") == 50
    db.SET("a", 60)
    db.BEGIN()
    db.DELETE("a")
    db.GET("a") == None
    db.ROLLBACK()
    db.GET("a") == 60
    db.COMMIT()
    db.GET("a") == 60
    db.END()
    print("test5 passed!")


def test6():
    """
        SET a 10
        BEGIN
        COUNT 10    ->   1
        BEGIN
        DELETE a
        COUNT 10    ->   0
        ROLLBACK
        COUNT 10    ->   1
        END
    """
    db.SET("a", 10)
    db.BEGIN()
    db.COUNT(10) == 1
    db.BEGIN()
    db.DELETE("a")
    db.COUNT(10) == 0
    db.ROLLBACK()
    db.COUNT(10) == 1
    db.END()
    print("test6 passed!")


test1()
test2()
test3()
test4()
test5()
test6()
