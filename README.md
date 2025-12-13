# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_08:15:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,586 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 08:15:55 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.043 |  |
| 2025-12-13 08:12:58 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:11:52 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:11:01 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-13 08:09:55 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.009 |  |
| 2025-12-13 08:09:44 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:09:12 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:08:51 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-13 08:08:14 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.047 |  |
| 2025-12-13 08:07:52 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2025-12-13 08:07:24 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2025-12-13 08:06:51 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-13 08:06:45 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.018 |  |
| 2025-12-13 08:06:31 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:06:27 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.031 |  |
| 2025-12-13 08:05:58 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-13 08:05:37 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2025-12-13 08:04:53 | Kithulgala (Kelani Ganga) | 0.77 | 🟢 Normal | -55.636 |  |
| 2025-12-13 08:04:36 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:04:21 | Weraganthota (Mahaweli Ganga) | -0.31 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-13 08:03:54 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2025-12-13 08:03:47 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -55.636 |  |
| 2025-12-13 08:03:09 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.010 |  |
| 2025-12-13 08:03:07 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.082 |  |
| 2025-12-13 08:02:53 | Thanthirimale (Malwathu Oya) | 4.23 | 🟢 Normal | -0.028 |  |
| 2025-12-13 08:02:32 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:02:28 | Manampitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.040 |  |
| 2025-12-13 08:02:19 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 08:02:17 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-13 08:02:13 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | -0.020 |  |
| 2025-12-13 08:02:08 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-13 08:01:45 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:01:12 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.050 |  |
| 2025-12-13 08:01:09 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:00:46 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:00:43 | Horowpothana (Yan Oya) | 6.05 | 🟡 Alert | -0.060 |  |
| 2025-12-13 08:00:25 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:00:07 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-13 07:50:52 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 08:00:43 | Horowpothana (Yan Oya) | 6.05 | 🟡 Alert | -0.060 |  |
| 2025-12-13 08:04:21 | Weraganthota (Mahaweli Ganga) | -0.31 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-13 08:02:17 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-13 08:08:51 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-13 08:06:51 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-13 08:02:19 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 08:11:01 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-13 08:00:25 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:11:52 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:03:09 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:09:12 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:01:09 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:12:58 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:04:36 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:02:32 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:00:46 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:00:07 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:06:31 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:09:44 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:01:45 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 08:09:55 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.009 |  |
| 2025-12-13 08:05:37 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2025-12-13 07:21:55 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-13 08:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.010 |  |
| 2025-12-13 08:02:08 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-13 08:03:54 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2025-12-13 08:05:58 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-13 08:06:45 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.018 |  |
| 2025-12-13 08:02:13 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | -0.020 |  |
| 2025-12-13 08:07:52 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2025-12-13 08:02:53 | Thanthirimale (Malwathu Oya) | 4.23 | 🟢 Normal | -0.028 |  |
| 2025-12-13 08:07:24 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2025-12-13 08:06:27 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.031 |  |
| 2025-12-13 08:02:28 | Manampitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.040 |  |
| 2025-12-13 08:15:55 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.043 |  |
| 2025-12-13 08:08:14 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.047 |  |
| 2025-12-13 08:01:12 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.050 |  |
| 2025-12-13 08:03:07 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.082 |  |
| 2025-12-13 08:04:53 | Kithulgala (Kelani Ganga) | 0.77 | 🟢 Normal | -55.636 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)