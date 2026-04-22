# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_20:22:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,262 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 20:22:21 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:18:12 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-22 20:13:09 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:12:47 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.082 |  |
| 2026-04-22 20:10:32 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-22 20:10:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:09:37 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-22 20:09:01 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.356 | 🔺 Rising |
| 2026-04-22 20:07:53 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-22 20:07:37 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-22 20:07:18 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-04-22 20:05:51 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:05:45 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:05:41 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:05:29 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:05:27 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-22 20:05:12 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-04-22 20:04:52 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.031 |  |
| 2026-04-22 20:04:34 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-22 20:04:24 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:04:12 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.424 | 🔺 Rising |
| 2026-04-22 20:04:08 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:04:03 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.029 |  |
| 2026-04-22 20:03:49 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.098 |  |
| 2026-04-22 20:03:26 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-22 20:03:15 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-04-22 20:02:59 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-04-22 20:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-22 20:02:42 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-22 20:02:28 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 20:02:04 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | -0.021 |  |
| 2026-04-22 20:01:43 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-22 20:01:42 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-22 20:01:13 | Kuda Oya (Kirindi Oya) | 4.15 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-04-22 20:00:17 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.342 | 🔺 Rising |
| 2026-04-22 20:00:11 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 20:04:12 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.424 | 🔺 Rising |
| 2026-04-22 20:09:01 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.356 | 🔺 Rising |
| 2026-04-22 20:00:17 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.342 | 🔺 Rising |
| 2026-04-22 20:01:13 | Kuda Oya (Kirindi Oya) | 4.15 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-04-22 20:03:15 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-04-22 20:02:42 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-22 20:18:12 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-22 20:05:27 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-22 20:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-22 20:09:37 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-22 20:03:26 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-22 20:00:11 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 20:01:43 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-22 20:07:37 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-22 20:01:42 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-22 20:07:53 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-22 20:02:28 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 20:10:32 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-22 20:13:09 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:04:08 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:22:21 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:05:41 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:06:20 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:05:45 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:05:29 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:05:51 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:10:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-22 20:05:12 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-22 20:04:34 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:52 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 20:07:18 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-04-22 20:02:59 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-04-22 20:02:04 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | -0.021 |  |
| 2026-04-22 20:04:03 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.029 |  |
| 2026-04-22 20:04:52 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.031 |  |
| 2026-04-22 20:12:47 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.082 |  |
| 2026-04-22 20:03:49 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)