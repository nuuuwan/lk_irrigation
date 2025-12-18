# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_08:11:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,108 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 08:11:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.026 |  |
| 2025-12-18 08:08:08 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-18 08:08:08 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-18 08:07:33 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.666 | 🔺 Rising |
| 2025-12-18 08:07:10 | Siyambalanduwa (Heda Oya) | 1.23 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-18 08:06:57 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:06:52 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-18 08:06:49 | Glencourse (Kelani Ganga) | 9.29 | 🟢 Normal | -0.040 |  |
| 2025-12-18 08:06:18 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:06:07 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:06:03 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:04:59 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2025-12-18 08:04:45 | Padiyathalawa (Maduru Oya) | 3.62 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2025-12-18 08:04:28 | Manampitiya (Mahaweli Ganga) | 3.50 | 🟡 Alert | 0.194 | 🔺 Rising |
| 2025-12-18 08:04:23 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:04:16 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-18 08:04:09 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.021 |  |
| 2025-12-18 08:03:45 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.033 |  |
| 2025-12-18 08:03:29 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:03:18 | Thaldena (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:03:07 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-18 08:03:00 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.012 |  |
| 2025-12-18 08:02:59 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:02:38 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 08:02:36 | Thanthirimale (Malwathu Oya) | 4.37 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-18 08:02:21 | Nakkala (Kumbukkan Oya) | 2.84 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2025-12-18 08:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.040 |  |
| 2025-12-18 08:02:13 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-18 08:02:09 | Yaka Wewa (Ma Oya) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 08:02:02 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 08:02:02 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:01:52 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:01:35 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:01:26 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:01:14 | Horowpothana (Yan Oya) | 5.47 | 🟢 Normal | -0.118 |  |
| 2025-12-18 08:01:06 | Moragaswewa (Deduru Oya) | 1.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-18 08:01:05 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.062 |  |
| 2025-12-18 08:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:47:31 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.029 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 08:04:28 | Manampitiya (Mahaweli Ganga) | 3.50 | 🟡 Alert | 0.194 | 🔺 Rising |
| 2025-12-18 08:07:33 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.666 | 🔺 Rising |
| 2025-12-18 08:04:45 | Padiyathalawa (Maduru Oya) | 3.62 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2025-12-18 08:06:52 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-18 08:02:21 | Nakkala (Kumbukkan Oya) | 2.84 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2025-12-18 08:02:13 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-18 08:02:36 | Thanthirimale (Malwathu Oya) | 4.37 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-18 08:07:10 | Siyambalanduwa (Heda Oya) | 1.23 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-18 08:04:16 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-18 08:03:07 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-18 08:08:08 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-18 08:02:38 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 08:08:08 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-18 08:01:06 | Moragaswewa (Deduru Oya) | 1.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-18 08:02:02 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 08:02:09 | Yaka Wewa (Ma Oya) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 08:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:06:18 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:04:23 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:01:26 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:01:35 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:06:57 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:03:18 | Thaldena (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:06:03 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:01:52 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:03:29 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:06:07 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:02:02 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:02:59 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 08:03:00 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.012 |  |
| 2025-12-18 08:04:09 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.021 |  |
| 2025-12-18 08:11:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.026 |  |
| 2025-12-18 08:03:45 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.033 |  |
| 2025-12-18 08:06:49 | Glencourse (Kelani Ganga) | 9.29 | 🟢 Normal | -0.040 |  |
| 2025-12-18 08:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.040 |  |
| 2025-12-18 08:04:59 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2025-12-18 08:01:05 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.062 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-18 08:01:14 | Horowpothana (Yan Oya) | 5.47 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)