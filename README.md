# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_14:28:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **257,130 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 14:28:23 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:25:45 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:18:20 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:14:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | -0.017 |  |
| 2026-09-10 14:11:11 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | -16.615 |  |
| 2026-09-10 14:10:43 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:10:19 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -16.615 |  |
| 2026-09-10 14:09:48 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:09:05 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:08:09 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:07:12 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-10 14:06:18 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-10 14:05:56 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:05:53 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:05:05 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:04:45 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-10 14:04:27 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.105 |  |
| 2026-09-10 14:04:17 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:04:06 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:04:03 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:03:35 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.010 |  |
| 2026-09-10 14:03:32 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:03:17 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:03:13 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-09-10 14:02:59 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-10 14:02:49 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:02:28 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-10 14:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-10 14:02:12 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:02:00 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:46 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:46 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:43 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-10 14:01:42 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:42 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:41 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:30 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-10 14:01:09 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:08 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:01 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-10 14:00:50 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-10 13:58:51 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 14:06:18 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-10 14:07:12 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-10 14:01:43 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-10 14:02:28 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-10 14:04:45 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-10 14:02:59 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-10 14:08:09 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:02:00 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:42 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:08 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:46 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:46 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:05:53 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:04:06 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:03:32 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:42 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:10:43 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:18:20 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:05:56 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:03:17 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:09:48 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:09 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:05:05 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:04:03 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:04:17 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:01:41 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:00:50 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:09:05 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:28:23 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:02:12 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:02:49 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-10 14:03:35 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.010 |  |
| 2026-09-10 14:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-10 14:01:30 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-10 14:01:01 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-10 14:03:13 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-09-10 14:14:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | -0.017 |  |
| 2026-09-10 14:04:27 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.105 |  |
| 2026-09-10 14:11:11 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | -16.615 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)