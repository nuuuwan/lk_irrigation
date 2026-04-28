# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_18:29:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,539 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 18:29:10 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.058 |  |
| 2026-04-28 18:12:46 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:08:19 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:07:43 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-04-28 18:05:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-04-28 18:05:42 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.049 |  |
| 2026-04-28 18:05:38 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:05:37 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.039 |  |
| 2026-04-28 18:05:27 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-28 18:05:16 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:05:15 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.052 |  |
| 2026-04-28 18:05:12 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:05:02 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.047 |  |
| 2026-04-28 18:05:02 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.097 |  |
| 2026-04-28 18:04:58 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 18:04:47 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.041 |  |
| 2026-04-28 18:04:12 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-04-28 18:03:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:03:42 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:03:17 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-04-28 18:03:08 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:02:58 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-28 18:02:58 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:02:49 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.090 |  |
| 2026-04-28 18:02:34 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | -0.044 |  |
| 2026-04-28 18:02:17 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:02:13 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:02:12 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-04-28 18:02:09 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.100 |  |
| 2026-04-28 18:02:03 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 18:01:59 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:01:44 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.132 |  |
| 2026-04-28 18:01:43 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-04-28 18:01:23 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-28 18:01:23 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-28 18:00:33 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-28 18:00:16 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:00:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 17:59:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 18:02:58 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-28 18:00:33 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-28 18:01:23 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-28 18:04:58 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 17:59:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-28 18:01:23 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-28 17:02:52 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 18:02:03 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 18:00:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:01:44 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:03:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:05:16 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:02:13 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:02:58 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:03:42 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:05:12 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:03:08 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:02:17 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:05:38 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:12:46 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:00:16 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:05:27 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-28 18:04:12 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-04-28 18:07:43 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-04-28 18:02:12 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-04-28 18:03:17 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-04-28 18:01:43 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-04-28 18:05:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-04-28 18:05:37 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.039 |  |
| 2026-04-28 18:04:47 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.041 |  |
| 2026-04-28 18:02:34 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | -0.044 |  |
| 2026-04-28 18:05:02 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.047 |  |
| 2026-04-28 18:05:42 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.049 |  |
| 2026-04-28 18:05:15 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.052 |  |
| 2026-04-28 18:29:10 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.058 |  |
| 2026-04-28 18:02:49 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.090 |  |
| 2026-04-28 18:05:02 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.097 |  |
| 2026-04-28 18:02:09 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.100 |  |
| 2026-04-28 18:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)