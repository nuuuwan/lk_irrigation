# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_20:17:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,844 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 20:17:18 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-26 20:15:12 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.026 |  |
| 2026-04-26 20:12:33 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-26 20:10:49 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-26 20:10:07 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:09:58 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.020 |  |
| 2026-04-26 20:08:53 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-26 20:08:37 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.038 |  |
| 2026-04-26 20:08:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.123 |  |
| 2026-04-26 20:07:21 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:07:12 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:06:44 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:06:39 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:06:23 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-26 20:05:58 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-04-26 20:05:52 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-04-26 20:04:59 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:04:45 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |
| 2026-04-26 20:04:31 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-04-26 20:04:20 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-26 20:03:59 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-26 20:03:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-04-26 20:03:10 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-26 20:03:05 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.159 |  |
| 2026-04-26 20:02:57 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.022 |  |
| 2026-04-26 20:02:45 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:02:43 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-04-26 20:02:28 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:02:17 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:02:09 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:01:59 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-04-26 20:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:01:09 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-26 20:01:07 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 20:01:02 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-04-26 20:00:32 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.060 |  |
| 2026-04-26 19:58:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.123 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 20:05:52 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-04-26 20:03:10 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-26 20:08:53 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-26 20:04:20 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-26 20:03:59 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-26 20:10:49 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-26 20:12:33 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-26 20:17:18 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-26 20:01:07 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 18:00:28 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:02:09 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:07:12 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:10:07 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:04:59 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:02:45 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:02:17 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:02:28 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:07:21 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-26 20:06:39 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:06:09 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-04-26 20:05:58 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-04-26 20:04:31 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-04-26 20:01:09 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-26 20:04:45 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |
| 2026-04-26 20:06:23 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-26 20:01:59 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-04-26 20:01:02 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-04-26 20:09:58 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.020 |  |
| 2026-04-26 20:02:57 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.022 |  |
| 2026-04-26 20:15:12 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.026 |  |
| 2026-04-26 18:03:51 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-04-26 20:02:43 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-04-26 19:01:28 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-04-26 20:03:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-04-26 20:08:37 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.038 |  |
| 2026-04-26 20:00:32 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.060 |  |
| 2026-04-26 20:08:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.123 |  |
| 2026-04-26 20:03:05 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)