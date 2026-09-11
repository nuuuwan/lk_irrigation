# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--11_20:06:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **258,239 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-11 20:06:15 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:06:11 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-11 20:05:48 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.095 |  |
| 2026-09-11 20:05:46 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:05:20 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:05:11 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:04:51 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.541 | 🔺 Rising |
| 2026-09-11 20:04:20 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-09-11 20:04:19 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:03:46 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:03:40 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:03:35 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-09-11 20:03:21 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:03:04 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:02:49 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-09-11 20:02:47 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:02:33 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:02:25 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:02:10 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.200 |  |
| 2026-09-11 20:02:07 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:01:59 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:01:56 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:01:47 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:01:39 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:01:30 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:01:23 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:01:18 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:00:58 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-11 19:21:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.015 |  |
| 2026-09-11 19:19:22 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:18:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-11 20:04:51 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.541 | 🔺 Rising |
| 2026-09-11 20:06:11 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-11 18:03:43 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-11 18:08:01 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:02:33 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:01:56 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:03:21 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:04:19 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:05:20 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:06:15 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:01:47 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:16:42 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:03:04 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:02:47 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:02:07 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:05:36 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:01:39 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:03:46 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:01:59 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:01:30 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:02:25 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:05:11 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:07:59 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:10:00 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:05:46 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:02:32 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:03:40 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:19:22 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:01:18 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:01:23 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-11 20:03:35 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-09-11 19:21:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.015 |  |
| 2026-09-11 19:18:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.016 |  |
| 2026-09-11 20:00:58 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-11 20:04:20 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-09-11 20:02:49 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-09-11 20:05:48 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.095 |  |
| 2026-09-11 19:08:38 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.133 |  |
| 2026-09-11 20:02:10 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.200 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)