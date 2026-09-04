# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_20:30:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **251,913 measurements** from **39** stations.
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
| 2026-09-04 20:30:07 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:18:16 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:15:11 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:14:43 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:11:20 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:10:02 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:09:54 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:09:12 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:08:53 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:08:46 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:08:10 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:06:00 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.029 |  |
| 2026-09-04 20:05:20 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:05:10 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.085 |  |
| 2026-09-04 20:05:01 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-04 20:04:47 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:04:43 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-04 20:04:30 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-09-04 20:04:10 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:03:48 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-09-04 20:03:47 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:03:36 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-04 20:03:12 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.031 |  |
| 2026-09-04 20:03:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:02:53 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-04 20:02:50 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:02:41 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.090 |  |
| 2026-09-04 20:02:31 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:02:21 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:02:17 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-09-04 20:02:16 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:01:53 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:01:13 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-09-04 20:00:35 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 19:58:33 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.210 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 19:58:33 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-09-04 20:05:01 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-04 20:02:53 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-04 20:02:31 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:09:54 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:03:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:02:21 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:01:53 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 18:03:45 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:30:07 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:14:43 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:08:10 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:18:16 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:09:12 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:05:20 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:04:10 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:08:46 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:02:50 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:00:35 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:02:16 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:03:47 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 18:02:31 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:08:53 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:04:47 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:15:11 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:11:20 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:01:13 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-04 20:03:36 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-04 20:04:43 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-04 20:02:17 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-09-04 20:03:48 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-09-04 20:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-09-04 20:06:00 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.029 |  |
| 2026-09-04 20:03:12 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.031 |  |
| 2026-09-04 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.060 |  |
| 2026-09-04 20:04:30 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-09-04 20:05:10 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.085 |  |
| 2026-09-04 20:02:41 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)