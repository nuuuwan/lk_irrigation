# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_20:19:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,698 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 20:19:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.023 |  |
| 2026-05-06 20:14:08 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-06 20:11:40 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 20:11:11 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:10:47 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.070 |  |
| 2026-05-06 20:09:38 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-06 20:09:34 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:09:19 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:09:19 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:07:56 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:07:50 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:07:23 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.088 |  |
| 2026-05-06 20:06:47 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 20:06:22 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 20:06:20 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-05-06 20:06:14 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:05:24 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-06 20:04:59 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 20:04:42 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-05-06 20:04:34 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.039 |  |
| 2026-05-06 20:04:25 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 20:04:22 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:03:30 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 20:03:11 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:03:07 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 20:02:49 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:02:27 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:02:25 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-05-06 20:02:21 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-06 20:02:09 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-05-06 20:02:00 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-05-06 20:01:42 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 20:01:11 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:01:07 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:00:43 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 20:02:00 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-05-06 20:05:24 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-06 20:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 20:03:07 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 20:06:22 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 20:11:40 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 20:09:38 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-06 20:14:08 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-06 20:02:21 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-06 20:04:25 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 20:04:59 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 20:03:30 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 20:06:47 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:05:19 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 20:00:43 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:02:49 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:01:42 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:09:19 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:03:11 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:01:07 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:07:56 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:11:11 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:02:27 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:09:34 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:04:22 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:06:14 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:09:19 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:07:50 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:01:11 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:06:20 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-05-06 20:04:42 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-05-06 20:02:25 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-06 20:02:09 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-05-06 20:19:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.023 |  |
| 2026-05-06 20:04:34 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.039 |  |
| 2026-05-06 20:10:47 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.070 |  |
| 2026-05-06 20:07:23 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)