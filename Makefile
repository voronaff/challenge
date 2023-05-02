PYTHON = /usr/bin/python3
PIP = /usr/bin/pip

build: build_ms_a build_ms_b build_ms_c

build_%:
	$*/build.sh

test: 
	$(PIP) install -r requirements.txt
	$(MAKE) clean test_ms_a test_ms_b test_ms_c

test_%:
	$(PYTHON) unit_test.py $*

clean:
	rm -f ./test-reports/*

push: push_ms_a push_ms_b push_ms_c

push_%:
	cat ./test-reports/TEST-TestMicroServiceHTTPaccess-$*.xml | grep 'message="500 != 200' > /dev/null;\
	if [ $$? -eq 0 ]; then\
		echo "The image of $* won't be pushed to the registry";\
	else\
		echo "The image of $* will be pushed to the registry";\
	fi;

