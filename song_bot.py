from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def finding_element(selector, selector_value, click = False):
	try:
		WebDriverWait(driver, 20).until(EC.presence_of_element_located((selector, selector_value)))
		found_element = driver.find_element(selector, selector_value)

	except:
		print("Sorry some error occured .... ")
		print("Refreshing site ...")
		driver.refresh()
		cookie_accept = finding_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/span", True)

	else:
		if found_element:
			if click:
				try:
					found_element.click()

				except:
					print("Some error occured ... Try again... ")
					print(selector_value)
					driver.refresh()
					cookie_accept = finding_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/span", True)

			return found_element

		else:
			driver.refresh()

	#finally:


		#return driver.find_element(selector, selector_value)


def song_command(command):
	if command.startswith("-play"):
		search_bar = finding_element(By.XPATH, "/html/body/div[1]/div[2]/header/aside/div[1]/div[1]/input")
		search_bar.clear()

		song_name = " ".join(command.split()[1:])
		search_bar.send_keys(song_name)
		time.sleep(1)
		search_bar.send_keys(Keys.RETURN)

		match = finding_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/main/div/div/section/ol/li[1]/div/article/div[2]/figure/figcaption/h4/a", True)
		#match.click()

		if match:
			play_button = finding_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/main/div[2]/figure/figcaption/div/p[1]/a", True)
			#play_button.click()

			driver.implicitly_wait(3)

			#cancel_button = False

			try:
				cancel_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/aside[3]/div/div[2]/span")

			except:
				pass

			else:
				cancel_button.scrollIntoView()
				cancel_button.click()

	elif command == "-next":
		next_button = finding_element(By.XPATH, "/html/body/div[1]/div[2]/aside[3]/div[1]/ul[2]/li[4]/span", True)
		#next_button.click()
		time.sleep(1)

	elif command == "-stop" or command == "-start":
		stop_button = finding_element(By.XPATH, "/html/body/div[1]/div[2]/aside[3]/div[1]/ul[2]/li[3]/span", True)
		#stop_button.click()
		time.sleep(1)

	elif command == "-previous":
		next_button = finding_element(By.XPATH, "/html/body/div[1]/div[2]/aside[3]/div[1]/ul[2]/li[2]/span", True)
		#next_button.click()

	else:
		print("Invalid command ....")


if __name__ == "__main__":
	user_query = input("Enter command :")

	print("setting up bot ....")

	driver = webdriver.Firefox()
	driver.get("https://www.jiosaavn.com/search")
	#driver.minimize_window()

	cookie_accept = finding_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/span", True)
	cookie_accept.click()

	print("bot ready to use ...")

	song_command(user_query)

	while user_query != "-exit":
		user_query = input("Enter command :")
		song_command(user_query)

	driver.close()
