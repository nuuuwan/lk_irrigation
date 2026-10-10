# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_00:22:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,493 measurements** from **39** stations.
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
| 2026-10-11 00:22:40 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.008 |  |
| 2026-10-11 00:19:08 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.031 |  |
| 2026-10-11 00:17:30 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.018 |  |
| 2026-10-11 00:15:37 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 5.577 | 🔺 Rising |
| 2026-10-11 00:15:32 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.008 |  |
| 2026-10-11 00:15:09 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 1.333 | 🔺 Rising |
| 2026-10-11 00:14:42 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 1.333 | 🔺 Rising |
| 2026-10-11 00:14:05 | Panadugama (Nilwala Ganga) | 4.11 | 🟢 Normal | -0.011 |  |
| 2026-10-11 00:12:19 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-11 00:10:54 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-10-11 00:08:42 | Dunamale (Aththanagalu Oya) | 2.78 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-11 00:08:25 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | -0.047 |  |
| 2026-10-11 00:07:35 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-11 00:07:09 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-10-11 00:07:01 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 00:06:58 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-11 00:06:10 | Badalgama (Maha Oya) | 3.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 00:05:19 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-11 00:04:46 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.106 |  |
| 2026-10-11 00:04:23 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 00:04:19 | Giriulla (Maha Oya) | 2.88 | 🟢 Normal | -0.011 |  |
| 2026-10-11 00:04:04 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.010 |  |
| 2026-10-11 00:03:44 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | -0.065 |  |
| 2026-10-11 00:03:41 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-11 00:03:38 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-11 00:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.01 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-11 00:02:50 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-11 00:02:48 | Thaldena (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.180 |  |
| 2026-10-11 00:02:45 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-11 00:02:42 | Moragaswewa (Deduru Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-10-11 00:02:24 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-11 00:02:18 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-10-11 00:01:42 | Moraketiya (Walawe Ganga) | 1.82 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-11 00:01:39 | Magura (Kalu Ganga) | 3.24 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-10-11 00:01:37 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-11 00:01:25 | Wellawaya (Kirindi Oya) | 0.00 | 🟢 Normal | 5.577 | 🔺 Rising |
| 2026-10-11 00:01:00 | Nakkala (Kumbukkan Oya) | 1.79 | 🟢 Normal | -0.247 |  |
| 2026-10-11 00:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-11 00:00:05 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 00:15:37 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 5.577 | 🔺 Rising |
| 2026-10-11 00:15:09 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 1.333 | 🔺 Rising |
| 2026-10-11 00:01:39 | Magura (Kalu Ganga) | 3.24 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-10-11 00:07:09 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-10-11 00:02:45 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-11 00:02:50 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-11 00:02:24 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-11 00:08:42 | Dunamale (Aththanagalu Oya) | 2.78 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-11 00:01:42 | Moraketiya (Walawe Ganga) | 1.82 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-11 00:12:19 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-11 00:05:19 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-11 00:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.01 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-11 00:03:38 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-11 00:03:41 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-11 00:06:58 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-11 00:06:10 | Badalgama (Maha Oya) | 3.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 00:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-11 00:01:37 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-11 00:00:05 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:26 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-11 00:07:01 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 00:07:35 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:00:50 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-11 00:22:40 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.008 |  |
| 2026-10-11 00:15:32 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.008 |  |
| 2026-10-11 00:10:54 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-10-11 00:04:04 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.010 |  |
| 2026-10-11 00:02:18 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-10-11 00:14:05 | Panadugama (Nilwala Ganga) | 4.11 | 🟢 Normal | -0.011 |  |
| 2026-10-11 00:04:19 | Giriulla (Maha Oya) | 2.88 | 🟢 Normal | -0.011 |  |
| 2026-10-11 00:17:30 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.018 |  |
| 2026-10-11 00:02:42 | Moragaswewa (Deduru Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-10-11 00:19:08 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.031 |  |
| 2026-10-11 00:08:25 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | -0.047 |  |
| 2026-10-10 18:05:26 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.050 |  |
| 2026-10-11 00:03:44 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | -0.065 |  |
| 2026-10-11 00:04:46 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.106 |  |
| 2026-10-11 00:02:48 | Thaldena (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.180 |  |
| 2026-10-11 00:01:00 | Nakkala (Kumbukkan Oya) | 1.79 | 🟢 Normal | -0.247 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)