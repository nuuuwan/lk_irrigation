# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_20:25:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,723 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 20:25:10 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-04-27 20:11:33 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:11:23 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:09:12 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.272 |  |
| 2026-04-27 20:08:28 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:08:08 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-27 20:07:55 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-27 20:07:02 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-27 20:06:40 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:06:24 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.020 |  |
| 2026-04-27 20:05:35 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.021 |  |
| 2026-04-27 20:04:34 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-27 20:04:26 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.010 |  |
| 2026-04-27 20:04:12 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:04:08 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:03:18 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:03:15 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 20:03:09 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 20:03:08 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:02:48 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:02:34 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 20:02:33 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-04-27 20:02:23 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-27 20:02:18 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 20:02:18 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.440 | 🔺 Rising |
| 2026-04-27 20:01:29 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.014 |  |
| 2026-04-27 20:01:28 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-04-27 20:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | -0.031 |  |
| 2026-04-27 20:01:10 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:01:09 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.031 |  |
| 2026-04-27 20:00:44 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:00:40 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-27 20:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-27 20:00:23 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 20:02:18 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.440 | 🔺 Rising |
| 2026-04-27 20:04:34 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-27 20:02:23 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-27 20:07:02 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-27 20:08:08 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-27 20:07:55 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-27 20:00:40 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-27 20:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-27 20:02:18 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 19:07:47 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-27 18:05:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 20:02:34 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 20:03:15 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 20:03:09 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 19:02:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:04:08 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:08:28 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:00:44 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:06:40 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:01:10 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:03:08 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:11:33 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:03:18 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:04 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:11:23 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:02:48 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:04:12 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-27 20:04:26 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.010 |  |
| 2026-04-27 20:01:28 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-04-27 20:01:29 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.014 |  |
| 2026-04-27 20:02:33 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-04-27 20:06:24 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.020 |  |
| 2026-04-27 20:05:35 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.021 |  |
| 2026-04-27 20:25:10 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-04-27 20:01:09 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.031 |  |
| 2026-04-27 20:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | -0.031 |  |
| 2026-04-27 20:00:23 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |
| 2026-04-27 20:09:12 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.272 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)