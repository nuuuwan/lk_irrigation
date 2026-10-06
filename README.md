# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_13:23:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,489 measurements** from **39** stations.
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
| 2026-10-06 13:23:11 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:17:07 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:08:26 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.195 |  |
| 2026-10-06 13:06:56 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:05:44 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-10-06 13:05:37 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-06 13:05:36 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-06 13:05:02 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.147 |  |
| 2026-10-06 13:04:54 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.064 |  |
| 2026-10-06 13:04:45 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:04:24 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.030 |  |
| 2026-10-06 13:04:05 | Hanwella (Kelani Ganga) | 3.58 | 🟢 Normal | -0.099 |  |
| 2026-10-06 13:03:50 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.189 |  |
| 2026-10-06 13:03:27 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.021 |  |
| 2026-10-06 13:03:22 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-06 13:03:19 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-10-06 13:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.063 |  |
| 2026-10-06 13:02:57 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-10-06 13:02:49 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.040 |  |
| 2026-10-06 13:02:43 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.050 |  |
| 2026-10-06 13:02:36 | Glencourse (Kelani Ganga) | 11.32 | 🟢 Normal | -0.083 |  |
| 2026-10-06 13:02:18 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.041 |  |
| 2026-10-06 13:02:04 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-06 13:01:47 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-10-06 13:01:39 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-06 13:01:37 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:01:25 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:01:22 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-10-06 13:01:17 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-10-06 13:01:13 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:01:13 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-06 13:01:07 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | -0.051 |  |
| 2026-10-06 13:00:47 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:00:46 | Pitabeddara (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-06 13:00:46 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-06 13:00:43 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-10-06 13:00:16 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-10-06 13:00:15 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 13:01:17 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-10-06 13:01:22 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-10-06 13:05:36 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-06 13:05:37 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-06 13:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:01:37 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:01:25 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:01:13 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:06:56 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:17:07 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:00:15 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:04:45 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:00:47 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:23:11 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-06 13:02:04 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-06 13:00:46 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-06 13:01:39 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-06 13:00:43 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-10-06 13:01:13 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-06 13:03:22 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-06 13:00:46 | Pitabeddara (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-06 12:02:42 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-10-06 13:03:19 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-10-06 13:02:57 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-10-06 13:03:27 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.021 |  |
| 2026-10-06 13:04:24 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.030 |  |
| 2026-10-06 13:01:47 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-10-06 13:05:44 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-10-06 13:02:49 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.040 |  |
| 2026-10-06 13:02:18 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.041 |  |
| 2026-10-06 13:02:43 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.050 |  |
| 2026-10-06 13:01:07 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | -0.051 |  |
| 2026-10-06 13:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.063 |  |
| 2026-10-06 13:04:54 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.064 |  |
| 2026-10-06 13:02:36 | Glencourse (Kelani Ganga) | 11.32 | 🟢 Normal | -0.083 |  |
| 2026-10-06 13:04:05 | Hanwella (Kelani Ganga) | 3.58 | 🟢 Normal | -0.099 |  |
| 2026-10-06 13:05:02 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.147 |  |
| 2026-10-06 13:03:50 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.189 |  |
| 2026-10-06 13:08:26 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)