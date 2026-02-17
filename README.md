# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--17_10:13:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **75,402 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 10:13:01 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-17 10:10:41 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:09:59 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:09:55 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-17 10:09:45 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:09:43 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:08:22 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:07:32 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-17 10:07:31 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:07:02 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.009 |  |
| 2026-02-17 10:06:31 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.048 |  |
| 2026-02-17 10:06:09 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:05:51 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.804 |  |
| 2026-02-17 10:05:05 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-02-17 10:04:44 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.029 |  |
| 2026-02-17 10:04:31 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-17 10:04:22 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:03:57 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 10:03:55 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:03:33 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:03:31 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.051 |  |
| 2026-02-17 10:03:27 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:02:59 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 10:02:52 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:02:43 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-02-17 10:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-02-17 10:02:23 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:02:20 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-02-17 10:02:13 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:02:05 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.010 |  |
| 2026-02-17 10:02:04 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 10:01:45 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-02-17 10:01:27 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-17 10:01:20 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:01:07 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-02-17 10:01:02 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:00:58 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.016 |  |
| 2026-02-17 10:00:40 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 10:07:32 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-17 10:09:55 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-17 10:04:31 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-17 10:02:04 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 10:02:59 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 10:03:57 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 10:13:01 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-17 10:01:02 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:03:33 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:10:41 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:01:20 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:02:23 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:02:13 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:08:22 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:09:45 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:09:59 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:02:52 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:04:22 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:09:43 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:06:09 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:07:31 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:03:27 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:03:55 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:00:40 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-17 10:07:02 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.009 |  |
| 2026-02-17 10:02:05 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.010 |  |
| 2026-02-17 10:01:27 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-17 10:05:05 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-02-17 10:00:58 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.016 |  |
| 2026-02-17 10:01:45 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-02-17 10:01:07 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-02-17 10:02:43 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-02-17 10:02:20 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-02-17 10:04:44 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.029 |  |
| 2026-02-17 10:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-02-17 10:06:31 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.048 |  |
| 2026-02-17 10:03:31 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.051 |  |
| 2026-02-17 10:05:51 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.804 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)