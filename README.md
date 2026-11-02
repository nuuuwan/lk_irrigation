# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_05:25:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,498 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 05:25:25 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:22:00 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:21:29 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | -0.016 |  |
| 2026-11-02 05:18:12 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-02 05:14:51 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-02 05:13:39 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-02 05:07:27 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-11-02 05:07:20 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:07:19 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-11-02 05:07:16 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-02 05:06:27 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:05:54 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:05:49 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-02 05:05:11 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.047 |  |
| 2026-11-02 05:04:43 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-02 05:04:01 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.059 |  |
| 2026-11-02 05:03:47 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-11-02 05:03:31 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:03:08 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-11-02 05:02:53 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-11-02 05:02:50 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:02:47 | Glencourse (Kelani Ganga) | 11.33 | 🟢 Normal | -0.090 |  |
| 2026-11-02 05:02:38 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:01:50 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-02 05:01:39 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-11-02 05:01:36 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-11-02 05:01:34 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-02 05:01:12 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 05:00:51 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-11-02 05:00:40 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 05:00:06 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 05:03:47 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-11-02 03:11:08 | Magura (Kalu Ganga) | 3.24 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-11-02 05:01:50 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-02 05:18:12 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-02 05:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-02 05:04:43 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-02 05:05:49 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-01 18:02:39 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-02 05:13:39 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-02 05:14:51 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-02 05:07:16 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-02 05:00:40 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 05:01:12 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 04:02:08 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-02 05:01:34 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:00:51 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:25:25 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:06:27 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-11-02 02:02:38 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:02:38 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:07:20 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:03:31 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:05:54 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:01:23 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.005 |  |
| 2026-11-02 05:07:27 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-11-02 05:03:08 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-11-02 05:02:53 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-11-02 05:01:39 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-11-02 05:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-11-02 05:00:06 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.012 |  |
| 2026-11-02 05:21:29 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | -0.016 |  |
| 2026-11-02 05:07:19 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-11-02 05:01:36 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-11-01 18:02:14 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-11-02 05:05:11 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.047 |  |
| 2026-11-02 05:04:01 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.059 |  |
| 2026-11-02 05:02:47 | Glencourse (Kelani Ganga) | 11.33 | 🟢 Normal | -0.090 |  |
| 2026-11-02 04:03:46 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)