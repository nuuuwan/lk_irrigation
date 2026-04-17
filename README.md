# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_15:10:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,620 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 15:10:20 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:09:21 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:09:07 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:06:56 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-17 15:06:50 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:06:14 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-17 15:06:08 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:06:00 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:05:58 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:05:55 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-04-17 15:05:09 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.066 |  |
| 2026-04-17 15:04:59 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:04:47 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:04:30 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:04:26 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:04:21 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:04:07 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:04:02 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:03:37 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:03:35 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:03:32 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-17 15:03:21 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:03:06 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.111 |  |
| 2026-04-17 15:03:01 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-04-17 15:02:47 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:02:41 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-17 15:02:38 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:02:35 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-04-17 15:02:21 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:02:19 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:02:02 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:01:24 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:01:22 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:01:00 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:00:49 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:00:35 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:00:26 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-17 14:58:57 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 15:06:56 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-17 15:02:41 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-17 15:06:14 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-17 15:03:32 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-17 15:02:47 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:04:02 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:01:22 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:09:21 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:06:00 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:04:47 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:01:00 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:00:26 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:00:49 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:00:35 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:02:02 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:04:21 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:06:08 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:04:30 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:09:07 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:10:20 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:02:21 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:05:55 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-04-17 15:02:38 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:04:59 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:03:21 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:04:26 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:03:37 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:02:19 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:03:35 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:04:07 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:01:24 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:06:50 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-17 15:03:01 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-04-17 15:02:35 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-04-17 14:58:57 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.031 |  |
| 2026-04-17 15:05:09 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.066 |  |
| 2026-04-17 15:03:06 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)