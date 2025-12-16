# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_11:07:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,419 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 11:07:35 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-16 11:07:22 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2025-12-16 11:06:49 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:06:05 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.011 |  |
| 2025-12-16 11:06:01 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:05:47 | Weraganthota (Mahaweli Ganga) | -1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:05:30 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-16 11:04:34 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:04:27 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:04:10 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:04:09 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:03:57 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:03:47 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2025-12-16 11:03:40 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | -0.050 |  |
| 2025-12-16 11:03:25 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:03:23 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-16 11:03:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:03:10 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 11:02:51 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:02:45 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.075 |  |
| 2025-12-16 11:02:34 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:02:27 | Thanthirimale (Malwathu Oya) | 3.75 | 🟢 Normal | -0.074 |  |
| 2025-12-16 11:02:20 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:02:19 | Yaka Wewa (Ma Oya) | 1.83 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-16 11:02:07 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:02:06 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 11:01:23 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:01:05 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:01:04 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:01:01 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-16 11:00:53 | Horowpothana (Yan Oya) | 5.08 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2025-12-16 11:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:59:18 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-16 10:20:10 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-16 10:13:59 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:12:59 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:11:28 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.011 |  |
| 2025-12-16 10:11:13 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 10:10:04 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 11:00:53 | Horowpothana (Yan Oya) | 5.08 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2025-12-16 11:05:30 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-16 11:03:23 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-16 11:02:19 | Yaka Wewa (Ma Oya) | 1.83 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-16 11:02:06 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 10:59:18 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-16 11:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 10:11:13 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 11:04:09 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:05:47 | Weraganthota (Mahaweli Ganga) | -1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:02:51 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:04:23 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:02:20 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:02:07 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:01:05 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:02:34 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:03:10 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:04:27 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:01:04 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:01:23 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:04:10 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:01:29 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:03:57 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:06:49 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:13:59 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:06:01 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:06:39 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:04:34 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 11:03:25 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 10:08:10 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2025-12-16 11:07:22 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2025-12-16 11:07:35 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-16 11:01:01 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-16 11:03:47 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2025-12-16 11:06:05 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.011 |  |
| 2025-12-16 11:03:40 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | -0.050 |  |
| 2025-12-16 11:02:27 | Thanthirimale (Malwathu Oya) | 3.75 | 🟢 Normal | -0.074 |  |
| 2025-12-16 11:02:45 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)