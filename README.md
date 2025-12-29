# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_10:13:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,960 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 10:13:58 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:10:51 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-29 10:09:33 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:09:29 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:09:27 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 10:09:18 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:09:04 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.107 |  |
| 2025-12-29 10:08:33 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:07:18 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 10:07:08 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:06:18 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:06:12 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-29 10:06:00 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:05:11 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:04:35 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2025-12-29 10:04:27 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:04:05 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:04:04 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:03:40 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:03:35 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:03:29 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:03:06 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:03:05 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:02:55 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-29 10:02:55 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2025-12-29 10:02:54 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-29 10:02:49 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-29 10:02:27 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:02:16 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.406 | 🔺 Rising |
| 2025-12-29 10:02:10 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 10:02:09 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.041 |  |
| 2025-12-29 10:02:08 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:01:39 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2025-12-29 10:01:36 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:01:12 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | -0.010 |  |
| 2025-12-29 10:01:02 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:00:39 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:00:34 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 10:02:16 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.406 | 🔺 Rising |
| 2025-12-29 10:01:39 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2025-12-29 10:10:51 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-29 10:02:49 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-29 10:02:10 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 10:07:18 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 10:09:27 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 10:02:55 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-29 10:00:34 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:00:39 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:03:06 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:07:08 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:13:58 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:04:04 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:08:33 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:06:00 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:02:08 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:03:06 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:03:35 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:04:27 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:09:33 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:03:40 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:01:36 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:04:05 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:03:29 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:03:05 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:09:29 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:01:02 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:09:18 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:02:27 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:06:18 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:04:35 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2025-12-29 10:06:12 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-29 10:02:54 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-29 10:01:12 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | -0.010 |  |
| 2025-12-29 10:02:09 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.041 |  |
| 2025-12-29 10:02:55 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2025-12-29 10:09:04 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)