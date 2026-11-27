# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_18:28:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,290 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 18:28:18 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -0.036 |  |
| 2026-11-27 18:09:14 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-27 18:08:04 | Moragaswewa (Deduru Oya) | 3.25 | 🟢 Normal | -1.020 |  |
| 2026-11-27 18:06:51 | Holombuwa (Kelani Ganga) | 1.52 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-11-27 18:06:23 | Pitabeddara (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.751 | 🔺 Rising |
| 2026-11-27 18:05:18 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-27 18:04:50 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-27 18:04:49 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.626 | 🔺 Rising |
| 2026-11-27 18:04:47 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | -0.028 |  |
| 2026-11-27 18:04:46 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-27 18:04:37 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:04:29 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-27 18:03:57 | Badalgama (Maha Oya) | 4.29 | 🟢 Normal | -0.070 |  |
| 2026-11-27 18:03:39 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-11-27 18:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.23 | 🟡 Alert | -0.020 |  |
| 2026-11-27 18:03:25 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.060 |  |
| 2026-11-27 18:03:01 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | 0.602 | 🔺 Rising |
| 2026-11-27 18:02:59 | Magura (Kalu Ganga) | 3.58 | 🟢 Normal | -0.143 |  |
| 2026-11-27 18:02:50 | Dunamale (Aththanagalu Oya) | 3.57 | 🟡 Alert | -0.050 |  |
| 2026-11-27 18:02:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.099 |  |
| 2026-11-27 18:02:18 | Giriulla (Maha Oya) | 3.26 | 🟢 Normal | -0.070 |  |
| 2026-11-27 18:02:11 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.160 |  |
| 2026-11-27 18:02:05 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:01:54 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 18:01:42 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-11-27 18:01:38 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.021 |  |
| 2026-11-27 18:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-27 18:01:29 | Kuda Oya (Kirindi Oya) | 2.24 | 🟢 Normal | -0.040 |  |
| 2026-11-27 18:01:26 | Wellawaya (Kirindi Oya) | 2.08 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-11-27 18:01:26 | Thanamalwila (Kirindi Oya) | 2.02 | 🟢 Normal | -0.070 |  |
| 2026-11-27 18:01:18 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:01:16 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:01:15 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:01:01 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:00:57 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-27 18:00:54 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-11-27 18:00:51 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.053 |  |
| 2026-11-27 18:00:45 | Moraketiya (Walawe Ganga) | 3.19 | 🟡 Alert | 0.126 | 🔺 Rising |
| 2026-11-27 18:00:16 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 18:00:45 | Moraketiya (Walawe Ganga) | 3.19 | 🟡 Alert | 0.126 | 🔺 Rising |
| 2026-11-27 18:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.23 | 🟡 Alert | -0.020 |  |
| 2026-11-27 18:02:50 | Dunamale (Aththanagalu Oya) | 3.57 | 🟡 Alert | -0.050 |  |
| 2026-11-27 18:06:23 | Pitabeddara (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.751 | 🔺 Rising |
| 2026-11-27 18:04:49 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.626 | 🔺 Rising |
| 2026-11-27 18:03:01 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | 0.602 | 🔺 Rising |
| 2026-11-27 18:01:26 | Wellawaya (Kirindi Oya) | 2.08 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-11-27 18:06:51 | Holombuwa (Kelani Ganga) | 1.52 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-11-27 18:03:39 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-11-27 18:09:14 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-27 18:04:29 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-27 18:04:46 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-27 18:01:54 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 18:05:18 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-27 18:01:01 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:01:16 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:04:37 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:02:05 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:01:18 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 17:03:05 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-11-27 18:04:50 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-27 18:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-27 18:00:57 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-27 18:00:54 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-11-27 18:01:38 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.021 |  |
| 2026-11-27 18:04:47 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | -0.028 |  |
| 2026-11-27 18:01:42 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-11-27 18:28:18 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -0.036 |  |
| 2026-11-27 18:01:29 | Kuda Oya (Kirindi Oya) | 2.24 | 🟢 Normal | -0.040 |  |
| 2026-11-27 18:00:16 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.041 |  |
| 2026-11-27 18:00:51 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.053 |  |
| 2026-11-27 18:03:25 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.060 |  |
| 2026-11-27 18:01:26 | Thanamalwila (Kirindi Oya) | 2.02 | 🟢 Normal | -0.070 |  |
| 2026-11-27 18:02:18 | Giriulla (Maha Oya) | 3.26 | 🟢 Normal | -0.070 |  |
| 2026-11-27 18:03:57 | Badalgama (Maha Oya) | 4.29 | 🟢 Normal | -0.070 |  |
| 2026-11-27 18:02:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.099 |  |
| 2026-11-27 18:02:59 | Magura (Kalu Ganga) | 3.58 | 🟢 Normal | -0.143 |  |
| 2026-11-27 18:02:11 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.160 |  |
| 2026-11-27 18:08:04 | Moragaswewa (Deduru Oya) | 3.25 | 🟢 Normal | -1.020 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)