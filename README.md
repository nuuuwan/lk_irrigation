# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_21:14:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,091 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 21:14:43 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:10:45 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-04-24 21:09:34 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.108 |  |
| 2026-04-24 21:07:15 | Katharagama (Menik Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-04-24 21:07:04 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:06:36 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:06:16 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.031 |  |
| 2026-04-24 21:06:02 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:06:01 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.048 |  |
| 2026-04-24 21:05:52 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:05:47 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-24 21:05:42 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.028 |  |
| 2026-04-24 21:05:41 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:05:02 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 21:04:48 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:04:43 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 21:04:27 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-04-24 21:04:20 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-04-24 21:03:57 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2026-04-24 21:03:37 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-04-24 21:03:01 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.030 |  |
| 2026-04-24 21:02:57 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.052 |  |
| 2026-04-24 21:02:50 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:02:47 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:02:46 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-04-24 21:02:32 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | -0.034 |  |
| 2026-04-24 21:02:27 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.021 |  |
| 2026-04-24 21:02:25 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.021 |  |
| 2026-04-24 21:02:18 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:02:15 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-24 21:01:56 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-24 21:01:34 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:01:22 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:01:13 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:00:49 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:00:19 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 21:10:45 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-04-24 21:02:15 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-24 21:05:47 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-24 21:05:02 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 21:04:43 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 18:01:26 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 21:01:34 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:04:48 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:01:56 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 18:01:28 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:05:52 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:02:50 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:00:49 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:05:41 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:01:22 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:02:18 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:14:43 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:07:04 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:01:13 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:02:47 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 21:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-24 21:04:27 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-04-24 21:07:15 | Katharagama (Menik Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-04-24 21:03:37 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-04-24 21:04:20 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-04-24 21:00:19 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-04-24 21:02:25 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.021 |  |
| 2026-04-24 21:02:27 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.021 |  |
| 2026-04-24 21:05:42 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.028 |  |
| 2026-04-24 18:04:10 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.028 |  |
| 2026-04-24 21:03:01 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.030 |  |
| 2026-04-24 21:02:46 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-04-24 21:06:16 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.031 |  |
| 2026-04-24 21:02:32 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | -0.034 |  |
| 2026-04-24 21:06:01 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.048 |  |
| 2026-04-24 21:02:57 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.052 |  |
| 2026-04-24 21:03:57 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2026-04-24 20:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.071 |  |
| 2026-04-24 21:09:34 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)