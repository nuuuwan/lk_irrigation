# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_08:14:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,586 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 08:14:59 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:14:34 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-04-24 08:12:26 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | -0.064 |  |
| 2026-04-24 08:09:37 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.121 |  |
| 2026-04-24 08:09:34 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.019 |  |
| 2026-04-24 08:09:14 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:08:39 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | -0.027 |  |
| 2026-04-24 08:08:37 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.028 |  |
| 2026-04-24 08:07:47 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-04-24 08:06:29 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:06:29 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-04-24 08:06:28 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.037 |  |
| 2026-04-24 08:06:07 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.031 |  |
| 2026-04-24 08:05:35 | Katharagama (Menik Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:05:28 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-24 08:05:16 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:05:15 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.056 |  |
| 2026-04-24 08:04:47 | Katharagama (Menik Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:04:17 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:03:42 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.086 |  |
| 2026-04-24 08:03:28 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.020 |  |
| 2026-04-24 08:03:21 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:03:08 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:02:57 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-24 08:02:54 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-24 08:02:51 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-24 08:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.029 |  |
| 2026-04-24 08:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | -0.050 |  |
| 2026-04-24 08:02:20 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.049 |  |
| 2026-04-24 08:02:13 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.021 |  |
| 2026-04-24 08:02:09 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-04-24 08:01:48 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-24 08:01:42 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-24 08:01:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:01:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-04-24 08:01:13 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-24 08:01:12 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-04-24 08:00:58 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.035 |  |
| 2026-04-24 08:00:38 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.089 |  |
| 2026-04-24 08:00:37 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 08:07:47 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-04-24 08:02:51 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-24 08:02:57 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-24 08:02:54 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-24 08:01:48 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-24 08:01:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:05:16 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:03:21 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:04:17 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:03:08 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:09:14 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:05:35 | Katharagama (Menik Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:06:29 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:14:59 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 08:05:28 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-24 08:01:13 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-24 08:01:42 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-24 08:06:29 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-04-24 08:09:34 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.019 |  |
| 2026-04-24 08:03:28 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.020 |  |
| 2026-04-24 08:02:09 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-04-24 08:14:34 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-04-24 08:01:12 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-04-24 08:02:13 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.021 |  |
| 2026-04-24 08:08:39 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | -0.027 |  |
| 2026-04-24 08:08:37 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.028 |  |
| 2026-04-24 08:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.029 |  |
| 2026-04-24 08:00:37 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-04-24 08:06:07 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.031 |  |
| 2026-04-24 08:00:58 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.035 |  |
| 2026-04-24 08:06:28 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.037 |  |
| 2026-04-24 08:02:20 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.049 |  |
| 2026-04-24 08:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | -0.050 |  |
| 2026-04-24 08:05:15 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.056 |  |
| 2026-04-24 08:01:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-04-24 08:12:26 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | -0.064 |  |
| 2026-04-24 08:03:42 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.086 |  |
| 2026-04-24 08:00:38 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.089 |  |
| 2026-04-24 08:09:37 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)