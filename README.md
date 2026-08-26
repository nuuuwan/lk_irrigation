# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_16:11:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **244,099 measurements** from **39** stations.
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
| 2026-08-26 16:11:08 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -0.101 |  |
| 2026-08-26 16:10:56 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-26 16:09:17 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:09:01 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:08:13 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-26 16:07:32 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-08-26 16:06:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:06:44 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:05:51 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-08-26 16:05:49 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-26 16:05:46 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-08-26 16:05:25 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:05:16 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:04:16 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | -0.097 |  |
| 2026-08-26 16:04:03 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-08-26 16:03:42 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.030 |  |
| 2026-08-26 16:03:40 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:03:33 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | -0.020 |  |
| 2026-08-26 16:03:25 | Rathnapura (Kalu Ganga) | 2.99 | 🟢 Normal | -0.124 |  |
| 2026-08-26 16:03:08 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.050 |  |
| 2026-08-26 16:03:04 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-08-26 16:03:00 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-08-26 16:02:42 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:02:32 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-08-26 16:02:19 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.096 |  |
| 2026-08-26 16:02:12 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-26 16:02:08 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:02:08 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:01:40 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-26 16:01:36 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:01:28 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:01:16 | Thanthirimale (Malwathu Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-26 16:01:12 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:00:49 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:00:37 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.051 |  |
| 2026-08-26 16:00:21 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 14:17:30 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-26 16:08:13 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-26 16:05:49 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-26 16:10:56 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-26 16:02:08 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:01:28 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:00:49 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:01:36 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:02:08 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:04:05 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:02:42 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:09:17 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:03:40 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:05:16 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:00:21 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:06:44 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:09:01 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:01:12 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:05:25 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:06:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-08-26 16:02:32 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-08-26 16:01:40 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-26 16:04:03 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-08-26 16:05:51 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-08-26 16:03:00 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-08-26 16:01:16 | Thanthirimale (Malwathu Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-26 16:02:12 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-26 16:07:32 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-08-26 16:03:33 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | -0.020 |  |
| 2026-08-26 16:03:42 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.030 |  |
| 2026-08-26 16:03:04 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-08-26 16:05:46 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-08-26 16:03:08 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.050 |  |
| 2026-08-26 16:00:37 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.051 |  |
| 2026-08-26 16:02:19 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.096 |  |
| 2026-08-26 16:04:16 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | -0.097 |  |
| 2026-08-26 16:11:08 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -0.101 |  |
| 2026-08-26 16:03:25 | Rathnapura (Kalu Ganga) | 2.99 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)