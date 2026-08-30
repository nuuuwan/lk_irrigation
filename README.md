# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_16:02:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **247,275 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 16:02:50 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:02:45 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-08-30 16:02:43 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:02:43 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:02:37 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-08-30 16:02:30 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 16:02:29 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-30 16:02:28 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 16:02:27 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.020 |  |
| 2026-08-30 16:02:24 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:55 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:46 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:33 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:12 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:00:33 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:00:17 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:13:59 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 16:02:29 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-30 16:02:30 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 16:02:28 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 15:05:26 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-30 15:01:21 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-30 15:00:45 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-30 15:09:01 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 16:02:43 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:00:17 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:52 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:55 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:02:24 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:00:33 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:57 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:02:43 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:51 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:13:59 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:07:04 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:12 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:02:50 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:03:00 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:04:08 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:46 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:07:34 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:03:27 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:08:30 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:00:44 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:33 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:47 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.010 |  |
| 2026-08-30 15:10:22 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-08-30 16:02:37 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-08-30 16:02:45 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-08-30 15:01:34 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-08-30 15:06:12 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.012 |  |
| 2026-08-30 16:02:27 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.020 |  |
| 2026-08-30 15:01:12 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.022 |  |
| 2026-08-30 15:03:21 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.032 |  |
| 2026-08-30 15:10:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)