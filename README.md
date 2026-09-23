# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_13:24:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,785 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 13:24:03 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:19:09 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.016 |  |
| 2026-09-23 13:17:57 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-23 13:14:28 | Thalgahagoda (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.025 |  |
| 2026-09-23 13:14:06 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:12:23 | Rathnapura (Kalu Ganga) | 3.77 | 🟢 Normal | -0.026 |  |
| 2026-09-23 13:09:32 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 13:08:53 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:08:29 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.009 |  |
| 2026-09-23 13:07:12 | Baddegama (Gin Ganga) | 3.75 | 🟡 Alert | -0.010 |  |
| 2026-09-23 13:07:05 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:06:53 | Putupaula (Kalu Ganga) | 2.87 | 🟢 Normal | 7.200 | 🔺 Rising |
| 2026-09-23 13:06:43 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:06:31 | Glencourse (Kelani Ganga) | 12.75 | 🟢 Normal | -0.030 |  |
| 2026-09-23 13:06:20 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-09-23 13:06:18 | Putupaula (Kalu Ganga) | 2.80 | 🟢 Normal | 7.200 | 🔺 Rising |
| 2026-09-23 13:06:16 | Ellagawa (Kalu Ganga) | 8.03 | 🟢 Normal | -0.029 |  |
| 2026-09-23 13:06:14 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | -0.009 |  |
| 2026-09-23 13:05:38 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-09-23 13:05:03 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 13:04:54 | Hanwella (Kelani Ganga) | 4.81 | 🟢 Normal | -0.010 |  |
| 2026-09-23 13:04:44 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-09-23 13:04:43 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.010 |  |
| 2026-09-23 13:04:17 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.060 |  |
| 2026-09-23 13:04:12 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.077 |  |
| 2026-09-23 13:03:35 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-09-23 13:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.97 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-23 13:03:22 | Deraniyagala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 13:03:09 | Nawalapitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 13:02:50 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:02:38 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 13:02:36 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-23 13:02:10 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:02:04 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.207 |  |
| 2026-09-23 13:02:03 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:01:35 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-23 13:01:27 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:01:13 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:00:57 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 13:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.97 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-23 13:06:14 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | -0.009 |  |
| 2026-09-23 13:07:12 | Baddegama (Gin Ganga) | 3.75 | 🟡 Alert | -0.010 |  |
| 2026-09-23 13:06:53 | Putupaula (Kalu Ganga) | 2.87 | 🟢 Normal | 7.200 | 🔺 Rising |
| 2026-09-23 13:17:57 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-23 13:02:36 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-23 13:01:35 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-23 13:03:22 | Deraniyagala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 13:03:09 | Nawalapitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 13:00:57 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-23 13:02:38 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 13:05:03 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 13:09:32 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 13:06:43 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:24:03 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:01:13 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:14:06 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:07:05 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:02:03 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:02:10 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:08:53 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:02:50 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:01:27 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 13:08:29 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.009 |  |
| 2026-09-23 13:04:54 | Hanwella (Kelani Ganga) | 4.81 | 🟢 Normal | -0.010 |  |
| 2026-09-23 13:04:43 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.010 |  |
| 2026-09-23 13:05:38 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-09-23 13:04:44 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-09-23 13:03:35 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-09-23 13:06:20 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-09-23 13:19:09 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.016 |  |
| 2026-09-23 13:14:28 | Thalgahagoda (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.025 |  |
| 2026-09-23 13:12:23 | Rathnapura (Kalu Ganga) | 3.77 | 🟢 Normal | -0.026 |  |
| 2026-09-23 13:06:16 | Ellagawa (Kalu Ganga) | 8.03 | 🟢 Normal | -0.029 |  |
| 2026-09-23 13:06:31 | Glencourse (Kelani Ganga) | 12.75 | 🟢 Normal | -0.030 |  |
| 2026-09-23 13:04:17 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.060 |  |
| 2026-09-23 13:04:12 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.077 |  |
| 2026-09-23 13:02:04 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.207 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)