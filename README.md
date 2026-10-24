# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_01:18:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,131 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 01:18:58 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-10-25 01:11:58 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.026 |  |
| 2026-10-25 01:11:12 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 2.124 | 🔺 Rising |
| 2026-10-25 01:09:31 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:08:31 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-10-25 01:07:11 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-25 01:06:29 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-25 01:06:01 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-25 01:05:37 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.023 |  |
| 2026-10-25 01:05:33 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 2.124 | 🔺 Rising |
| 2026-10-25 01:05:31 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:05:30 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 01:04:30 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-25 01:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.58 | 🟢 Normal | -0.023 |  |
| 2026-10-25 01:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:03:48 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-10-25 01:03:30 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:03:01 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.013 |  |
| 2026-10-25 01:02:37 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.091 |  |
| 2026-10-25 01:02:28 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:02:24 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:02:18 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-25 01:02:11 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.020 |  |
| 2026-10-25 01:01:42 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-10-25 01:01:13 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-10-25 01:01:06 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 01:00:18 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:00:11 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-25 00:58:42 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 01:11:12 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 2.124 | 🔺 Rising |
| 2026-10-25 00:03:35 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-25 01:05:30 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 01:01:06 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 01:07:11 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-25 01:04:30 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-25 01:09:31 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:00:18 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:00:11 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:02:24 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:05:31 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:03:30 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-10-25 00:13:36 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 23:02:47 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:02:28 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 01:18:58 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-10-25 01:08:31 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-10-25 01:06:01 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-25 00:01:09 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-10-25 01:02:18 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-25 01:06:29 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-25 00:04:46 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-25 01:01:42 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-10-25 00:02:34 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-10-25 00:47:04 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-10-25 01:03:01 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.013 |  |
| 2026-10-25 00:10:25 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -0.018 |  |
| 2026-10-24 18:00:25 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.020 |  |
| 2026-10-25 01:02:11 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.020 |  |
| 2026-10-24 21:12:32 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.022 |  |
| 2026-10-25 01:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.58 | 🟢 Normal | -0.023 |  |
| 2026-10-25 01:05:37 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.023 |  |
| 2026-10-25 01:11:58 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.026 |  |
| 2026-10-25 01:03:48 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-10-24 18:02:58 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-10-25 01:01:13 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-10-24 18:01:50 | Galgamuwa (Mee Oya) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-10-25 01:02:37 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)