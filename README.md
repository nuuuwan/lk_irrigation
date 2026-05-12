# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_08:21:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,617 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 08:21:51 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.079 |  |
| 2026-05-12 08:17:27 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.028 |  |
| 2026-05-12 08:13:11 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.019 |  |
| 2026-05-12 08:10:21 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-12 08:09:11 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.018 |  |
| 2026-05-12 08:08:52 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-05-12 08:08:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 08:08:10 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.029 |  |
| 2026-05-12 08:07:08 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.055 |  |
| 2026-05-12 08:06:14 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:06:09 | Thanthirimale (Malwathu Oya) | 3.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 08:05:51 | Katharagama (Menik Ganga) | 2.15 | 🟢 Normal | -0.038 |  |
| 2026-05-12 08:05:36 | Thanamalwila (Kirindi Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-05-12 08:05:31 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:04:59 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:04:54 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 08:04:54 | Moragaswewa (Deduru Oya) | 2.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 08:04:48 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.055 |  |
| 2026-05-12 08:04:42 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-12 08:04:38 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.137 |  |
| 2026-05-12 08:04:33 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:04:26 | Dunamale (Aththanagalu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-12 08:03:47 | Hanwella (Kelani Ganga) | 2.15 | 🟢 Normal | -0.031 |  |
| 2026-05-12 08:03:29 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-05-12 08:03:25 | Kuda Oya (Kirindi Oya) | 2.08 | 🟢 Normal | -0.074 |  |
| 2026-05-12 08:03:23 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-12 08:03:13 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 08:03:00 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:02:58 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:02:52 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | -0.111 |  |
| 2026-05-12 08:02:49 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-12 08:02:15 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-12 08:02:03 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-05-12 08:02:01 | Wellawaya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.060 |  |
| 2026-05-12 08:01:57 | Ellagawa (Kalu Ganga) | 5.86 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:01:42 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:01:14 | Galgamuwa (Mee Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-05-12 08:00:31 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-12 07:43:43 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.079 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 06:02:26 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-12 08:10:21 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-12 08:00:31 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-12 08:02:15 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-12 08:06:09 | Thanthirimale (Malwathu Oya) | 3.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 08:04:54 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 08:04:54 | Moragaswewa (Deduru Oya) | 2.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 08:08:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 08:03:13 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 08:04:42 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-12 08:02:58 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:03:00 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:06:14 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:01:57 | Ellagawa (Kalu Ganga) | 5.86 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:04:59 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:04:33 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:05:31 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:01:42 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-12 08:04:26 | Dunamale (Aththanagalu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-12 08:05:36 | Thanamalwila (Kirindi Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-05-12 08:03:23 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-12 08:02:49 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-12 08:01:14 | Galgamuwa (Mee Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-05-12 08:09:11 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.018 |  |
| 2026-05-12 08:03:29 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-05-12 08:13:11 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.019 |  |
| 2026-05-12 08:17:27 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.028 |  |
| 2026-05-12 08:08:10 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.029 |  |
| 2026-05-12 08:02:03 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-05-12 08:03:47 | Hanwella (Kelani Ganga) | 2.15 | 🟢 Normal | -0.031 |  |
| 2026-05-12 08:05:51 | Katharagama (Menik Ganga) | 2.15 | 🟢 Normal | -0.038 |  |
| 2026-05-12 08:08:52 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-05-12 08:04:48 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.055 |  |
| 2026-05-12 08:07:08 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.055 |  |
| 2026-05-12 08:02:01 | Wellawaya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.060 |  |
| 2026-05-12 08:03:25 | Kuda Oya (Kirindi Oya) | 2.08 | 🟢 Normal | -0.074 |  |
| 2026-05-12 08:21:51 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.079 |  |
| 2026-05-12 08:02:52 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | -0.111 |  |
| 2026-05-12 08:04:38 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)