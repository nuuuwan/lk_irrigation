# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--25_20:18:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **107,246 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 20:18:05 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:16:44 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:10:51 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:09:22 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:09:19 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-25 20:08:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-03-25 20:07:24 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:07:24 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-25 20:06:57 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:06:46 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-25 20:06:28 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:06:27 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:06:27 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | -0.019 |  |
| 2026-03-25 20:05:59 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:05:17 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-03-25 20:04:19 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:04:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2026-03-25 20:04:09 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:04:06 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-03-25 20:04:04 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-25 20:03:54 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:03:41 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:03:40 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-03-25 20:03:39 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:03:07 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:02:53 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:02:43 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:02:41 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:02:37 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-25 20:02:28 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:01:56 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:01:39 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:01:35 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:01:17 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-25 20:01:13 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 20:01:08 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 20:02:37 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-25 20:01:17 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-25 20:07:24 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-25 20:09:19 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-25 20:01:13 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 20:01:08 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:02:43 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:09:22 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:03:39 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:01:39 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:06:28 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 18:00:29 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:18:05 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:01:35 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:04:09 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:04:19 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:03:54 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:02:53 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:10:51 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:06:57 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:03:07 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:02:28 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:02:41 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:03:41 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-25 18:02:01 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:16:44 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:07:24 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:01:56 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:05:59 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 20:05:17 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-03-25 20:04:04 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-25 20:03:40 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-03-25 20:06:46 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-25 20:04:06 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-03-25 20:08:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-03-25 20:06:27 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | -0.019 |  |
| 2026-03-25 18:01:39 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.060 |  |
| 2026-03-25 20:04:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2026-03-25 19:07:18 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)