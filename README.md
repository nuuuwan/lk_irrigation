# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_16:19:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,210 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 16:19:15 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:14:24 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-21 16:10:12 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-04-21 16:09:31 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.129 |  |
| 2026-04-21 16:09:23 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:08:44 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.037 |  |
| 2026-04-21 16:08:36 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-21 16:08:01 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:07:27 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-04-21 16:07:09 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:06:45 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:06:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.019 |  |
| 2026-04-21 16:05:24 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.056 |  |
| 2026-04-21 16:05:11 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-21 16:05:11 | Dunamale (Aththanagalu Oya) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-04-21 16:04:59 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.071 |  |
| 2026-04-21 16:04:34 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-04-21 16:04:23 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-21 16:04:17 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-21 16:03:57 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-21 16:03:47 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 16:03:22 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-21 16:03:16 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | -0.070 |  |
| 2026-04-21 16:03:10 | Ellagawa (Kalu Ganga) | 6.41 | 🟢 Normal | -0.050 |  |
| 2026-04-21 16:03:01 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-04-21 16:02:57 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:02:56 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-04-21 16:02:16 | Norwood (Kelani Ganga) | 1.49 | 🟢 Normal | 0.616 | 🔺 Rising |
| 2026-04-21 16:02:13 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 16:02:00 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-21 16:01:56 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:01:43 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:01:40 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.050 |  |
| 2026-04-21 16:01:19 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-21 16:01:19 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.053 |  |
| 2026-04-21 16:00:51 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.041 |  |
| 2026-04-21 16:00:38 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-21 16:00:18 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 16:02:16 | Norwood (Kelani Ganga) | 1.49 | 🟢 Normal | 0.616 | 🔺 Rising |
| 2026-04-21 16:03:01 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-04-21 16:04:34 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-04-21 16:03:57 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-21 16:08:36 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-21 16:03:22 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-21 16:04:17 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-21 16:14:24 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-21 16:02:13 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 16:03:47 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 16:00:38 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-21 16:01:43 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:19:15 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:09:23 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:07:09 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:01:56 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:06:45 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:08:01 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:02:57 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:07:27 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-04-21 16:01:19 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-21 16:05:11 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-21 16:02:00 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-21 16:00:18 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.010 |  |
| 2026-04-21 16:02:56 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-04-21 16:04:23 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-21 16:06:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.019 |  |
| 2026-04-21 16:05:11 | Dunamale (Aththanagalu Oya) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-04-21 15:05:59 | Galgamuwa (Mee Oya) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-04-21 16:10:12 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-04-21 16:08:44 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.037 |  |
| 2026-04-21 16:00:51 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.041 |  |
| 2026-04-21 16:01:40 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.050 |  |
| 2026-04-21 16:03:10 | Ellagawa (Kalu Ganga) | 6.41 | 🟢 Normal | -0.050 |  |
| 2026-04-21 16:01:19 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.053 |  |
| 2026-04-21 16:05:24 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.056 |  |
| 2026-04-21 16:03:16 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | -0.070 |  |
| 2026-04-21 16:04:59 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.071 |  |
| 2026-04-21 16:09:31 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)