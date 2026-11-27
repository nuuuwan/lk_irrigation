# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_14:03:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,117 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 14:03:50 | Kuda Oya (Kirindi Oya) | 2.43 | 🟢 Normal | -0.030 |  |
| 2026-11-27 14:03:44 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 100.000 | 🔺 Rising |
| 2026-11-27 14:03:33 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | -0.059 |  |
| 2026-11-27 14:03:28 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-11-27 14:03:08 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 100.000 | 🔺 Rising |
| 2026-11-27 14:03:00 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-11-27 14:02:48 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-11-27 14:02:38 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | -0.040 |  |
| 2026-11-27 14:02:19 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-11-27 14:02:18 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 14:02:18 | Glencourse (Kelani Ganga) | 10.77 | 🟢 Normal | -0.090 |  |
| 2026-11-27 14:02:18 | Dunamale (Aththanagalu Oya) | 3.83 | 🟡 Alert | -0.050 |  |
| 2026-11-27 14:02:16 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 14:02:14 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.040 |  |
| 2026-11-27 14:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | -0.010 |  |
| 2026-11-27 14:02:07 | Thanamalwila (Kirindi Oya) | 2.25 | 🟢 Normal | -0.020 |  |
| 2026-11-27 14:01:57 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 14:01:51 | Putupaula (Kalu Ganga) | 1.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-27 14:01:47 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.051 |  |
| 2026-11-27 14:01:10 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.064 |  |
| 2026-11-27 14:00:55 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-27 14:00:11 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-11-27 13:26:53 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 14:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | -0.010 |  |
| 2026-11-27 14:02:18 | Dunamale (Aththanagalu Oya) | 3.83 | 🟡 Alert | -0.050 |  |
| 2026-11-27 13:06:50 | Magura (Kalu Ganga) | 4.07 | 🟡 Alert | -0.106 |  |
| 2026-11-27 13:00:58 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.135 |  |
| 2026-11-27 14:03:44 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 100.000 | 🔺 Rising |
| 2026-11-27 13:05:40 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-11-27 14:01:51 | Putupaula (Kalu Ganga) | 1.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-27 14:00:55 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-27 14:01:57 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 14:02:18 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 13:03:17 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-27 14:02:16 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 13:07:11 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 13:26:53 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.007 |  |
| 2026-11-27 13:06:52 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-11-27 13:04:58 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-27 13:13:38 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.017 |  |
| 2026-11-27 13:11:12 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.018 |  |
| 2026-11-27 13:09:16 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | -0.018 |  |
| 2026-11-27 14:03:00 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-11-27 14:02:48 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-11-27 14:02:07 | Thanamalwila (Kirindi Oya) | 2.25 | 🟢 Normal | -0.020 |  |
| 2026-11-27 14:02:19 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-11-27 13:02:02 | Moragaswewa (Deduru Oya) | 3.35 | 🟢 Normal | -0.020 |  |
| 2026-11-27 14:03:28 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-11-27 13:04:24 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-11-27 14:00:11 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-11-27 14:03:50 | Kuda Oya (Kirindi Oya) | 2.43 | 🟢 Normal | -0.030 |  |
| 2026-11-27 14:02:14 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.040 |  |
| 2026-11-27 14:02:38 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | -0.040 |  |
| 2026-11-27 13:10:50 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | -0.043 |  |
| 2026-11-27 13:08:21 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.050 |  |
| 2026-11-27 14:01:47 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.051 |  |
| 2026-11-27 14:03:33 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | -0.059 |  |
| 2026-11-27 14:01:10 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.064 |  |
| 2026-11-27 13:06:24 | Badalgama (Maha Oya) | 4.67 | 🟢 Normal | -0.090 |  |
| 2026-11-27 14:02:18 | Glencourse (Kelani Ganga) | 10.77 | 🟢 Normal | -0.090 |  |
| 2026-11-27 13:07:58 | Giriulla (Maha Oya) | 3.64 | 🟢 Normal | -0.101 |  |
| 2026-11-27 13:04:55 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)