# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_02:20:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **254,861 measurements** from **39** stations.
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
| 2026-09-08 02:20:31 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:12:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:10:57 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-09-08 02:08:01 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-08 02:07:05 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-09-08 02:06:43 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -1.019 |  |
| 2026-09-08 02:06:16 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:06:08 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:06:00 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.030 |  |
| 2026-09-08 02:05:37 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:04:28 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-08 02:04:17 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-08 02:04:06 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -36.000 |  |
| 2026-09-08 02:04:05 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -36.000 |  |
| 2026-09-08 02:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:03:35 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:03:21 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:03:17 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:02:37 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:02:36 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.052 |  |
| 2026-09-08 02:02:27 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:02:26 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-08 02:02:21 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-08 02:02:09 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:02:08 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:02:04 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:01:38 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-09-08 02:01:38 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:01:26 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:00:52 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:59:39 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -1.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-08 02:02:26 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-08 02:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-08 00:07:37 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-08 02:04:28 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-08 02:04:17 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-08 02:08:01 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-07 18:10:27 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-08 02:01:38 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:05:37 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:02:27 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:01:51 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:02:09 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:02:08 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 18:04:43 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:00:44 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:02:04 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:03:35 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:06:16 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:12:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:03:17 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:00:52 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:02:37 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:02:21 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:01:26 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:03:21 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:03:47 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:06:57 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:20:31 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:31:53 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.008 |  |
| 2026-09-08 02:10:57 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-09-08 02:07:05 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-09-08 02:01:38 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-09-08 02:06:00 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.030 |  |
| 2026-09-07 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.050 |  |
| 2026-09-08 02:02:36 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.052 |  |
| 2026-09-08 01:03:10 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.222 |  |
| 2026-09-08 02:06:43 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -1.019 |  |
| 2026-09-08 02:04:06 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)