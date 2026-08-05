# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_02:14:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,077 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 02:14:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:11:07 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.018 |  |
| 2026-08-06 02:08:36 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:07:55 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:07:53 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 02:07:52 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.029 |  |
| 2026-08-06 02:07:21 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-06 02:07:17 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:06:25 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:06:19 | Ellagawa (Kalu Ganga) | 8.20 | 🟢 Normal | -7.059 |  |
| 2026-08-06 02:05:44 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:05:39 | Hanwella (Kelani Ganga) | 3.55 | 🟢 Normal | -0.077 |  |
| 2026-08-06 02:05:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.029 |  |
| 2026-08-06 02:04:37 | Glencourse (Kelani Ganga) | 11.53 | 🟢 Normal | -0.062 |  |
| 2026-08-06 02:04:23 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:03:52 | Kithulgala (Kelani Ganga) | 2.49 | 🟢 Normal | -0.159 |  |
| 2026-08-06 02:03:46 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -7.059 |  |
| 2026-08-06 02:03:08 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:02:50 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-08-06 02:02:45 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-08-06 02:02:26 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:02:17 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:02:10 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.031 |  |
| 2026-08-06 02:01:56 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:01:50 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:01:31 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:01:28 | Nawalapitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-08-06 02:00:50 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-06 01:48:24 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 01:04:41 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-06 02:07:53 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 02:01:56 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:00:50 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-06 01:03:44 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-06 01:06:18 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:11:01 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-06 01:48:24 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:05:44 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:08:36 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:02:17 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 01:08:47 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:03:02 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:02:26 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:06:25 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:03:08 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:09:25 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:07:17 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:04:23 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:01:50 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 02:14:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-08-06 02:07:21 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-06 02:02:50 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-08-06 02:01:28 | Nawalapitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-08-06 01:05:05 | Putupaula (Kalu Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-08-06 02:11:07 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.018 |  |
| 2026-08-06 01:01:48 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-08-06 02:02:45 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-08-06 01:08:59 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-08-06 02:05:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.029 |  |
| 2026-08-06 02:07:52 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.029 |  |
| 2026-08-06 02:02:10 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.031 |  |
| 2026-08-06 02:04:37 | Glencourse (Kelani Ganga) | 11.53 | 🟢 Normal | -0.062 |  |
| 2026-08-06 02:05:39 | Hanwella (Kelani Ganga) | 3.55 | 🟢 Normal | -0.077 |  |
| 2026-08-06 01:04:50 | Rathnapura (Kalu Ganga) | 3.17 | 🟢 Normal | -0.129 |  |
| 2026-08-06 02:03:52 | Kithulgala (Kelani Ganga) | 2.49 | 🟢 Normal | -0.159 |  |
| 2026-08-06 01:02:26 | Peradeniya (Mahaweli Ganga) | 4.82 | 🟢 Normal | -0.180 |  |
| 2026-08-06 02:06:19 | Ellagawa (Kalu Ganga) | 8.20 | 🟢 Normal | -7.059 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)