# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_22:16:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,864 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 22:16:13 | Horowpothana (Yan Oya) | 2.97 | 🟢 Normal | -0.008 |  |
| 2026-05-15 22:16:01 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-15 22:15:04 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:13:51 | Panadugama (Nilwala Ganga) | 3.91 | 🟢 Normal | -0.062 |  |
| 2026-05-15 22:12:18 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | -0.061 |  |
| 2026-05-15 22:10:31 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:10:26 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 22:07:48 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:07:43 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:06:22 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:05:59 | Badalgama (Maha Oya) | 3.87 | 🟢 Normal | -0.020 |  |
| 2026-05-15 22:05:46 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.005 |  |
| 2026-05-15 22:04:54 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.021 |  |
| 2026-05-15 22:04:51 | Moragaswewa (Deduru Oya) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-05-15 22:03:56 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-15 22:03:56 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:03:48 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-15 22:03:39 | Giriulla (Maha Oya) | 2.84 | 🟢 Normal | -0.020 |  |
| 2026-05-15 22:03:38 | Magura (Kalu Ganga) | 4.13 | 🟡 Alert | -0.031 |  |
| 2026-05-15 22:03:36 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:03:29 | Hanwella (Kelani Ganga) | 4.64 | 🟢 Normal | -0.124 |  |
| 2026-05-15 22:03:05 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:02:54 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-05-15 22:02:49 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.03 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-05-15 22:02:47 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:02:20 | Dunamale (Aththanagalu Oya) | 4.62 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-15 22:02:12 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.163 |  |
| 2026-05-15 22:02:03 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:01:32 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:01:24 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-05-15 22:01:22 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-15 22:01:17 | Ellagawa (Kalu Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:01:07 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:00:16 | Nawalapitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 22:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.03 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-05-15 22:02:20 | Dunamale (Aththanagalu Oya) | 4.62 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-15 22:03:38 | Magura (Kalu Ganga) | 4.13 | 🟡 Alert | -0.031 |  |
| 2026-05-15 22:03:48 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-15 22:03:56 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-15 18:03:02 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 22:10:26 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 22:00:16 | Nawalapitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-15 22:16:01 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-15 18:01:07 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:01:07 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:10:31 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:15:04 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:02:03 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:03:56 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:01:17 | Ellagawa (Kalu Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:07:43 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:07:48 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:03:05 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:02:47 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:06:22 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:01:32 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:34 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:03:36 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:02:49 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-15 22:05:46 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.005 |  |
| 2026-05-15 22:16:13 | Horowpothana (Yan Oya) | 2.97 | 🟢 Normal | -0.008 |  |
| 2026-05-15 22:01:22 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-15 22:04:51 | Moragaswewa (Deduru Oya) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-05-15 22:01:24 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-05-15 22:03:39 | Giriulla (Maha Oya) | 2.84 | 🟢 Normal | -0.020 |  |
| 2026-05-15 22:02:54 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-05-15 22:05:59 | Badalgama (Maha Oya) | 3.87 | 🟢 Normal | -0.020 |  |
| 2026-05-15 22:04:54 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.021 |  |
| 2026-05-15 21:05:35 | Baddegama (Gin Ganga) | 3.24 | 🟢 Normal | -0.021 |  |
| 2026-05-15 22:12:18 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | -0.061 |  |
| 2026-05-15 22:13:51 | Panadugama (Nilwala Ganga) | 3.91 | 🟢 Normal | -0.062 |  |
| 2026-05-15 22:03:29 | Hanwella (Kelani Ganga) | 4.64 | 🟢 Normal | -0.124 |  |
| 2026-05-15 22:02:12 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)