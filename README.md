# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_04:03:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,771 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 04:03:06 | Thawalama (Gin Ganga) | 3.41 | 🟢 Normal | -0.446 |  |
| 2026-11-09 04:02:55 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-09 04:02:38 | Giriulla (Maha Oya) | 3.87 | 🟢 Normal | -0.184 |  |
| 2026-11-09 04:02:20 | Glencourse (Kelani Ganga) | 12.75 | 🟢 Normal | -0.222 |  |
| 2026-11-09 04:02:12 | Peradeniya (Mahaweli Ganga) | 3.52 | 🟢 Normal | -0.060 |  |
| 2026-11-09 04:01:43 | Horowpothana (Yan Oya) | 3.09 | 🟢 Normal | -0.051 |  |
| 2026-11-09 04:01:23 | Moragaswewa (Deduru Oya) | 3.24 | 🟢 Normal | -0.079 |  |
| 2026-11-09 04:01:21 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.042 |  |
| 2026-11-09 04:01:21 | Holombuwa (Kelani Ganga) | 1.79 | 🟢 Normal | -0.079 |  |
| 2026-11-09 04:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.052 |  |
| 2026-11-09 04:01:11 | Ellagawa (Kalu Ganga) | 8.06 | 🟢 Normal | -0.020 |  |
| 2026-11-09 04:00:25 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-11-09 03:44:14 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | -72.000 |  |
| 2026-11-09 03:44:13 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -72.000 |  |
| 2026-11-09 03:44:12 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -72.000 |  |
| 2026-11-09 03:33:46 | Panadugama (Nilwala Ganga) | 5.84 | 🟡 Alert | 0.000 |  |
| 2026-11-09 03:31:14 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 03:21:37 | Magura (Kalu Ganga) | 5.12 | 🟡 Alert | 0.468 | 🔺 Rising |
| 2026-11-09 03:03:00 | Dunamale (Aththanagalu Oya) | 4.10 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-09 02:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.66 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-09 03:33:46 | Panadugama (Nilwala Ganga) | 5.84 | 🟡 Alert | 0.000 |  |
| 2026-11-09 03:31:14 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | 0.000 |  |
| 2026-11-09 03:11:11 | Moraketiya (Walawe Ganga) | 3.04 | 🟡 Alert | -0.007 |  |
| 2026-11-09 03:05:30 | Badalgama (Maha Oya) | 4.42 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-11-08 18:01:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-09 03:08:58 | Hanwella (Kelani Ganga) | 5.26 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-09 03:04:45 | Baddegama (Gin Ganga) | 3.45 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-09 03:09:00 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-09 03:09:24 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-09 03:03:44 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 03:11:10 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-09 03:03:00 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 03:19:20 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-09 04:02:55 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-08 18:02:22 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-08 23:07:10 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-11-09 03:04:04 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-11-09 03:06:24 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-11-08 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-09 04:01:11 | Ellagawa (Kalu Ganga) | 8.06 | 🟢 Normal | -0.020 |  |
| 2026-11-09 03:00:14 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-11-09 03:07:57 | Urawa (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.029 |  |
| 2026-11-09 04:00:25 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-11-09 04:01:21 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.042 |  |
| 2026-11-09 04:01:43 | Horowpothana (Yan Oya) | 3.09 | 🟢 Normal | -0.051 |  |
| 2026-11-09 04:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.052 |  |
| 2026-11-09 04:02:12 | Peradeniya (Mahaweli Ganga) | 3.52 | 🟢 Normal | -0.060 |  |
| 2026-11-09 03:15:26 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.078 |  |
| 2026-11-09 04:01:23 | Moragaswewa (Deduru Oya) | 3.24 | 🟢 Normal | -0.079 |  |
| 2026-11-09 04:01:21 | Holombuwa (Kelani Ganga) | 1.79 | 🟢 Normal | -0.079 |  |
| 2026-11-09 04:02:38 | Giriulla (Maha Oya) | 3.87 | 🟢 Normal | -0.184 |  |
| 2026-11-09 03:06:42 | Rathnapura (Kalu Ganga) | 3.82 | 🟢 Normal | -0.201 |  |
| 2026-11-09 04:02:20 | Glencourse (Kelani Ganga) | 12.75 | 🟢 Normal | -0.222 |  |
| 2026-11-09 04:03:06 | Thawalama (Gin Ganga) | 3.41 | 🟢 Normal | -0.446 |  |
| 2026-11-09 03:05:51 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | -1.333 |  |
| 2026-11-09 03:44:14 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)