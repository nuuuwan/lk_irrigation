# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_18:08:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,288 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 18:08:34 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.047 |  |
| 2025-12-04 18:08:06 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-04 18:07:48 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:06:54 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:06:23 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.031 |  |
| 2025-12-04 18:06:17 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:05:41 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:05:39 | Manampitiya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.019 |  |
| 2025-12-04 18:05:10 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:05:02 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:04:54 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | -0.039 |  |
| 2025-12-04 18:04:49 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:04:34 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:04:34 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.020 |  |
| 2025-12-04 18:04:34 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:04:16 | Deraniyagala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.554 | 🔺 Rising |
| 2025-12-04 18:04:16 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-04 18:04:07 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 18:04:02 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2025-12-04 18:03:50 | Dunamale (Aththanagalu Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:03:48 | Dunamale (Aththanagalu Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:03:45 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-04 18:03:37 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.643 | 🔺 Rising |
| 2025-12-04 18:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2025-12-04 18:02:30 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:02:25 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2025-12-04 18:02:22 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-04 18:02:08 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:01:37 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-04 18:01:35 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2025-12-04 18:01:10 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.095 |  |
| 2025-12-04 18:01:09 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:01:08 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:00:36 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.012 |  |
| 2025-12-04 18:00:10 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-04 18:00:08 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:00:07 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:20:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.029 |  |
| 2025-12-04 17:17:21 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | -0.047 |  |
| 2025-12-04 17:17:17 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -0.047 |  |
| 2025-12-04 17:17:12 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | -0.047 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 15:07:05 | Thanthirimale (Malwathu Oya) | 5.95 | 🟡 Alert | -0.063 |  |
| 2025-12-04 18:03:37 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.643 | 🔺 Rising |
| 2025-12-04 18:04:16 | Deraniyagala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.554 | 🔺 Rising |
| 2025-12-04 18:03:45 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-04 18:08:06 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-04 18:04:16 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-04 18:02:22 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-04 18:04:07 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 18:05:02 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:01:08 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:04:34 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:00:08 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:06:54 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:04:34 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:05:10 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:07:48 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:01:46 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:00:07 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:03:50 | Dunamale (Aththanagalu Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:32 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:02:08 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:04:49 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:05:41 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:01:09 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-04 18:01:37 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-04 18:02:25 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2025-12-04 18:01:35 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2025-12-04 18:00:10 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-04 18:00:36 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.012 |  |
| 2025-12-04 18:05:39 | Manampitiya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.019 |  |
| 2025-12-04 18:04:34 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.020 |  |
| 2025-12-04 18:04:02 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2025-12-04 18:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2025-12-04 18:06:23 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.031 |  |
| 2025-12-04 18:04:54 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | -0.039 |  |
| 2025-12-04 18:08:34 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.047 |  |
| 2025-12-04 18:01:10 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)