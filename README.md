# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_19:33:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,533 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 19:33:07 | Horowpothana (Yan Oya) | 5.30 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:32:51 | Horowpothana (Yan Oya) | 5.30 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:26:40 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-18 19:14:52 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:12:18 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 1.135 | 🔺 Rising |
| 2025-12-18 19:11:25 | Manampitiya (Mahaweli Ganga) | 4.73 | 🟠 Minor Flood | 0.064 | 🔺 Rising |
| 2025-12-18 19:09:14 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 19:07:43 | Padiyathalawa (Maduru Oya) | 2.35 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-18 19:07:16 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 19:07:10 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 19:06:42 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.018 |  |
| 2025-12-18 19:06:02 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:05:42 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:04:50 | Thaldena (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2025-12-18 19:04:32 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 19:04:22 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-18 19:04:22 | Siyambalanduwa (Heda Oya) | 1.55 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-18 19:04:11 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-18 19:04:02 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-18 19:03:46 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-18 19:03:36 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.078 |  |
| 2025-12-18 19:03:18 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2025-12-18 19:02:51 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-18 19:02:42 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 19:02:25 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:02:23 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:02:21 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:02:06 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:01:48 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2025-12-18 19:01:33 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:01:14 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:01:08 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-18 19:00:44 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-18 19:00:22 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2025-12-18 19:00:14 | Nakkala (Kumbukkan Oya) | 2.48 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 19:11:25 | Manampitiya (Mahaweli Ganga) | 4.73 | 🟠 Minor Flood | 0.064 | 🔺 Rising |
| 2025-12-18 18:06:17 | Thanthirimale (Malwathu Oya) | 5.40 | 🟡 Alert | 0.074 | 🔺 Rising |
| 2025-12-18 19:12:18 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 1.135 | 🔺 Rising |
| 2025-12-18 19:01:48 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2025-12-18 19:00:44 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-18 19:04:22 | Siyambalanduwa (Heda Oya) | 1.55 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-18 18:02:47 | Weraganthota (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-18 19:07:43 | Padiyathalawa (Maduru Oya) | 2.35 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-18 19:04:22 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-18 19:04:11 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-18 19:02:51 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-18 19:01:08 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-18 19:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 19:07:10 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 19:04:32 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 19:07:16 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 18:06:01 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 19:09:14 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 19:26:40 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-18 19:02:42 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:02:21 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:33:07 | Horowpothana (Yan Oya) | 5.30 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:02:23 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:01:33 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:14:52 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:05:42 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:02:06 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:02:25 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:06:02 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:01:14 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:03:46 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-18 18:04:57 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-18 19:04:02 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-18 19:06:42 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.018 |  |
| 2025-12-18 19:04:50 | Thaldena (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2025-12-18 19:03:18 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2025-12-18 19:00:14 | Nakkala (Kumbukkan Oya) | 2.48 | 🟢 Normal | -0.040 |  |
| 2025-12-18 19:00:22 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2025-12-18 19:03:36 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)