# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_10:16:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,507 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 10:16:39 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:10:31 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:08:55 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-19 10:08:35 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-03-19 10:08:22 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-19 10:08:12 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 10:08:02 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2026-03-19 10:07:10 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.057 |  |
| 2026-03-19 10:07:08 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.088 |  |
| 2026-03-19 10:06:37 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-19 10:06:35 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:06:12 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-03-19 10:05:51 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:05:00 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:04:54 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:04:43 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-03-19 10:03:56 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 10:03:43 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-03-19 10:03:43 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-19 10:03:41 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:03:18 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 10:03:16 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.108 |  |
| 2026-03-19 10:02:44 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:02:43 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:02:32 | Kithulgala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.188 |  |
| 2026-03-19 10:02:26 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 10:02:14 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.072 |  |
| 2026-03-19 10:02:06 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:02:01 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:01:57 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 10:01:56 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-19 10:01:18 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:00:54 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:00:48 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:00:44 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:00:37 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:00:31 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:00:15 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.103 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 10:00:15 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-03-19 10:04:43 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-03-19 10:08:22 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-19 10:06:37 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-19 10:08:35 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-03-19 10:03:56 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 10:03:43 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-19 10:08:55 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-19 10:02:26 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 10:08:12 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 10:03:18 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 10:01:57 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 10:02:01 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:01:18 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:00:37 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:16:39 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:03:16 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:00:44 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:02:06 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:05:00 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:06:35 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:05:51 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:10:31 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:00:48 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:02:44 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:03:41 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:04:54 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:00:31 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:02:43 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:00:54 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:06:12 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-03-19 10:08:02 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2026-03-19 10:01:56 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-19 10:03:43 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-03-19 10:07:10 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.057 |  |
| 2026-03-19 10:02:14 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.072 |  |
| 2026-03-19 10:07:08 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.088 |  |
| 2026-03-19 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.108 |  |
| 2026-03-19 10:02:32 | Kithulgala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.188 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)