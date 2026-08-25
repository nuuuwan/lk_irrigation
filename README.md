# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_23:15:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **243,469 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 23:15:52 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:08:25 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-25 23:06:09 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.037 |  |
| 2026-08-25 23:05:55 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-25 23:05:54 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.060 |  |
| 2026-08-25 23:05:54 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-25 23:05:29 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:05:13 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.863 | 🔺 Rising |
| 2026-08-25 23:04:57 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-08-25 23:04:56 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:04:48 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-08-25 23:04:44 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:04:28 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 23:04:09 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:03:55 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-25 23:03:34 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-08-25 23:03:22 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-08-25 23:03:13 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-25 23:02:56 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-25 23:02:56 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-25 23:02:51 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:02:34 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:02:27 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:02:21 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:02:19 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-25 23:01:51 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:01:14 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:00:37 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-08-25 23:00:30 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 22:58:47 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 0.161 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 23:05:13 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.863 | 🔺 Rising |
| 2026-08-25 21:09:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-08-25 23:03:34 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-08-25 22:58:47 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-08-25 23:03:22 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-08-25 23:03:55 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-25 23:04:57 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-08-25 22:13:24 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-25 23:02:56 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-25 23:02:19 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-25 22:05:55 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-25 23:08:25 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-25 23:05:54 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-25 23:05:55 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-25 23:02:56 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-25 23:03:13 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-25 23:04:28 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 23:04:56 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:04:44 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:01:14 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:02:34 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:00:30 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 22:01:18 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-08-25 18:03:25 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:15:52 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:04:09 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:02:27 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-25 22:04:04 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:05:29 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-25 22:03:11 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:02:51 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 18:02:21 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:01:51 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:02:21 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-25 18:08:33 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.019 |  |
| 2026-08-25 23:04:48 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-08-25 23:00:37 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-08-25 23:06:09 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.037 |  |
| 2026-08-25 23:05:54 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)