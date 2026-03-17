# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--18_05:23:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **100,401 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 05:23:52 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:10:06 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.081 |  |
| 2026-03-18 05:06:35 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-18 05:06:08 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:06:07 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:05:49 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-18 05:05:25 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.088 |  |
| 2026-03-18 05:05:18 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-18 05:04:48 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:04:46 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:04:25 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-18 05:04:23 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-18 05:04:15 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:04:07 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.072 |  |
| 2026-03-18 05:03:55 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:03:54 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:03:48 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:03:22 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:03:02 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:02:29 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:02:26 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-03-18 05:02:17 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:02:13 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.006 |  |
| 2026-03-18 05:01:46 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:01:42 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-18 05:01:41 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.091 |  |
| 2026-03-18 05:01:35 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-18 05:01:09 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:01:08 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:01:08 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:00:50 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-18 05:00:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-18 04:59:56 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 05:04:25 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-18 02:09:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-03-18 04:00:19 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-03-18 05:00:50 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-18 05:01:35 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-18 05:05:49 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-18 05:06:35 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-18 05:05:18 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-18 05:01:42 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-18 05:04:48 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:01:09 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:23:52 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:01:46 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:02:29 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:03:54 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:01:08 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-17 18:04:05 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:03:22 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:04:15 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:01:08 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:06:07 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:03:02 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 03:03:45 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:00:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:02:17 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:06:08 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:03:55 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:03:48 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-17 18:01:54 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:04:46 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-18 04:01:21 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-18 05:02:13 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.006 |  |
| 2026-03-18 05:02:26 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-03-17 21:02:27 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.045 |  |
| 2026-03-18 05:04:07 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.072 |  |
| 2026-03-18 05:10:06 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.081 |  |
| 2026-03-18 05:05:25 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.088 |  |
| 2026-03-18 05:01:41 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)