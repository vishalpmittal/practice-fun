import ConfigParser
sum_rps = 0
test_str = "; 2015-09-26T06:18:04+0000\n; Horizontal Scaling Test\n; isTestingThroughCode=true\n; Test launched. Please check every minute for update.\n; Your goal is too achieve rps=4000 in 30 min\n; Minimal interval of adding instances is 100 sec\n[Test]\ntype=horizontal\ntestId=1443248284562\ntestFile=test.1443248284562.log\n\n[Minute 1]\nec2-54-86-7-194.compute-1.amazonaws.com=545.51\n\n[Minute 20]\nec2-54-86-7-194.compute-1.amazonaws.com=713.38\nec2-54-209-126-46.compute-1.amazonaws.com=713.21"

a_list=['ec2-54-86-7-194.compute-1.amazonaws.com','ec2-54-209-126-46.compute-1.amazonaws.com']
test_file =open("temp_testresult.ini","w")
test_file.write(test_str)
test_file.close()

config = ConfigParser.RawConfigParser()
config.read("temp_testresult.ini")
last_section =config.sections()[-1]
for key in a_list:
    if config.has_option(last_section, key):
        a_float = config.getfloat(last_section,key)
        sum_rps +=a_float
print sum_rps