# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_21:14:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,608 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 21:14:09 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.008 |  |
| 2025-12-27 21:12:28 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:09:35 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.045 |  |
| 2025-12-27 21:08:43 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.086 |  |
| 2025-12-27 21:08:25 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-27 21:07:14 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:05:43 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-27 21:05:37 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:05:36 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:05:06 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:04:41 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:04:34 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:04:27 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 21:04:07 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:03:59 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:03:54 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:03:40 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.065 |  |
| 2025-12-27 21:03:33 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:03:24 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-27 21:03:23 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:03:12 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:03:09 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-27 21:03:04 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:03:02 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 21:02:18 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-27 21:02:18 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-27 21:02:18 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 21:01:39 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:01:27 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-27 21:01:22 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:01:07 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:00:47 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-27 21:00:45 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:00:42 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:00:23 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.563 | 🔺 Rising |
| 2025-12-27 20:30:13 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 21:00:23 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.563 | 🔺 Rising |
| 2025-12-27 21:05:43 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-27 21:00:47 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-27 21:02:18 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 21:03:09 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-27 21:02:18 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-27 21:04:27 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 21:03:02 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 19:15:41 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:04:07 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:01:39 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:00:42 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:01:22 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:01:07 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:28 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:03:33 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-27 20:30:13 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:05:37 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:03:23 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:12:28 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:03:54 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:04:41 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:00:45 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:03:04 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:09:35 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:03:59 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:05:36 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:03:12 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:07:14 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:04:34 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:14:09 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.008 |  |
| 2025-12-27 18:01:19 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-27 21:08:25 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-27 21:01:27 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-27 21:03:24 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-27 21:02:18 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-27 21:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.045 |  |
| 2025-12-27 21:03:40 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.065 |  |
| 2025-12-27 21:08:43 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)