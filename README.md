# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_14:13:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,015 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Baddegama — Alert; 🟡 Magura — Alert; 🟡 Rathnapura — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 14:13:11 | Magura (Kalu Ganga) | 5.47 | 🟡 Alert | -0.009 |  |
| 2026-09-21 14:11:27 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.018 |  |
| 2026-09-21 14:10:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:10:32 | Nawalapitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-09-21 14:09:28 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 14:09:04 | Rathnapura (Kalu Ganga) | 5.62 | 🟡 Alert | -0.047 |  |
| 2026-09-21 14:07:54 | Panadugama (Nilwala Ganga) | 5.62 | 🟡 Alert | -0.055 |  |
| 2026-09-21 14:06:14 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.069 |  |
| 2026-09-21 14:05:48 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2026-09-21 14:05:25 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-21 14:05:17 | Ellagawa (Kalu Ganga) | 9.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-21 14:05:02 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.084 |  |
| 2026-09-21 14:05:01 | Glencourse (Kelani Ganga) | 13.04 | 🟢 Normal | -0.110 |  |
| 2026-09-21 14:04:38 | Hanwella (Kelani Ganga) | 5.92 | 🟢 Normal | -0.137 |  |
| 2026-09-21 14:04:22 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.049 |  |
| 2026-09-21 14:04:12 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-21 14:03:56 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.082 |  |
| 2026-09-21 14:03:52 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 14:03:48 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-09-21 14:03:42 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:03:39 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-09-21 14:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.94 | 🟠 Minor Flood | 0.039 | 🔺 Rising |
| 2026-09-21 14:03:22 | Deraniyagala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:03:20 | Baddegama (Gin Ganga) | 3.99 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-21 14:03:04 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:03:01 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | -0.112 |  |
| 2026-09-21 14:02:55 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:02:12 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 14:02:08 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:01:47 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:01:35 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:01:33 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 14:01:30 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:01:21 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-21 14:01:17 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.031 |  |
| 2026-09-21 14:01:12 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 14:00:45 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | -0.056 |  |
| 2026-09-21 13:59:50 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 14:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.94 | 🟠 Minor Flood | 0.039 | 🔺 Rising |
| 2026-09-21 14:03:39 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-09-21 14:03:20 | Baddegama (Gin Ganga) | 3.99 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-21 14:13:11 | Magura (Kalu Ganga) | 5.47 | 🟡 Alert | -0.009 |  |
| 2026-09-21 14:09:04 | Rathnapura (Kalu Ganga) | 5.62 | 🟡 Alert | -0.047 |  |
| 2026-09-21 14:07:54 | Panadugama (Nilwala Ganga) | 5.62 | 🟡 Alert | -0.055 |  |
| 2026-09-21 14:10:32 | Nawalapitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-09-21 14:04:12 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-21 14:05:25 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-21 14:01:12 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 14:03:52 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 14:05:17 | Ellagawa (Kalu Ganga) | 9.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-21 14:02:12 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 14:01:33 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 14:09:28 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 14:02:08 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:01:30 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:03:22 | Deraniyagala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:10:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:03:04 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:01:35 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:03:42 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:02:55 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:01:47 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 14:01:21 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-21 14:11:27 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.018 |  |
| 2026-09-21 14:03:48 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-09-21 14:05:48 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2026-09-21 14:01:17 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.031 |  |
| 2026-09-21 13:59:50 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | -0.032 |  |
| 2026-09-21 14:04:22 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.049 |  |
| 2026-09-21 14:00:45 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | -0.056 |  |
| 2026-09-21 14:06:14 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.069 |  |
| 2026-09-21 14:03:56 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.082 |  |
| 2026-09-21 14:05:02 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.084 |  |
| 2026-09-21 14:05:01 | Glencourse (Kelani Ganga) | 13.04 | 🟢 Normal | -0.110 |  |
| 2026-09-21 14:03:01 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | -0.112 |  |
| 2026-09-21 14:04:38 | Hanwella (Kelani Ganga) | 5.92 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)