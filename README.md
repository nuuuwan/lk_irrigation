# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_14:19:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,642 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 14:19:13 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-05 14:16:26 | Rathnapura (Kalu Ganga) | 4.36 | 🟢 Normal | -0.112 |  |
| 2026-08-05 14:12:05 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:12:05 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.050 |  |
| 2026-08-05 14:07:16 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:06:52 | Peradeniya (Mahaweli Ganga) | 6.20 | 🟡 Alert | 0.213 | 🔺 Rising |
| 2026-08-05 14:06:48 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-08-05 14:05:45 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:05:40 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.031 |  |
| 2026-08-05 14:05:05 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.034 |  |
| 2026-08-05 14:04:46 | Glencourse (Kelani Ganga) | 12.36 | 🟢 Normal | -0.021 |  |
| 2026-08-05 14:04:30 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.049 |  |
| 2026-08-05 14:04:04 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:03:58 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:03:54 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-05 14:03:46 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:03:42 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:03:22 | Kithulgala (Kelani Ganga) | 2.62 | 🟢 Normal | -0.040 |  |
| 2026-08-05 14:03:11 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.041 |  |
| 2026-08-05 14:03:09 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.069 |  |
| 2026-08-05 14:03:08 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:03:01 | Hanwella (Kelani Ganga) | 4.30 | 🟢 Normal | -0.071 |  |
| 2026-08-05 14:02:55 | Ellagawa (Kalu Ganga) | 8.84 | 🟢 Normal | -0.020 |  |
| 2026-08-05 14:02:51 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-08-05 14:02:42 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:02:18 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.09 | 🟢 Normal | -0.061 |  |
| 2026-08-05 14:02:11 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | -0.041 |  |
| 2026-08-05 14:02:03 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-08-05 14:02:02 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | -0.051 |  |
| 2026-08-05 14:01:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:01:24 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:00:56 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:00:49 | Nawalapitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.074 |  |
| 2026-08-05 14:00:42 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-08-05 14:00:36 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:00:25 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:00:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 14:06:52 | Peradeniya (Mahaweli Ganga) | 6.20 | 🟡 Alert | 0.213 | 🔺 Rising |
| 2026-08-05 13:00:48 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-05 14:19:13 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-05 14:00:25 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:07:16 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:01:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:05:45 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:02:18 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:03:42 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:00:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:04:04 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:01:24 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:03:58 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:03:08 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:02:42 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:00:56 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:12:05 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:00:36 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:03:46 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 14:02:51 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-08-05 14:00:42 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-08-05 14:03:54 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-05 14:02:03 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-08-05 14:06:48 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-08-05 14:02:55 | Ellagawa (Kalu Ganga) | 8.84 | 🟢 Normal | -0.020 |  |
| 2026-08-05 14:04:46 | Glencourse (Kelani Ganga) | 12.36 | 🟢 Normal | -0.021 |  |
| 2026-08-05 14:05:40 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.031 |  |
| 2026-08-05 14:05:05 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.034 |  |
| 2026-08-05 14:03:22 | Kithulgala (Kelani Ganga) | 2.62 | 🟢 Normal | -0.040 |  |
| 2026-08-05 14:02:11 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | -0.041 |  |
| 2026-08-05 14:03:11 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.041 |  |
| 2026-08-05 14:04:30 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.049 |  |
| 2026-08-05 14:12:05 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.050 |  |
| 2026-08-05 14:02:02 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | -0.051 |  |
| 2026-08-05 14:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.09 | 🟢 Normal | -0.061 |  |
| 2026-08-05 14:03:09 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.069 |  |
| 2026-08-05 14:03:01 | Hanwella (Kelani Ganga) | 4.30 | 🟢 Normal | -0.071 |  |
| 2026-08-05 14:00:49 | Nawalapitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.074 |  |
| 2026-08-05 14:16:26 | Rathnapura (Kalu Ganga) | 4.36 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)