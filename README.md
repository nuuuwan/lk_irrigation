# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_12:17:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,686 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 12:17:46 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:11:18 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:08:29 | Thanthirimale (Malwathu Oya) | 3.30 | 🟢 Normal | -0.038 |  |
| 2025-12-23 12:07:08 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:06:44 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.009 |  |
| 2025-12-23 12:06:43 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.019 |  |
| 2025-12-23 12:06:29 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:05:52 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:05:12 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:05:05 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | -0.012 |  |
| 2025-12-23 12:04:56 | Manampitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.047 |  |
| 2025-12-23 12:04:33 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:04:11 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2025-12-23 12:04:06 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:03:34 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:03:16 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:03:04 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2025-12-23 12:02:51 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.031 |  |
| 2025-12-23 12:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:02:46 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:02:44 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:02:36 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:02:34 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 12:02:31 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 12:02:30 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | -0.113 |  |
| 2025-12-23 12:02:29 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:02:21 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-23 12:01:55 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:01:32 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.040 |  |
| 2025-12-23 12:01:25 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:01:24 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-23 12:01:09 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:01:08 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:00:40 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:00:28 | Horowpothana (Yan Oya) | 2.63 | 🟢 Normal | -0.032 |  |
| 2025-12-23 12:00:08 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 12:01:24 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-23 12:02:21 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-23 12:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 11:04:39 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 06:11:09 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-23 12:02:31 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 12:04:06 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:00:08 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:07:08 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:02:29 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:06:29 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:03:34 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:05:12 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:04:33 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:17:46 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:05:52 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:01:55 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:02:46 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:02:44 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-23 12:06:44 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.009 |  |
| 2025-12-23 12:11:18 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:02:36 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:02:34 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:01:08 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:01:25 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:03:16 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:01:09 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:00:40 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-23 12:05:05 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | -0.012 |  |
| 2025-12-23 12:06:43 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.019 |  |
| 2025-12-23 12:04:11 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2025-12-23 12:03:04 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2025-12-23 12:02:51 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.031 |  |
| 2025-12-23 12:00:28 | Horowpothana (Yan Oya) | 2.63 | 🟢 Normal | -0.032 |  |
| 2025-12-23 12:08:29 | Thanthirimale (Malwathu Oya) | 3.30 | 🟢 Normal | -0.038 |  |
| 2025-12-23 12:01:32 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.040 |  |
| 2025-12-23 12:04:56 | Manampitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.047 |  |
| 2025-12-23 12:02:30 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)