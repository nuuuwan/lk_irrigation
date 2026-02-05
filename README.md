# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--05_17:15:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **64,937 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 17:15:00 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:09:54 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-05 17:07:59 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-02-05 17:07:54 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-05 17:07:07 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 17:06:55 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:06:35 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-05 17:06:14 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-05 17:06:08 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-02-05 17:05:12 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-05 17:04:59 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.057 |  |
| 2026-02-05 17:04:57 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.025 |  |
| 2026-02-05 17:04:31 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-05 17:04:08 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:04:08 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:04:03 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:03:14 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-05 17:03:08 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.011 |  |
| 2026-02-05 17:03:04 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-02-05 17:03:00 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-05 17:02:53 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:02:49 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:02:46 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-05 17:02:32 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:02:26 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:02:19 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:02:13 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:01:47 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:01:43 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-02-05 17:01:41 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:00:56 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:00:37 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.083 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 17:03:04 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-02-05 17:05:12 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-05 17:06:14 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-05 06:07:34 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-05 17:02:46 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-05 17:03:00 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-05 17:07:54 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-05 17:03:14 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-05 17:07:07 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 17:06:35 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-05 17:09:54 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-05 15:04:06 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.003 |  |
| 2026-02-05 17:02:32 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:01:41 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:04:08 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:02:53 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:00:56 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:15:00 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:02:19 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:02:13 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:01:47 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:02:26 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:02:49 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:04:03 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:06:55 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-05 17:04:08 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-05 17:07:59 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-02-05 17:04:31 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-05 17:03:08 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.011 |  |
| 2026-02-05 17:01:43 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-02-05 17:06:08 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-02-05 17:04:57 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.025 |  |
| 2026-02-05 17:04:59 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.057 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-05 17:00:37 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)