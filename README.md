# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_17:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,740 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 17:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 17:03:23 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-23 17:03:14 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.207 |  |
| 2026-11-23 17:03:11 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.408 | 🔺 Rising |
| 2026-11-23 17:02:50 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | -0.031 |  |
| 2026-11-23 17:02:44 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-11-23 17:02:34 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-23 17:02:26 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-11-23 17:02:15 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-11-23 17:02:08 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-11-23 17:02:01 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | 0.000 |  |
| 2026-11-23 17:02:00 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-11-23 17:01:36 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 17:00:59 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-23 17:00:23 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.079 |  |
| 2026-11-23 17:00:16 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.051 |  |
| 2026-11-23 17:00:15 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.080 |  |
| 2026-11-23 17:00:14 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 17:03:11 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.408 | 🔺 Rising |
| 2026-11-23 16:04:38 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2026-11-23 16:07:19 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-23 16:02:59 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 17:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 17:00:14 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 17:01:36 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 17:02:34 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-23 16:02:11 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-23 16:01:58 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 16:02:46 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 17:03:23 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-23 17:02:01 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | 0.000 |  |
| 2026-11-23 16:03:16 | Moraketiya (Walawe Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-23 16:06:29 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-23 16:04:48 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 16:04:16 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-23 16:13:20 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.009 |  |
| 2026-11-23 16:05:30 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-11-23 16:03:00 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-23 16:05:13 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-23 17:00:59 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-23 16:04:37 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-11-23 17:02:00 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-11-23 17:02:08 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-11-23 17:02:26 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-11-23 17:02:15 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-11-23 17:02:44 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 16:02:47 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | -0.031 |  |
| 2026-11-23 17:02:50 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | -0.031 |  |
| 2026-11-23 16:09:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.035 |  |
| 2026-11-23 16:04:33 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.041 |  |
| 2026-11-23 17:00:16 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.051 |  |
| 2026-11-23 16:01:30 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.072 |  |
| 2026-11-23 17:00:23 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.079 |  |
| 2026-11-23 17:00:15 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.080 |  |
| 2026-11-23 16:02:43 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.091 |  |
| 2026-11-23 17:03:14 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.207 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)