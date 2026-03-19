# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_14:10:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,666 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 14:10:32 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 14:10:30 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-19 14:10:11 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 14:07:09 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-19 14:06:46 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-19 14:06:19 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.027 |  |
| 2026-03-19 14:06:12 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-03-19 14:05:48 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-03-19 14:05:10 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-03-19 14:04:56 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 14:04:48 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.062 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 14:01:45 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-03-19 14:06:12 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-03-19 14:02:20 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-03-19 14:05:10 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-03-19 14:02:18 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-19 14:06:46 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-19 14:02:06 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-19 14:02:34 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 14:10:30 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-19 14:01:25 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-19 14:00:23 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 14:01:47 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 14:02:10 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 14:03:38 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 14:04:56 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 14:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-19 14:03:35 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 14:10:11 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:01:54 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 14:02:12 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-19 14:02:19 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-19 14:04:18 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-19 14:07:09 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-19 14:03:28 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 14:02:51 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 14:02:16 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 14:10:32 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 14:02:52 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-03-19 14:04:10 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-03-19 14:05:48 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-03-19 14:03:33 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.020 |  |
| 2026-03-19 14:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-03-19 14:01:30 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.023 |  |
| 2026-03-19 14:06:19 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.027 |  |
| 2026-03-19 14:02:20 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.030 |  |
| 2026-03-19 14:02:39 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-03-19 14:01:41 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.031 |  |
| 2026-03-19 14:04:48 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.062 |  |
| 2026-03-19 14:02:58 | Weraganthota (Mahaweli Ganga) | -2.56 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)