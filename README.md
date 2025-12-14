# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_23:04:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,066 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 23:04:09 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-14 23:04:06 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-14 23:03:59 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:03:57 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:03:42 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.033 |  |
| 2025-12-14 23:03:16 | Padiyathalawa (Maduru Oya) | 1.26 | 🟢 Normal | -0.088 |  |
| 2025-12-14 23:03:09 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2025-12-14 23:03:00 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:02:34 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-14 23:02:29 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:02:16 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:02:15 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2025-12-14 23:02:12 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.101 |  |
| 2025-12-14 23:01:59 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.048 |  |
| 2025-12-14 23:01:43 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-14 23:01:42 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.040 |  |
| 2025-12-14 23:01:34 | Horowpothana (Yan Oya) | 4.22 | 🟢 Normal | -0.010 |  |
| 2025-12-14 23:01:30 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:01:24 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:01:20 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-14 23:01:12 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-14 23:00:43 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.022 |  |
| 2025-12-14 23:00:36 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-14 22:37:05 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.048 |  |
| 2025-12-14 22:37:04 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.048 |  |
| 2025-12-14 22:20:08 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | -0.008 |  |
| 2025-12-14 22:15:18 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-14 22:11:46 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-14 22:10:06 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-14 22:09:00 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-14 22:08:57 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-14 22:08:21 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.033 |  |
| 2025-12-14 22:08:18 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-14 22:07:05 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-14 22:06:58 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.022 |  |
| 2025-12-14 22:06:48 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-14 22:06:40 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-14 22:06:31 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-14 22:06:28 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.019 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 23:01:43 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-14 23:02:34 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-14 23:01:12 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-14 22:08:57 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-14 22:06:28 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-14 23:04:09 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-14 23:04:06 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-14 21:05:07 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 23:02:29 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-14 22:02:41 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:01:24 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:03:00 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:09 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-14 22:15:18 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:01:30 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:03:59 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-14 22:03:08 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-14 22:08:18 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:02:16 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 22:01:25 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 22:10:06 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:24 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:03:57 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:00:36 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-14 22:20:08 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | -0.008 |  |
| 2025-12-14 23:01:34 | Horowpothana (Yan Oya) | 4.22 | 🟢 Normal | -0.010 |  |
| 2025-12-14 23:01:20 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:05:18 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-14 22:04:19 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-14 22:02:30 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-14 23:02:15 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2025-12-14 23:03:09 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2025-12-14 23:00:43 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.022 |  |
| 2025-12-14 23:03:42 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.033 |  |
| 2025-12-14 22:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.035 |  |
| 2025-12-14 23:01:42 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.040 |  |
| 2025-12-14 23:01:59 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.048 |  |
| 2025-12-14 23:03:16 | Padiyathalawa (Maduru Oya) | 1.26 | 🟢 Normal | -0.088 |  |
| 2025-12-14 23:02:12 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)