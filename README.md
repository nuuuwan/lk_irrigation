# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_02:59:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,368 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 02:59:33 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.014 |  |
| 2026-04-24 02:25:54 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-24 02:19:43 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-04-24 02:17:40 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 02:16:14 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-24 02:15:30 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-24 02:10:28 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.028 |  |
| 2026-04-24 02:10:20 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | -0.019 |  |
| 2026-04-24 02:08:03 | Katharagama (Menik Ganga) | 1.59 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-24 02:07:24 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 02:06:39 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-24 02:06:29 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.086 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 02:01:17 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-04-24 02:00:56 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-24 02:08:03 | Katharagama (Menik Ganga) | 1.59 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-24 01:00:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-24 02:15:30 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-24 02:06:39 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-24 02:05:14 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-24 02:04:52 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-24 02:25:54 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-24 02:01:52 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-24 02:03:26 | Ellagawa (Kalu Ganga) | 5.47 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-24 02:01:45 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-24 02:16:14 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-23 18:03:04 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 02:02:09 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 02:07:24 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 02:05:36 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-24 02:17:40 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 02:02:58 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-24 02:02:02 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 01:02:56 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-04-24 02:01:25 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.005 |  |
| 2026-04-24 02:19:43 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-04-23 18:03:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-24 02:59:33 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.014 |  |
| 2026-04-24 02:10:20 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | -0.019 |  |
| 2026-04-24 02:02:06 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.019 |  |
| 2026-04-24 02:05:55 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-04-24 02:03:32 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.021 |  |
| 2026-04-24 02:01:08 | Kuda Oya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.026 |  |
| 2026-04-24 02:10:28 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.028 |  |
| 2026-04-24 02:04:16 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.040 |  |
| 2026-04-24 02:01:29 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.040 |  |
| 2026-04-24 02:02:31 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.059 |  |
| 2026-04-24 02:01:11 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | -0.079 |  |
| 2026-04-24 02:06:29 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.086 |  |
| 2026-04-24 02:03:35 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.090 |  |
| 2026-04-24 02:02:23 | Thanamalwila (Kirindi Oya) | 2.19 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)