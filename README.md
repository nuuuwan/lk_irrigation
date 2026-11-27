# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_11:19:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,018 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 11:19:44 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:17:59 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:14:39 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.042 |  |
| 2026-11-27 11:10:10 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.129 |  |
| 2026-11-27 11:09:03 | Panadugama (Nilwala Ganga) | 4.32 | 🟢 Normal | -0.023 |  |
| 2026-11-27 11:06:50 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:06:35 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-11-27 11:05:45 | Moragaswewa (Deduru Oya) | 3.40 | 🟢 Normal | -0.041 |  |
| 2026-11-27 11:05:11 | Giriulla (Maha Oya) | 3.85 | 🟢 Normal | -0.126 |  |
| 2026-11-27 11:05:10 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-27 11:04:52 | Badalgama (Maha Oya) | 4.83 | 🟢 Normal | -0.077 |  |
| 2026-11-27 11:04:25 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 11:04:13 | Siyambalanduwa (Heda Oya) | 1.21 | 🟢 Normal | -0.050 |  |
| 2026-11-27 11:04:06 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.055 |  |
| 2026-11-27 11:03:44 | Ellagawa (Kalu Ganga) | 6.72 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:03:14 | Moraketiya (Walawe Ganga) | 3.56 | 🟡 Alert | -0.203 |  |
| 2026-11-27 11:03:10 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:03:08 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.067 |  |
| 2026-11-27 11:03:01 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:02:45 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | -0.069 |  |
| 2026-11-27 11:02:43 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.060 |  |
| 2026-11-27 11:02:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:02:35 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.050 |  |
| 2026-11-27 11:02:31 | Kuda Oya (Kirindi Oya) | 2.57 | 🟢 Normal | -0.044 |  |
| 2026-11-27 11:02:28 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:02:26 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | -0.030 |  |
| 2026-11-27 11:02:24 | Dunamale (Aththanagalu Oya) | 3.96 | 🟡 Alert | -0.020 |  |
| 2026-11-27 11:02:16 | Galgamuwa (Mee Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-27 11:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.33 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-27 11:02:05 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:01:55 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-27 11:01:55 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | -0.060 |  |
| 2026-11-27 11:01:46 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 11:01:36 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-27 11:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-27 11:01:19 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.066 |  |
| 2026-11-27 11:00:45 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:00:11 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:00:09 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-27 10:59:09 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 11:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.33 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-27 11:02:24 | Dunamale (Aththanagalu Oya) | 3.96 | 🟡 Alert | -0.020 |  |
| 2026-11-27 11:01:55 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | -0.060 |  |
| 2026-11-27 11:03:14 | Moraketiya (Walawe Ganga) | 3.56 | 🟡 Alert | -0.203 |  |
| 2026-11-27 11:01:55 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-27 11:05:10 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-27 11:01:46 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 11:04:25 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 11:02:05 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:02:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:19:44 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:03:10 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:00:45 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:17:59 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-27 11:01:36 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-27 11:02:16 | Galgamuwa (Mee Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-27 11:06:35 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-11-27 11:03:44 | Ellagawa (Kalu Ganga) | 6.72 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:03:01 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:00:11 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:02:28 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:06:50 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:09:03 | Panadugama (Nilwala Ganga) | 4.32 | 🟢 Normal | -0.023 |  |
| 2026-11-27 11:02:26 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | -0.030 |  |
| 2026-11-27 10:59:09 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.034 |  |
| 2026-11-27 11:05:45 | Moragaswewa (Deduru Oya) | 3.40 | 🟢 Normal | -0.041 |  |
| 2026-11-27 11:14:39 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.042 |  |
| 2026-11-27 11:02:31 | Kuda Oya (Kirindi Oya) | 2.57 | 🟢 Normal | -0.044 |  |
| 2026-11-27 11:04:13 | Siyambalanduwa (Heda Oya) | 1.21 | 🟢 Normal | -0.050 |  |
| 2026-11-27 11:02:35 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.050 |  |
| 2026-11-27 11:04:06 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.055 |  |
| 2026-11-27 11:02:43 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.060 |  |
| 2026-11-27 11:01:19 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.066 |  |
| 2026-11-27 11:03:08 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.067 |  |
| 2026-11-27 11:02:45 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | -0.069 |  |
| 2026-11-27 11:04:52 | Badalgama (Maha Oya) | 4.83 | 🟢 Normal | -0.077 |  |
| 2026-11-27 11:05:11 | Giriulla (Maha Oya) | 3.85 | 🟢 Normal | -0.126 |  |
| 2026-11-27 11:10:10 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)