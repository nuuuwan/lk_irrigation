# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_18:18:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,078 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 18:18:41 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.008 |  |
| 2025-12-12 18:13:00 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | -0.039 |  |
| 2025-12-12 18:10:24 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:46 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:37 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:30 | Horowpothana (Yan Oya) | 6.38 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2025-12-12 18:07:50 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:07:31 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.009 |  |
| 2025-12-12 18:07:17 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:06:01 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.019 |  |
| 2025-12-12 18:05:21 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | -0.020 |  |
| 2025-12-12 18:05:16 | Padiyathalawa (Maduru Oya) | 1.43 | 🟢 Normal | -0.009 |  |
| 2025-12-12 18:04:58 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-12 18:04:53 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.074 |  |
| 2025-12-12 18:04:49 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-12 18:04:27 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 18:04:26 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:30 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-12 18:03:10 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:02 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-12 18:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.17 | 🟢 Normal | -0.032 |  |
| 2025-12-12 18:02:28 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-12 18:02:24 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.011 |  |
| 2025-12-12 18:02:20 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.022 |  |
| 2025-12-12 18:02:19 | Manampitiya (Mahaweli Ganga) | 3.06 | 🟡 Alert | -0.071 |  |
| 2025-12-12 18:02:11 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2025-12-12 18:01:56 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2025-12-12 18:01:47 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:01:41 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2025-12-12 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.106 |  |
| 2025-12-12 18:01:38 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-12 18:01:38 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:01:37 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-12 18:01:27 | Ellagawa (Kalu Ganga) | 6.22 | 🟢 Normal | -0.080 |  |
| 2025-12-12 18:01:21 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.020 |  |
| 2025-12-12 18:01:14 | Moragaswewa (Deduru Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 18:01:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:00:08 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 0.073 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 18:09:30 | Horowpothana (Yan Oya) | 6.38 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2025-12-12 18:02:19 | Manampitiya (Mahaweli Ganga) | 3.06 | 🟡 Alert | -0.071 |  |
| 2025-12-12 18:02:11 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2025-12-12 18:01:56 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2025-12-12 18:00:08 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-12 18:02:28 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-12 18:04:58 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-12 18:03:02 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-12 18:03:30 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-12 18:04:27 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 18:01:14 | Moragaswewa (Deduru Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 18:01:47 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:07:17 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:46 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:10:24 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:01:38 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:01:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:37 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:04:26 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:07:50 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:10 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:18:41 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.008 |  |
| 2025-12-12 18:05:16 | Padiyathalawa (Maduru Oya) | 1.43 | 🟢 Normal | -0.009 |  |
| 2025-12-12 18:07:31 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.009 |  |
| 2025-12-12 17:05:41 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2025-12-12 18:04:49 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-12 18:01:38 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-12 18:01:37 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-12 18:02:24 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.011 |  |
| 2025-12-12 18:01:41 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2025-12-12 18:06:01 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.019 |  |
| 2025-12-12 18:01:21 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.020 |  |
| 2025-12-12 18:05:21 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | -0.020 |  |
| 2025-12-12 18:02:20 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.022 |  |
| 2025-12-12 18:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.17 | 🟢 Normal | -0.032 |  |
| 2025-12-12 18:13:00 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | -0.039 |  |
| 2025-12-12 18:04:53 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.074 |  |
| 2025-12-12 18:01:27 | Ellagawa (Kalu Ganga) | 6.22 | 🟢 Normal | -0.080 |  |
| 2025-12-12 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)