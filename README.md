# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_18:21:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,951 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 18:21:50 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.008 |  |
| 2026-04-15 18:15:28 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:14:07 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.017 |  |
| 2026-04-15 18:10:53 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:09:14 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.028 |  |
| 2026-04-15 18:08:56 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.018 |  |
| 2026-04-15 18:08:29 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.058 |  |
| 2026-04-15 18:08:01 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:07:50 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.083 |  |
| 2026-04-15 18:07:48 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:06:53 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:06:43 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:06:35 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:05:35 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-15 18:05:24 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:05:24 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.038 |  |
| 2026-04-15 18:05:14 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-15 18:04:47 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-15 18:04:27 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-15 18:04:06 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-15 18:03:43 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:03:27 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-15 18:03:24 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-04-15 18:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-15 18:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-15 18:03:11 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:02:53 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:02:51 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:02:32 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-15 18:02:21 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:02:12 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:01:18 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:01:07 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.011 |  |
| 2026-04-15 18:01:03 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.062 |  |
| 2026-04-15 18:00:59 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:54 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:44 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-04-15 18:00:15 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-04-15 18:00:07 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 18:03:24 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-04-15 18:02:32 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-15 18:05:14 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-15 18:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-15 18:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-15 18:06:35 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:07:48 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:01:18 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:07 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:05:24 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:02:12 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:06:53 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:15:28 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:02:21 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:02:51 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:59 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:03:11 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:06:43 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:03:43 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:02:53 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:10:53 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:54 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:21:50 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.008 |  |
| 2026-04-15 18:04:27 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-15 18:03:27 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-15 18:04:47 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-15 18:05:35 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-15 18:04:06 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-15 18:01:07 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.011 |  |
| 2026-04-15 18:14:07 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.017 |  |
| 2026-04-15 18:08:56 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.018 |  |
| 2026-04-15 17:04:50 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.019 |  |
| 2026-04-15 18:00:15 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-04-15 18:09:14 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.028 |  |
| 2026-04-15 18:00:44 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-04-15 18:05:24 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.038 |  |
| 2026-04-15 18:08:29 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.058 |  |
| 2026-04-15 18:01:03 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.062 |  |
| 2026-04-15 18:07:50 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)