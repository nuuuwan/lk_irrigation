# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_12:20:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,062 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 12:20:38 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.030 |  |
| 2026-05-09 12:12:27 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-09 12:12:23 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.133 |  |
| 2026-05-09 12:10:17 | Galgamuwa (Mee Oya) | 2.60 | 🟢 Normal | -0.088 |  |
| 2026-05-09 12:09:41 | Rathnapura (Kalu Ganga) | 2.94 | 🟢 Normal | -0.232 |  |
| 2026-05-09 12:09:08 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | -0.047 |  |
| 2026-05-09 12:08:34 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-05-09 12:08:34 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.019 |  |
| 2026-05-09 12:08:04 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-09 12:06:58 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.035 |  |
| 2026-05-09 12:06:22 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-09 12:06:14 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-05-09 12:04:54 | Thanamalwila (Kirindi Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-09 12:04:33 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.071 |  |
| 2026-05-09 12:04:10 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-09 12:04:03 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-05-09 12:04:02 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.042 |  |
| 2026-05-09 12:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.75 | 🟢 Normal | -0.042 |  |
| 2026-05-09 12:03:52 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 12:03:46 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 12:03:39 | Katharagama (Menik Ganga) | 2.38 | 🟢 Normal | -0.043 |  |
| 2026-05-09 12:03:35 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | -0.060 |  |
| 2026-05-09 12:03:23 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.041 |  |
| 2026-05-09 12:03:19 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.059 |  |
| 2026-05-09 12:02:53 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.060 |  |
| 2026-05-09 12:02:47 | Moragaswewa (Deduru Oya) | 3.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-09 12:02:34 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-09 12:02:33 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 12:02:18 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-09 12:02:17 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 12:02:05 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.000 |  |
| 2026-05-09 12:01:58 | Kuda Oya (Kirindi Oya) | 2.61 | 🟢 Normal | -0.110 |  |
| 2026-05-09 12:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.041 |  |
| 2026-05-09 12:01:38 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-09 12:01:31 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2026-05-09 12:00:50 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-09 12:00:26 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-09 12:00:25 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 12:04:10 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-09 12:02:47 | Moragaswewa (Deduru Oya) | 3.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-09 12:02:34 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-09 12:12:27 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-09 12:03:52 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 12:02:17 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 12:02:33 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 12:08:04 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-09 12:03:46 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 12:00:26 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-09 12:02:05 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.000 |  |
| 2026-05-09 12:04:54 | Thanamalwila (Kirindi Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-09 12:04:03 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-05-09 12:06:22 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-09 12:01:38 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-09 12:02:18 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-09 12:00:25 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-05-09 12:06:14 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-05-09 12:08:34 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.019 |  |
| 2026-05-09 12:08:34 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-05-09 10:59:32 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | -0.020 |  |
| 2026-05-09 12:00:50 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-09 12:01:31 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2026-05-09 12:20:38 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.030 |  |
| 2026-05-09 12:06:58 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.035 |  |
| 2026-05-09 12:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.041 |  |
| 2026-05-09 12:03:23 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.041 |  |
| 2026-05-09 12:04:02 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.042 |  |
| 2026-05-09 12:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.75 | 🟢 Normal | -0.042 |  |
| 2026-05-09 12:03:39 | Katharagama (Menik Ganga) | 2.38 | 🟢 Normal | -0.043 |  |
| 2026-05-09 12:09:08 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | -0.047 |  |
| 2026-05-09 12:03:19 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.059 |  |
| 2026-05-09 12:02:53 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.060 |  |
| 2026-05-09 12:03:35 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | -0.060 |  |
| 2026-05-09 12:04:33 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.071 |  |
| 2026-05-09 12:10:17 | Galgamuwa (Mee Oya) | 2.60 | 🟢 Normal | -0.088 |  |
| 2026-05-09 12:01:58 | Kuda Oya (Kirindi Oya) | 2.61 | 🟢 Normal | -0.110 |  |
| 2026-05-09 12:12:23 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.133 |  |
| 2026-05-09 12:09:41 | Rathnapura (Kalu Ganga) | 2.94 | 🟢 Normal | -0.232 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)