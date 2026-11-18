# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--19_02:11:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,668 measurements** from **39** stations.
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
| 2026-11-19 02:11:50 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:10:36 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-11-19 02:08:04 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-11-19 02:08:04 | Dunamale (Aththanagalu Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:08:02 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.246 |  |
| 2026-11-19 02:07:09 | Panadugama (Nilwala Ganga) | 3.42 | 🟢 Normal | -0.010 |  |
| 2026-11-19 02:06:26 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-19 02:05:48 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-11-19 02:05:36 | Katharagama (Menik Ganga) | 0.53 | 🟢 Normal | -0.031 |  |
| 2026-11-19 02:04:55 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 02:04:49 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-11-19 02:04:42 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:04:24 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:04:11 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:04:11 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:03:55 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:03:44 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-11-19 02:03:14 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-11-19 02:03:04 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:03:02 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:02:16 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:02:15 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 02:02:12 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 02:01:46 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:01:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-11-19 02:01:18 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:01:15 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:01:11 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:01:08 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:01:00 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 02:06:26 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-19 02:02:15 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 02:04:55 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 02:02:12 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 18:02:04 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:03:04 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:01:00 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:00:24 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:01:46 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:01:18 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:01:15 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:13 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:03:02 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:01:08 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:04:24 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:01:11 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:02:55 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:08:04 | Dunamale (Aththanagalu Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:03:55 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:11:50 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:04:42 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:10 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:04:11 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-19 01:03:47 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:02:16 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-19 02:05:48 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-11-19 02:07:09 | Panadugama (Nilwala Ganga) | 3.42 | 🟢 Normal | -0.010 |  |
| 2026-11-19 02:01:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-11-19 02:03:44 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-11-19 01:02:37 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.011 |  |
| 2026-11-19 02:10:36 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-11-19 02:04:49 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-11-19 02:03:14 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-11-19 01:04:00 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.021 |  |
| 2026-11-19 02:08:04 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-11-19 02:05:36 | Katharagama (Menik Ganga) | 0.53 | 🟢 Normal | -0.031 |  |
| 2026-11-19 01:01:34 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.044 |  |
| 2026-11-19 00:12:45 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.052 |  |
| 2026-11-19 02:08:02 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.246 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)