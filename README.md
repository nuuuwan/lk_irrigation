# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_10:15:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,465 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 10:15:25 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:13:09 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:11:46 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-09-15 10:11:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:11:40 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.065 |  |
| 2026-09-15 10:09:48 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | -0.038 |  |
| 2026-09-15 10:09:15 | Baddegama (Gin Ganga) | 3.05 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-15 10:07:30 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-15 10:07:23 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:06:53 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.019 |  |
| 2026-09-15 10:06:36 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 10:05:37 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-09-15 10:05:36 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-09-15 10:05:31 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.038 |  |
| 2026-09-15 10:05:29 | Thawalama (Gin Ganga) | 2.83 | 🟢 Normal | -0.075 |  |
| 2026-09-15 10:05:17 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-15 10:04:15 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:04:03 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-09-15 10:03:57 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:03:46 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:03:36 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:03:30 | Hanwella (Kelani Ganga) | 3.09 | 🟢 Normal | -0.040 |  |
| 2026-09-15 10:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.77 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-15 10:03:11 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:03:03 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:02:58 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 10:02:49 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:02:41 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-09-15 10:02:13 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-15 10:02:06 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.010 |  |
| 2026-09-15 10:02:03 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | -0.174 |  |
| 2026-09-15 10:01:47 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:01:39 | Thanthirimale (Malwathu Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-09-15 10:01:26 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-09-15 10:01:15 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:01:13 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-09-15 10:01:04 | Panadugama (Nilwala Ganga) | 4.22 | 🟢 Normal | -0.080 |  |
| 2026-09-15 10:01:01 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-09-15 10:00:08 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 09:58:53 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 10:01:01 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-09-15 10:09:48 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | -0.038 |  |
| 2026-09-15 10:01:13 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-09-15 10:05:37 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-09-15 10:02:13 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-15 10:09:15 | Baddegama (Gin Ganga) | 3.05 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-15 10:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.77 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-15 10:07:30 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-15 10:02:58 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 10:06:36 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 10:01:15 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:01:47 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:11:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:03:46 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:07:23 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:02:49 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:03:57 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:00:08 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:03:03 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:03:11 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:13:09 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:15:25 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:03:36 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:11:46 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-09-15 10:04:03 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-09-15 10:01:39 | Thanthirimale (Malwathu Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-09-15 10:05:17 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-15 10:02:06 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.010 |  |
| 2026-09-15 10:01:26 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-09-15 10:05:36 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-09-15 10:06:53 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.019 |  |
| 2026-09-15 10:02:41 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-09-15 10:05:31 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.038 |  |
| 2026-09-15 10:03:30 | Hanwella (Kelani Ganga) | 3.09 | 🟢 Normal | -0.040 |  |
| 2026-09-15 10:11:40 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.065 |  |
| 2026-09-15 10:05:29 | Thawalama (Gin Ganga) | 2.83 | 🟢 Normal | -0.075 |  |
| 2026-09-15 10:01:04 | Panadugama (Nilwala Ganga) | 4.22 | 🟢 Normal | -0.080 |  |
| 2026-09-15 10:02:03 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | -0.174 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)