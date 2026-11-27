# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_03:14:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,606 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 03:14:41 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.008 |  |
| 2026-11-28 03:14:26 | Holombuwa (Kelani Ganga) | 1.87 | 🟢 Normal | -0.171 |  |
| 2026-11-28 03:12:56 | Pitabeddara (Nilwala Ganga) | 1.77 | 🟢 Normal | -0.961 |  |
| 2026-11-28 03:12:05 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-11-28 03:11:26 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-11-28 03:08:43 | Urawa (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.335 |  |
| 2026-11-28 03:08:07 | Panadugama (Nilwala Ganga) | 5.46 | 🟡 Alert | 4.696 | 🔺 Rising |
| 2026-11-28 03:07:44 | Panadugama (Nilwala Ganga) | 5.43 | 🟡 Alert | 4.696 | 🔺 Rising |
| 2026-11-28 03:05:39 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-28 03:05:29 | Magura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-28 03:05:28 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-11-28 03:04:57 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-11-28 03:04:34 | Hanwella (Kelani Ganga) | 4.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-28 03:04:29 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-11-28 03:04:23 | Badalgama (Maha Oya) | 4.43 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-11-28 03:04:01 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | -0.042 |  |
| 2026-11-28 03:03:54 | Thanamalwila (Kirindi Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2026-11-28 03:03:44 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-11-28 03:03:39 | Rathnapura (Kalu Ganga) | 3.13 | 🟢 Normal | -0.035 |  |
| 2026-11-28 03:03:35 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.098 |  |
| 2026-11-28 03:03:31 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.041 |  |
| 2026-11-28 03:02:55 | Kuda Oya (Kirindi Oya) | 3.45 | 🟢 Normal | -0.262 |  |
| 2026-11-28 03:02:43 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-11-28 03:02:41 | Giriulla (Maha Oya) | 3.45 | 🟢 Normal | -0.112 |  |
| 2026-11-28 03:02:39 | Ellagawa (Kalu Ganga) | 7.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-28 03:02:32 | Moragaswewa (Deduru Oya) | 2.71 | 🟢 Normal | -0.059 |  |
| 2026-11-28 03:02:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 03:02:15 | Moraketiya (Walawe Ganga) | 3.80 | 🟡 Alert | 0.000 |  |
| 2026-11-28 03:02:03 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-28 03:01:45 | Glencourse (Kelani Ganga) | 12.35 | 🟢 Normal | -0.109 |  |
| 2026-11-28 03:01:35 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.087 |  |
| 2026-11-28 03:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | -0.040 |  |
| 2026-11-28 03:01:03 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-28 03:00:08 | Wellawaya (Kirindi Oya) | 0.16 | 🟢 Normal | -1.518 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 03:08:07 | Panadugama (Nilwala Ganga) | 5.46 | 🟡 Alert | 4.696 | 🔺 Rising |
| 2026-11-28 03:02:43 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-11-28 03:02:15 | Moraketiya (Walawe Ganga) | 3.80 | 🟡 Alert | 0.000 |  |
| 2026-11-28 03:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | -0.040 |  |
| 2026-11-28 03:03:44 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-11-28 03:12:05 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-11-28 03:04:23 | Badalgama (Maha Oya) | 4.43 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-11-28 03:05:29 | Magura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-28 03:04:34 | Hanwella (Kelani Ganga) | 4.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-28 03:02:39 | Ellagawa (Kalu Ganga) | 7.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-28 02:04:42 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-28 03:05:39 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-28 03:02:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:03:47 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:04:37 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-28 03:11:26 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-11-28 03:03:54 | Thanamalwila (Kirindi Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2026-11-28 03:14:41 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.008 |  |
| 2026-11-28 03:04:29 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-11-28 03:01:03 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-28 03:02:03 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-28 01:04:28 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-11-28 03:05:28 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-11-28 03:04:57 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-11-27 18:01:42 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-11-28 03:03:39 | Rathnapura (Kalu Ganga) | 3.13 | 🟢 Normal | -0.035 |  |
| 2026-11-28 03:03:31 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.041 |  |
| 2026-11-27 18:00:16 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.041 |  |
| 2026-11-28 03:04:01 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | -0.042 |  |
| 2026-11-28 03:02:32 | Moragaswewa (Deduru Oya) | 2.71 | 🟢 Normal | -0.059 |  |
| 2026-11-28 03:01:35 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.087 |  |
| 2026-11-28 03:03:35 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.098 |  |
| 2026-11-28 03:01:45 | Glencourse (Kelani Ganga) | 12.35 | 🟢 Normal | -0.109 |  |
| 2026-11-28 03:02:41 | Giriulla (Maha Oya) | 3.45 | 🟢 Normal | -0.112 |  |
| 2026-11-28 03:14:26 | Holombuwa (Kelani Ganga) | 1.87 | 🟢 Normal | -0.171 |  |
| 2026-11-28 03:02:55 | Kuda Oya (Kirindi Oya) | 3.45 | 🟢 Normal | -0.262 |  |
| 2026-11-28 03:08:43 | Urawa (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.335 |  |
| 2026-11-28 03:12:56 | Pitabeddara (Nilwala Ganga) | 1.77 | 🟢 Normal | -0.961 |  |
| 2026-11-28 03:00:08 | Wellawaya (Kirindi Oya) | 0.16 | 🟢 Normal | -1.518 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)