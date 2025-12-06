# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_17:14:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,933 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 17:14:17 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-06 17:13:51 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | -36.000 |  |
| 2025-12-06 17:13:50 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | -36.000 |  |
| 2025-12-06 17:13:48 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | -36.000 |  |
| 2025-12-06 17:13:04 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.063 |  |
| 2025-12-06 17:11:30 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.037 |  |
| 2025-12-06 17:09:22 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.009 |  |
| 2025-12-06 17:09:21 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:08:20 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | -0.036 |  |
| 2025-12-06 17:08:08 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:07:36 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:07:36 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | -0.102 |  |
| 2025-12-06 17:05:43 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:05:43 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-06 17:05:32 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-06 17:05:29 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-06 17:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.042 |  |
| 2025-12-06 17:04:47 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.072 |  |
| 2025-12-06 17:04:42 | Giriulla (Maha Oya) | 1.87 | 🟢 Normal | -0.009 |  |
| 2025-12-06 17:04:16 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.068 |  |
| 2025-12-06 17:04:11 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:03:56 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.021 |  |
| 2025-12-06 17:03:47 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | -0.040 |  |
| 2025-12-06 17:03:14 | Thanthirimale (Malwathu Oya) | 6.73 | 🟡 Alert | -0.039 |  |
| 2025-12-06 17:02:53 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:02:52 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-06 17:02:33 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.029 |  |
| 2025-12-06 17:02:31 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:02:27 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:02:17 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.124 |  |
| 2025-12-06 17:01:37 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:01:30 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.010 |  |
| 2025-12-06 17:01:22 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.070 |  |
| 2025-12-06 17:00:43 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.034 |  |
| 2025-12-06 17:00:41 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-06 17:00:40 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 17:03:14 | Thanthirimale (Malwathu Oya) | 6.73 | 🟡 Alert | -0.039 |  |
| 2025-12-06 17:05:32 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-06 17:02:52 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-06 17:05:29 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-06 17:05:43 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-06 17:14:17 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-06 17:02:27 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:01:37 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 16:11:40 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:00:40 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:05:43 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:02:53 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:08:08 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:04:11 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:09:21 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:07:36 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:02:31 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-06 17:09:22 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.009 |  |
| 2025-12-06 17:04:42 | Giriulla (Maha Oya) | 1.87 | 🟢 Normal | -0.009 |  |
| 2025-12-06 17:00:41 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-06 16:05:28 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-06 17:01:30 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.010 |  |
| 2025-12-06 17:03:56 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.021 |  |
| 2025-12-06 17:02:33 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.029 |  |
| 2025-12-06 17:00:43 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.034 |  |
| 2025-12-06 17:08:20 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | -0.036 |  |
| 2025-12-06 17:11:30 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.037 |  |
| 2025-12-06 17:03:47 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | -0.040 |  |
| 2025-12-06 17:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.042 |  |
| 2025-12-06 17:13:04 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.063 |  |
| 2025-12-06 17:04:16 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.068 |  |
| 2025-12-06 17:01:22 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.070 |  |
| 2025-12-06 17:04:47 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.072 |  |
| 2025-12-06 17:07:36 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | -0.102 |  |
| 2025-12-06 17:02:17 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.124 |  |
| 2025-12-06 17:13:51 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)