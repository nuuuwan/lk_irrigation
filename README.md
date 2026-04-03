# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_16:28:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,163 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 16:28:05 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-03 16:19:06 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.886 | 🔺 Rising |
| 2026-04-03 16:15:40 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:15:30 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.042 |  |
| 2026-04-03 16:15:29 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.018 |  |
| 2026-04-03 16:14:06 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:11:53 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:11:16 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:10:35 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.038 |  |
| 2026-04-03 16:08:40 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:08:03 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-03 16:07:45 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:07:42 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-03 16:06:58 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-03 16:05:58 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-03 16:05:30 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 16:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-03 16:05:24 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-03 16:05:12 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:05:06 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.088 |  |
| 2026-04-03 16:05:03 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-03 16:05:01 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 16:04:11 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-03 16:03:17 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2026-04-03 16:03:06 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:02:58 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:02:57 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.082 |  |
| 2026-04-03 16:02:48 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 16:02:29 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 16:02:27 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.050 |  |
| 2026-04-03 16:02:17 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 16:02:15 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 16:02:08 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:01:54 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-03 16:01:10 | Thanthirimale (Malwathu Oya) | 3.32 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-03 16:01:04 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.099 |  |
| 2026-04-03 16:00:11 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 16:19:06 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.886 | 🔺 Rising |
| 2026-04-03 16:05:24 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-03 16:04:11 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-03 16:01:10 | Thanthirimale (Malwathu Oya) | 3.32 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-03 16:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-03 16:01:54 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-03 16:28:05 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-03 16:06:58 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-03 16:07:42 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-03 16:08:03 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-03 16:05:01 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 16:02:29 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 16:02:15 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 16:02:17 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 16:05:58 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-03 16:00:11 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 16:02:48 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 16:05:30 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 16:02:08 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:14:06 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:11:16 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:05:12 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:11:53 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:07:45 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:08:40 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:15:40 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:02:58 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:02:31 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 16:03:06 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 15:11:00 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-03 16:05:03 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-03 16:15:29 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.018 |  |
| 2026-04-03 16:03:17 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2026-04-03 16:10:35 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.038 |  |
| 2026-04-03 16:15:30 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.042 |  |
| 2026-04-03 16:02:27 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.050 |  |
| 2026-04-03 16:02:57 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.082 |  |
| 2026-04-03 16:05:06 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.088 |  |
| 2026-04-03 16:01:04 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)