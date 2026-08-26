# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_14:15:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **244,020 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 14:15:50 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.017 |  |
| 2026-08-26 14:13:19 | Magura (Kalu Ganga) | 2.79 | 🟢 Normal | -0.052 |  |
| 2026-08-26 14:13:09 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-26 14:12:53 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-26 14:10:43 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | -0.009 |  |
| 2026-08-26 14:09:41 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.012 |  |
| 2026-08-26 14:07:36 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:06:24 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:05:58 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-26 14:05:04 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:04:18 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:04:07 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:03:56 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.059 |  |
| 2026-08-26 14:03:48 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-26 14:03:31 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:03:21 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-08-26 14:03:20 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 14:03:00 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-26 14:02:52 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-26 14:02:46 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:02:30 | Thanthirimale (Malwathu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:02:29 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-08-26 14:02:18 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 14:02:10 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:02:05 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:01:52 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.031 |  |
| 2026-08-26 14:01:50 | Rathnapura (Kalu Ganga) | 3.25 | 🟢 Normal | -0.126 |  |
| 2026-08-26 14:01:44 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.016 |  |
| 2026-08-26 14:01:39 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:01:32 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-08-26 14:01:30 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:01:22 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:00:54 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-08-26 14:00:07 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 14:03:00 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-26 14:02:52 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-26 14:03:48 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-26 14:05:58 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-26 14:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 14:02:18 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 14:12:53 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-26 14:02:10 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:03:20 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:00:07 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:01:22 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:01:30 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:05:04 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:04:18 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:07:36 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:04:07 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:06:24 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:01:39 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:02:46 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:03:31 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:02:30 | Thanthirimale (Malwathu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-26 13:08:01 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-08-26 13:25:33 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:02:05 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 14:10:43 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | -0.009 |  |
| 2026-08-26 14:13:09 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-26 14:03:21 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-08-26 14:01:32 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-08-26 14:00:54 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-08-26 14:02:29 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-08-26 14:09:41 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.012 |  |
| 2026-08-26 14:01:44 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.016 |  |
| 2026-08-26 14:15:50 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.017 |  |
| 2026-08-26 13:13:21 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.018 |  |
| 2026-08-26 14:01:52 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.031 |  |
| 2026-08-26 14:13:19 | Magura (Kalu Ganga) | 2.79 | 🟢 Normal | -0.052 |  |
| 2026-08-26 14:03:56 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.059 |  |
| 2026-08-26 14:01:50 | Rathnapura (Kalu Ganga) | 3.25 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)