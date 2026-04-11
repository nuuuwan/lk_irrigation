# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_10:16:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,065 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 10:16:02 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-11 10:12:52 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.026 |  |
| 2026-04-11 10:10:07 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.029 |  |
| 2026-04-11 10:09:40 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:08:27 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:08:20 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.056 |  |
| 2026-04-11 10:07:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:07:24 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:07:05 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:06:46 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:04:55 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 10:04:47 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:04:29 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:04:16 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:03:45 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 10:03:39 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:03:38 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-04-11 10:03:35 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.038 |  |
| 2026-04-11 10:03:26 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-11 10:03:20 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:03:08 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 10:02:51 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:02:46 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:02:46 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:02:45 | Weraganthota (Mahaweli Ganga) | -2.68 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-11 10:02:34 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.253 |  |
| 2026-04-11 10:02:22 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-11 10:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:02:12 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-04-11 10:02:08 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:01:52 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:01:34 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-11 10:01:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:01:18 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.041 |  |
| 2026-04-11 10:01:09 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:01:03 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.012 |  |
| 2026-04-11 10:00:54 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 10:02:45 | Weraganthota (Mahaweli Ganga) | -2.68 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-11 10:01:34 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-11 10:03:26 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-11 10:16:02 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-11 10:03:08 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 10:03:45 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 10:04:55 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 10:03:20 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:01:09 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:08:27 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:04:47 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:04:16 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:07:21 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:01:52 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:03:39 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:02:46 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:07:05 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:07:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:02:46 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:01:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:06:46 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:02:51 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:02:08 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:00:54 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:04:29 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:09:40 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:07:24 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:03:38 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-04-11 10:02:22 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-11 10:01:03 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.012 |  |
| 2026-04-11 10:12:52 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.026 |  |
| 2026-04-11 10:10:07 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.029 |  |
| 2026-04-11 10:02:12 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-04-11 10:03:35 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.038 |  |
| 2026-04-11 10:01:18 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.041 |  |
| 2026-04-11 10:08:20 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.056 |  |
| 2026-04-11 10:02:34 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.253 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)