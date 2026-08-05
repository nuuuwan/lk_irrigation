# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_05:15:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,287 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Nawalapitiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 05:15:56 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | -0.008 |  |
| 2026-08-05 05:11:50 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.382 | 🔺 Rising |
| 2026-08-05 05:09:42 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-05 05:07:35 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.042 |  |
| 2026-08-05 05:07:31 | Kithulgala (Kelani Ganga) | 2.75 | 🟢 Normal | -0.107 |  |
| 2026-08-05 05:07:16 | Rathnapura (Kalu Ganga) | 5.16 | 🟢 Normal | -0.349 |  |
| 2026-08-05 05:07:14 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:07:13 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:06:38 | Glencourse (Kelani Ganga) | 12.85 | 🟢 Normal | -0.193 |  |
| 2026-08-05 05:06:23 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.028 |  |
| 2026-08-05 05:06:04 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.017 |  |
| 2026-08-05 05:05:51 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:05:42 | Dunamale (Aththanagalu Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-08-05 05:04:54 | Nawalapitiya (Mahaweli Ganga) | 3.60 | 🟡 Alert | -0.134 |  |
| 2026-08-05 05:04:52 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.021 |  |
| 2026-08-05 05:04:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:04:26 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.029 |  |
| 2026-08-05 05:04:08 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.053 |  |
| 2026-08-05 05:03:24 | Ellagawa (Kalu Ganga) | 8.94 | 🟢 Normal | -0.020 |  |
| 2026-08-05 05:03:14 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-08-05 05:02:49 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:02:45 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-05 05:02:16 | Hanwella (Kelani Ganga) | 5.02 | 🟢 Normal | -0.164 |  |
| 2026-08-05 05:02:15 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2026-08-05 05:02:14 | Deraniyagala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-08-05 05:02:08 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.085 |  |
| 2026-08-05 05:01:23 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.012 |  |
| 2026-08-05 05:01:20 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:01:18 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:01:05 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:01:02 | Peradeniya (Mahaweli Ganga) | 4.48 | 🟢 Normal | -0.032 |  |
| 2026-08-05 05:01:01 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:00:39 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 04:51:47 | Rathnapura (Kalu Ganga) | 5.25 | 🟡 Alert | -0.349 |  |
| 2026-08-05 04:51:25 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.382 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 05:04:54 | Nawalapitiya (Mahaweli Ganga) | 3.60 | 🟡 Alert | -0.134 |  |
| 2026-08-05 05:11:50 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.382 | 🔺 Rising |
| 2026-08-05 05:02:14 | Deraniyagala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-08-05 05:02:45 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-05 05:09:42 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-05 05:05:51 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:01:20 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:00:39 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:17:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:04:08 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:07:14 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:04:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:02:49 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:01:01 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:19:00 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:32 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:01:18 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:01:05 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 05:15:56 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | -0.008 |  |
| 2026-08-05 05:03:14 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-08-05 05:05:42 | Dunamale (Aththanagalu Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-08-05 05:01:23 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.012 |  |
| 2026-08-05 05:06:04 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.017 |  |
| 2026-08-05 05:03:24 | Ellagawa (Kalu Ganga) | 8.94 | 🟢 Normal | -0.020 |  |
| 2026-08-05 04:03:46 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-08-05 05:04:52 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.021 |  |
| 2026-08-05 05:06:23 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.028 |  |
| 2026-08-05 05:04:26 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.029 |  |
| 2026-08-05 05:01:02 | Peradeniya (Mahaweli Ganga) | 4.48 | 🟢 Normal | -0.032 |  |
| 2026-08-05 05:07:35 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.042 |  |
| 2026-08-05 05:02:15 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2026-08-05 05:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.053 |  |
| 2026-08-05 05:02:08 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.085 |  |
| 2026-08-05 05:07:31 | Kithulgala (Kelani Ganga) | 2.75 | 🟢 Normal | -0.107 |  |
| 2026-08-04 18:04:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.115 |  |
| 2026-08-05 05:02:16 | Hanwella (Kelani Ganga) | 5.02 | 🟢 Normal | -0.164 |  |
| 2026-08-05 05:06:38 | Glencourse (Kelani Ganga) | 12.85 | 🟢 Normal | -0.193 |  |
| 2026-08-05 05:07:16 | Rathnapura (Kalu Ganga) | 5.16 | 🟢 Normal | -0.349 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)