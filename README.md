# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_06:42:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,930 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 06:42:33 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.036 |  |
| 2026-05-08 06:17:27 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-08 06:14:01 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-08 06:12:14 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 06:09:00 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.055 |  |
| 2026-05-08 06:08:39 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-08 06:08:22 | Weraganthota (Mahaweli Ganga) | -2.62 | 🟢 Normal | -0.468 |  |
| 2026-05-08 06:06:57 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.019 |  |
| 2026-05-08 06:05:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 1.039 | 🔺 Rising |
| 2026-05-08 06:05:38 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | -0.070 |  |
| 2026-05-08 06:05:20 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-08 06:04:32 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.261 |  |
| 2026-05-08 06:04:24 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.081 |  |
| 2026-05-08 06:04:16 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.062 |  |
| 2026-05-08 06:03:55 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.041 |  |
| 2026-05-08 06:03:54 | Panadugama (Nilwala Ganga) | 5.04 | 🟡 Alert | -0.092 |  |
| 2026-05-08 06:03:54 | Nakkala (Kumbukkan Oya) | 0.19 | 🟢 Normal | -1.114 |  |
| 2026-05-08 06:03:49 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-05-08 06:03:48 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-08 06:03:38 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-08 06:03:30 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | -0.210 |  |
| 2026-05-08 06:03:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-08 06:03:18 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.029 |  |
| 2026-05-08 06:03:15 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-08 06:02:52 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-08 06:02:33 | Katharagama (Menik Ganga) | 0.60 | 🟢 Normal | -0.128 |  |
| 2026-05-08 06:02:31 | Giriulla (Maha Oya) | 2.31 | 🟢 Normal | -0.060 |  |
| 2026-05-08 06:02:15 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-08 06:02:01 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.678 |  |
| 2026-05-08 06:02:01 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-05-08 06:01:44 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-05-08 06:01:32 | Kuda Oya (Kirindi Oya) | 2.20 | 🟢 Normal | -2.103 |  |
| 2026-05-08 06:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-05-08 06:01:28 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 06:01:25 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 06:01:15 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-08 06:00:51 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.167 |  |
| 2026-05-08 06:00:12 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-05-08 05:54:24 | Kuda Oya (Kirindi Oya) | 2.45 | 🟢 Normal | -2.103 |  |
| 2026-05-08 05:50:54 | Panadugama (Nilwala Ganga) | 5.06 | 🟡 Alert | -0.092 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 06:03:54 | Panadugama (Nilwala Ganga) | 5.04 | 🟡 Alert | -0.092 |  |
| 2026-05-08 06:05:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 1.039 | 🔺 Rising |
| 2026-05-08 06:02:01 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-05-08 06:03:49 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-05-08 06:03:38 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-08 06:14:01 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-08 06:03:15 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-08 06:05:20 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-08 06:08:39 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-08 06:02:52 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-08 06:01:25 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 06:03:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-08 06:01:28 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 06:17:27 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-08 06:12:14 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 06:01:15 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-08 06:03:48 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-08 06:02:15 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-07 18:02:03 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-08 06:01:44 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-05-08 06:06:57 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.019 |  |
| 2026-05-08 06:00:12 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-05-08 06:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-05-08 06:03:18 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.029 |  |
| 2026-05-08 06:42:33 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.036 |  |
| 2026-05-08 06:03:55 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.041 |  |
| 2026-05-08 06:09:00 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.055 |  |
| 2026-05-08 06:02:31 | Giriulla (Maha Oya) | 2.31 | 🟢 Normal | -0.060 |  |
| 2026-05-08 06:04:16 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.062 |  |
| 2026-05-08 06:05:38 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | -0.070 |  |
| 2026-05-08 06:04:24 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.081 |  |
| 2026-05-08 06:02:33 | Katharagama (Menik Ganga) | 0.60 | 🟢 Normal | -0.128 |  |
| 2026-05-08 06:00:51 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.167 |  |
| 2026-05-08 06:03:30 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | -0.210 |  |
| 2026-05-08 06:04:32 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.261 |  |
| 2026-05-08 06:08:22 | Weraganthota (Mahaweli Ganga) | -2.62 | 🟢 Normal | -0.468 |  |
| 2026-05-08 06:02:01 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.678 |  |
| 2026-05-08 06:03:54 | Nakkala (Kumbukkan Oya) | 0.19 | 🟢 Normal | -1.114 |  |
| 2026-05-08 06:01:32 | Kuda Oya (Kirindi Oya) | 2.20 | 🟢 Normal | -2.103 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)