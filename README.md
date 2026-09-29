# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_10:33:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,062 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 10:33:56 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.007 |  |
| 2026-09-29 10:26:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:20:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.008 |  |
| 2026-09-29 10:14:57 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-09-29 10:12:39 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:11:00 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-09-29 10:09:01 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.179 |  |
| 2026-09-29 10:08:30 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:06:56 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-09-29 10:06:50 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:05:51 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:05:33 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.068 |  |
| 2026-09-29 10:05:32 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:05:07 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:04:58 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | -0.040 |  |
| 2026-09-29 10:04:47 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.070 |  |
| 2026-09-29 10:04:27 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.042 |  |
| 2026-09-29 10:04:01 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:03:58 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:03:48 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-09-29 10:03:29 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:02:49 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:02:43 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:02:39 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:02:35 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:02:33 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:02:08 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-09-29 10:01:58 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.059 |  |
| 2026-09-29 10:01:57 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | -0.011 |  |
| 2026-09-29 10:01:56 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-09-29 10:01:53 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-09-29 10:01:42 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:01:20 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:00:41 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:00:39 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | -0.015 |  |
| 2026-09-29 10:00:38 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.060 |  |
| 2026-09-29 10:00:36 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:00:08 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 10:00:41 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:00:08 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:02:39 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:26:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:05:32 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:00:36 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:12:39 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:08:30 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:04:01 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:02:49 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:03:48 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:01:42 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:03:58 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:05:07 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:05:51 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:02:35 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:01:20 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-29 09:01:22 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:03:29 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:06:50 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:02:43 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 10:33:56 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.007 |  |
| 2026-09-29 10:20:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.008 |  |
| 2026-09-29 10:11:00 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-09-29 10:06:56 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-09-29 10:01:53 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-09-29 10:02:08 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-09-29 10:01:56 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-09-29 10:01:57 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | -0.011 |  |
| 2026-09-29 10:00:39 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | -0.015 |  |
| 2026-09-29 10:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-09-29 10:14:57 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-09-29 10:04:58 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | -0.040 |  |
| 2026-09-29 10:04:27 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.042 |  |
| 2026-09-29 10:01:58 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.059 |  |
| 2026-09-29 10:00:38 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.060 |  |
| 2026-09-29 10:05:33 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.068 |  |
| 2026-09-29 10:04:47 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.070 |  |
| 2026-09-29 10:09:01 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.179 |  |

## River Water Level Charts by Station

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)