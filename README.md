# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_01:33:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,360 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 01:33:36 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.007 |  |
| 2026-11-02 01:19:31 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-02 01:09:49 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.141 |  |
| 2026-11-02 01:09:27 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.072 |  |
| 2026-11-02 01:09:01 | Magura (Kalu Ganga) | 3.07 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-02 01:08:53 | Thawalama (Gin Ganga) | 3.08 | 🟢 Normal | -0.069 |  |
| 2026-11-02 01:07:46 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-02 01:05:22 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-02 01:05:04 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-02 01:04:58 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:04:52 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-11-02 01:04:35 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:04:22 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.023 |  |
| 2026-11-02 01:03:46 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-11-02 01:03:44 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | -0.022 |  |
| 2026-11-02 01:03:43 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.070 |  |
| 2026-11-02 01:03:39 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-02 01:03:22 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:03:12 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.031 |  |
| 2026-11-02 01:02:56 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-02 01:02:21 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:02:08 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:02:03 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-11-02 01:02:01 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:54 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-02 01:01:36 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:30 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:20 | Glencourse (Kelani Ganga) | 11.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 01:01:11 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:03 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:00:43 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | -0.010 |  |
| 2026-11-02 01:00:36 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 01:00:43 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | -0.010 |  |
| 2026-11-02 01:04:52 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-11-02 01:02:56 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-02 01:09:01 | Magura (Kalu Ganga) | 3.07 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-02 00:13:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-02 01:03:39 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-02 01:07:46 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-01 18:02:39 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-02 01:01:20 | Glencourse (Kelani Ganga) | 11.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 01:19:31 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-02 01:01:54 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-02 00:02:03 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 01:05:22 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-02 01:02:08 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:03 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:02:21 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:30 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:36 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 00:07:46 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:02:01 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:04:35 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:04:58 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 00:04:19 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:11 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:33:36 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.007 |  |
| 2026-11-02 01:05:04 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-02 00:03:13 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-11-02 01:03:46 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-11-02 01:02:03 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-11-02 01:00:36 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-11-02 01:03:44 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | -0.022 |  |
| 2026-11-02 01:04:22 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.023 |  |
| 2026-11-01 18:02:14 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-11-02 01:03:12 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.031 |  |
| 2026-11-02 01:08:53 | Thawalama (Gin Ganga) | 3.08 | 🟢 Normal | -0.069 |  |
| 2026-11-02 01:03:43 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.070 |  |
| 2026-11-02 01:09:27 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.072 |  |
| 2026-11-02 01:09:49 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)