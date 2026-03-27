# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--27_17:17:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **108,944 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 17:17:42 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-03-27 17:15:18 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:13:39 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:13:28 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:10:13 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-03-27 17:09:57 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:08:29 | Rathnapura (Kalu Ganga) | 0.33 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-27 17:05:47 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:05:39 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:05:38 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:05:36 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:05:30 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:05:11 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.039 |  |
| 2026-03-27 17:04:56 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-27 17:04:52 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-03-27 17:04:49 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 17:04:26 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-27 17:04:17 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.019 |  |
| 2026-03-27 17:04:16 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-27 17:03:54 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:03:53 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:03:47 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:03:46 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-27 17:03:09 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:03:09 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 17:02:54 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-27 17:02:35 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:02:31 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-27 17:02:14 | Ellagawa (Kalu Ganga) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:02:10 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.100 |  |
| 2026-03-27 17:02:08 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-27 17:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-03-27 17:02:01 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-03-27 17:01:53 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:01:49 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:01:30 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-27 17:01:29 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:00:54 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:00:43 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:00:41 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 17:02:31 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-27 17:01:30 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-27 17:04:26 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-27 17:08:29 | Rathnapura (Kalu Ganga) | 0.33 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-27 17:04:16 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-27 17:04:49 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 17:03:09 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 17:05:39 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:00:43 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:03:54 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:01:53 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:02:35 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:00:41 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:15:18 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:03:53 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:02:14 | Ellagawa (Kalu Ganga) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:09:57 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:13:39 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:05:47 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:03:47 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:13:28 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:03:09 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:05:38 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:05:30 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:00:54 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:05:36 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:01:49 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-27 17:10:13 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-03-27 17:17:42 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-03-27 17:04:56 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-27 17:04:52 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-03-27 17:03:46 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-27 17:02:08 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-27 17:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-03-27 17:02:54 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-27 17:02:01 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-03-27 17:04:17 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.019 |  |
| 2026-03-27 17:05:11 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.039 |  |
| 2026-03-27 17:02:10 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)