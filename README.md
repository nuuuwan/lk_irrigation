# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_22:23:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,970 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 22:23:35 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:16:49 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-03-19 22:11:22 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-19 22:07:39 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 22:06:53 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-19 22:05:29 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-03-19 22:05:12 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-03-19 22:05:02 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-03-19 22:04:38 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:04:38 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 22:04:24 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:04:21 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-03-19 22:04:10 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.022 |  |
| 2026-03-19 22:03:38 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-03-19 22:03:34 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:03:03 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:02:38 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-03-19 22:02:30 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.055 |  |
| 2026-03-19 22:02:29 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-19 22:02:28 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.083 |  |
| 2026-03-19 22:02:24 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.041 |  |
| 2026-03-19 22:02:15 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | 0.827 | 🔺 Rising |
| 2026-03-19 22:02:01 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.030 |  |
| 2026-03-19 22:02:00 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:01:50 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-03-19 22:01:43 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-19 22:01:37 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:01:31 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:01:27 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-03-19 22:01:23 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-19 22:01:12 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 22:01:11 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:00:09 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 22:02:15 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | 0.827 | 🔺 Rising |
| 2026-03-19 22:16:49 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-03-19 22:01:27 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-03-19 22:01:43 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-19 22:06:53 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-19 22:01:23 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-19 22:11:22 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-19 22:04:38 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 21:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-19 22:01:12 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 22:07:39 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 22:02:00 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:04:24 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:05 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:00:09 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:23:35 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:03:34 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:01:37 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:01:31 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:04:38 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:03:03 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:01:11 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:12:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-03-19 22:05:29 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-03-19 22:01:50 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-03-19 22:02:29 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-19 22:05:02 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-03-19 22:05:12 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-03-19 22:02:38 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-03-19 22:04:10 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.022 |  |
| 2026-03-19 22:02:01 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.030 |  |
| 2026-03-19 22:03:38 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-03-19 22:02:24 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.041 |  |
| 2026-03-19 22:04:21 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-03-19 22:02:30 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.055 |  |
| 2026-03-19 22:02:28 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.083 |  |
| 2026-03-19 18:02:05 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.128 |  |
| 2026-03-19 21:09:33 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)