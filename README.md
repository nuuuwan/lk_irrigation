# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_10:11:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,047 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 10:11:34 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2025-12-10 10:11:07 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:10:03 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 4.547 | 🔺 Rising |
| 2025-12-10 10:08:34 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:07:46 | Manampitiya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-10 10:07:31 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:07:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.028 |  |
| 2025-12-10 10:07:11 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-10 10:06:53 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 4.547 | 🔺 Rising |
| 2025-12-10 10:06:26 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-10 10:05:44 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:04:59 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:04:58 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 10:04:37 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.031 |  |
| 2025-12-10 10:04:29 | Thanthirimale (Malwathu Oya) | 3.52 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-10 10:04:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.117 |  |
| 2025-12-10 10:03:43 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | -0.030 |  |
| 2025-12-10 10:03:42 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -0.082 |  |
| 2025-12-10 10:03:35 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2025-12-10 10:03:30 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.107 |  |
| 2025-12-10 10:03:17 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-10 10:03:17 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-10 10:03:07 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.129 |  |
| 2025-12-10 10:03:02 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:02:59 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:02:55 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.040 |  |
| 2025-12-10 10:02:54 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.090 |  |
| 2025-12-10 10:02:42 | Horowpothana (Yan Oya) | 4.97 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2025-12-10 10:02:40 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:02:19 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:02:12 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-10 10:01:35 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:01:14 | Yaka Wewa (Ma Oya) | 2.16 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2025-12-10 10:00:54 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-10 10:00:40 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.031 |  |
| 2025-12-10 10:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 09:13:09 | Horowpothana (Yan Oya) | 4.76 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2025-12-10 09:12:56 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-10 09:12:54 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | 0.009 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 10:10:03 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 4.547 | 🔺 Rising |
| 2025-12-10 10:01:14 | Yaka Wewa (Ma Oya) | 2.16 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2025-12-10 10:02:42 | Horowpothana (Yan Oya) | 4.97 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2025-12-10 10:02:12 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-10 10:04:29 | Thanthirimale (Malwathu Oya) | 3.52 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-10 10:00:54 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-10 10:07:46 | Manampitiya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-10 10:03:17 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-10 09:02:49 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-10 10:04:58 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 09:12:54 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-10 10:02:19 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:02:59 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:03:02 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:04:59 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:11:07 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:07:31 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:05:44 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:02:40 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:08:34 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-10 10:06:26 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-10 09:06:51 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-10 10:07:11 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-10 10:03:35 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2025-12-10 10:03:17 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-10 10:11:34 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2025-12-10 10:07:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.028 |  |
| 2025-12-10 10:03:43 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | -0.030 |  |
| 2025-12-10 10:00:40 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.031 |  |
| 2025-12-10 10:04:37 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.031 |  |
| 2025-12-10 10:02:55 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.040 |  |
| 2025-12-10 09:06:26 | Weraganthota (Mahaweli Ganga) | -1.39 | 🟢 Normal | -0.057 |  |
| 2025-12-10 10:03:42 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -0.082 |  |
| 2025-12-10 10:02:54 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.090 |  |
| 2025-12-10 10:03:30 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.107 |  |
| 2025-12-10 10:04:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.117 |  |
| 2025-12-10 10:03:07 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)