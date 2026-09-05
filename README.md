# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_21:16:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **252,858 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-05 21:16:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.016 |  |
| 2026-09-05 21:14:58 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-09-05 21:11:32 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:10:41 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-05 21:10:40 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:10:09 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:09:37 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:09:13 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:07:42 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 7.883 | 🔺 Rising |
| 2026-09-05 21:06:58 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.048 |  |
| 2026-09-05 21:06:15 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.029 |  |
| 2026-09-05 21:05:52 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-09-05 21:05:25 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 7.883 | 🔺 Rising |
| 2026-09-05 21:05:03 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.029 |  |
| 2026-09-05 21:04:52 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-05 21:04:51 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:04:37 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:04:23 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.030 |  |
| 2026-09-05 21:04:21 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-05 21:04:13 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:04:00 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.040 |  |
| 2026-09-05 21:03:47 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:03:43 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:03:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:03:23 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:56 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:45 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-05 21:02:40 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:25 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-05 21:02:21 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:17 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-09-05 21:02:09 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:07 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:01:46 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-09-05 21:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 21:01:23 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:01:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:01:06 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:00:49 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:00:09 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-05 21:07:42 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 7.883 | 🔺 Rising |
| 2026-09-05 21:02:17 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-09-05 21:14:58 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-09-05 21:01:46 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-09-05 21:04:21 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-05 21:02:45 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-05 21:04:52 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-05 21:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 21:10:41 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-05 21:01:23 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:40 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:07 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:01:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:09 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:00:09 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:05:48 | Galgamuwa (Mee Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:04:51 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:11:32 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:09:37 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:03:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:10:09 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:21 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:09:13 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:03:23 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:13:48 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:03:47 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:04:37 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:00:49 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:02:56 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:04:13 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-05 21:05:52 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-09-05 21:02:25 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-05 21:16:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.016 |  |
| 2026-09-05 21:05:03 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.029 |  |
| 2026-09-05 21:06:15 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.029 |  |
| 2026-09-05 21:04:23 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.030 |  |
| 2026-09-05 21:04:00 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.040 |  |
| 2026-09-05 21:06:58 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.048 |  |
| 2026-09-05 18:09:31 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)