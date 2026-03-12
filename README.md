# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_21:12:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,675 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 21:12:42 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-03-12 21:11:25 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-03-12 21:09:40 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-12 21:09:24 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 21:07:33 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:07:20 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.024 |  |
| 2026-03-12 21:06:49 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 21:06:41 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:06:20 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-12 21:06:18 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.048 |  |
| 2026-03-12 21:06:02 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.269 |  |
| 2026-03-12 21:05:23 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:04:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:04:50 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-12 21:04:18 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-03-12 21:04:04 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.010 |  |
| 2026-03-12 21:03:59 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-03-12 21:03:41 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:03:19 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:02:43 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-03-12 21:02:41 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:02:18 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:02:17 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.040 |  |
| 2026-03-12 21:02:17 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:02:16 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:02:07 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-12 21:02:07 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-03-12 21:02:04 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:01:51 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:01:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:01:30 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:00:16 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:00:13 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 21:12:42 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-03-12 21:11:25 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-03-12 21:02:43 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-03-12 21:09:40 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-12 21:02:07 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-12 21:06:49 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 21:09:24 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 21:06:20 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-12 21:00:16 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:05:23 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:01:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:03:41 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:00:13 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:05:52 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:07:33 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:06:41 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:02:04 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:03:19 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:02:17 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:01:51 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:02:41 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:02:18 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 20:15:12 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:03:01 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:01:30 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:02:16 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:04:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-12 21:04:18 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-03-12 21:04:50 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-12 21:03:59 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-03-12 21:04:04 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.010 |  |
| 2026-03-12 20:02:45 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.023 |  |
| 2026-03-12 21:07:20 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.024 |  |
| 2026-03-12 21:02:07 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-03-12 21:02:17 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.040 |  |
| 2026-03-12 21:06:18 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.048 |  |
| 2026-03-12 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.083 |  |
| 2026-03-12 21:06:02 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.269 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)