# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_16:17:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,212 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 16:17:07 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-11-27 16:13:30 | Kuda Oya (Kirindi Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:09:11 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:08:24 | Badalgama (Maha Oya) | 4.42 | 🟢 Normal | -0.087 |  |
| 2026-11-27 16:07:59 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.027 |  |
| 2026-11-27 16:07:13 | Thanamalwila (Kirindi Oya) | 2.13 | 🟢 Normal | -0.075 |  |
| 2026-11-27 16:07:11 | Giriulla (Maha Oya) | 3.39 | 🟢 Normal | -0.038 |  |
| 2026-11-27 16:06:44 | Moraketiya (Walawe Ganga) | 3.05 | 🟡 Alert | 0.000 |  |
| 2026-11-27 16:06:37 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-11-27 16:06:21 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-11-27 16:05:42 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-11-27 16:05:23 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-27 16:04:54 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-11-27 16:04:47 | Kuda Oya (Kirindi Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:04:11 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | -0.126 |  |
| 2026-11-27 16:04:03 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 16:03:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.029 |  |
| 2026-11-27 16:03:30 | Hanwella (Kelani Ganga) | 2.97 | 🟢 Normal | -0.111 |  |
| 2026-11-27 16:03:29 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.016 |  |
| 2026-11-27 16:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.029 |  |
| 2026-11-27 16:03:00 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.041 |  |
| 2026-11-27 16:02:59 | Moragaswewa (Deduru Oya) | 4.29 | 🟢 Normal | 0.954 | 🔺 Rising |
| 2026-11-27 16:02:43 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.26 | 🟡 Alert | -0.020 |  |
| 2026-11-27 16:02:30 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-27 16:02:27 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.079 |  |
| 2026-11-27 16:02:26 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | -0.071 |  |
| 2026-11-27 16:02:14 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-11-27 16:02:07 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:02 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:02 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:01 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.061 |  |
| 2026-11-27 16:01:44 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-11-27 16:01:38 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-11-27 16:01:08 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:00:34 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:59:26 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 16:06:44 | Moraketiya (Walawe Ganga) | 3.05 | 🟡 Alert | 0.000 |  |
| 2026-11-27 16:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.26 | 🟡 Alert | -0.020 |  |
| 2026-11-27 16:02:26 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | -0.071 |  |
| 2026-11-27 16:02:59 | Moragaswewa (Deduru Oya) | 4.29 | 🟢 Normal | 0.954 | 🔺 Rising |
| 2026-11-27 16:04:54 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-11-27 16:02:30 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-27 16:04:03 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 16:05:23 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-27 16:00:34 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:09:11 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:02 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:07 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:02:45 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:43 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:14:43 | Panadugama (Nilwala Ganga) | 4.24 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:59:26 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:01:08 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:02 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:13:30 | Kuda Oya (Kirindi Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:06:21 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-11-27 16:17:07 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-11-27 16:03:29 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.016 |  |
| 2026-11-27 16:01:38 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-11-27 16:02:14 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-11-27 16:01:44 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-11-27 16:05:42 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-11-27 16:07:59 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.027 |  |
| 2026-11-27 16:03:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.029 |  |
| 2026-11-27 16:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.029 |  |
| 2026-11-27 16:06:37 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-11-27 16:07:11 | Giriulla (Maha Oya) | 3.39 | 🟢 Normal | -0.038 |  |
| 2026-11-27 16:03:00 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.041 |  |
| 2026-11-27 16:02:01 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.061 |  |
| 2026-11-27 16:07:13 | Thanamalwila (Kirindi Oya) | 2.13 | 🟢 Normal | -0.075 |  |
| 2026-11-27 16:02:27 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.079 |  |
| 2026-11-27 16:08:24 | Badalgama (Maha Oya) | 4.42 | 🟢 Normal | -0.087 |  |
| 2026-11-27 15:11:41 | Magura (Kalu Ganga) | 3.88 | 🟢 Normal | -0.093 |  |
| 2026-11-27 16:03:30 | Hanwella (Kelani Ganga) | 2.97 | 🟢 Normal | -0.111 |  |
| 2026-11-27 16:04:11 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)