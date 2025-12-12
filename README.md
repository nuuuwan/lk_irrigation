# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_09:27:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,724 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 09:27:12 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.050 |  |
| 2025-12-12 09:13:05 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.027 |  |
| 2025-12-12 09:12:10 | Weraganthota (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.045 |  |
| 2025-12-12 09:10:36 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-12 09:10:30 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:09:39 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:07:44 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-12 09:07:10 | Padiyathalawa (Maduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:07:08 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.039 |  |
| 2025-12-12 09:07:02 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:06:02 | Galgamuwa (Mee Oya) | 1.36 | 🟢 Normal | -0.011 |  |
| 2025-12-12 09:06:01 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | -0.010 |  |
| 2025-12-12 09:05:57 | Rathnapura (Kalu Ganga) | 3.38 | 🟢 Normal | -0.175 |  |
| 2025-12-12 09:04:58 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:04:22 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:04:09 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:03:55 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-12 09:03:50 | Thanthirimale (Malwathu Oya) | 4.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-12 09:03:48 | Manampitiya (Mahaweli Ganga) | 3.48 | 🟡 Alert | -0.019 |  |
| 2025-12-12 09:03:42 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:03:33 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:03:25 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:03:20 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 09:03:17 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-12 09:03:13 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2025-12-12 09:03:01 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2025-12-12 09:02:58 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-12 09:02:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2025-12-12 09:02:28 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 09:02:23 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-12 09:02:12 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.039 |  |
| 2025-12-12 09:02:11 | Horowpothana (Yan Oya) | 5.47 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2025-12-12 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-12 09:01:53 | Moraketiya (Walawe Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2025-12-12 09:01:39 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-12 09:01:33 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.071 |  |
| 2025-12-12 09:01:13 | Yaka Wewa (Ma Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-12 09:00:11 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 09:03:48 | Manampitiya (Mahaweli Ganga) | 3.48 | 🟡 Alert | -0.019 |  |
| 2025-12-12 09:02:11 | Horowpothana (Yan Oya) | 5.47 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2025-12-12 09:02:23 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-12 09:10:36 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-12 09:01:39 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-12 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-12 09:03:50 | Thanthirimale (Malwathu Oya) | 4.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-12 09:07:44 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-12 09:02:28 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 09:03:20 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 09:00:11 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:10:30 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:03:25 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:03:33 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-12 08:04:12 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:07:10 | Padiyathalawa (Maduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:04:58 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:07:02 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:04:09 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:03:42 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:04:22 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-12 09:06:01 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | -0.010 |  |
| 2025-12-12 09:03:17 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-12 09:01:13 | Yaka Wewa (Ma Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-12 09:02:58 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-12 09:03:55 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-12 09:06:02 | Galgamuwa (Mee Oya) | 1.36 | 🟢 Normal | -0.011 |  |
| 2025-12-12 09:03:01 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2025-12-12 09:01:53 | Moraketiya (Walawe Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2025-12-12 09:03:13 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2025-12-12 09:13:05 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.027 |  |
| 2025-12-12 08:03:17 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.030 |  |
| 2025-12-12 09:02:12 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.039 |  |
| 2025-12-12 09:07:08 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.039 |  |
| 2025-12-12 09:12:10 | Weraganthota (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.045 |  |
| 2025-12-12 09:27:12 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.050 |  |
| 2025-12-12 09:02:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2025-12-12 09:01:33 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.071 |  |
| 2025-12-12 09:05:57 | Rathnapura (Kalu Ganga) | 3.38 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)