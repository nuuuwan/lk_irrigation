# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_19:00:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,771 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 19:00:23 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-01 19:00:06 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:09:01 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | -0.028 |  |
| 2026-02-01 18:09:00 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 18:08:33 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-01 18:08:29 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-01 18:07:45 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:07:44 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:07:35 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:06:48 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:06:41 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-02-01 18:06:35 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:06:21 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:06:16 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:06:06 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:05:25 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.090 |  |
| 2026-02-01 18:05:11 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-02-01 18:04:59 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:04:58 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -0.021 |  |
| 2026-02-01 18:04:42 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:04:25 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.051 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 18:08:29 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-01 18:00:43 | Thanthirimale (Malwathu Oya) | 2.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-01 18:04:25 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-01 19:00:23 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-01 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 17:19:43 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-01 18:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 18:09:00 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 18:03:21 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:00:06 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:06:06 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:06:21 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:06:35 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:03:22 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:07:45 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:04:59 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:07:44 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:02:32 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:02:30 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:04:42 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:06:48 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:01:14 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:06:16 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:03:39 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:03:02 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:07:35 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:02:53 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:02:10 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:02:44 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:03:07 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:05:11 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-02-01 18:01:08 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-02-01 18:04:58 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -0.021 |  |
| 2026-02-01 18:09:01 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | -0.028 |  |
| 2026-02-01 18:02:51 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-02-01 18:01:47 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.050 |  |
| 2026-02-01 18:06:41 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-02-01 18:01:34 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.090 |  |
| 2026-02-01 18:05:25 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)