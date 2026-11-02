# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_06:16:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,543 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **45** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 06:16:46 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:11:33 | Thalgahagoda (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.018 |  |
| 2026-11-02 06:10:42 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-02 06:07:41 | Baddegama (Gin Ganga) | 2.53 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-02 06:06:59 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-11-02 06:06:49 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:06:47 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:06:46 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:06:42 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:05:50 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-02 06:05:07 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-02 06:04:34 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.086 |  |
| 2026-11-02 06:04:30 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-02 06:04:03 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.079 |  |
| 2026-11-02 06:03:39 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.041 |  |
| 2026-11-02 06:03:37 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-02 06:03:15 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-02 06:03:11 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.011 |  |
| 2026-11-02 06:03:01 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:02:51 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:02:51 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.073 |  |
| 2026-11-02 06:02:47 | Dunamale (Aththanagalu Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:02:43 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-11-02 06:02:37 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-02 06:02:36 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:01:55 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-02 06:01:54 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-11-02 06:01:52 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | -0.102 |  |
| 2026-11-02 06:01:49 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.094 |  |
| 2026-11-02 06:01:43 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.005 |  |
| 2026-11-02 06:01:33 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.074 |  |
| 2026-11-02 06:01:32 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:01:24 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-11-02 06:01:21 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:00:59 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.021 |  |
| 2026-11-02 06:00:37 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-11-02 06:00:23 | Magura (Kalu Ganga) | 2.76 | 🟢 Normal | -576.000 |  |
| 2026-11-02 06:00:22 | Magura (Kalu Ganga) | 2.92 | 🟢 Normal | -576.000 |  |
| 2026-11-02 06:00:21 | Magura (Kalu Ganga) | 3.09 | 🟢 Normal | -576.000 |  |
| 2026-11-02 06:00:10 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.070 |  |
| 2026-11-02 06:00:01 | Dunamale (Aththanagalu Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:48:59 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.094 |  |
| 2026-11-02 05:43:32 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.086 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 06:05:07 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-02 06:10:42 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-02 06:01:55 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-02 06:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-02 06:07:41 | Baddegama (Gin Ganga) | 2.53 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-02 06:03:37 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-02 06:05:50 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-02 06:03:01 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:03:15 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:06:42 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:16:46 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:06:49 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:02:47 | Dunamale (Aththanagalu Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:02:51 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:01:21 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:02:36 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:01:43 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.005 |  |
| 2026-11-02 06:04:30 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-02 06:02:37 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-02 06:01:24 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-11-02 06:00:37 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-11-02 06:03:11 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.011 |  |
| 2026-11-02 06:01:54 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-11-02 06:11:33 | Thalgahagoda (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.018 |  |
| 2026-11-02 06:06:59 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-11-02 06:00:59 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.021 |  |
| 2026-11-02 06:02:43 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-11-01 18:02:14 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-11-02 06:03:39 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.041 |  |
| 2026-11-02 06:00:10 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.070 |  |
| 2026-11-02 06:02:51 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.073 |  |
| 2026-11-02 06:01:33 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.074 |  |
| 2026-11-02 06:04:03 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.079 |  |
| 2026-11-02 06:04:34 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.086 |  |
| 2026-11-02 06:01:49 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.094 |  |
| 2026-11-02 06:01:52 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | -0.102 |  |
| 2026-11-02 06:00:23 | Magura (Kalu Ganga) | 2.76 | 🟢 Normal | -576.000 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)