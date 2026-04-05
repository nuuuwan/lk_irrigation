# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_02:43:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,325 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 02:43:45 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -72.000 |  |
| 2026-04-06 02:43:44 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -72.000 |  |
| 2026-04-06 02:43:11 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.006 |  |
| 2026-04-06 02:40:58 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.012 |  |
| 2026-04-06 02:34:54 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:25:57 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:25:24 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:17:26 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:16:56 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -72.000 |  |
| 2026-04-06 02:16:55 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | -72.000 |  |
| 2026-04-06 02:16:53 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -72.000 |  |
| 2026-04-06 02:07:58 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-06 02:06:26 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-04-06 02:05:56 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 02:05:55 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:04:58 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:04:47 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-06 02:04:38 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-04-06 02:04:17 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:03:35 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.100 |  |
| 2026-04-06 02:02:27 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:02:09 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:01:55 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-06 02:01:51 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:01:51 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.040 |  |
| 2026-04-06 02:01:19 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.012 |  |
| 2026-04-06 02:01:10 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:01:09 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:00:50 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-06 02:00:49 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2026-04-06 02:00:35 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 02:04:47 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-06 02:00:50 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-06 01:06:36 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-06 02:01:55 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-06 02:07:58 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-06 02:05:56 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 02:34:54 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:01:19 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:02:27 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:02:09 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:01:09 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:01:51 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 01:01:18 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 00:01:54 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:04:58 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:05:55 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:17:26 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:04:17 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:25:57 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:25:24 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:43:11 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.006 |  |
| 2026-04-06 02:06:26 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-04-06 01:02:12 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-04-06 02:04:38 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-04-06 01:00:55 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-06 01:01:33 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-04-06 02:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.012 |  |
| 2026-04-06 02:40:58 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.012 |  |
| 2026-04-06 02:00:35 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-04-06 02:01:51 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.040 |  |
| 2026-04-05 18:02:13 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.050 |  |
| 2026-04-06 02:00:49 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2026-04-06 00:05:48 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.056 |  |
| 2026-04-05 21:08:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.081 |  |
| 2026-04-05 18:02:28 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | -0.088 |  |
| 2026-04-06 02:03:35 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.100 |  |
| 2026-04-06 02:16:56 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -72.000 |  |
| 2026-04-06 02:43:45 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)