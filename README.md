# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_03:31:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,214 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 03:31:36 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.014 |  |
| 2025-12-15 03:16:53 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.026 |  |
| 2025-12-15 03:16:52 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.124 |  |
| 2025-12-15 03:16:21 | Kithulgala (Kelani Ganga) | 0.90 | 🟢 Normal | -13.941 |  |
| 2025-12-15 03:16:16 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | -0.005 |  |
| 2025-12-15 03:15:31 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.025 |  |
| 2025-12-15 03:14:04 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-15 03:12:57 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -13.941 |  |
| 2025-12-15 03:11:33 | Glencourse (Kelani Ganga) | 9.39 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-15 03:08:10 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:06:27 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.029 |  |
| 2025-12-15 03:06:11 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -6.545 |  |
| 2025-12-15 03:06:10 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:06:04 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:06:01 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -126.000 |  |
| 2025-12-15 03:05:59 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -126.000 |  |
| 2025-12-15 03:05:57 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -126.000 |  |
| 2025-12-15 03:05:53 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:05:51 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.006 |  |
| 2025-12-15 03:05:49 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -6.545 |  |
| 2025-12-15 03:05:21 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -6.545 |  |
| 2025-12-15 03:05:20 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:03:59 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:03:30 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:03:25 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.040 |  |
| 2025-12-15 03:03:17 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:03:11 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:03:07 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | -0.010 |  |
| 2025-12-15 03:02:47 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 03:02:42 | Horowpothana (Yan Oya) | 4.18 | 🟢 Normal | -1.565 |  |
| 2025-12-15 03:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-15 03:02:24 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.022 |  |
| 2025-12-15 03:02:23 | Rathnapura (Kalu Ganga) | 2.07 | 🟢 Normal | 1.561 | 🔺 Rising |
| 2025-12-15 03:02:19 | Horowpothana (Yan Oya) | 4.19 | 🟢 Normal | -1.565 |  |
| 2025-12-15 03:01:57 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:01:28 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:01:19 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:01:09 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:00:23 | Manampitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.021 |  |
| 2025-12-15 02:56:37 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 1.561 | 🔺 Rising |
| 2025-12-15 02:49:40 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 03:02:23 | Rathnapura (Kalu Ganga) | 2.07 | 🟢 Normal | 1.561 | 🔺 Rising |
| 2025-12-15 03:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-15 01:03:44 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-15 03:11:33 | Glencourse (Kelani Ganga) | 9.39 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-15 03:02:47 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 03:14:04 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-15 03:01:28 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:01:57 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:03:11 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:09 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:06:04 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:05:20 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:03:17 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:03:30 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:08:10 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:06:10 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:24 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:01:19 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:01:09 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:03:59 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:16:16 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | -0.005 |  |
| 2025-12-15 03:05:51 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.006 |  |
| 2025-12-15 03:03:07 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:05:18 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-15 02:01:24 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-15 03:31:36 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.014 |  |
| 2025-12-15 03:00:23 | Manampitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.021 |  |
| 2025-12-15 03:02:24 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.022 |  |
| 2025-12-15 03:15:31 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.025 |  |
| 2025-12-15 03:16:53 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.026 |  |
| 2025-12-15 03:06:27 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.029 |  |
| 2025-12-15 03:03:25 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.040 |  |
| 2025-12-15 02:02:33 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.091 |  |
| 2025-12-15 03:16:52 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.124 |  |
| 2025-12-15 03:02:42 | Horowpothana (Yan Oya) | 4.18 | 🟢 Normal | -1.565 |  |
| 2025-12-15 03:06:11 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -6.545 |  |
| 2025-12-15 03:16:21 | Kithulgala (Kelani Ganga) | 0.90 | 🟢 Normal | -13.941 |  |
| 2025-12-15 03:06:01 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -126.000 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)