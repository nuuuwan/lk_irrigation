# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_08:06:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,100 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 08:06:07 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:05:52 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:05:24 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-02-19 08:04:31 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.021 |  |
| 2026-02-19 08:04:25 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:04:24 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 08:03:54 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:03:18 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:03:18 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:59 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:52 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-19 08:02:43 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-19 08:02:39 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:36 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:18 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:12 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 08:02:08 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:08 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.051 |  |
| 2026-02-19 08:02:05 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:01:52 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-19 08:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 08:01:35 | Manampitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.031 |  |
| 2026-02-19 08:01:21 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-02-19 08:01:17 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-02-19 08:01:02 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:01:00 | Weraganthota (Mahaweli Ganga) | -2.36 | 🟢 Normal | -0.061 |  |
| 2026-02-19 08:00:58 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.125 |  |
| 2026-02-19 08:00:55 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:00:23 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-19 07:35:36 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 07:23:53 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 07:18:32 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 07:17:32 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.008 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 08:02:12 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 08:04:24 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 07:04:21 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 08:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 07:17:32 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-19 07:06:27 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:05:52 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:03:18 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 07:18:32 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:00:23 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:36 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:08 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:18 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:08 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 07:06:20 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 07:23:53 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:00:55 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:05 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:59 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:04:25 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:06:07 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:03:18 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:01:02 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 07:07:55 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:08:47 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:39 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:05:24 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-02-19 08:02:52 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-19 07:06:52 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-02-19 08:02:43 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-19 08:01:21 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-02-19 08:01:17 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-02-19 08:01:52 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-19 08:04:31 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.021 |  |
| 2026-02-19 08:01:35 | Manampitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.031 |  |
| 2026-02-19 08:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.051 |  |
| 2026-02-19 08:01:00 | Weraganthota (Mahaweli Ganga) | -2.36 | 🟢 Normal | -0.061 |  |
| 2026-02-19 07:07:09 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.119 |  |
| 2026-02-19 08:00:58 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)