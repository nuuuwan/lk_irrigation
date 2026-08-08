# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_14:30:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,913 measurements** from **39** stations.
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
| 2026-08-08 14:30:11 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:13:56 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-08-08 14:10:18 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-08-08 14:09:13 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:07:58 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:07:13 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 14:07:00 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-08-08 14:06:47 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:06:12 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.038 |  |
| 2026-08-08 14:06:06 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-08 14:06:06 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-08 14:05:55 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:05:39 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:05:18 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-08 14:04:03 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 14:04:01 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:03:57 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:03:35 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:03:21 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 14:03:09 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-08-08 14:03:01 | Kithulgala (Kelani Ganga) | 2.36 | 🟢 Normal | -0.023 |  |
| 2026-08-08 14:02:59 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-08-08 14:02:55 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-08 14:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.064 |  |
| 2026-08-08 14:02:13 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:02:07 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:02:02 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-08-08 14:01:58 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:54 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:54 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:32 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:14 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:10 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:08 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.010 |  |
| 2026-08-08 14:01:04 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:00:54 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:00:52 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:00:11 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 14:03:09 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-08-08 14:02:02 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-08-08 14:05:18 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-08 14:06:06 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-08 14:07:13 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 14:06:06 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-08 14:04:03 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 14:03:21 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 14:00:52 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:10 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-08 13:04:27 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:07:58 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:00:54 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:03:57 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:02:07 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:30:11 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:14 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:54 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:32 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:00:11 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:03:35 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:54 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:02:13 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:05:39 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:05:55 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:04 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:06:47 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-08-08 14:01:58 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 13:01:54 | Thanthirimale (Malwathu Oya) | 0.67 | 🟢 Normal | -0.005 |  |
| 2026-08-08 14:07:00 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-08-08 14:13:56 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-08-08 14:02:55 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-08 14:02:59 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-08-08 14:01:08 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.010 |  |
| 2026-08-08 14:10:18 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-08-08 14:03:01 | Kithulgala (Kelani Ganga) | 2.36 | 🟢 Normal | -0.023 |  |
| 2026-08-08 14:06:12 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.038 |  |
| 2026-08-08 14:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)