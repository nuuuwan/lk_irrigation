# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_09:14:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,252 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 09:14:12 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.046 |  |
| 2025-12-26 09:14:08 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-26 09:11:23 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | -0.021 |  |
| 2025-12-26 09:11:08 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-26 09:10:05 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.030 |  |
| 2025-12-26 09:09:08 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:09:07 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:08:43 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:07:09 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:06:51 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:06:43 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.019 |  |
| 2025-12-26 09:06:16 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2025-12-26 09:06:01 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.095 |  |
| 2025-12-26 09:05:30 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:05:29 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:04:27 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:04:24 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:04:19 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.071 |  |
| 2025-12-26 09:04:07 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:03:29 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:03:25 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:03:20 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-26 09:03:03 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:02:53 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.019 |  |
| 2025-12-26 09:02:53 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-26 09:02:45 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-26 09:02:45 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:02:39 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | -0.020 |  |
| 2025-12-26 09:01:46 | Thanthirimale (Malwathu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:01:45 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:01:36 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.155 |  |
| 2025-12-26 09:01:29 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:01:21 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.189 |  |
| 2025-12-26 09:01:17 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:00:55 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2025-12-26 08:55:00 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.189 |  |
| 2025-12-26 08:43:18 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.021 |  |
| 2025-12-26 08:25:38 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.016 |  |
| 2025-12-26 08:21:49 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.095 |  |
| 2025-12-26 08:19:24 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 09:02:53 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-26 09:11:08 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-26 09:14:08 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-26 09:08:43 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:00:55 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:04:27 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:04:24 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:04:07 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:03:29 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:05:30 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:09:07 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:01:45 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:03:03 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:01:17 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:03:25 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:09:08 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:06:51 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:07:09 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:01:46 | Thanthirimale (Malwathu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:02:39 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:01:29 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:02:45 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 08:12:17 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.009 |  |
| 2025-12-26 09:03:20 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-26 09:02:45 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-26 09:06:16 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2025-12-26 08:25:38 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.016 |  |
| 2025-12-26 09:06:43 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.019 |  |
| 2025-12-26 09:02:53 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.019 |  |
| 2025-12-26 09:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | -0.020 |  |
| 2025-12-26 09:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2025-12-26 09:11:23 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | -0.021 |  |
| 2025-12-26 09:10:05 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.030 |  |
| 2025-12-26 08:08:58 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.032 |  |
| 2025-12-26 09:14:12 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.046 |  |
| 2025-12-26 09:04:19 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.071 |  |
| 2025-12-26 09:06:01 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.095 |  |
| 2025-12-26 09:01:36 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.155 |  |
| 2025-12-26 09:01:21 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)