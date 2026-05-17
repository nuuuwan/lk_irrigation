# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_07:28:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,079 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 07:28:52 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-17 07:13:06 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.128 |  |
| 2026-05-17 07:12:55 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:11:29 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 07:09:28 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-05-17 07:08:48 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 07:08:18 | Magura (Kalu Ganga) | 3.24 | 🟢 Normal | -0.009 |  |
| 2026-05-17 07:06:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.81 | 🟠 Minor Flood | -0.047 |  |
| 2026-05-17 07:06:49 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:06:40 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:06:24 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:06:10 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:05:35 | Moragaswewa (Deduru Oya) | 1.55 | 🟢 Normal | -0.056 |  |
| 2026-05-17 07:05:16 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 07:04:51 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-17 07:04:39 | Thanthirimale (Malwathu Oya) | 3.72 | 🟢 Normal | -0.006 |  |
| 2026-05-17 07:04:21 | Galgamuwa (Mee Oya) | 1.86 | 🟢 Normal | -0.019 |  |
| 2026-05-17 07:04:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.088 |  |
| 2026-05-17 07:03:55 | Rathnapura (Kalu Ganga) | 3.42 | 🟢 Normal | -0.076 |  |
| 2026-05-17 07:03:54 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | -0.054 |  |
| 2026-05-17 07:03:54 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 07:03:52 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:03:47 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:03:33 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-17 07:03:14 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.099 |  |
| 2026-05-17 07:02:55 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.005 |  |
| 2026-05-17 07:02:44 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:02:20 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:02:14 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.041 |  |
| 2026-05-17 07:02:10 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:01:32 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-17 07:01:32 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | -0.042 |  |
| 2026-05-17 07:01:27 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.072 |  |
| 2026-05-17 07:01:07 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-05-17 07:01:06 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 07:00:37 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-05-17 07:00:35 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:00:31 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 07:06:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.81 | 🟠 Minor Flood | -0.047 |  |
| 2026-05-17 07:03:33 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-17 07:04:51 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-17 07:01:06 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 07:05:16 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 07:03:54 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 07:08:48 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 07:11:29 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 07:28:52 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-17 07:00:35 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:00:31 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:06:10 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:03:47 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:06:40 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:06:49 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:02:44 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:03:52 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:02:20 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:06:24 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:12:55 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:01:01 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:02:10 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 07:02:55 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.005 |  |
| 2026-05-17 07:04:39 | Thanthirimale (Malwathu Oya) | 3.72 | 🟢 Normal | -0.006 |  |
| 2026-05-17 07:08:18 | Magura (Kalu Ganga) | 3.24 | 🟢 Normal | -0.009 |  |
| 2026-05-17 07:01:32 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-17 07:09:28 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-05-17 07:04:21 | Galgamuwa (Mee Oya) | 1.86 | 🟢 Normal | -0.019 |  |
| 2026-05-17 07:01:07 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-05-17 07:00:37 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-05-17 07:02:14 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.041 |  |
| 2026-05-17 07:01:32 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | -0.042 |  |
| 2026-05-17 07:03:54 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | -0.054 |  |
| 2026-05-17 07:05:35 | Moragaswewa (Deduru Oya) | 1.55 | 🟢 Normal | -0.056 |  |
| 2026-05-17 07:01:27 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.072 |  |
| 2026-05-17 07:03:55 | Rathnapura (Kalu Ganga) | 3.42 | 🟢 Normal | -0.076 |  |
| 2026-05-17 07:04:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.088 |  |
| 2026-05-17 07:03:14 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.099 |  |
| 2026-05-17 07:13:06 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)