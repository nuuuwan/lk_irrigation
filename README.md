# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_14:29:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,291 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 14:29:47 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:17:10 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-01 14:12:23 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:08:34 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:08:19 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.028 |  |
| 2026-04-01 14:07:53 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:07:29 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:07:12 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-04-01 14:07:07 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:05:51 | Glencourse (Kelani Ganga) | 8.18 | 🟢 Normal | -0.049 |  |
| 2026-04-01 14:04:51 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-04-01 14:04:22 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 14:03:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:03:40 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:03:24 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | -0.196 |  |
| 2026-04-01 14:03:23 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:03:20 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:03:17 | Rathnapura (Kalu Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:03:16 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:03:09 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:03:09 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-04-01 14:03:06 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-01 14:02:56 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:42 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:41 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:23 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.049 |  |
| 2026-04-01 14:02:21 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:17 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-04-01 14:02:09 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:08 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:06 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:04 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:01:55 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:01:46 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:01:44 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | -0.010 |  |
| 2026-04-01 14:01:36 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-01 14:01:16 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:01:08 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 14:04:51 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-04-01 14:01:36 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-01 14:04:22 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 14:17:10 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-01 14:02:06 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:03:16 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:42 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:56 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:07:07 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:01:55 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:09 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:01:46 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:04 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:12:23 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:01:16 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:07:53 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:08 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:03:23 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:03:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:03:40 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:17 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:03:20 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:29:47 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:03:17 | Rathnapura (Kalu Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:01:08 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:07:29 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:03:09 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:08:34 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:41 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:02:21 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 14:07:12 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-04-01 14:03:06 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-01 14:01:44 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | -0.010 |  |
| 2026-04-01 14:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-04-01 14:03:09 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-04-01 14:08:19 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.028 |  |
| 2026-04-01 14:02:23 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.049 |  |
| 2026-04-01 14:05:51 | Glencourse (Kelani Ganga) | 8.18 | 🟢 Normal | -0.049 |  |
| 2026-04-01 14:03:24 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | -0.196 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)