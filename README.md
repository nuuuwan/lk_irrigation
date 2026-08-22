# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_11:12:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **240,334 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 11:12:50 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-22 11:09:17 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.222 |  |
| 2026-08-22 11:08:47 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.009 |  |
| 2026-08-22 11:08:20 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.051 |  |
| 2026-08-22 11:06:32 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-08-22 11:06:24 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.018 |  |
| 2026-08-22 11:05:46 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-08-22 11:04:58 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:04:53 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 11:04:51 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:04:46 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 11:12:50 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-22 11:04:53 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 11:03:51 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:00:43 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:02:51 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:01:15 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:04:13 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:01:31 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:01:16 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:00:15 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:00:30 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:04:51 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:01:46 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:02:19 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:04:58 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:04:09 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:01:41 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:01:09 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-22 11:00:54 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-22 10:14:36 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-08-22 11:08:47 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.009 |  |
| 2026-08-22 11:03:36 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-08-22 11:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | -0.010 |  |
| 2026-08-22 11:03:34 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-22 11:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-08-22 11:02:11 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-08-22 11:01:26 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | -0.018 |  |
| 2026-08-22 11:06:24 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.018 |  |
| 2026-08-22 11:06:32 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-08-22 11:05:46 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-08-22 11:01:00 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.030 |  |
| 2026-08-22 11:04:46 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.040 |  |
| 2026-08-22 11:02:33 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | -0.041 |  |
| 2026-08-22 11:01:28 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.041 |  |
| 2026-08-22 11:00:49 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.051 |  |
| 2026-08-22 11:08:20 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.051 |  |
| 2026-08-22 11:03:11 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.114 |  |
| 2026-08-22 11:09:17 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.222 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)