# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_00:24:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,863 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 00:24:12 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-04-28 00:17:48 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-28 00:13:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.005 |  |
| 2026-04-28 00:12:15 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.005 |  |
| 2026-04-28 00:08:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-28 00:07:38 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 46.753 | 🔺 Rising |
| 2026-04-28 00:07:28 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.029 |  |
| 2026-04-28 00:07:02 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-04-28 00:06:57 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 00:06:40 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-04-28 00:06:21 | Peradeniya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 46.753 | 🔺 Rising |
| 2026-04-28 00:06:19 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-28 00:06:19 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 00:07:38 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 46.753 | 🔺 Rising |
| 2026-04-28 00:07:02 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-04-28 00:08:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-28 00:03:01 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-28 00:02:55 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-28 00:03:47 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-28 00:06:19 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-28 00:03:24 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 18:05:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 00:01:33 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 00:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 00:12:15 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.005 |  |
| 2026-04-27 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-28 00:03:19 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 00:06:57 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 00:17:48 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-28 00:02:52 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-28 00:04:03 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-28 00:04:36 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-28 00:05:50 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:04 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-28 00:04:10 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-28 00:01:20 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-28 00:06:19 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-28 00:13:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.005 |  |
| 2026-04-27 23:07:50 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-04-27 23:01:18 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-28 00:01:04 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-28 00:03:24 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-04-28 00:24:12 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-04-28 00:06:40 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-04-28 00:01:06 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-04-28 00:07:28 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.029 |  |
| 2026-04-28 00:03:31 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-04-28 00:01:28 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.060 |  |
| 2026-04-28 00:03:20 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.067 |  |
| 2026-04-27 22:07:59 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.072 |  |
| 2026-04-28 00:04:45 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.180 |  |
| 2026-04-28 00:05:52 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)