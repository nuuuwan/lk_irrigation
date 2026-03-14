# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_14:18:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,190 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 14:18:19 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.025 |  |
| 2026-03-14 14:16:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-03-14 14:15:39 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.016 |  |
| 2026-03-14 14:11:21 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:08:56 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:08:27 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.049 |  |
| 2026-03-14 14:08:16 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:08:01 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:07:11 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-14 14:06:49 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.030 |  |
| 2026-03-14 14:06:49 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-03-14 14:06:30 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-03-14 14:05:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-14 14:05:33 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-14 14:04:47 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-03-14 14:04:04 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:04:01 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:03:38 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-03-14 14:03:32 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-03-14 14:03:32 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:03:18 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-14 14:03:07 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:02:50 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.041 |  |
| 2026-03-14 14:02:46 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-03-14 14:02:39 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:02:34 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:02:28 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-03-14 14:02:25 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:02:24 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-14 14:02:21 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 14:02:11 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-14 14:02:08 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 14:03:18 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-14 14:02:24 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-14 14:05:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-14 14:16:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-03-14 14:05:33 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-14 14:07:11 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-14 14:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-14 14:02:21 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 14:08:01 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:00:14 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:00:51 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:02:25 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:04:01 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:07:57 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:02:11 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:04:04 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:08:16 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:03:32 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:01:25 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:02:34 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:08:56 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:02:39 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:03:07 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:11:21 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-14 14:06:30 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-03-14 14:03:38 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-03-14 14:15:39 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.016 |  |
| 2026-03-14 14:02:46 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-03-14 14:02:28 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-03-14 14:04:47 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-03-14 14:18:19 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.025 |  |
| 2026-03-14 14:01:44 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.025 |  |
| 2026-03-14 14:06:49 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-03-14 14:06:49 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.030 |  |
| 2026-03-14 14:03:32 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-03-14 14:02:08 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.031 |  |
| 2026-03-14 14:02:50 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.041 |  |
| 2026-03-14 14:08:27 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.049 |  |
| 2026-03-14 14:01:16 | Weraganthota (Mahaweli Ganga) | -2.58 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)