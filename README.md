# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_17:17:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,664 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 17:17:54 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:13:32 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.017 |  |
| 2026-08-06 17:11:52 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-06 17:10:14 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:08:42 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:08:02 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:07:32 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-06 17:07:24 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-08-06 17:05:46 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-06 17:05:16 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:05:05 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:04:54 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:04:31 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:04:08 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:04:01 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-08-06 17:03:59 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-06 17:03:56 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.130 |  |
| 2026-08-06 17:03:44 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-08-06 17:03:32 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:03:32 | Deraniyagala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.089 |  |
| 2026-08-06 17:03:19 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:03:12 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:03:09 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:03:02 | Peradeniya (Mahaweli Ganga) | 4.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-06 17:02:55 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-06 17:02:50 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-08-06 17:02:41 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:02:25 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-08-06 17:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.101 |  |
| 2026-08-06 17:02:19 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:02:16 | Hanwella (Kelani Ganga) | 2.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 17:02:13 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:01:57 | Ellagawa (Kalu Ganga) | 6.44 | 🟢 Normal | -0.131 |  |
| 2026-08-06 17:01:49 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:01:38 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:01:32 | Nawalapitiya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-06 17:01:15 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-08-06 17:01:09 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:00:34 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:00:26 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 17:02:50 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-08-06 17:02:25 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-08-06 17:11:52 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-06 17:02:55 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-06 17:01:32 | Nawalapitiya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-06 17:07:32 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-06 17:03:02 | Peradeniya (Mahaweli Ganga) | 4.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-06 17:05:46 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-06 17:03:59 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-06 17:02:16 | Hanwella (Kelani Ganga) | 2.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 17:02:19 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:03:19 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:01:49 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:00:34 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:04:08 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:08:42 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:01:38 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:02:41 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:01:09 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:10:14 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:05:05 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:04:31 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:05:16 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:17:54 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:03:32 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:04:54 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:08:02 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:02:13 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:03:09 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-06 17:07:24 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-08-06 17:00:26 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.010 |  |
| 2026-08-06 17:01:15 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-08-06 17:13:32 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.017 |  |
| 2026-08-06 17:03:44 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-08-06 17:04:01 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-08-06 17:03:32 | Deraniyagala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.089 |  |
| 2026-08-06 17:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.101 |  |
| 2026-08-06 17:03:56 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.130 |  |
| 2026-08-06 17:01:57 | Ellagawa (Kalu Ganga) | 6.44 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)