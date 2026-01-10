# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_04:16:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,352 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 04:16:10 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-01-11 04:14:52 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:11:25 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-11 04:09:30 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.023 |  |
| 2026-01-11 04:09:24 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.019 |  |
| 2026-01-11 04:06:45 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:06:05 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.022 |  |
| 2026-01-11 04:05:38 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 04:04:06 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-11 04:03:56 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-11 04:03:45 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-11 04:03:39 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 04:02:59 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-11 04:02:49 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:02:38 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:02:31 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:02:08 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:02:02 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.012 |  |
| 2026-01-11 04:01:49 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.124 |  |
| 2026-01-11 04:01:45 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-01-11 04:01:34 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-01-11 04:01:34 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:00:52 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:00:51 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:00:25 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.035 |  |
| 2026-01-11 04:00:20 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:44:26 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 04:11:25 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-11 03:04:16 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-11 04:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-11 04:03:45 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-11 04:03:56 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-11 04:05:38 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 04:03:39 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 03:05:52 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 04:02:59 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-11 04:00:52 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:00:20 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:02:31 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:14:52 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:22 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:02:08 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:04:06 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:06:45 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:02:49 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:02:38 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:01:48 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:00:07 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:01:34 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:00:51 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:01:35 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:08:31 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:01:51 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:06:11 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 04:01:45 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-01-11 04:01:34 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-01-11 04:02:02 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.012 |  |
| 2026-01-11 04:09:24 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.019 |  |
| 2026-01-11 04:16:10 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-01-10 18:02:45 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-11 04:06:05 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.022 |  |
| 2026-01-11 04:09:30 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.023 |  |
| 2026-01-11 04:00:25 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.035 |  |
| 2026-01-11 04:01:49 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.124 |  |
| 2026-01-11 03:04:20 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)