# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_20:02:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,919 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 20:02:15 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-04-25 20:02:12 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:02:06 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.059 |  |
| 2026-04-25 20:01:56 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:01:49 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.022 |  |
| 2026-04-25 20:01:41 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:01:40 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-25 20:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-04-25 20:01:11 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-25 20:01:09 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:00:23 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:43:16 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:30:59 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.007 |  |
| 2026-04-25 19:26:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:23:28 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-25 19:13:59 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:13:48 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-25 19:13:41 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:12:20 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:11:13 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-04-25 19:10:46 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.018 |  |
| 2026-04-25 19:09:43 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 20:01:11 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-25 20:01:40 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-25 19:00:49 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-25 19:07:18 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-25 19:04:29 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 19:05:04 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:00:44 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:01:41 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:03:47 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:01:56 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:02:57 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:02:56 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:02:09 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:12:20 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:00:23 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:04:17 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:43:16 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:02:12 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:07:09 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:13:41 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:01:09 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:26:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-04-25 19:30:59 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.007 |  |
| 2026-04-25 19:11:13 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-04-25 19:07:53 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.009 |  |
| 2026-04-25 19:02:22 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-04-25 19:02:15 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-25 20:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-04-25 19:05:24 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | -0.012 |  |
| 2026-04-25 19:10:46 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.018 |  |
| 2026-04-25 19:09:43 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.018 |  |
| 2026-04-25 19:08:39 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.019 |  |
| 2026-04-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:01:09 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-04-25 20:01:49 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.022 |  |
| 2026-04-25 20:02:15 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-04-25 18:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-04-25 19:02:50 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.056 |  |
| 2026-04-25 20:02:06 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)