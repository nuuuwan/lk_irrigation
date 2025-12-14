# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_00:07:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,104 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 00:07:46 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-15 00:07:25 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | -0.028 |  |
| 2025-12-15 00:07:04 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-15 00:06:56 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.028 |  |
| 2025-12-15 00:06:47 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-15 00:05:59 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2025-12-15 00:05:39 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 00:04:56 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 00:04:36 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | 0.000 |  |
| 2025-12-15 00:04:33 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-15 00:03:41 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-15 00:03:31 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-15 00:03:22 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.090 |  |
| 2025-12-15 00:03:09 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-15 00:02:56 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.059 |  |
| 2025-12-15 00:02:31 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-15 00:02:26 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-15 00:02:03 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-15 00:02:02 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.040 |  |
| 2025-12-15 00:01:37 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.021 |  |
| 2025-12-15 00:01:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-15 00:01:20 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-15 00:00:57 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 00:00:14 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:57:08 | Horowpothana (Yan Oya) | 4.21 | 🟢 Normal | -0.011 |  |
| 2025-12-14 23:51:47 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-14 23:39:39 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -3.600 |  |
| 2025-12-14 23:39:12 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -3.600 |  |
| 2025-12-14 23:13:51 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:12:04 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 00:06:47 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-15 00:04:33 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-14 23:02:34 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-15 00:03:41 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-15 00:02:31 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-15 00:07:04 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-14 23:04:09 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-15 00:04:56 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 00:01:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-15 00:03:09 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-15 00:00:57 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:01:24 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:09 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-15 00:04:36 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | 0.000 |  |
| 2025-12-15 00:02:26 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-15 00:05:39 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:03:59 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:05:07 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 00:07:46 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:24 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:03:57 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 00:00:14 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:05:47 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 23:08:30 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2025-12-15 00:01:20 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-15 00:03:31 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:05:18 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-15 00:02:03 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-15 00:05:59 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2025-12-14 23:57:08 | Horowpothana (Yan Oya) | 4.21 | 🟢 Normal | -0.011 |  |
| 2025-12-14 23:02:15 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2025-12-15 00:01:37 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.021 |  |
| 2025-12-15 00:06:56 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.028 |  |
| 2025-12-15 00:07:25 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | -0.028 |  |
| 2025-12-14 22:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.035 |  |
| 2025-12-15 00:02:02 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.040 |  |
| 2025-12-15 00:02:56 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.059 |  |
| 2025-12-15 00:03:22 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.090 |  |
| 2025-12-14 23:39:39 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -3.600 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)