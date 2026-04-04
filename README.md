# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_16:20:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,072 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 16:20:16 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:20:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 16:15:28 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-04 16:15:19 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:09:50 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.036 |  |
| 2026-04-04 16:09:11 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-04 16:07:47 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:06:33 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:06:24 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-04-04 16:05:42 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-04-04 16:05:20 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-04 16:05:05 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.051 |  |
| 2026-04-04 16:04:52 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:04:07 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-04 16:03:57 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-04 16:03:53 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 16:03:34 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 16:03:25 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:03:22 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 16:03:21 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.059 |  |
| 2026-04-04 16:03:19 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-04 16:02:55 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:02:46 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.019 |  |
| 2026-04-04 16:02:44 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:02:25 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.060 |  |
| 2026-04-04 16:02:00 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-04 16:02:00 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-04 16:01:49 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 16:01:47 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:01:42 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 16:05:20 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-04 16:15:28 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-04 16:02:00 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-04 16:20:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 16:00:43 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-04 16:01:49 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 16:09:11 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-04 16:00:22 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-04 16:03:53 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 16:03:34 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 16:03:22 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 16:02:25 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:01:35 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:03:25 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:01:47 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:01:01 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:02:44 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:04:52 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:15:19 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:07:47 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:02:55 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:00:19 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:06:33 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:20:16 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 16:03:19 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-04 16:03:57 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-04 16:04:07 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-04 15:02:24 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-04 16:02:00 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-04 16:06:24 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-04-04 16:02:46 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.019 |  |
| 2026-04-04 16:00:58 | Thanthirimale (Malwathu Oya) | 2.57 | 🟢 Normal | -0.030 |  |
| 2026-04-04 16:01:42 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.030 |  |
| 2026-04-04 16:05:42 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-04-04 16:09:50 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.036 |  |
| 2026-04-04 16:05:05 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.051 |  |
| 2026-04-04 16:03:21 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.059 |  |
| 2026-04-04 16:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.060 |  |
| 2026-04-04 16:01:31 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)