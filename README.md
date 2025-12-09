# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_08:37:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,129 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 08:37:22 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2025-12-09 08:19:17 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:16:33 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2025-12-09 08:11:14 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.018 |  |
| 2025-12-09 08:09:41 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2025-12-09 08:09:21 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:08:28 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:08:15 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:07:42 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:07:40 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:07:18 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.009 |  |
| 2025-12-09 08:06:57 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:06:04 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-09 08:06:04 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.026 |  |
| 2025-12-09 08:05:46 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | -0.105 |  |
| 2025-12-09 08:05:44 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2025-12-09 08:04:28 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.039 |  |
| 2025-12-09 08:04:26 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:04:22 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 08:04:10 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:04:02 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.010 |  |
| 2025-12-09 08:03:52 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 08:03:47 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:03:43 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | -0.029 |  |
| 2025-12-09 08:03:22 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:03:21 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | -0.110 |  |
| 2025-12-09 08:03:17 | Rathnapura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.104 |  |
| 2025-12-09 08:02:59 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2025-12-09 08:02:58 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:02:35 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.040 |  |
| 2025-12-09 08:02:23 | Galgamuwa (Mee Oya) | 1.29 | 🟢 Normal | -0.014 |  |
| 2025-12-09 08:02:23 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:02:14 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 08:01:56 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:01:44 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:01:05 | Thanthirimale (Malwathu Oya) | 7.46 | 🟠 Minor Flood | 3.987 | 🔺 Rising |
| 2025-12-09 08:00:44 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:00:40 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 08:01:05 | Thanthirimale (Malwathu Oya) | 7.46 | 🟠 Minor Flood | 3.987 | 🔺 Rising |
| 2025-12-09 08:09:41 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2025-12-09 08:06:04 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-09 08:02:14 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 08:00:40 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 08:04:22 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 08:03:52 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 08:01:44 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:01:56 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:08:28 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:09:21 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:06:57 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:04:26 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:03:22 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:04:10 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:07:42 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:03:43 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:02:58 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:07:40 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:19:17 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:00:44 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:02:23 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:03:47 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:07:18 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.009 |  |
| 2025-12-09 08:04:02 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.010 |  |
| 2025-12-09 08:16:33 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2025-12-09 08:02:23 | Galgamuwa (Mee Oya) | 1.29 | 🟢 Normal | -0.014 |  |
| 2025-12-09 08:11:14 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.018 |  |
| 2025-12-09 08:37:22 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2025-12-09 08:02:59 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2025-12-09 08:05:44 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2025-12-09 08:06:04 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.026 |  |
| 2025-12-09 08:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | -0.029 |  |
| 2025-12-09 08:04:28 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.039 |  |
| 2025-12-09 08:02:35 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.040 |  |
| 2025-12-09 08:03:17 | Rathnapura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.104 |  |
| 2025-12-09 08:05:46 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | -0.105 |  |
| 2025-12-09 08:03:21 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)