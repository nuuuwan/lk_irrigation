# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_10:08:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,759 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 10:08:05 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:08:02 | Weraganthota (Mahaweli Ganga) | -0.96 | 🟢 Normal | -2.159 |  |
| 2025-12-12 10:07:23 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:06:35 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-12 10:05:08 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-12 10:05:00 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 10:04:55 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:04:36 | Rathnapura (Kalu Ganga) | 3.23 | 🟢 Normal | -0.153 |  |
| 2025-12-12 10:04:23 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.030 |  |
| 2025-12-12 10:04:19 | Manampitiya (Mahaweli Ganga) | 3.46 | 🟡 Alert | -0.020 |  |
| 2025-12-12 10:03:39 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2025-12-12 10:03:38 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-12 10:03:26 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.040 |  |
| 2025-12-12 10:03:18 | Moragaswewa (Deduru Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:03:14 | Galgamuwa (Mee Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:03:08 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.091 |  |
| 2025-12-12 10:03:04 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-12 10:02:57 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:02:49 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.114 |  |
| 2025-12-12 10:02:38 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2025-12-12 10:02:37 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2025-12-12 10:02:31 | Padiyathalawa (Maduru Oya) | 1.48 | 🟢 Normal | -0.011 |  |
| 2025-12-12 10:02:28 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | -0.020 |  |
| 2025-12-12 10:02:27 | Moragaswewa (Deduru Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 10:02:23 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:02:16 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:02:12 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.021 |  |
| 2025-12-12 10:01:48 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.020 |  |
| 2025-12-12 10:01:28 | Ellagawa (Kalu Ganga) | 6.41 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-12 10:01:24 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-12 10:01:21 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-12 10:01:11 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.005 |  |
| 2025-12-12 10:00:54 | Horowpothana (Yan Oya) | 5.68 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2025-12-12 09:36:33 | Moraketiya (Walawe Ganga) | 1.33 | 🟢 Normal | -0.114 |  |
| 2025-12-12 09:27:12 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.050 |  |
| 2025-12-12 09:13:05 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.027 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 10:04:19 | Manampitiya (Mahaweli Ganga) | 3.46 | 🟡 Alert | -0.020 |  |
| 2025-12-12 10:00:54 | Horowpothana (Yan Oya) | 5.68 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2025-12-12 09:02:23 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-12 10:01:28 | Ellagawa (Kalu Ganga) | 6.41 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-12 10:06:35 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-12 10:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 09:03:50 | Thanthirimale (Malwathu Oya) | 4.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-12 10:05:08 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-12 09:07:44 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-12 10:05:00 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 10:03:18 | Moragaswewa (Deduru Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:03:14 | Galgamuwa (Mee Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:02:23 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:02:57 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:02:16 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:07:23 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:04:55 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:08:05 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-12 10:01:11 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.005 |  |
| 2025-12-12 10:03:04 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-12 10:01:24 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-12 10:03:38 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-12 10:02:37 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2025-12-12 10:01:21 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-12 10:02:38 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2025-12-12 10:02:31 | Padiyathalawa (Maduru Oya) | 1.48 | 🟢 Normal | -0.011 |  |
| 2025-12-12 10:03:39 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2025-12-12 10:01:48 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.020 |  |
| 2025-12-12 10:02:28 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | -0.020 |  |
| 2025-12-12 10:02:12 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.021 |  |
| 2025-12-12 09:13:05 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.027 |  |
| 2025-12-12 10:04:23 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.030 |  |
| 2025-12-12 09:07:08 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.039 |  |
| 2025-12-12 10:03:26 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.040 |  |
| 2025-12-12 09:27:12 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.050 |  |
| 2025-12-12 10:03:08 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.091 |  |
| 2025-12-12 10:02:49 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.114 |  |
| 2025-12-12 10:04:36 | Rathnapura (Kalu Ganga) | 3.23 | 🟢 Normal | -0.153 |  |
| 2025-12-12 10:08:02 | Weraganthota (Mahaweli Ganga) | -0.96 | 🟢 Normal | -2.159 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)