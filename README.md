# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--23_20:13:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **105,466 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 20:13:55 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:13:22 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.019 |  |
| 2026-03-23 20:13:02 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-03-23 20:10:14 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-23 20:09:28 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:09:23 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-03-23 20:08:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.018 |  |
| 2026-03-23 20:08:00 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:06:57 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-03-23 20:05:39 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:05:38 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 20:04:37 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:04:34 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:04:33 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:04:30 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.063 |  |
| 2026-03-23 20:04:27 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.056 |  |
| 2026-03-23 20:04:18 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.059 |  |
| 2026-03-23 20:03:38 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:03:18 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:03:05 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-23 20:02:49 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:02:49 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:02:43 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 20:02:31 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 20:02:24 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:02:24 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:02:15 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:02:14 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:01:40 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:01:37 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:01:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.097 |  |
| 2026-03-23 20:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:00:16 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:31:20 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 20:03:05 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-23 20:02:31 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 20:02:43 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 20:05:38 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 20:10:14 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-23 20:00:16 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:02:49 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:31:20 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:01:37 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:09:28 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:01:40 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:00:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:02:49 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:03:18 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:05:39 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:13:55 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:02:15 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:41 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:02:24 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:04:33 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:08:00 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:02:24 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:04:34 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:03:38 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:04:37 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:02:14 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-23 20:13:02 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-03-23 20:06:57 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:02:17 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-03-23 20:08:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.018 |  |
| 2026-03-23 20:09:23 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-03-23 20:13:22 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.019 |  |
| 2026-03-23 20:04:27 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.056 |  |
| 2026-03-23 20:04:18 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.059 |  |
| 2026-03-23 19:10:20 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.061 |  |
| 2026-03-23 20:04:30 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.063 |  |
| 2026-03-23 20:01:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.097 |  |
| 2026-03-23 18:00:42 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)