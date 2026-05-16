# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_03:38:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,934 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 03:38:47 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.013 |  |
| 2026-05-17 03:19:46 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 03:17:26 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.017 |  |
| 2026-05-17 03:16:56 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.060 |  |
| 2026-05-17 03:14:47 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-17 03:13:52 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-17 03:12:04 | Baddegama (Gin Ganga) | 2.47 | 🟢 Normal | -72.000 |  |
| 2026-05-17 03:12:03 | Baddegama (Gin Ganga) | 2.49 | 🟢 Normal | -72.000 |  |
| 2026-05-17 03:09:34 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-17 03:08:26 | Putupaula (Kalu Ganga) | 2.83 | 🟢 Normal | -0.010 |  |
| 2026-05-17 03:08:08 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.071 |  |
| 2026-05-17 03:07:23 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 00:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-17 02:02:59 | Dunamale (Aththanagalu Oya) | 3.39 | 🟡 Alert | -0.026 |  |
| 2026-05-17 03:09:34 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-17 03:01:07 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-17 03:02:25 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-16 18:01:12 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 03:04:47 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-17 03:14:47 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-17 02:03:39 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 02:07:10 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.003 |  |
| 2026-05-17 03:02:53 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-17 03:06:09 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-17 03:05:46 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 03:13:52 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-17 03:04:27 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | 0.000 |  |
| 2026-05-17 03:19:46 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 03:07:23 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-17 03:04:38 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 03:01:07 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-17 03:02:20 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 03:04:22 | Ellagawa (Kalu Ganga) | 8.04 | 🟢 Normal | -0.010 |  |
| 2026-05-17 03:02:57 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-05-17 03:02:35 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-05-17 02:02:08 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | -0.010 |  |
| 2026-05-17 03:02:14 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-17 03:08:26 | Putupaula (Kalu Ganga) | 2.83 | 🟢 Normal | -0.010 |  |
| 2026-05-17 03:38:47 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.013 |  |
| 2026-05-17 03:17:26 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.017 |  |
| 2026-05-17 03:01:58 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-05-16 18:01:55 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | -0.030 |  |
| 2026-05-17 03:05:05 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.040 |  |
| 2026-05-17 03:05:10 | Magura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.046 |  |
| 2026-05-16 18:04:15 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-05-17 03:16:56 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.060 |  |
| 2026-05-17 03:08:08 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.071 |  |
| 2026-05-17 03:02:44 | Rathnapura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.084 |  |
| 2026-05-17 03:03:47 | Moragaswewa (Deduru Oya) | 2.13 | 🟢 Normal | -0.108 |  |
| 2026-05-17 03:04:15 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.131 |  |
| 2026-05-17 03:12:04 | Baddegama (Gin Ganga) | 2.47 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)