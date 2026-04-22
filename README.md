# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_12:01:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,912 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 12:01:06 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-04-22 12:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-04-22 12:00:18 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-04-22 11:21:21 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-22 11:10:49 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | -0.017 |  |
| 2026-04-22 11:10:31 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.047 |  |
| 2026-04-22 11:10:20 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-04-22 11:09:39 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.016 |  |
| 2026-04-22 11:09:08 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.018 |  |
| 2026-04-22 11:07:15 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | -0.037 |  |
| 2026-04-22 11:07:14 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 11:10:20 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-04-22 11:21:21 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-22 11:02:32 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 11:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-22 11:04:19 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 11:01:58 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 11:06:40 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 11:02:02 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 11:01:10 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 11:01:46 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-22 11:04:15 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-22 11:02:25 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 11:05:47 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-22 11:06:01 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-22 11:02:41 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 11:07:14 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-22 11:03:58 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.010 |  |
| 2026-04-22 11:02:36 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-22 11:01:14 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-22 11:02:24 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-04-22 11:09:39 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.016 |  |
| 2026-04-22 11:10:49 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | -0.017 |  |
| 2026-04-22 11:09:08 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.018 |  |
| 2026-04-22 11:05:25 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.019 |  |
| 2026-04-22 11:03:19 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-04-22 12:01:06 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-04-22 12:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-04-22 11:03:16 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | -0.021 |  |
| 2026-04-22 11:02:00 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.021 |  |
| 2026-04-22 11:02:45 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.022 |  |
| 2026-04-22 11:04:40 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.029 |  |
| 2026-04-22 12:00:18 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-04-22 11:04:02 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.031 |  |
| 2026-04-22 11:07:15 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | -0.037 |  |
| 2026-04-22 11:03:32 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.040 |  |
| 2026-04-22 11:10:31 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.047 |  |
| 2026-04-22 11:00:47 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.054 |  |
| 2026-04-22 11:03:18 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.079 |  |
| 2026-04-22 11:02:29 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)