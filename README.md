# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_01:34:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **236,373 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 01:34:09 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-08-18 01:22:42 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-18 01:14:20 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:08:51 | Glencourse (Kelani Ganga) | 10.28 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-18 01:07:29 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-18 01:05:55 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-18 01:05:37 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-18 01:05:32 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-08-18 01:05:06 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:04:37 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:04:28 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-18 01:04:03 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:04:02 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-08-18 01:03:55 | Rathnapura (Kalu Ganga) | 2.93 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-08-18 01:03:42 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.038 |  |
| 2026-08-18 01:03:32 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:03:21 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-18 01:03:04 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:02:52 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-18 01:02:43 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:02:35 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 01:03:55 | Rathnapura (Kalu Ganga) | 2.93 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-08-17 21:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-18 01:07:29 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-18 01:08:51 | Glencourse (Kelani Ganga) | 10.28 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-18 01:03:21 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-18 01:05:37 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-18 01:02:52 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-18 01:22:42 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-18 01:05:55 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-18 01:01:11 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:02:35 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:02:43 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-18 00:01:15 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:01:30 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:03:32 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-18 00:00:16 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:04:13 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-18 00:03:11 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:04:37 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-18 00:13:07 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:01:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-18 00:03:29 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:14:20 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:04:03 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 00:08:58 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:05:06 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:00:44 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:01:18 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-18 01:03:04 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-18 00:11:25 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-08-18 01:04:28 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-18 01:04:02 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-08-18 01:05:32 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-08-18 01:01:08 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-08-18 01:34:09 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-08-18 01:03:42 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.038 |  |
| 2026-08-18 01:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.041 |  |
| 2026-08-17 23:17:12 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)