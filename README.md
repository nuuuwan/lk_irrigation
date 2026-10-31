# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_20:23:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,274 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 20:23:14 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:14:04 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:13:12 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-31 20:12:53 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-10-31 20:12:44 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:10:10 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-10-31 20:09:42 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-10-31 20:09:31 | Hanwella (Kelani Ganga) | 2.42 | 🟢 Normal | -0.036 |  |
| 2026-10-31 20:08:51 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-31 20:06:59 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.021 |  |
| 2026-10-31 20:06:42 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:06:07 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.010 |  |
| 2026-10-31 20:05:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.32 | 🟢 Normal | -0.049 |  |
| 2026-10-31 20:05:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2026-10-31 20:05:08 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:04:39 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:04:30 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-10-31 20:03:47 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-31 20:03:20 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.050 |  |
| 2026-10-31 20:03:16 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.054 |  |
| 2026-10-31 20:03:14 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 20:03:03 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 20:02:52 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-31 20:02:52 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:02:46 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.061 |  |
| 2026-10-31 20:02:43 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:02:36 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-10-31 20:02:19 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.148 |  |
| 2026-10-31 20:02:16 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-31 20:02:10 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:01:53 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:01:12 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.021 |  |
| 2026-10-31 20:01:06 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:00:53 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 20:02:36 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-10-31 20:08:51 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-31 20:03:47 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-31 20:03:14 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 20:03:03 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 20:02:16 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-31 20:13:12 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-31 20:01:53 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:04:39 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:12:44 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:14:04 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:06:42 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:05:08 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:01:06 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:02:43 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:02:10 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:23:14 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:10:10 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-10-31 20:09:42 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-10-31 20:06:07 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.010 |  |
| 2026-10-31 20:00:53 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-31 20:02:52 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:51 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-31 20:04:30 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-10-31 18:04:44 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.020 |  |
| 2026-10-31 20:12:53 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-10-31 20:01:12 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.021 |  |
| 2026-10-31 20:06:59 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.021 |  |
| 2026-10-31 19:01:36 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | -0.031 |  |
| 2026-10-31 20:09:31 | Hanwella (Kelani Ganga) | 2.42 | 🟢 Normal | -0.036 |  |
| 2026-10-31 20:05:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.32 | 🟢 Normal | -0.049 |  |
| 2026-10-31 20:03:20 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.050 |  |
| 2026-10-31 20:03:16 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.054 |  |
| 2026-10-31 20:05:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2026-10-31 20:02:46 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.061 |  |
| 2026-10-31 18:59:17 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.070 |  |
| 2026-10-31 20:02:19 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.148 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)