# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_20:12:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,486 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 20:12:28 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.017 |  |
| 2026-05-18 20:09:27 | Putupaula (Kalu Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-05-18 20:07:13 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.085 |  |
| 2026-05-18 20:05:34 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.005 |  |
| 2026-05-18 20:05:34 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | -0.021 |  |
| 2026-05-18 20:05:32 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-05-18 20:05:29 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-18 20:05:29 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | -0.010 |  |
| 2026-05-18 20:05:28 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.028 |  |
| 2026-05-18 20:05:09 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-05-18 20:05:08 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-18 20:05:03 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-18 20:04:30 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-18 20:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.026 |  |
| 2026-05-18 20:04:08 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:04:07 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-18 20:04:03 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-18 20:03:59 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 20:03:35 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:03:17 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:03:13 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:02:53 | Hanwella (Kelani Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-05-18 20:02:39 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:02:17 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:02:01 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-05-18 20:01:56 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:01:43 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.072 |  |
| 2026-05-18 20:01:21 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:01:14 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:00:53 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | -0.015 |  |
| 2026-05-18 20:00:43 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:00:37 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:00:18 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:00:12 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-18 19:34:16 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-18 19:33:53 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-18 19:33:35 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.058 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 20:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.026 |  |
| 2026-05-18 20:05:03 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-18 20:04:03 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-18 20:04:07 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-18 20:05:29 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-18 20:05:08 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-18 20:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:00:18 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:01:21 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:01:56 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:04:08 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:03:13 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-18 18:51:29 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:03:59 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:00:37 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:03:17 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:02:39 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:03:35 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:00:43 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:01:14 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:02:17 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:05:34 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.005 |  |
| 2026-05-18 20:05:29 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | -0.010 |  |
| 2026-05-18 20:04:30 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-18 20:02:53 | Hanwella (Kelani Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-05-18 20:02:01 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-05-18 20:05:32 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-05-18 19:02:01 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | -0.014 |  |
| 2026-05-18 20:00:53 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | -0.015 |  |
| 2026-05-18 20:12:28 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.017 |  |
| 2026-05-18 20:05:09 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-05-18 20:09:27 | Putupaula (Kalu Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-05-18 20:05:34 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | -0.021 |  |
| 2026-05-18 20:05:28 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.028 |  |
| 2026-05-18 18:01:53 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | -0.033 |  |
| 2026-05-18 20:01:43 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.072 |  |
| 2026-05-18 18:01:24 | Thanthirimale (Malwathu Oya) | 2.75 | 🟢 Normal | -0.082 |  |
| 2026-05-18 20:07:13 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)