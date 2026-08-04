# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_19:19:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,943 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 19:19:50 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.008 |  |
| 2026-08-04 19:14:00 | Ellagawa (Kalu Ganga) | 8.87 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-04 19:11:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | -0.035 |  |
| 2026-08-04 19:11:27 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.078 |  |
| 2026-08-04 19:08:47 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | -0.059 |  |
| 2026-08-04 19:08:08 | Kithulgala (Kelani Ganga) | 2.96 | 🟢 Normal | -0.219 |  |
| 2026-08-04 19:08:04 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-08-04 19:07:30 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:06:45 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.011 |  |
| 2026-08-04 19:06:43 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:06:08 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-04 19:06:03 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.031 |  |
| 2026-08-04 19:05:17 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-08-04 19:05:16 | Peradeniya (Mahaweli Ganga) | 4.68 | 🟢 Normal | -0.019 |  |
| 2026-08-04 19:05:06 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.037 |  |
| 2026-08-04 19:04:50 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.029 |  |
| 2026-08-04 19:04:48 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-04 19:04:15 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:03:56 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:03:54 | Rathnapura (Kalu Ganga) | 6.05 | 🟡 Alert | -0.113 |  |
| 2026-08-04 19:03:36 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-08-04 19:03:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:03:17 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 19:03:13 | Deraniyagala (Kelani Ganga) | 3.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-04 19:03:12 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.074 |  |
| 2026-08-04 19:02:32 | Hanwella (Kelani Ganga) | 5.22 | 🟢 Normal | -0.122 |  |
| 2026-08-04 19:02:25 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.042 |  |
| 2026-08-04 19:02:21 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-08-04 19:01:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:01:33 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:01:27 | Nawalapitiya (Mahaweli Ganga) | 2.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-04 19:00:56 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:00:37 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:00:36 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:00:31 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 19:11:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | -0.035 |  |
| 2026-08-04 19:03:54 | Rathnapura (Kalu Ganga) | 6.05 | 🟡 Alert | -0.113 |  |
| 2026-08-04 19:03:13 | Deraniyagala (Kelani Ganga) | 3.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-04 19:01:27 | Nawalapitiya (Mahaweli Ganga) | 2.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-04 19:06:08 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-04 19:14:00 | Ellagawa (Kalu Ganga) | 8.87 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-04 19:03:17 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 19:00:36 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:00:56 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:06:43 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:01:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:00:37 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:03:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:01:33 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:03:56 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:07:30 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:32 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:04:15 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:00:31 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-04 19:19:50 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.008 |  |
| 2026-08-04 19:08:04 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-08-04 19:05:17 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-08-04 19:04:48 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-04 19:02:21 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-08-04 19:06:45 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.011 |  |
| 2026-08-04 19:05:16 | Peradeniya (Mahaweli Ganga) | 4.68 | 🟢 Normal | -0.019 |  |
| 2026-08-04 19:03:36 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-08-04 19:04:50 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.029 |  |
| 2026-08-04 19:06:03 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.031 |  |
| 2026-08-04 19:05:06 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.037 |  |
| 2026-08-04 18:11:17 | Glencourse (Kelani Ganga) | 12.76 | 🟢 Normal | -0.038 |  |
| 2026-08-04 19:02:25 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.042 |  |
| 2026-08-04 19:08:47 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | -0.059 |  |
| 2026-08-04 19:03:12 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.074 |  |
| 2026-08-04 19:11:27 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.078 |  |
| 2026-08-04 18:04:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.115 |  |
| 2026-08-04 19:02:32 | Hanwella (Kelani Ganga) | 5.22 | 🟢 Normal | -0.122 |  |
| 2026-08-04 19:08:08 | Kithulgala (Kelani Ganga) | 2.96 | 🟢 Normal | -0.219 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)