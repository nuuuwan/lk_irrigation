# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_05:44:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,478 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 05:44:06 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -36.000 |  |
| 2026-05-03 05:44:05 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -36.000 |  |
| 2026-05-03 05:44:04 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -36.000 |  |
| 2026-05-03 05:44:03 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -36.000 |  |
| 2026-05-03 05:44:01 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -36.000 |  |
| 2026-05-03 05:26:02 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-03 05:20:50 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.023 |  |
| 2026-05-03 05:14:26 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-03 05:13:12 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-03 05:09:54 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.049 |  |
| 2026-05-03 05:08:34 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:08:21 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.122 |  |
| 2026-05-03 05:08:14 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.051 |  |
| 2026-05-03 05:08:05 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.004 |  |
| 2026-05-03 05:06:31 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:06:07 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:06:04 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-03 05:05:53 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-03 05:05:42 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-03 05:05:35 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-05-03 05:05:06 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:04:50 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-05-03 05:04:15 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-05-03 05:03:24 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:03:15 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:03:02 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.228 |  |
| 2026-05-03 05:02:51 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:02:51 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.019 |  |
| 2026-05-03 05:02:43 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-05-03 05:02:22 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:02:04 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-03 05:01:57 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-03 05:01:26 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:01:26 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:00:57 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.050 |  |
| 2026-05-03 05:00:46 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.041 |  |
| 2026-05-03 05:00:32 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.109 |  |
| 2026-05-03 04:53:08 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.337 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 05:05:35 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-05-03 05:02:04 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-03 03:16:02 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-03 05:01:57 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-03 02:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-02 18:01:54 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-03 05:05:53 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-03 05:26:02 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-03 05:14:26 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-03 05:13:12 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-03 05:05:42 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-03 05:06:04 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-03 05:01:26 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:03:24 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:02:22 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:03:15 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:05:06 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:08:34 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:02:51 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:06:07 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:06:31 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:01:26 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:02:51 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-03 05:08:05 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.004 |  |
| 2026-05-02 18:01:54 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-03 05:04:15 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-05-03 05:04:50 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-05-03 05:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.019 |  |
| 2026-05-03 05:02:43 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-05-03 05:20:50 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.023 |  |
| 2026-05-03 05:00:46 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.041 |  |
| 2026-05-03 05:09:54 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.049 |  |
| 2026-05-03 05:00:57 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.050 |  |
| 2026-05-03 05:08:14 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.051 |  |
| 2026-05-03 05:00:32 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.109 |  |
| 2026-05-03 05:08:21 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.122 |  |
| 2026-05-03 05:03:02 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.228 |  |
| 2026-05-03 05:44:06 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)