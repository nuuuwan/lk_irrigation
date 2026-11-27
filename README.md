# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_02:03:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,554 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Panadugama — Alert; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 02:03:05 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-28 02:02:59 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-28 02:02:37 | Moraketiya (Walawe Ganga) | 3.80 | 🟡 Alert | 0.000 |  |
| 2026-11-28 02:02:18 | Badalgama (Maha Oya) | 4.32 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-11-28 02:02:05 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.101 |  |
| 2026-11-28 02:01:40 | Moragaswewa (Deduru Oya) | 2.77 | 🟢 Normal | -0.020 |  |
| 2026-11-28 02:01:29 | Ellagawa (Kalu Ganga) | 7.36 | 🟢 Normal | -0.040 |  |
| 2026-11-28 02:01:21 | Glencourse (Kelani Ganga) | 12.46 | 🟢 Normal | -0.120 |  |
| 2026-11-28 02:01:12 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-28 02:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.050 |  |
| 2026-11-28 02:00:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | -0.012 |  |
| 2026-11-28 02:00:12 | Wellawaya (Kirindi Oya) | 1.68 | 🟢 Normal | 1.404 | 🔺 Rising |
| 2026-11-28 01:28:37 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 01:03:15 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | 0.147 | 🔺 Rising |
| 2026-11-28 01:04:00 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-28 02:02:37 | Moraketiya (Walawe Ganga) | 3.80 | 🟡 Alert | 0.000 |  |
| 2026-11-28 02:00:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | -0.012 |  |
| 2026-11-28 02:00:12 | Wellawaya (Kirindi Oya) | 1.68 | 🟢 Normal | 1.404 | 🔺 Rising |
| 2026-11-28 01:12:45 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-11-28 01:07:30 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-11-28 01:06:03 | Hanwella (Kelani Ganga) | 4.15 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-11-28 02:02:18 | Badalgama (Maha Oya) | 4.32 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-11-28 01:00:45 | Magura (Kalu Ganga) | 3.88 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-11-28 01:13:07 | Pitabeddara (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-28 01:07:33 | Rathnapura (Kalu Ganga) | 3.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-28 01:03:48 | Urawa (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-28 02:03:05 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:03:47 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:04:37 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:22:27 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-28 01:09:02 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-28 01:19:43 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-28 01:01:09 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 02:02:59 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-28 01:14:40 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:12:15 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-11-28 02:01:12 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-28 01:04:28 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-11-28 02:01:40 | Moragaswewa (Deduru Oya) | 2.77 | 🟢 Normal | -0.020 |  |
| 2026-11-28 01:28:37 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.021 |  |
| 2026-11-27 18:01:42 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-11-28 02:01:29 | Ellagawa (Kalu Ganga) | 7.36 | 🟢 Normal | -0.040 |  |
| 2026-11-27 18:00:16 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.041 |  |
| 2026-11-28 02:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.050 |  |
| 2026-11-28 01:03:49 | Giriulla (Maha Oya) | 3.69 | 🟢 Normal | -0.059 |  |
| 2026-11-28 01:01:01 | Peradeniya (Mahaweli Ganga) | 3.68 | 🟢 Normal | -0.060 |  |
| 2026-11-28 01:16:13 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.066 |  |
| 2026-11-28 02:02:05 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.101 |  |
| 2026-11-28 01:03:38 | Kuda Oya (Kirindi Oya) | 3.97 | 🟢 Normal | -0.118 |  |
| 2026-11-28 02:01:21 | Glencourse (Kelani Ganga) | 12.46 | 🟢 Normal | -0.120 |  |
| 2026-11-28 00:10:11 | Thanamalwila (Kirindi Oya) | 3.50 | 🟢 Normal | -0.123 |  |
| 2026-11-28 01:12:11 | Holombuwa (Kelani Ganga) | 2.31 | 🟢 Normal | -0.206 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)