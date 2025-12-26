# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_11:22:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,333 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 11:22:03 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.106 |  |
| 2025-12-26 11:17:19 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.034 |  |
| 2025-12-26 11:17:08 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.045 |  |
| 2025-12-26 11:11:21 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.026 |  |
| 2025-12-26 11:10:49 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | -0.011 |  |
| 2025-12-26 11:09:29 | Weraganthota (Mahaweli Ganga) | 1.54 | 🟢 Normal | 3.052 | 🔺 Rising |
| 2025-12-26 11:08:21 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-26 11:07:51 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.041 |  |
| 2025-12-26 11:07:34 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:07:27 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.095 |  |
| 2025-12-26 11:06:56 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-26 11:06:27 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:06:16 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:06:07 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.061 |  |
| 2025-12-26 11:05:54 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.040 |  |
| 2025-12-26 11:05:31 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:05:13 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:05:12 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:05:11 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-26 11:04:57 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2025-12-26 11:04:56 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:04:39 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:04:32 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-26 11:03:29 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:03:03 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.021 |  |
| 2025-12-26 11:02:40 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-26 11:02:30 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:02:29 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.010 |  |
| 2025-12-26 11:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | -0.040 |  |
| 2025-12-26 11:02:14 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.166 |  |
| 2025-12-26 11:02:05 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:01:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2025-12-26 11:01:56 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:01:30 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:00:57 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:00:50 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.021 |  |
| 2025-12-26 11:00:31 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-26 11:00:11 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 11:09:29 | Weraganthota (Mahaweli Ganga) | 1.54 | 🟢 Normal | 3.052 | 🔺 Rising |
| 2025-12-26 11:02:40 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-26 11:08:21 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-26 11:06:56 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-26 11:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-26 11:04:32 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-26 11:00:57 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:00:11 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:06:27 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:01:56 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:03:29 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:07:34 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:06:16 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:04:39 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:05:31 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:04:56 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:00:31 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:01:30 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:05:13 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:02:05 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:02:30 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 11:04:57 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2025-12-26 11:05:11 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:02:21 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-26 11:02:29 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.010 |  |
| 2025-12-26 11:10:49 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | -0.011 |  |
| 2025-12-26 11:01:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2025-12-26 11:03:03 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.021 |  |
| 2025-12-26 11:00:50 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.021 |  |
| 2025-12-26 11:11:21 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.026 |  |
| 2025-12-26 11:17:19 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.034 |  |
| 2025-12-26 11:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | -0.040 |  |
| 2025-12-26 11:05:54 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.040 |  |
| 2025-12-26 11:07:51 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.041 |  |
| 2025-12-26 11:17:08 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.045 |  |
| 2025-12-26 11:06:07 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.061 |  |
| 2025-12-26 11:07:27 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.095 |  |
| 2025-12-26 11:22:03 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.106 |  |
| 2025-12-26 11:02:14 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.166 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)