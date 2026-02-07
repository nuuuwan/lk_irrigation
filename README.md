# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_19:00:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,806 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 19:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:00:32 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:00:09 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:23:08 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.007 |  |
| 2026-02-07 18:15:37 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.034 |  |
| 2026-02-07 18:12:02 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-02-07 18:10:34 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:08:34 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:07:47 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:07:35 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.026 |  |
| 2026-02-07 18:07:14 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.022 |  |
| 2026-02-07 18:07:05 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:06:43 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.009 |  |
| 2026-02-07 18:06:10 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-02-07 18:05:47 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-07 18:05:37 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -72.000 |  |
| 2026-02-07 18:05:35 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -72.000 |  |
| 2026-02-07 18:05:20 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:05:18 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.050 |  |
| 2026-02-07 18:05:10 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 18:06:10 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-02-07 18:02:29 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-02-07 18:05:47 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-07 18:03:11 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 18:01:06 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:02:23 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:02:38 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:03:02 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:05:20 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 17:17:32 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:07:47 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:00:32 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:03:18 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:00:44 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:00:09 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:07:05 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:05:10 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:08:34 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:04:10 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:02:19 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:23:08 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.007 |  |
| 2026-02-07 18:12:02 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-02-07 18:06:43 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.009 |  |
| 2026-02-07 18:02:51 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-02-07 18:03:09 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-02-07 18:02:38 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-02-07 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.020 |  |
| 2026-02-07 18:00:20 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-02-07 18:00:39 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-02-07 18:07:14 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.022 |  |
| 2026-02-07 18:07:35 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.026 |  |
| 2026-02-07 18:15:37 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.034 |  |
| 2026-02-07 18:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.039 |  |
| 2026-02-07 18:05:18 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.050 |  |
| 2026-02-07 18:02:37 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.058 |  |
| 2026-02-07 18:01:43 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.058 |  |
| 2026-02-07 18:04:22 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-02-07 18:05:37 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)