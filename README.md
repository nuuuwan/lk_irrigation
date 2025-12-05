# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_05:14:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,485 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 05:14:06 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.071 |  |
| 2025-12-06 05:08:42 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-06 05:07:47 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:06:24 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | -0.039 |  |
| 2025-12-06 05:05:30 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:05:25 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-06 05:05:20 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:05:02 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:04:28 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-06 05:04:05 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2025-12-06 05:03:51 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2025-12-06 05:03:44 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:03:43 | Thanthirimale (Malwathu Oya) | 6.83 | 🟠 Minor Flood | 0.032 | 🔺 Rising |
| 2025-12-06 05:03:33 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:03:28 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:03:25 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:03:18 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.041 |  |
| 2025-12-06 05:03:16 | Thawalama (Gin Ganga) | 2.92 | 🟢 Normal | -324.000 |  |
| 2025-12-06 05:03:14 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -324.000 |  |
| 2025-12-06 05:02:41 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.022 |  |
| 2025-12-06 05:02:36 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.005 |  |
| 2025-12-06 05:02:35 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 05:02:31 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -6.091 |  |
| 2025-12-06 05:02:26 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2025-12-06 05:02:00 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.011 |  |
| 2025-12-06 05:01:19 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:01:10 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.180 |  |
| 2025-12-06 05:01:06 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:01:03 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-06 04:28:10 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-06 04:18:23 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.223 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 05:03:43 | Thanthirimale (Malwathu Oya) | 6.83 | 🟠 Minor Flood | 0.032 | 🔺 Rising |
| 2025-12-06 03:04:29 | Magura (Kalu Ganga) | 4.49 | 🟡 Alert | 0.094 | 🔺 Rising |
| 2025-12-06 05:04:05 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-06 05:01:03 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-06 04:01:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-06 05:05:25 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-06 05:04:28 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-06 05:08:42 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-06 05:02:35 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 05:01:19 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:03:25 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:05:02 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:05:30 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:03:46 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:03:44 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:01:06 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:07:47 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:05:20 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:03:28 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:02:36 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.005 |  |
| 2025-12-06 03:17:34 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.006 |  |
| 2025-12-06 05:02:26 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2025-12-06 05:02:00 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.011 |  |
| 2025-12-06 05:03:51 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2025-12-06 05:02:41 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.022 |  |
| 2025-12-06 04:05:25 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.032 |  |
| 2025-12-06 05:06:24 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | -0.039 |  |
| 2025-12-06 05:03:18 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.041 |  |
| 2025-12-06 05:14:06 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.071 |  |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |
| 2025-12-06 05:01:10 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.180 |  |
| 2025-12-06 05:02:31 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -6.091 |  |
| 2025-12-06 05:03:16 | Thawalama (Gin Ganga) | 2.92 | 🟢 Normal | -324.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)