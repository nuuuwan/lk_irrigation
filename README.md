# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_14:15:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,121 measurements** from **39** stations.
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
| 2026-09-30 14:15:13 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:14:37 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.019 |  |
| 2026-09-30 14:13:44 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.016 |  |
| 2026-09-30 14:12:07 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:09:15 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:08:27 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.037 |  |
| 2026-09-30 14:08:08 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:07:21 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-09-30 14:06:47 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:06:37 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:06:19 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-30 14:06:08 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.067 |  |
| 2026-09-30 14:06:08 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.021 |  |
| 2026-09-30 14:06:01 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-30 14:05:57 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:04:52 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.010 |  |
| 2026-09-30 14:04:39 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-30 14:04:37 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:03:36 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:03:28 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-09-30 14:03:27 | Glencourse (Kelani Ganga) | 10.47 | 🟢 Normal | -0.041 |  |
| 2026-09-30 14:03:14 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-30 14:03:12 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-09-30 14:03:11 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.049 |  |
| 2026-09-30 14:03:09 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:03:00 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-30 14:02:58 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.070 |  |
| 2026-09-30 14:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.01 | 🟢 Normal | -0.050 |  |
| 2026-09-30 14:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-09-30 14:01:57 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:01:52 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:01:46 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:01:33 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | -0.010 |  |
| 2026-09-30 14:01:29 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-30 14:01:26 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-30 14:00:56 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:00:54 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-09-30 14:00:25 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:00:13 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 14:03:14 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-30 14:03:00 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-30 14:06:01 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-30 14:01:26 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-30 14:06:19 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-30 14:04:39 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-30 14:01:46 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:01:52 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:12:07 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:03:09 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:15:13 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:00:13 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:06:37 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:06:47 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:00:25 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:04:37 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:09:15 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:08:08 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:05:57 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:00:56 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:03:36 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:01:57 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:07:21 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-09-30 14:04:52 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.010 |  |
| 2026-09-30 14:01:33 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | -0.010 |  |
| 2026-09-30 14:01:29 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-30 14:03:12 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-09-30 14:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-09-30 14:00:54 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-09-30 14:13:44 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.016 |  |
| 2026-09-30 14:14:37 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.019 |  |
| 2026-09-30 14:03:28 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-09-30 14:06:08 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.021 |  |
| 2026-09-30 14:08:27 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.037 |  |
| 2026-09-30 14:03:27 | Glencourse (Kelani Ganga) | 10.47 | 🟢 Normal | -0.041 |  |
| 2026-09-30 14:03:11 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.049 |  |
| 2026-09-30 14:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.01 | 🟢 Normal | -0.050 |  |
| 2026-09-30 14:06:08 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.067 |  |
| 2026-09-30 14:02:58 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)