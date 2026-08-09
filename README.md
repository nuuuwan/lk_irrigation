# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_20:19:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,053 measurements** from **39** stations.
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
| 2026-08-09 20:19:54 | Rathnapura (Kalu Ganga) | 3.25 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-08-09 20:11:39 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-09 20:11:37 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:10:02 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-08-09 20:09:22 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:09:03 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-08-09 20:08:47 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.070 |  |
| 2026-08-09 20:08:43 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-08-09 20:08:20 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 20:08:09 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-09 20:06:04 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:06:02 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | -0.010 |  |
| 2026-08-09 20:05:46 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-08-09 20:05:42 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:05:29 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:05:26 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:05:19 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-08-09 20:05:17 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-08-09 20:05:10 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:05:00 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-08-09 20:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-09 20:04:34 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:03:37 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:03:26 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:03:16 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-08-09 20:03:02 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:03:02 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-08-09 20:03:01 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 20:02:39 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 20:02:32 | Peradeniya (Mahaweli Ganga) | 3.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-09 20:02:11 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:02:07 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-09 20:01:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:00:59 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:00:49 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:00:48 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:00:27 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 20:05:19 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-08-09 20:19:54 | Rathnapura (Kalu Ganga) | 3.25 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-08-09 20:02:07 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-09 20:08:09 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-09 20:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-09 20:02:32 | Peradeniya (Mahaweli Ganga) | 3.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-09 20:03:01 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 18:01:36 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 20:02:39 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 20:08:20 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 20:11:39 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-09 20:05:10 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:05:26 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:11:37 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:01:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:00:59 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:02:11 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:05:29 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:06:04 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:09:22 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:03:37 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:00:48 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:03:26 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:05:42 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:00:49 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:03:02 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-09 20:05:00 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-08-09 20:03:02 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-08-09 20:05:46 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-08-09 20:06:02 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | -0.010 |  |
| 2026-08-09 20:08:43 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-08-09 20:09:03 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-08-09 20:05:17 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-08-09 20:10:02 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-08-09 20:00:27 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.030 |  |
| 2026-08-09 20:03:16 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-08-09 18:02:25 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-08-09 20:08:47 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)