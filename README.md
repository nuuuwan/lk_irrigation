# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_14:17:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,920 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 14:17:30 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.024 |  |
| 2025-12-12 14:14:23 | Panadugama (Nilwala Ganga) | 4.06 | 🟢 Normal | -0.047 |  |
| 2025-12-12 14:13:49 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-12 14:13:25 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.457 |  |
| 2025-12-12 14:10:58 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.009 |  |
| 2025-12-12 14:07:47 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:07:18 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:06:53 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | -0.117 |  |
| 2025-12-12 14:06:29 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.029 |  |
| 2025-12-12 14:06:27 | Manampitiya (Mahaweli Ganga) | 3.27 | 🟡 Alert | -0.039 |  |
| 2025-12-12 14:06:23 | Peradeniya (Mahaweli Ganga) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 14:05:50 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.192 |  |
| 2025-12-12 14:05:15 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.127 |  |
| 2025-12-12 14:05:08 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:04:50 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2025-12-12 14:04:36 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2025-12-12 14:04:30 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.040 |  |
| 2025-12-12 14:03:47 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:03:30 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-12 14:03:11 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 14:03:10 | Hanwella (Kelani Ganga) | 1.71 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 14:02:59 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:02:58 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 14:02:57 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-12 14:02:55 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -0.011 |  |
| 2025-12-12 14:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | -0.030 |  |
| 2025-12-12 14:02:40 | Horowpothana (Yan Oya) | 6.25 | 🟡 Alert | 0.072 | 🔺 Rising |
| 2025-12-12 14:02:29 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:02:18 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | -0.077 |  |
| 2025-12-12 14:02:05 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:01:48 | Galgamuwa (Mee Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 14:01:30 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-12 14:01:25 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.021 |  |
| 2025-12-12 14:01:20 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:01:12 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 14:01:10 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | -0.021 |  |
| 2025-12-12 14:01:00 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-12 14:00:56 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:00:48 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-12 14:00:17 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 13:28:05 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.024 |  |
| 2025-12-12 13:25:20 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 14:02:40 | Horowpothana (Yan Oya) | 6.25 | 🟡 Alert | 0.072 | 🔺 Rising |
| 2025-12-12 14:06:27 | Manampitiya (Mahaweli Ganga) | 3.27 | 🟡 Alert | -0.039 |  |
| 2025-12-12 14:03:10 | Hanwella (Kelani Ganga) | 1.71 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 14:02:58 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 14:01:12 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 14:03:11 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 14:01:48 | Galgamuwa (Mee Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 14:06:23 | Peradeniya (Mahaweli Ganga) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 14:00:17 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:03:47 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:01:20 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:02:29 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:02:59 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:07:18 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-12 13:25:20 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:05:08 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:07:47 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:10:58 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.009 |  |
| 2025-12-12 14:02:57 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-12 14:01:30 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-12 14:01:00 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-12 14:00:48 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-12 14:13:49 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-12 14:03:30 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-12 14:02:55 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -0.011 |  |
| 2025-12-12 14:04:50 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2025-12-12 14:01:25 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.021 |  |
| 2025-12-12 14:01:10 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | -0.021 |  |
| 2025-12-12 14:17:30 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.024 |  |
| 2025-12-12 14:06:29 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.029 |  |
| 2025-12-12 14:04:36 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2025-12-12 14:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | -0.030 |  |
| 2025-12-12 14:04:30 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.040 |  |
| 2025-12-12 14:14:23 | Panadugama (Nilwala Ganga) | 4.06 | 🟢 Normal | -0.047 |  |
| 2025-12-12 14:02:18 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | -0.077 |  |
| 2025-12-12 14:06:53 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | -0.117 |  |
| 2025-12-12 14:05:15 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.127 |  |
| 2025-12-12 14:05:50 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.192 |  |
| 2025-12-12 14:13:25 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.457 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)