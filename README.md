# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_01:47:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,145 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 01:47:35 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | -0.018 |  |
| 2025-12-15 01:42:47 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.013 |  |
| 2025-12-15 01:37:51 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:37:30 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:35:23 | Horowpothana (Yan Oya) | 4.20 | 🟢 Normal | -0.006 |  |
| 2025-12-15 01:29:45 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2025-12-15 01:23:28 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.007 |  |
| 2025-12-15 01:19:48 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2025-12-15 01:17:47 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:13:08 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:11:59 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-15 01:11:40 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-15 01:08:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | -0.063 |  |
| 2025-12-15 01:08:00 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-15 01:07:03 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:06:11 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:06:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:05:51 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-15 01:05:06 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-15 01:04:16 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-15 01:04:13 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:04:10 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-15 01:03:48 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-15 01:03:44 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-15 01:03:25 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:03:23 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:03:22 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.079 |  |
| 2025-12-15 01:03:09 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2025-12-15 01:02:35 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:02:19 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:02:00 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:01:51 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | -0.040 |  |
| 2025-12-15 01:01:35 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:01:16 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 01:29:45 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2025-12-15 01:11:59 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-15 01:05:06 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-15 01:04:16 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-15 00:07:04 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-15 01:03:44 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-15 01:03:48 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-15 01:08:00 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-15 01:11:40 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-15 01:01:35 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:02:35 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:37:51 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:02:19 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:09 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:13:08 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:06:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:17:47 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:03:25 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:07:03 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:01:16 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:24 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:04:13 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:06:11 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:02:00 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:35:23 | Horowpothana (Yan Oya) | 4.20 | 🟢 Normal | -0.006 |  |
| 2025-12-15 01:23:28 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.007 |  |
| 2025-12-15 01:19:48 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2025-12-15 01:04:10 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-15 00:01:20 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:05:18 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-15 01:05:51 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-15 01:42:47 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.013 |  |
| 2025-12-15 01:47:35 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | -0.018 |  |
| 2025-12-15 01:03:09 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2025-12-15 01:01:51 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | -0.040 |  |
| 2025-12-15 01:08:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | -0.063 |  |
| 2025-12-15 01:03:22 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.079 |  |
| 2025-12-15 00:03:22 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)