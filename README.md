# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_20:18:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **234,422 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 20:18:25 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:10:59 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.056 |  |
| 2026-08-15 20:10:50 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:08:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -1.433 |  |
| 2026-08-15 20:08:01 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:06:33 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:05:16 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:05:15 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-15 20:05:05 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:04:46 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:04:45 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.059 |  |
| 2026-08-15 20:04:20 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-15 20:04:14 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-15 20:04:07 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-08-15 20:03:59 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-15 20:03:56 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-15 20:03:37 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-15 20:03:36 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:03:24 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.100 |  |
| 2026-08-15 20:02:50 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-08-15 20:02:47 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:02:41 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:02:35 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-08-15 20:02:16 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.031 |  |
| 2026-08-15 20:02:06 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:02:04 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:02:01 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:01:54 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.032 |  |
| 2026-08-15 20:01:53 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-15 20:01:52 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-08-15 20:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:01:46 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.027 |  |
| 2026-08-15 20:01:25 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.122 |  |
| 2026-08-15 20:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:01:12 | Ellagawa (Kalu Ganga) | 5.86 | 🟢 Normal | -0.030 |  |
| 2026-08-15 20:00:39 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 19:59:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 20:04:07 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-08-15 20:03:37 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-15 20:03:59 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-15 20:04:20 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-15 20:04:14 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-15 20:03:56 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-15 20:02:01 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:05:16 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:02:06 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:05:05 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-15 18:11:23 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:00:39 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:10:50 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:04:46 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-15 19:59:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:02:41 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:02:47 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:06:33 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-15 18:01:43 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:18:25 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:08:01 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:03:36 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-15 20:05:15 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-15 20:02:50 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-08-15 20:02:35 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-08-15 20:01:53 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-15 20:01:52 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-08-15 20:01:46 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.027 |  |
| 2026-08-15 20:01:12 | Ellagawa (Kalu Ganga) | 5.86 | 🟢 Normal | -0.030 |  |
| 2026-08-15 20:02:16 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.031 |  |
| 2026-08-15 18:00:55 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.031 |  |
| 2026-08-15 20:01:54 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.032 |  |
| 2026-08-15 20:10:59 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.056 |  |
| 2026-08-15 20:04:45 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.059 |  |
| 2026-08-15 20:03:24 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.100 |  |
| 2026-08-15 20:01:25 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.122 |  |
| 2026-08-15 20:08:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -1.433 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)