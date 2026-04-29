# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_12:03:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,172 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 12:03:13 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:03:08 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.041 |  |
| 2026-04-29 12:03:04 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:03:03 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:02:56 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:02:46 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-04-29 12:02:37 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.010 |  |
| 2026-04-29 12:02:34 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-29 12:02:16 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:02:14 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:01:50 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-04-29 12:01:47 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:01:46 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:01:22 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:01:18 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-04-29 12:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-04-29 12:01:05 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:00:45 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 1044.000 | 🔺 Rising |
| 2026-04-29 12:00:43 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 1044.000 | 🔺 Rising |
| 2026-04-29 12:00:12 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 11:59:14 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 1044.000 | 🔺 Rising |
| 2026-04-29 11:57:56 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-29 11:16:58 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.008 |  |
| 2026-04-29 11:16:26 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 12:00:45 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 1044.000 | 🔺 Rising |
| 2026-04-29 11:06:24 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-29 11:02:55 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-29 11:05:43 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-29 11:57:56 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-29 12:00:12 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 11:05:06 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 12:02:16 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:01:22 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:02:06 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:08:59 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:05:48 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:03:13 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:01:32 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:01:22 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:01:47 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:01:46 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:03:04 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:03:03 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:02:56 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:01:05 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:02:14 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:03:09 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:00:28 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:16:26 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.008 |  |
| 2026-04-29 11:16:58 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.008 |  |
| 2026-04-29 12:02:37 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.010 |  |
| 2026-04-29 12:02:34 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-29 12:01:50 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-04-29 12:01:18 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-04-29 11:02:50 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.020 |  |
| 2026-04-29 11:06:21 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-04-29 11:05:43 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-04-29 12:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-04-29 12:02:46 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-04-29 11:07:15 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.040 |  |
| 2026-04-29 12:03:08 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.041 |  |
| 2026-04-29 11:03:08 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.041 |  |
| 2026-04-29 11:08:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)