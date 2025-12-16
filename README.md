# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_03:28:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,013 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 03:28:43 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:26:17 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.029 |  |
| 2025-12-17 03:23:03 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:17:06 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-17 03:16:50 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-17 03:11:49 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2025-12-17 03:10:24 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.005 |  |
| 2025-12-17 03:08:16 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:08:03 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 03:07:43 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:06:33 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.002 |  |
| 2025-12-17 03:06:04 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.604 | 🔺 Rising |
| 2025-12-17 03:04:17 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:03:59 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.011 |  |
| 2025-12-17 03:03:52 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.667 | 🔺 Rising |
| 2025-12-17 03:03:40 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-17 03:03:37 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-17 03:03:30 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 03:03:03 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:02:58 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.667 | 🔺 Rising |
| 2025-12-17 03:02:52 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:02:50 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:02:35 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.010 |  |
| 2025-12-17 03:01:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2025-12-17 03:01:37 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:01:22 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2025-12-17 03:01:11 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-17 03:00:51 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:00:09 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 02:01:56 | Horowpothana (Yan Oya) | 6.07 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2025-12-17 03:03:52 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.667 | 🔺 Rising |
| 2025-12-17 03:06:04 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.604 | 🔺 Rising |
| 2025-12-17 00:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2025-12-17 03:16:50 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-17 03:01:11 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-17 03:03:37 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-17 03:17:06 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-17 03:03:40 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-17 03:03:30 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 03:08:03 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 03:06:33 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.002 |  |
| 2025-12-17 03:02:50 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:31 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:03:03 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:08:16 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:23:03 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:01:37 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-17 02:33:23 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:00:09 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:07:43 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:04:17 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:02:52 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:28:43 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:00:51 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:10:24 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.005 |  |
| 2025-12-17 03:11:49 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2025-12-17 02:05:42 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-17 03:02:35 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.010 |  |
| 2025-12-17 02:03:31 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-17 03:03:59 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.011 |  |
| 2025-12-17 01:02:45 | Yaka Wewa (Ma Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2025-12-17 03:01:22 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2025-12-17 03:26:17 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.029 |  |
| 2025-12-17 03:01:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2025-12-16 18:03:31 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | -0.101 |  |
| 2025-12-17 02:12:28 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.114 |  |
| 2025-12-16 18:05:13 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)