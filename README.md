# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_18:12:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,566 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 18:12:07 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:10:22 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.047 |  |
| 2026-03-12 18:09:11 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:08:42 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-03-12 18:08:13 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:07:52 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:07:17 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.012 |  |
| 2026-03-12 18:06:22 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-03-12 18:05:52 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:05:49 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-03-12 18:05:39 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-12 18:05:26 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:04:48 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:04:36 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:04:35 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:04:34 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-03-12 18:04:26 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:04:23 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:04:16 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:04:09 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:04:04 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:03:24 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | -0.075 |  |
| 2026-03-12 18:03:16 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-12 18:03:14 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-03-12 18:03:01 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:02:56 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.041 |  |
| 2026-03-12 18:02:49 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:02:44 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:02:39 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-12 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.083 |  |
| 2026-03-12 18:02:01 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:01:57 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:01:54 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:01:51 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-12 18:01:27 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-12 18:01:25 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:01:17 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:01:16 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-12 18:00:30 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.679 |  |
| 2026-03-12 17:59:35 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.679 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 18:04:34 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-03-12 18:01:16 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-12 18:02:39 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-12 18:01:27 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-12 18:05:39 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-12 18:00:30 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:01:25 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:01:54 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:02:01 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:04:09 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:08:13 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:05:52 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:07:52 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:03:14 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:12:07 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:09:11 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:04:35 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:05:26 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:04:23 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:04:48 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:04:26 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:02:49 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:04:36 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:03:01 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:01:17 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:01:57 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:02:44 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:06:22 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-03-12 18:08:42 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-03-12 18:03:16 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-12 18:01:51 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-12 18:07:17 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.012 |  |
| 2026-03-12 18:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-03-12 18:05:49 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-03-12 18:02:56 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.041 |  |
| 2026-03-12 18:10:22 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.047 |  |
| 2026-03-12 18:03:24 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | -0.075 |  |
| 2026-03-12 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.083 |  |
| 2026-03-12 18:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.679 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)