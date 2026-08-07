# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_00:13:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,383 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 00:13:12 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:12:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:09:44 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:07:31 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:07:16 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:06:37 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | -0.019 |  |
| 2026-08-08 00:05:51 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-08-08 00:05:42 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:05:39 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-08-08 00:05:21 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.050 |  |
| 2026-08-08 00:04:50 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:04:36 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.015 |  |
| 2026-08-08 00:04:27 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:04:16 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.054 |  |
| 2026-08-08 00:04:02 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:03:40 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:03:23 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.079 |  |
| 2026-08-08 00:03:16 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-08-08 00:03:09 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:03:02 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:03:02 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.031 |  |
| 2026-08-08 00:03:01 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:02:58 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:02:45 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-08-08 00:02:40 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-08-08 00:02:28 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-08-08 00:02:26 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:02:12 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:02:01 | Peradeniya (Mahaweli Ganga) | 3.85 | 🟢 Normal | -0.031 |  |
| 2026-08-08 00:01:53 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:01:36 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:01:25 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:01:16 | Kithulgala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.052 |  |
| 2026-08-08 00:01:03 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-08-08 00:01:00 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 00:02:40 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-08-07 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:01:25 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:01:36 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:01:53 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:03:02 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:02:26 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-07 18:10:22 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:02:58 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:05:42 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:04:50 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:04:27 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:13:12 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:07:16 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:03:09 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:07:31 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:04:02 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-07 18:01:27 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:09:44 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:03:40 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:02:12 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:03:01 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:12:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-08-08 00:01:00 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-08 00:03:16 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-08-08 00:02:28 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-08-08 00:04:36 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.015 |  |
| 2026-08-08 00:06:37 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | -0.019 |  |
| 2026-08-08 00:05:39 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-08-08 00:05:51 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-08-08 00:02:45 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-08-08 00:01:03 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-08-08 00:02:01 | Peradeniya (Mahaweli Ganga) | 3.85 | 🟢 Normal | -0.031 |  |
| 2026-08-08 00:03:02 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.031 |  |
| 2026-08-08 00:05:21 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.050 |  |
| 2026-08-08 00:01:16 | Kithulgala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.052 |  |
| 2026-08-08 00:04:16 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.054 |  |
| 2026-08-08 00:03:23 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.079 |  |
| 2026-08-07 21:16:00 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)