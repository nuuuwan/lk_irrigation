# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_13:02:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **247,155 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 13:02:52 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-30 13:02:40 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:02:39 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | -0.010 |  |
| 2026-08-30 13:02:35 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:02:29 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.041 |  |
| 2026-08-30 13:02:27 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.090 |  |
| 2026-08-30 13:02:22 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:02:06 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:02:03 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:01:52 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 13:01:31 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:01:30 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-08-30 13:01:22 | Weraganthota (Mahaweli Ganga) | -3.65 | 🟢 Normal | -0.010 |  |
| 2026-08-30 13:01:18 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:01:09 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:01:07 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:00:59 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:00:51 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.030 |  |
| 2026-08-30 13:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 12:01:52 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-08-30 13:01:30 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-08-30 13:01:52 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 12:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 12:01:51 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 13:02:22 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:02:06 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:02:03 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:02:40 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:00:59 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-30 12:03:28 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-30 12:05:20 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-30 12:05:34 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-30 12:07:31 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:01:31 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 12:04:13 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:01:07 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-30 12:11:24 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:02:35 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-30 12:05:23 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-30 12:04:35 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:01:09 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 12:08:04 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-30 12:07:35 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-08-30 12:04:27 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 13:01:18 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-30 12:06:36 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.009 |  |
| 2026-08-30 12:03:22 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-08-30 13:01:22 | Weraganthota (Mahaweli Ganga) | -3.65 | 🟢 Normal | -0.010 |  |
| 2026-08-30 13:02:52 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-30 13:02:39 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | -0.010 |  |
| 2026-08-30 12:02:40 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | -0.021 |  |
| 2026-08-30 12:00:48 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-08-30 13:00:51 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.030 |  |
| 2026-08-30 12:02:13 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | -0.032 |  |
| 2026-08-30 13:02:29 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.041 |  |
| 2026-08-30 12:08:02 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.043 |  |
| 2026-08-30 13:02:27 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)