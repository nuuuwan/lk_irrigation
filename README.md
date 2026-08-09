# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_12:28:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,743 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 12:28:04 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:19:06 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:15:49 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.020 |  |
| 2026-08-09 12:10:28 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:09:59 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | -0.121 |  |
| 2026-08-09 12:09:42 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.019 |  |
| 2026-08-09 12:07:55 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-09 12:07:02 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 12:05:37 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.077 |  |
| 2026-08-09 12:04:47 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:04:38 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-08-09 12:04:19 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:04:09 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-08-09 12:04:06 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:04:06 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:03:51 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 12:03:40 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-08-09 12:03:38 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-09 12:03:31 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:03:30 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-08-09 12:03:21 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 12:03:17 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:03:01 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-09 12:02:57 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-09 12:02:56 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:02:42 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:02:40 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.032 |  |
| 2026-08-09 12:02:13 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:02:08 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:02:04 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:02:04 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 12:01:58 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-08-09 12:03:38 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-09 12:07:55 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-09 12:03:01 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-09 12:02:04 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-09 12:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 12:03:51 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 12:07:02 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 11:59:41 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 12:03:21 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 12:02:04 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:10:28 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:01:41 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:02:13 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:00:19 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:02:56 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:04:19 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:19:06 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:02:42 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:03:17 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:04:06 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:03:31 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:04:47 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:28:04 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:00:29 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:02:08 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:02:57 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-09 12:04:38 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-08-09 12:03:30 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-08-09 12:03:40 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-08-09 12:01:09 | Peradeniya (Mahaweli Ganga) | 3.62 | 🟢 Normal | -0.011 |  |
| 2026-08-09 12:09:42 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.019 |  |
| 2026-08-09 12:15:49 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.020 |  |
| 2026-08-09 12:04:09 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-08-09 12:02:40 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.032 |  |
| 2026-08-09 12:05:37 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.077 |  |
| 2026-08-09 12:01:14 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.105 |  |
| 2026-08-09 12:09:59 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)