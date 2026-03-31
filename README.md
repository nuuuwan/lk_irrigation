# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_18:28:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **112,555 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 18:28:52 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:21:11 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:21:10 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:20:57 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | -0.071 |  |
| 2026-03-31 18:12:33 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | -0.071 |  |
| 2026-03-31 18:10:24 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-31 18:08:56 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:08:09 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-03-31 18:06:49 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:06:48 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:06:04 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:04:31 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:04:22 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:03:40 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:03:29 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:03:21 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-03-31 18:03:13 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:03:08 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-31 18:03:06 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-03-31 18:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:02:48 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:02:46 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:02:44 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-31 18:02:39 | Giriulla (Maha Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:02:31 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-31 18:02:20 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-03-31 18:02:13 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:02:13 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:01:49 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-03-31 18:01:48 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.090 |  |
| 2026-03-31 18:01:45 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:01:42 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:01:28 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-03-31 18:01:23 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-03-31 18:01:15 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:01:04 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.088 |  |
| 2026-03-31 18:00:40 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.062 |  |
| 2026-03-31 18:00:39 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:00:35 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-31 18:00:27 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-03-31 18:00:26 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.117 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 18:03:06 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-03-31 18:01:28 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-03-31 18:03:08 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-31 18:02:44 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-31 18:10:24 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-31 18:02:13 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:01:15 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:01:42 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:06:48 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:02:39 | Giriulla (Maha Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:02:13 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:04:31 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:01:45 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:08:56 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:03:40 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:04:22 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:03:13 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:06:04 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:02:48 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:02:46 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:06:49 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:03:29 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:28:52 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:00:39 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:02:20 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:01:49 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-03-31 18:00:35 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-31 18:02:31 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-31 18:08:09 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-03-31 18:01:23 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-03-31 18:00:27 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-03-31 18:03:21 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-03-31 18:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-03-31 18:00:40 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.062 |  |
| 2026-03-31 18:20:57 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | -0.071 |  |
| 2026-03-31 18:01:04 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.088 |  |
| 2026-03-31 18:01:48 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.090 |  |
| 2026-03-31 18:00:26 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)