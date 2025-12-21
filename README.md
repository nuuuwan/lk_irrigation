# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_07:25:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,716 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 07:25:28 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.007 |  |
| 2025-12-21 07:15:08 | Galgamuwa (Mee Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:12:03 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.018 |  |
| 2025-12-21 07:10:30 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-21 07:10:06 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:09:43 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-21 07:09:07 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:07:50 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:07:30 | Nakkala (Kumbukkan Oya) | 1.35 | 🟢 Normal | -0.018 |  |
| 2025-12-21 07:07:09 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:06:52 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-21 07:06:47 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-21 07:06:26 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 07:06:03 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:05:58 | Weraganthota (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.242 |  |
| 2025-12-21 07:05:58 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-21 07:05:51 | Moragaswewa (Deduru Oya) | 1.66 | 🟢 Normal | -0.058 |  |
| 2025-12-21 07:05:14 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2025-12-21 07:05:11 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 07:05:06 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -0.010 |  |
| 2025-12-21 07:04:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2025-12-21 07:04:10 | Thanthirimale (Malwathu Oya) | 5.20 | 🟡 Alert | -0.008 |  |
| 2025-12-21 07:03:50 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:03:26 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-21 07:03:21 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:03:20 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-21 07:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2025-12-21 07:02:51 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:02:50 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:02:49 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2025-12-21 07:02:36 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:02:26 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-21 07:02:18 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:02:03 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:01:42 | Horowpothana (Yan Oya) | 5.65 | 🟢 Normal | -0.131 |  |
| 2025-12-21 07:01:28 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2025-12-21 07:01:04 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:00:52 | Manampitiya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 07:04:10 | Thanthirimale (Malwathu Oya) | 5.20 | 🟡 Alert | -0.008 |  |
| 2025-12-21 07:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2025-12-21 07:05:14 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2025-12-21 07:05:58 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-21 07:09:43 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-21 07:02:26 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-21 07:03:20 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-21 07:06:52 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-21 07:10:30 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-21 07:05:11 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 07:06:26 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 07:02:50 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:03:21 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:02:03 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:02:18 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:15:08 | Galgamuwa (Mee Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:03:50 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:07:50 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:10:06 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:01:04 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:06:03 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:02:36 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:02:51 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:09:07 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:07:09 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 07:25:28 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.007 |  |
| 2025-12-21 07:03:26 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-21 07:05:06 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -0.010 |  |
| 2025-12-21 07:12:03 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.018 |  |
| 2025-12-21 07:07:30 | Nakkala (Kumbukkan Oya) | 1.35 | 🟢 Normal | -0.018 |  |
| 2025-12-21 07:06:47 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-21 07:02:49 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2025-12-21 07:01:28 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2025-12-21 07:04:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2025-12-21 07:00:52 | Manampitiya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.041 |  |
| 2025-12-21 07:05:51 | Moragaswewa (Deduru Oya) | 1.66 | 🟢 Normal | -0.058 |  |
| 2025-12-21 06:01:02 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.061 |  |
| 2025-12-21 07:01:42 | Horowpothana (Yan Oya) | 5.65 | 🟢 Normal | -0.131 |  |
| 2025-12-21 07:05:58 | Weraganthota (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.242 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)