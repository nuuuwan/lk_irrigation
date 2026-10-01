# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_15:09:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,062 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 15:09:01 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 15:08:12 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:07:20 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-10-01 15:07:13 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-10-01 15:06:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-10-01 15:06:16 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:06:03 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:06:01 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:05:48 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:05:48 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:04:58 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:03:51 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:03:48 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:03:37 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-10-01 15:03:19 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:03:09 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-01 15:03:07 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.010 |  |
| 2026-10-01 15:03:04 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-10-01 15:02:59 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.071 |  |
| 2026-10-01 15:02:48 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.012 |  |
| 2026-10-01 15:02:31 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:01:57 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:01:54 | Weraganthota (Mahaweli Ganga) | -3.53 | 🟢 Normal | -0.010 |  |
| 2026-10-01 15:01:52 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.088 |  |
| 2026-10-01 15:01:50 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:01:49 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.111 |  |
| 2026-10-01 15:01:42 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:01:34 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:01:14 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-01 15:00:55 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 15:00:42 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-10-01 15:00:27 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-10-01 15:00:26 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:00:07 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 15:07:13 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-10-01 14:05:52 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-01 15:03:09 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-01 15:01:14 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-01 15:00:55 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 15:09:01 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 15:00:26 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:01:34 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:01:42 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:02:31 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:06:16 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:12:01 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:02:59 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:03:19 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:06:01 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:00:07 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:04:58 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:03:48 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:05:48 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:06:03 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:03:51 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:01:57 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:08:12 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:01:50 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:05:48 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-01 15:06:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-10-01 15:03:07 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:05:11 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | -0.010 |  |
| 2026-10-01 15:00:27 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-10-01 15:01:54 | Weraganthota (Mahaweli Ganga) | -3.53 | 🟢 Normal | -0.010 |  |
| 2026-10-01 15:03:37 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-10-01 15:07:20 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-10-01 15:00:42 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-10-01 15:02:48 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.012 |  |
| 2026-10-01 15:03:04 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-10-01 14:05:48 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.022 |  |
| 2026-10-01 15:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.071 |  |
| 2026-10-01 15:01:52 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.088 |  |
| 2026-10-01 15:01:49 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)