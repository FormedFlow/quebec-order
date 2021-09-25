import subprocess
import time

pages_count = 20
page_size_max = 50
command_template = "curl 'https://w12.eudonet.com/Specif/EUDO_07390/dev/v1/contact/tableaudesmembres' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: \"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"' \
  -H 'Accept: application/json' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Origin: https://w12.eudonet.com' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://w12.eudonet.com/specif/eudo_07390/web/index.html' \
  -H 'Accept-Language: en-US,en;q=0.9,ru;q=0.8' \
  --data-raw '{{\"Parameters\":{{\"PageSize\":{page_size},\"PageNumber\":{page_number}}},\"SearchCriterias\":{{\"firstName\":\"\",\"lastName\":\"\",\"ville\":\"\",\"region\":\"\",\"pratiqueProf\":\"\",\"champExer\":\"\",\"expertise\":\"\",\"typeOrganisation\":\"\"}}}}' \
  --compressed > json_data/page_{page_number}.json"

for page_num in range(pages_count + 1):
    result = subprocess.run(command_template.format(page_size=page_size_max, page_number=page_num), shell=True, capture_output=True)
    time.sleep(2)
    print(result)