# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_23:06:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,767 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 23:06:08 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.009 |  |
| 2025-12-17 23:05:28 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.010 |  |
| 2025-12-17 23:05:19 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:05:18 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:04:10 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:04:08 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-17 23:03:58 | Yaka Wewa (Ma Oya) | 1.44 | 🟢 Normal | -0.062 |  |
| 2025-12-17 23:03:58 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.031 |  |
| 2025-12-17 23:03:56 | Padiyathalawa (Maduru Oya) | 3.70 | 🟢 Normal | 1.567 | 🔺 Rising |
| 2025-12-17 23:03:55 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 23:03:54 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:03:47 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 23:03:40 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.098 |  |
| 2025-12-17 23:03:33 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:03:33 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:03:22 | Thaldena (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2025-12-17 23:02:57 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | -0.163 |  |
| 2025-12-17 23:02:49 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:02:32 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-17 23:02:26 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-17 23:02:17 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:02:11 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:02:09 | Horowpothana (Yan Oya) | 5.69 | 🟢 Normal | -0.024 |  |
| 2025-12-17 23:01:45 | Moragaswewa (Deduru Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-17 23:01:39 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:01:32 | Dunamale (Aththanagalu Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 23:01:29 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:01:10 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 22:37:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.163 |  |
| 2025-12-17 22:19:00 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.344 |  |
| 2025-12-17 22:11:17 | Horowpothana (Yan Oya) | 5.71 | 🟢 Normal | -0.024 |  |
| 2025-12-17 22:10:45 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:10:19 | Padiyathalawa (Maduru Oya) | 2.30 | 🟢 Normal | 1.567 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 23:03:56 | Padiyathalawa (Maduru Oya) | 3.70 | 🟢 Normal | 1.567 | 🔺 Rising |
| 2025-12-17 23:03:22 | Thaldena (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2025-12-17 22:03:35 | Manampitiya (Mahaweli Ganga) | 2.33 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-17 23:04:08 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-17 23:02:26 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-17 18:01:03 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 18:04:33 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-17 23:03:47 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 23:01:10 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 23:01:32 | Dunamale (Aththanagalu Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 23:03:55 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 21:08:41 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-17 23:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:02:11 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:05:19 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:07:51 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:03:33 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:01:39 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:04:37 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:02:57 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:04:10 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:05:18 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:02:17 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:03:54 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:00:55 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:03:04 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:02:49 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:03:33 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 23:06:08 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.009 |  |
| 2025-12-17 23:05:28 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.010 |  |
| 2025-12-17 23:01:45 | Moragaswewa (Deduru Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-17 23:02:32 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-17 23:02:09 | Horowpothana (Yan Oya) | 5.69 | 🟢 Normal | -0.024 |  |
| 2025-12-17 23:03:58 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.031 |  |
| 2025-12-17 23:03:58 | Yaka Wewa (Ma Oya) | 1.44 | 🟢 Normal | -0.062 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-17 23:03:40 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.098 |  |
| 2025-12-17 23:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | -0.163 |  |
| 2025-12-17 22:19:00 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.344 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)