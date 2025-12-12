# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_21:25:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,187 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 21:25:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.09 | 🟢 Normal | -0.015 |  |
| 2025-12-12 21:17:48 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.023 |  |
| 2025-12-12 21:12:58 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:10:30 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:09:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.054 |  |
| 2025-12-12 21:08:36 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.022 |  |
| 2025-12-12 21:07:33 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | -0.009 |  |
| 2025-12-12 21:07:08 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-12 21:07:05 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.017 |  |
| 2025-12-12 21:06:06 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | -0.082 |  |
| 2025-12-12 21:06:06 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.014 |  |
| 2025-12-12 21:05:40 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | -0.021 |  |
| 2025-12-12 21:05:30 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 1.369 | 🔺 Rising |
| 2025-12-12 21:05:25 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:04:47 | Manampitiya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.121 |  |
| 2025-12-12 21:04:40 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.011 |  |
| 2025-12-12 21:04:20 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-12 21:04:11 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:04:07 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:03:58 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 21:03:51 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:03:38 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-12 21:03:36 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:03:27 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-12 21:03:23 | Padiyathalawa (Maduru Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-12 21:03:23 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-12 21:03:21 | Horowpothana (Yan Oya) | 6.38 | 🟡 Alert | 0.000 |  |
| 2025-12-12 21:03:16 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:02:50 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-12 21:02:17 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:02:02 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 21:01:30 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-12 21:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:01:25 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.030 |  |
| 2025-12-12 21:01:23 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-12 21:01:18 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 21:03:21 | Horowpothana (Yan Oya) | 6.38 | 🟡 Alert | 0.000 |  |
| 2025-12-12 21:05:30 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 1.369 | 🔺 Rising |
| 2025-12-12 21:04:20 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-12 21:03:27 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-12 21:01:30 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-12 21:03:58 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 21:02:02 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 21:07:08 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-12 21:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:46 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:05:25 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:10:30 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:03:36 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:12:58 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:04:11 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:02:17 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:03:51 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:10 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:03:16 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:04:07 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:07:33 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | -0.009 |  |
| 2025-12-12 21:03:38 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-12 21:02:50 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-12 21:03:23 | Padiyathalawa (Maduru Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-12 21:01:23 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-12 21:01:18 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-12 21:03:23 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-12 21:04:40 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.011 |  |
| 2025-12-12 21:06:06 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.014 |  |
| 2025-12-12 21:25:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.09 | 🟢 Normal | -0.015 |  |
| 2025-12-12 21:07:05 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.017 |  |
| 2025-12-12 21:05:40 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | -0.021 |  |
| 2025-12-12 21:08:36 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.022 |  |
| 2025-12-12 21:17:48 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.023 |  |
| 2025-12-12 21:01:25 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.030 |  |
| 2025-12-12 21:09:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.054 |  |
| 2025-12-12 21:06:06 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | -0.082 |  |
| 2025-12-12 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.106 |  |
| 2025-12-12 21:04:47 | Manampitiya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)