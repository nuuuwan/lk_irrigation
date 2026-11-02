# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_09:12:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,665 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 09:12:31 | Panadugama (Nilwala Ganga) | 4.62 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:09:14 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:06:38 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:05:19 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.107 |  |
| 2026-11-02 09:05:09 | Panadugama (Nilwala Ganga) | 4.62 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:05:09 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | -0.061 |  |
| 2026-11-02 09:04:58 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:04:47 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:04:44 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.072 |  |
| 2026-11-02 09:04:36 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 09:04:22 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:04:02 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-02 09:03:56 | Thalgahagoda (Nilwala Ganga) | 1.41 | 🟡 Alert | 0.000 |  |
| 2026-11-02 09:03:44 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.039 |  |
| 2026-11-02 09:03:36 | Moragaswewa (Deduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:03:20 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:03:13 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.267 |  |
| 2026-11-02 09:03:08 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.041 |  |
| 2026-11-02 09:03:08 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.061 |  |
| 2026-11-02 09:03:01 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-02 09:03:01 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.037 |  |
| 2026-11-02 09:02:49 | Ellagawa (Kalu Ganga) | 6.17 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-02 09:02:38 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.107 |  |
| 2026-11-02 09:02:34 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:02:28 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 09:02:28 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-02 09:02:18 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-02 09:02:12 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-11-02 09:02:10 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-02 09:01:58 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-02 09:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:19 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:10 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:09 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:00:54 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-02 09:00:37 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-02 09:00:27 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:00:13 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.050 |  |
| 2026-11-02 09:00:05 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.056 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 09:03:56 | Thalgahagoda (Nilwala Ganga) | 1.41 | 🟡 Alert | 0.000 |  |
| 2026-11-02 09:00:37 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-02 09:02:49 | Ellagawa (Kalu Ganga) | 6.17 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-02 09:02:10 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-02 09:03:01 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-02 09:01:58 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-02 09:02:28 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 09:00:54 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-02 09:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 09:03:36 | Moragaswewa (Deduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:19 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:09:14 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:06:38 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:12:31 | Panadugama (Nilwala Ganga) | 4.62 | 🟢 Normal | 0.000 |  |
| 2026-11-02 08:14:18 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:04:36 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:03:20 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:04:58 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:04:47 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:02:34 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:09 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:10 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:04:22 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:04:02 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-02 09:02:18 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-02 09:02:28 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-02 09:02:12 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-11-02 09:03:01 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.037 |  |
| 2026-11-02 09:03:44 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.039 |  |
| 2026-11-02 09:03:08 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.041 |  |
| 2026-11-02 09:00:13 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.050 |  |
| 2026-11-02 09:00:05 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.056 |  |
| 2026-11-02 09:03:08 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.061 |  |
| 2026-11-02 09:05:09 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | -0.061 |  |
| 2026-11-02 09:04:44 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.072 |  |
| 2026-11-02 09:02:38 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.107 |  |
| 2026-11-02 09:05:19 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.107 |  |
| 2026-11-02 09:03:13 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.267 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)