# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_15:18:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,785 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 15:18:12 | Panadugama (Nilwala Ganga) | 5.17 | 🟡 Alert | 0.224 | 🔺 Rising |
| 2026-05-13 15:15:36 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.017 |  |
| 2026-05-13 15:10:57 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -936.000 |  |
| 2026-05-13 15:10:56 | Thawalama (Gin Ganga) | 3.36 | 🟢 Normal | -936.000 |  |
| 2026-05-13 15:08:10 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-13 15:07:29 | Moragaswewa (Deduru Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-13 15:07:02 | Katharagama (Menik Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-13 15:06:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.38 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-05-13 15:05:57 | Moraketiya (Walawe Ganga) | 2.16 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-05-13 15:05:50 | Magura (Kalu Ganga) | 5.11 | 🟡 Alert | 0.084 | 🔺 Rising |
| 2026-05-13 15:05:39 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-05-13 15:04:56 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-13 15:04:51 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.106 |  |
| 2026-05-13 15:04:42 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-13 15:04:31 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-13 15:04:28 | Rathnapura (Kalu Ganga) | 6.26 | 🟡 Alert | -0.021 |  |
| 2026-05-13 15:04:06 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.122 |  |
| 2026-05-13 15:03:54 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.028 |  |
| 2026-05-13 15:03:54 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-13 15:03:48 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.128 |  |
| 2026-05-13 15:03:11 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.156 |  |
| 2026-05-13 15:03:07 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-13 15:02:56 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.030 |  |
| 2026-05-13 15:02:45 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 15:02:44 | Baddegama (Gin Ganga) | 2.90 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-05-13 15:02:41 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-13 15:02:37 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-13 15:02:35 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-05-13 15:02:28 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-13 15:02:20 | Galgamuwa (Mee Oya) | 2.83 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-13 15:02:16 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-05-13 15:01:57 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-13 15:01:53 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-05-13 15:01:35 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | 0.084 | 🔺 Rising |
| 2026-05-13 15:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.056 |  |
| 2026-05-13 15:01:19 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-13 15:01:13 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-13 15:01:12 | Thanthirimale (Malwathu Oya) | 3.48 | 🟢 Normal | -0.020 |  |
| 2026-05-13 15:00:46 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 15:18:12 | Panadugama (Nilwala Ganga) | 5.17 | 🟡 Alert | 0.224 | 🔺 Rising |
| 2026-05-13 15:05:50 | Magura (Kalu Ganga) | 5.11 | 🟡 Alert | 0.084 | 🔺 Rising |
| 2026-05-13 15:01:35 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | 0.084 | 🔺 Rising |
| 2026-05-13 15:06:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.38 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-05-13 15:04:28 | Rathnapura (Kalu Ganga) | 6.26 | 🟡 Alert | -0.021 |  |
| 2026-05-13 15:02:44 | Baddegama (Gin Ganga) | 2.90 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-05-13 15:05:39 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-05-13 15:05:57 | Moraketiya (Walawe Ganga) | 2.16 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-05-13 15:01:19 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-13 15:03:54 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-13 15:01:13 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-13 15:04:31 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-13 15:04:42 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-13 15:04:56 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-13 15:02:20 | Galgamuwa (Mee Oya) | 2.83 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-13 15:08:10 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-13 15:07:29 | Moragaswewa (Deduru Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-13 15:02:45 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:14:51 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 15:02:28 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-13 15:02:41 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-13 15:07:02 | Katharagama (Menik Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-13 15:01:57 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-13 15:03:07 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-13 15:02:16 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-05-13 15:02:37 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-13 15:15:36 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.017 |  |
| 2026-05-13 15:00:46 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.020 |  |
| 2026-05-13 15:01:53 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-05-13 15:01:12 | Thanthirimale (Malwathu Oya) | 3.48 | 🟢 Normal | -0.020 |  |
| 2026-05-13 15:02:35 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-05-13 15:03:54 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.028 |  |
| 2026-05-13 15:02:56 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.030 |  |
| 2026-05-13 15:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.056 |  |
| 2026-05-13 15:04:51 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.106 |  |
| 2026-05-13 15:04:06 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.122 |  |
| 2026-05-13 15:03:48 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.128 |  |
| 2026-05-13 15:03:11 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.156 |  |
| 2026-05-13 15:10:57 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -936.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)