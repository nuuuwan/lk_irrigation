# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_15:11:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,579 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 15:11:57 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.020 |  |
| 2025-12-16 15:11:03 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-16 15:09:40 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:09:06 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:08:23 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.010 |  |
| 2025-12-16 15:06:40 | Moragaswewa (Deduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:06:19 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:05:55 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:05:31 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:04:59 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.009 |  |
| 2025-12-16 15:04:47 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2025-12-16 15:04:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.059 |  |
| 2025-12-16 15:04:37 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:04:09 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 15:04:01 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:03:44 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:03:40 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2025-12-16 15:03:25 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2025-12-16 15:03:23 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:03:17 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2025-12-16 15:03:08 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:02:53 | Thanthirimale (Malwathu Oya) | 3.48 | 🟢 Normal | -0.073 |  |
| 2025-12-16 15:02:46 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:02:24 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:02:15 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.041 |  |
| 2025-12-16 15:02:14 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 15:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.27 | 🟢 Normal | -0.062 |  |
| 2025-12-16 15:01:49 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-16 15:01:39 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:01:37 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:01:21 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:01:18 | Yaka Wewa (Ma Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2025-12-16 15:01:11 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.065 |  |
| 2025-12-16 15:00:51 | Horowpothana (Yan Oya) | 5.68 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-16 15:00:49 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2025-12-16 15:00:37 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-16 15:00:09 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 15:00:51 | Horowpothana (Yan Oya) | 5.68 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-16 15:04:09 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 15:01:49 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-16 15:02:14 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 15:11:03 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-16 15:02:24 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:02:46 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:06:40 | Moragaswewa (Deduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 14:03:59 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:01:37 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:05:55 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:03:08 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:01:21 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:04:37 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:00:09 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:09:40 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:01:39 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:04:01 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:03:44 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:06:19 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:09:06 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:03:23 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:05:31 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 15:04:59 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.009 |  |
| 2025-12-16 15:08:23 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.010 |  |
| 2025-12-16 15:00:37 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-16 15:00:49 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2025-12-16 15:03:17 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2025-12-16 15:03:40 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2025-12-16 15:03:25 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2025-12-16 15:01:18 | Yaka Wewa (Ma Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2025-12-16 15:11:57 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.020 |  |
| 2025-12-16 15:04:47 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2025-12-16 15:02:15 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.041 |  |
| 2025-12-16 15:04:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.059 |  |
| 2025-12-16 15:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.27 | 🟢 Normal | -0.062 |  |
| 2025-12-16 15:01:11 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.065 |  |
| 2025-12-16 15:02:53 | Thanthirimale (Malwathu Oya) | 3.48 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)