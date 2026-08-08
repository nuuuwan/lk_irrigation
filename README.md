# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_11:30:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,792 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 11:30:22 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-08 11:13:29 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-08-08 11:10:38 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:10:27 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-08 11:10:01 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:09:27 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-08 11:09:25 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:09:13 | Nawalapitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-08-08 11:06:18 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:05:38 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:05:37 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-08-08 11:04:56 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | -0.020 |  |
| 2026-08-08 11:04:29 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-08 11:04:05 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:03:42 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-08 11:03:25 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:03:11 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:03:06 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-08 11:03:05 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-08-08 11:02:51 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:02:49 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:02:36 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:02:36 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | -0.020 |  |
| 2026-08-08 11:02:24 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:02:24 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:02:20 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-08 11:02:16 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.040 |  |
| 2026-08-08 11:02:06 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-08-08 11:02:03 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:01:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:01:33 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:01:29 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:01:09 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-08 11:01:00 | Thanthirimale (Malwathu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:00:42 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:00:40 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:00:29 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:00:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-08-08 11:00:22 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 11:13:29 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-08-08 11:30:22 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-08 11:04:29 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-08 11:01:09 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-08 11:03:42 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-08 11:09:27 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-08 11:03:06 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-08 11:10:27 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-08 11:02:49 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:02:24 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:01:33 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:01:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:03:25 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:00:42 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:10:01 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:02:51 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:02:24 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:02:03 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:10:38 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:06:18 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:09:25 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:00:29 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:02:36 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:04:05 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:05:38 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:00:40 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:01:00 | Thanthirimale (Malwathu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:03:11 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:01:29 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:00:22 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:09:13 | Nawalapitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-08-08 11:02:06 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-08-08 11:02:20 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-08 11:00:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-08-08 11:05:37 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-08-08 11:02:36 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | -0.020 |  |
| 2026-08-08 11:04:56 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | -0.020 |  |
| 2026-08-08 11:03:05 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-08-08 11:02:16 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)