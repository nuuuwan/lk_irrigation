# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_22:10:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,063 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 22:10:06 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-01 22:08:35 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:07:57 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-01 22:07:18 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:06:21 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.056 |  |
| 2026-01-01 22:06:06 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:05:14 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-01-01 22:04:52 | Katharagama (Menik Ganga) | 1.33 | 🟢 Normal | -0.072 |  |
| 2026-01-01 22:04:42 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:04:35 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-01-01 22:04:20 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-01-01 22:04:13 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:04:10 | Thanamalwila (Kirindi Oya) | 2.06 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-01-01 22:03:59 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-01-01 22:03:44 | Padiyathalawa (Maduru Oya) | 3.59 | 🟢 Normal | 1.518 | 🔺 Rising |
| 2026-01-01 22:03:37 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-01 22:03:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-01 22:02:31 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-01-01 22:02:03 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.010 |  |
| 2026-01-01 22:01:59 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-01 22:01:46 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | -0.035 |  |
| 2026-01-01 22:01:38 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:01:25 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:01:23 | Horowpothana (Yan Oya) | 3.69 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-01 22:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:01:07 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.075 |  |
| 2026-01-01 22:00:23 | Kuda Oya (Kirindi Oya) | 2.10 | 🟢 Normal | -0.120 |  |
| 2026-01-01 21:59:53 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-01 21:17:39 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 21:15:03 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-01 21:13:34 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.048 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 22:03:44 | Padiyathalawa (Maduru Oya) | 3.59 | 🟢 Normal | 1.518 | 🔺 Rising |
| 2026-01-01 22:05:14 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-01-01 22:02:31 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-01-01 22:04:10 | Thanamalwila (Kirindi Oya) | 2.06 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-01-01 22:03:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-01 22:07:57 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-01 21:13:34 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-01 22:01:23 | Horowpothana (Yan Oya) | 3.69 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-01 21:09:37 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-01 22:10:06 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-01 22:01:38 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-01 21:01:21 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:09:46 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:07:18 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-01 21:01:26 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-01 21:01:45 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:08:35 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:04:13 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-01 21:17:39 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 21:59:53 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-01 21:04:02 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:06:06 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:04:42 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-01 22:04:20 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-01-01 22:03:37 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-01 22:02:03 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.010 |  |
| 2026-01-01 22:01:59 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-01 22:03:59 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-01-01 18:02:09 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.020 |  |
| 2026-01-01 22:04:35 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-01-01 20:14:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-01-01 21:03:02 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-01-01 22:01:46 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | -0.035 |  |
| 2026-01-01 18:00:31 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-01-01 22:06:21 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.056 |  |
| 2026-01-01 22:04:52 | Katharagama (Menik Ganga) | 1.33 | 🟢 Normal | -0.072 |  |
| 2026-01-01 22:01:07 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.075 |  |
| 2026-01-01 22:00:23 | Kuda Oya (Kirindi Oya) | 2.10 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)