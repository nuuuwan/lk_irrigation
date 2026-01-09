# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_08:17:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,712 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 08:17:34 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:15:49 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-01-09 08:12:51 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-01-09 08:11:10 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:08:15 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:07:19 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:06:24 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-01-09 08:06:16 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | -0.066 |  |
| 2026-01-09 08:06:07 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-01-09 08:06:04 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.029 |  |
| 2026-01-09 08:05:37 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:05:17 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:05:12 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:05:02 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-01-09 08:04:58 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.070 |  |
| 2026-01-09 08:04:36 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:04:09 | Padiyathalawa (Maduru Oya) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-01-09 08:04:01 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-09 08:03:39 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-09 08:03:32 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:03:07 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-09 08:02:57 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.121 |  |
| 2026-01-09 08:02:53 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 08:02:42 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:02:41 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:02:40 | Manampitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-09 08:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.060 |  |
| 2026-01-09 08:02:26 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:02:05 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-01-09 08:01:58 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-09 08:01:55 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.010 |  |
| 2026-01-09 08:01:45 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:01:37 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-09 08:01:16 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:01:14 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:01:13 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:01:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:01:06 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 07:26:36 | Moragaswewa (Deduru Oya) | 3.20 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-01-09 08:05:02 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-01-09 08:06:24 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-01-09 08:02:40 | Manampitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-09 08:01:58 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-09 08:03:07 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-09 08:04:01 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-09 08:02:53 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 08:01:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:02:26 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:02:42 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:11:10 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:05:37 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:17:34 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:07:19 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:01:14 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:08:15 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:05:17 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:01:13 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:01:16 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:03:32 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:04:36 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:05:12 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:02:41 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:01:45 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 08:01:55 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.010 |  |
| 2026-01-09 08:03:39 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-09 08:01:37 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-09 08:02:05 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-01-09 08:15:49 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-01-09 08:01:06 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.014 |  |
| 2026-01-09 08:12:51 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-01-09 08:04:09 | Padiyathalawa (Maduru Oya) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-01-09 08:06:04 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.029 |  |
| 2026-01-09 08:06:07 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-01-09 08:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.060 |  |
| 2026-01-09 08:06:16 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | -0.066 |  |
| 2026-01-09 08:04:58 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.070 |  |
| 2026-01-09 08:02:57 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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