# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_00:16:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,910 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 00:16:52 | Panadugama (Nilwala Ganga) | 6.35 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 00:15:33 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-17 00:14:27 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:14:02 | Baddegama (Gin Ganga) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:13:44 | Baddegama (Gin Ganga) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:13:11 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 00:12:10 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-17 00:09:35 | Panadugama (Nilwala Ganga) | 6.35 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 00:09:16 | Pitabeddara (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.044 |  |
| 2026-10-17 00:08:08 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.097 |  |
| 2026-10-17 00:07:52 | Putupaula (Kalu Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:06:55 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.180 |  |
| 2026-10-17 00:06:19 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:06:16 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.020 |  |
| 2026-10-17 00:05:39 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | -0.041 |  |
| 2026-10-17 00:04:38 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-17 00:04:33 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 00:03:45 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:03:36 | Moragaswewa (Deduru Oya) | 1.96 | 🟢 Normal | -0.049 |  |
| 2026-10-17 00:03:34 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-10-17 00:03:32 | Urawa (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:03:32 | Ellagawa (Kalu Ganga) | 7.39 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:03:30 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.089 |  |
| 2026-10-17 00:03:29 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-10-17 00:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | -0.010 |  |
| 2026-10-17 00:03:23 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:03:14 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-10-17 00:02:47 | Magura (Kalu Ganga) | 3.93 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-17 00:02:33 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.121 |  |
| 2026-10-17 00:02:23 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:02:21 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 00:02:15 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:01:57 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.123 |  |
| 2026-10-17 00:01:30 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-17 00:01:26 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:01:15 | Rathnapura (Kalu Ganga) | 4.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-17 00:00:36 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:00:25 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 00:16:52 | Panadugama (Nilwala Ganga) | 6.35 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 00:13:11 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 00:03:29 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-10-17 00:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | -0.010 |  |
| 2026-10-17 00:03:14 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-10-17 00:03:34 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-10-17 00:02:47 | Magura (Kalu Ganga) | 3.93 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-17 00:15:33 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-16 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-17 00:01:30 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-17 00:01:15 | Rathnapura (Kalu Ganga) | 4.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-17 00:04:38 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-17 00:12:10 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-16 18:01:05 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-17 00:02:21 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 00:04:33 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 00:14:02 | Baddegama (Gin Ganga) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:14:27 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:01:26 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:03:23 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:03:32 | Urawa (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:02:23 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:07:52 | Putupaula (Kalu Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:03:32 | Ellagawa (Kalu Ganga) | 7.39 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:06:19 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:00:36 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:03:45 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:02:15 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.010 |  |
| 2026-10-17 00:06:16 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.020 |  |
| 2026-10-16 18:02:38 | Galgamuwa (Mee Oya) | 2.02 | 🟢 Normal | -0.023 |  |
| 2026-10-17 00:05:39 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | -0.041 |  |
| 2026-10-17 00:09:16 | Pitabeddara (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.044 |  |
| 2026-10-17 00:03:36 | Moragaswewa (Deduru Oya) | 1.96 | 🟢 Normal | -0.049 |  |
| 2026-10-17 00:00:25 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.050 |  |
| 2026-10-17 00:03:30 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.089 |  |
| 2026-10-17 00:08:08 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.097 |  |
| 2026-10-17 00:02:33 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.121 |  |
| 2026-10-17 00:01:57 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.123 |  |
| 2026-10-17 00:06:55 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)