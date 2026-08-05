# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_08:05:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,395 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 08:05:34 | Kithulgala (Kelani Ganga) | 2.86 | 🟢 Normal | -0.100 |  |
| 2026-08-05 08:05:32 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:05:28 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:05:27 | Hanwella (Kelani Ganga) | 4.74 | 🟢 Normal | -0.091 |  |
| 2026-08-05 08:05:17 | Rathnapura (Kalu Ganga) | 4.92 | 🟢 Normal | -0.062 |  |
| 2026-08-05 08:05:13 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:05:00 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-08-05 08:04:43 | Deraniyagala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.078 |  |
| 2026-08-05 08:04:24 | Ellagawa (Kalu Ganga) | 8.93 | 🟢 Normal | -0.010 |  |
| 2026-08-05 08:04:21 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-05 08:04:08 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:04:03 | Peradeniya (Mahaweli Ganga) | 4.90 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-08-05 08:03:59 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:03:49 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:03:29 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:03:25 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-08-05 08:03:17 | Putupaula (Kalu Ganga) | 2.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-05 08:03:07 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-08-05 08:02:34 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-08-05 08:02:26 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:02:26 | Nawalapitiya (Mahaweli Ganga) | 2.91 | 🟢 Normal | -0.142 |  |
| 2026-08-05 08:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | -0.070 |  |
| 2026-08-05 08:02:04 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.474 |  |
| 2026-08-05 08:02:01 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:01:40 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:01:33 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.029 |  |
| 2026-08-05 08:01:19 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-08-05 08:00:48 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.474 |  |
| 2026-08-05 08:00:41 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:00:32 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:00:07 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-05 07:24:02 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 08:04:03 | Peradeniya (Mahaweli Ganga) | 4.90 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-08-05 07:04:21 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-05 07:03:17 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-05 08:03:17 | Putupaula (Kalu Ganga) | 2.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-05 08:04:21 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-05 08:03:59 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 07:01:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:00:41 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-05 07:03:36 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:05:28 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:05:13 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:02:26 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:02:01 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:03:49 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:04:08 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:05:32 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:01:40 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:03:29 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:00:32 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 08:05:00 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-08-05 08:02:34 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-08-05 08:00:07 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-05 08:04:24 | Ellagawa (Kalu Ganga) | 8.93 | 🟢 Normal | -0.010 |  |
| 2026-08-05 08:03:25 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-08-05 08:01:19 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-08-05 08:03:07 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-08-05 07:24:02 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.023 |  |
| 2026-08-05 07:13:28 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.025 |  |
| 2026-08-05 08:01:33 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.029 |  |
| 2026-08-05 07:05:06 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | -0.040 |  |
| 2026-08-05 07:11:33 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.058 |  |
| 2026-08-05 08:05:17 | Rathnapura (Kalu Ganga) | 4.92 | 🟢 Normal | -0.062 |  |
| 2026-08-05 08:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | -0.070 |  |
| 2026-08-05 08:04:43 | Deraniyagala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.078 |  |
| 2026-08-05 08:05:27 | Hanwella (Kelani Ganga) | 4.74 | 🟢 Normal | -0.091 |  |
| 2026-08-05 07:09:38 | Glencourse (Kelani Ganga) | 12.63 | 🟢 Normal | -0.093 |  |
| 2026-08-05 08:05:34 | Kithulgala (Kelani Ganga) | 2.86 | 🟢 Normal | -0.100 |  |
| 2026-08-05 08:02:26 | Nawalapitiya (Mahaweli Ganga) | 2.91 | 🟢 Normal | -0.142 |  |
| 2026-08-05 08:02:04 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.474 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)