# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_11:14:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,941 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 11:14:40 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.019 |  |
| 2026-05-10 11:13:57 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:11:35 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2026-05-10 11:10:27 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-10 11:09:04 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:08:08 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.028 |  |
| 2026-05-10 11:08:00 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-10 11:07:06 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-10 11:05:54 | Glencourse (Kelani Ganga) | 9.68 | 🟢 Normal | -0.059 |  |
| 2026-05-10 11:05:37 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-05-10 11:05:23 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.040 |  |
| 2026-05-10 11:04:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | -0.031 |  |
| 2026-05-10 11:04:48 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | -0.023 |  |
| 2026-05-10 11:04:45 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-05-10 11:04:30 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-05-10 11:04:27 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.027 |  |
| 2026-05-10 11:04:06 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:04:01 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:03:48 | Kuda Oya (Kirindi Oya) | 2.06 | 🟢 Normal | -0.048 |  |
| 2026-05-10 11:03:44 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:03:36 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.048 |  |
| 2026-05-10 11:03:28 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-10 11:03:25 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-05-10 11:03:20 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:03:17 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-10 11:03:04 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.029 |  |
| 2026-05-10 11:02:53 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-05-10 11:02:21 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-05-10 11:02:19 | Katharagama (Menik Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-05-10 11:02:19 | Moragaswewa (Deduru Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:02:04 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 11:02:03 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.040 |  |
| 2026-05-10 11:02:01 | Moragaswewa (Deduru Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:01:49 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:01:23 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | -0.041 |  |
| 2026-05-10 11:01:10 | Thanamalwila (Kirindi Oya) | 2.14 | 🟢 Normal | -0.076 |  |
| 2026-05-10 11:01:00 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-10 11:00:57 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2026-05-10 11:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-10 11:00:15 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-10 10:30:23 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.015 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 11:07:06 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-10 11:00:15 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-10 11:01:00 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-10 11:08:00 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-10 11:02:04 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 11:10:27 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-10 11:02:19 | Moragaswewa (Deduru Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:01:49 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:03:44 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:13:57 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:09:04 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:03:20 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:04:06 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:04:01 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-10 11:03:17 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-10 11:03:28 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-10 11:02:53 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-05-10 11:05:37 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-05-10 11:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-10 11:00:57 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2026-05-10 11:11:35 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2026-05-10 11:14:40 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.019 |  |
| 2026-05-10 11:03:25 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-05-10 11:02:21 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-05-10 11:02:19 | Katharagama (Menik Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-05-10 11:04:45 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-05-10 11:04:48 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | -0.023 |  |
| 2026-05-10 11:04:27 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.027 |  |
| 2026-05-10 11:08:08 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.028 |  |
| 2026-05-10 11:03:04 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.029 |  |
| 2026-05-10 11:04:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | -0.031 |  |
| 2026-05-10 11:02:03 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.040 |  |
| 2026-05-10 11:05:23 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.040 |  |
| 2026-05-10 11:01:23 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | -0.041 |  |
| 2026-05-10 11:03:48 | Kuda Oya (Kirindi Oya) | 2.06 | 🟢 Normal | -0.048 |  |
| 2026-05-10 11:03:36 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.048 |  |
| 2026-05-10 11:05:54 | Glencourse (Kelani Ganga) | 9.68 | 🟢 Normal | -0.059 |  |
| 2026-05-10 11:04:30 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-05-10 11:01:10 | Thanamalwila (Kirindi Oya) | 2.14 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)