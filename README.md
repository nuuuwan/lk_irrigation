# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_15:09:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,376 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 15:09:00 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-27 15:09:00 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.011 |  |
| 2025-12-27 15:06:57 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:06:15 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.046 |  |
| 2025-12-27 15:05:46 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-27 15:05:04 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:04:45 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.009 |  |
| 2025-12-27 15:04:19 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -1.576 |  |
| 2025-12-27 15:04:18 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2025-12-27 15:04:07 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:03:59 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:03:54 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:03:48 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2025-12-27 15:03:44 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:03:29 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:03:23 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-27 15:03:14 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 15:03:06 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-27 15:03:01 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 15:02:52 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2025-12-27 15:02:42 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:02:35 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:02:34 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:02:16 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-27 15:02:08 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2025-12-27 15:01:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:01:45 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:01:43 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:01:30 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 15:01:28 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:01:27 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 15:01:26 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:01:23 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.030 |  |
| 2025-12-27 15:01:21 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:01:00 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 15:09:00 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-27 15:04:18 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2025-12-27 15:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-27 15:02:16 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-27 15:01:27 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 15:03:01 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 15:01:30 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 15:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 15:03:14 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 15:03:59 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:02:35 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:01:28 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:01:45 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:03:44 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:06:57 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:03:54 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:03:29 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:02:42 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:04:07 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:03:23 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:05:30 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:01:26 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:01:21 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:05:04 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:01:00 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:01:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:01:43 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 15:04:45 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.009 |  |
| 2025-12-27 14:07:01 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-27 15:05:46 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-27 15:02:08 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2025-12-27 15:03:06 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:04:19 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-27 15:02:52 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2025-12-27 15:09:00 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.011 |  |
| 2025-12-27 15:03:48 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2025-12-27 15:01:23 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.030 |  |
| 2025-12-27 15:06:15 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.046 |  |
| 2025-12-27 15:04:19 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -1.576 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)