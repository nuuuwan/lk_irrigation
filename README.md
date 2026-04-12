# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_16:12:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,184 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 16:12:44 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:11:03 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-12 16:09:30 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-04-12 16:07:07 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:06:43 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.019 |  |
| 2026-04-12 16:06:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:06:27 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-04-12 16:05:01 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-12 16:04:43 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.011 |  |
| 2026-04-12 16:04:35 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:04:34 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.038 |  |
| 2026-04-12 16:04:31 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:04:27 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-12 16:03:33 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 16:03:22 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-12 16:03:19 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:02:47 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:02:47 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:02:47 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:02:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:02:24 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 16:02:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.259 |  |
| 2026-04-12 16:01:49 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-12 16:01:43 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-12 16:01:34 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 16:01:33 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:01:32 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.022 |  |
| 2026-04-12 16:01:13 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-04-12 16:01:11 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 16:01:09 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-12 16:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-04-12 16:00:59 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-12 16:00:19 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.051 |  |
| 2026-04-12 16:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 15:59:29 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:57:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 16:03:22 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-12 16:01:09 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-12 16:01:43 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-12 16:05:01 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-12 16:04:27 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-12 16:03:33 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 16:01:11 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 16:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 16:02:24 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 16:01:34 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 16:11:03 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-12 15:02:04 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:01:33 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:57:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:02:47 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:09:59 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:03:19 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:12:44 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:04:31 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:06:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:02:47 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:02:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:02:47 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:04:35 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:59:29 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:09:30 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-04-12 15:05:49 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-04-12 16:06:27 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-04-12 16:01:49 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-12 16:00:59 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-12 16:04:43 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.011 |  |
| 2026-04-12 15:02:59 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-04-12 16:06:43 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.019 |  |
| 2026-04-12 16:01:13 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-04-12 16:01:32 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.022 |  |
| 2026-04-12 16:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-04-12 16:04:34 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.038 |  |
| 2026-04-12 16:00:19 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.051 |  |
| 2026-04-12 16:02:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.259 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)