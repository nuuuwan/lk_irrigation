# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_22:20:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,709 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 22:20:02 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.017 |  |
| 2026-03-12 22:16:26 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-12 22:12:15 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:09:03 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-12 22:08:25 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.036 |  |
| 2026-03-12 22:07:09 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.029 |  |
| 2026-03-12 22:06:43 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-12 22:06:21 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:05:28 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-12 22:05:24 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:05:01 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-12 22:04:48 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-03-12 22:04:42 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-03-12 22:04:36 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:04:30 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.039 |  |
| 2026-03-12 22:03:29 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:03:22 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:02:47 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:02:37 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-12 22:02:26 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-12 22:02:22 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:02:16 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.040 |  |
| 2026-03-12 22:02:13 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.070 |  |
| 2026-03-12 22:02:08 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:01:59 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-03-12 22:01:57 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:01:57 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:01:34 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:01:32 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:00:54 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:00:18 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:00:15 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 22:04:42 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-03-12 22:16:26 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-12 22:04:48 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-03-12 22:09:03 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-12 22:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-12 22:06:43 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-12 22:05:28 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-12 22:01:59 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-03-12 22:00:18 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:01:32 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:00:54 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:01:57 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:02:37 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:00:15 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:05:52 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:03:22 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:01:34 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:12:15 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:06:21 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:05:24 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:02:04 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:04:36 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:02:22 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:02:08 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:02:47 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:01:57 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:03:01 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:03:29 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:05:01 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-12 22:02:26 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-12 22:20:02 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.017 |  |
| 2026-03-12 22:07:09 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.029 |  |
| 2026-03-12 22:08:25 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.036 |  |
| 2026-03-12 22:04:30 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.039 |  |
| 2026-03-12 22:02:16 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.040 |  |
| 2026-03-12 21:06:18 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.048 |  |
| 2026-03-12 22:02:13 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.070 |  |
| 2026-03-12 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)