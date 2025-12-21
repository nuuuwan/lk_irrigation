# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_08:33:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,755 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 08:33:08 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.013 |  |
| 2025-12-21 08:18:34 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2025-12-21 08:09:05 | Galgamuwa (Mee Oya) | 1.73 | 🟢 Normal | -0.011 |  |
| 2025-12-21 08:08:46 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.085 |  |
| 2025-12-21 08:08:29 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.019 |  |
| 2025-12-21 08:08:11 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:08:00 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2025-12-21 08:07:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:07:32 | Thanthirimale (Malwathu Oya) | 5.19 | 🟡 Alert | -0.009 |  |
| 2025-12-21 08:06:23 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-21 08:06:02 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:05:47 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2025-12-21 08:05:22 | Weraganthota (Mahaweli Ganga) | -0.66 | 🟢 Normal | -0.323 |  |
| 2025-12-21 08:05:22 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2025-12-21 08:05:12 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | -0.192 |  |
| 2025-12-21 08:05:04 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 08:04:57 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.100 |  |
| 2025-12-21 08:04:39 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:04:27 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-21 08:04:23 | Horowpothana (Yan Oya) | 5.51 | 🟢 Normal | -0.134 |  |
| 2025-12-21 08:03:59 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:03:39 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:03:25 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2025-12-21 08:03:21 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:03:12 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2025-12-21 08:03:09 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:03:06 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | -0.011 |  |
| 2025-12-21 08:02:50 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-21 08:02:43 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-21 08:02:42 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2025-12-21 08:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:02:04 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:01:51 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:01:47 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-21 08:01:44 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2025-12-21 08:01:41 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-21 08:01:39 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 08:01:23 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:00:41 | Manampitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.070 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 08:07:32 | Thanthirimale (Malwathu Oya) | 5.19 | 🟡 Alert | -0.009 |  |
| 2025-12-21 08:04:27 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-21 08:02:50 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-21 08:06:23 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-21 08:05:04 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 08:01:39 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 08:03:21 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:03:09 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:04:39 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:01:51 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:01:23 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:03:59 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:02:04 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:06:02 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:08:11 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:03:39 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:07:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 08:18:34 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2025-12-21 08:08:00 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2025-12-21 08:05:22 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2025-12-21 08:02:43 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-21 08:01:47 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-21 08:03:06 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | -0.011 |  |
| 2025-12-21 08:01:41 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-21 08:09:05 | Galgamuwa (Mee Oya) | 1.73 | 🟢 Normal | -0.011 |  |
| 2025-12-21 08:01:44 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2025-12-21 08:02:42 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2025-12-21 08:33:08 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.013 |  |
| 2025-12-21 08:08:29 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.019 |  |
| 2025-12-21 08:03:25 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2025-12-21 08:05:47 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2025-12-21 08:03:12 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2025-12-21 08:00:41 | Manampitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.070 |  |
| 2025-12-21 08:08:46 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.085 |  |
| 2025-12-21 08:04:57 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.100 |  |
| 2025-12-21 08:04:23 | Horowpothana (Yan Oya) | 5.51 | 🟢 Normal | -0.134 |  |
| 2025-12-21 08:05:12 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | -0.192 |  |
| 2025-12-21 08:05:22 | Weraganthota (Mahaweli Ganga) | -0.66 | 🟢 Normal | -0.323 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)