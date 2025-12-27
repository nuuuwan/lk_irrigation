# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_14:26:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,339 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 14:26:32 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-27 14:21:18 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.016 |  |
| 2025-12-27 14:20:30 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:13:47 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.009 |  |
| 2025-12-27 14:10:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-27 14:08:44 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:07:03 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:07:01 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:05:30 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:05:27 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-27 14:05:05 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:04:47 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.019 |  |
| 2025-12-27 14:04:19 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:04:18 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 14:04:15 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:03:18 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:03:12 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2025-12-27 14:03:10 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:03:02 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 14:02:52 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:02:51 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2025-12-27 14:02:40 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:02:31 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:02:24 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-27 14:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:02:01 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:01:57 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.022 |  |
| 2025-12-27 14:01:57 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:01:46 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2025-12-27 14:01:36 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2025-12-27 14:01:32 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:01:31 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 14:01:28 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:01:28 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:01:24 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2025-12-27 14:01:18 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:01:12 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:01:11 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.020 |  |
| 2025-12-27 14:01:06 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:00:26 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 14:03:12 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2025-12-27 13:03:59 | Weraganthota (Mahaweli Ganga) | 1.58 | 🟢 Normal | 1.616 | 🔺 Rising |
| 2025-12-27 14:01:46 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2025-12-27 14:26:32 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-27 14:10:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-27 14:01:31 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 14:03:02 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 14:02:24 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-27 14:04:18 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 14:05:27 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-27 14:01:28 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:04:15 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:05:05 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:02:52 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:03:10 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:05:30 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:02:01 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:01:57 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:01:12 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:20:30 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:01:32 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 14:13:47 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.009 |  |
| 2025-12-27 14:07:01 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:07:03 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:02:40 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:03:18 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:01:18 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:02:31 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:00:26 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:04:19 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:08:44 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:01:28 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-27 14:01:24 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2025-12-27 14:21:18 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.016 |  |
| 2025-12-27 14:04:47 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.019 |  |
| 2025-12-27 14:01:11 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.020 |  |
| 2025-12-27 14:01:36 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2025-12-27 14:01:57 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.022 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)