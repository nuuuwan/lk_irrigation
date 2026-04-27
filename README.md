# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_21:25:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,759 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 21:25:54 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.014 |  |
| 2026-04-27 21:21:39 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-04-27 21:16:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.008 |  |
| 2026-04-27 21:11:29 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-27 21:10:53 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-04-27 21:10:49 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.146 |  |
| 2026-04-27 21:08:00 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:07:19 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 21:06:50 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.039 |  |
| 2026-04-27 21:06:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:06:20 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-27 21:05:36 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-27 21:04:52 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:04:50 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-04-27 21:04:00 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 21:03:34 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-27 21:03:22 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-27 21:03:21 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-27 21:03:15 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-27 21:03:10 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-27 21:03:07 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:02:59 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.030 |  |
| 2026-04-27 21:02:43 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-27 21:02:33 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.359 | 🔺 Rising |
| 2026-04-27 21:02:26 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-27 21:02:08 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-27 21:02:08 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:02:00 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-04-27 21:01:53 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-04-27 21:01:52 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:01:39 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-27 21:01:29 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:01:24 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.079 |  |
| 2026-04-27 21:00:43 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-27 21:00:20 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 21:00:19 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 21:02:33 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.359 | 🔺 Rising |
| 2026-04-27 21:01:53 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-04-27 21:02:43 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-27 21:06:20 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-27 21:00:43 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-27 21:07:19 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 21:03:15 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-27 21:05:36 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-27 21:03:34 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-27 21:00:20 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 21:02:26 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-27 21:11:29 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-27 21:03:21 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-27 18:05:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 21:04:00 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:02:08 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:01:52 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:03:07 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:01:29 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:00:19 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:08:00 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:04 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:06:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:04:52 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-27 21:16:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.008 |  |
| 2026-04-27 21:10:53 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-04-27 21:03:22 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-27 21:03:10 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-27 21:02:08 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-27 21:01:39 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-27 21:25:54 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.014 |  |
| 2026-04-27 21:04:50 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-04-27 21:02:00 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-04-27 21:21:39 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-04-27 21:02:59 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.030 |  |
| 2026-04-27 21:06:50 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.039 |  |
| 2026-04-27 21:01:24 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.079 |  |
| 2026-04-27 21:10:49 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)