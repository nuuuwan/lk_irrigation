# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_14:14:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,492 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 14:14:21 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.017 |  |
| 2026-04-27 14:14:09 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-27 14:13:03 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:11:04 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.073 |  |
| 2026-04-27 14:10:54 | Ellagawa (Kalu Ganga) | 4.86 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-27 14:09:52 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-27 14:08:56 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.051 |  |
| 2026-04-27 14:08:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.045 |  |
| 2026-04-27 14:06:59 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-04-27 14:06:56 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.043 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 14:04:27 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-04-27 14:09:52 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-27 14:14:09 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-27 14:03:26 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-27 14:06:56 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-27 14:10:54 | Ellagawa (Kalu Ganga) | 4.86 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-27 14:02:51 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-27 14:02:02 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 14:01:13 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 14:01:25 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:03:27 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:01:01 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:02:17 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:00:37 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:02:19 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:02:02 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:13:38 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:05:38 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:02:29 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:05:29 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:13:03 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:06:07 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:03:39 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:02:07 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:02:07 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-27 14:02:16 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-27 14:02:56 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-27 14:00:33 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-27 14:06:59 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-04-27 14:01:47 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-04-27 14:14:21 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.017 |  |
| 2026-04-27 14:04:52 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-04-27 14:03:06 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.041 |  |
| 2026-04-27 14:08:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.045 |  |
| 2026-04-27 14:08:56 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.051 |  |
| 2026-04-27 14:00:35 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-04-27 14:11:04 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.073 |  |
| 2026-04-27 14:02:08 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.089 |  |
| 2026-04-27 14:05:15 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)