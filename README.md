# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_04:27:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,599 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 04:27:27 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:24:24 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.005 |  |
| 2026-04-04 04:17:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-04 04:10:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-04 04:10:33 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:09:53 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-04-04 04:08:26 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-04-04 04:07:00 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:06:41 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-04 04:06:22 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.337 |  |
| 2026-04-04 04:06:10 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.061 |  |
| 2026-04-04 04:05:30 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.034 |  |
| 2026-04-04 04:05:19 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-04 04:05:17 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 04:04:46 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.029 |  |
| 2026-04-04 04:04:18 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-04-04 04:04:16 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:04:11 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-04-04 04:04:10 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.268 |  |
| 2026-04-04 04:03:48 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:03:27 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:02:53 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-04-04 04:02:28 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 04:02:16 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:02:09 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-04-04 04:01:46 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:01:24 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-04-04 04:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-04 04:00:58 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:00:55 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:00:33 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 03:41:47 | Magura (Kalu Ganga) | 3.08 | 🟢 Normal | -0.268 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 04:08:26 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-04-04 04:09:53 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-04-04 03:01:11 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-04 04:06:41 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-03 18:05:32 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-04 03:04:40 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-04 03:07:56 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-04 04:00:33 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 04:02:28 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 04:17:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-04 04:05:17 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:02:55 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 04:10:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-04 04:04:16 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:00:55 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:01:46 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:00:58 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:03:27 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:07:00 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:27:27 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:10:33 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:02:16 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-04 04:24:24 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.005 |  |
| 2026-04-04 03:18:04 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.005 |  |
| 2026-04-04 04:04:11 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-04-04 04:01:24 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-04-04 04:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-04 04:05:19 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-04 04:02:09 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-04-04 00:04:26 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-04-04 04:04:18 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-04-04 04:02:53 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-04-04 04:04:46 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.029 |  |
| 2026-04-04 04:05:30 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.034 |  |
| 2026-04-04 03:02:39 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.055 |  |
| 2026-04-03 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.060 |  |
| 2026-04-04 04:06:10 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.061 |  |
| 2026-04-04 04:04:10 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.268 |  |
| 2026-04-04 04:06:22 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)