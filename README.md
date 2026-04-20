# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_09:14:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,035 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 09:14:32 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:11:14 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.044 |  |
| 2026-04-20 09:08:36 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-20 09:08:26 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.049 |  |
| 2026-04-20 09:06:12 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:05:54 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:05:37 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:05:31 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-20 09:05:23 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.120 |  |
| 2026-04-20 09:05:22 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.016 |  |
| 2026-04-20 09:04:47 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.126 |  |
| 2026-04-20 09:04:44 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-20 09:04:43 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-04-20 09:04:35 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:04:32 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:04:20 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:04:11 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:03:51 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-04-20 09:03:47 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 09:03:39 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-20 09:03:38 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.063 |  |
| 2026-04-20 09:03:26 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 09:03:24 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:03:18 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:03:12 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:03:01 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:02:36 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-20 09:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.054 |  |
| 2026-04-20 09:02:12 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:02:06 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.031 |  |
| 2026-04-20 09:01:51 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.131 |  |
| 2026-04-20 09:01:44 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-04-20 09:01:43 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:01:31 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-04-20 09:01:29 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:00:59 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:00:25 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 09:00:23 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-04-20 09:00:08 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 09:05:31 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-20 09:04:44 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-20 09:08:36 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-20 09:03:47 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 09:00:25 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 09:03:26 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 09:04:35 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:00:59 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:03:24 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:01:43 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:02:12 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:00:08 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:03:18 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:14:32 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:05:54 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:04:11 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:05:37 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:03:01 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:03:12 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:06:12 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:04:32 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:01:29 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:04:20 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-20 09:03:39 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-20 09:03:51 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-04-20 09:01:44 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-04-20 09:05:22 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.016 |  |
| 2026-04-20 09:02:36 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-20 09:00:23 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-04-20 09:04:43 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-04-20 09:02:06 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.031 |  |
| 2026-04-20 09:11:14 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.044 |  |
| 2026-04-20 09:08:26 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.049 |  |
| 2026-04-20 09:01:31 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-04-20 09:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.054 |  |
| 2026-04-20 09:03:38 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.063 |  |
| 2026-04-20 09:05:23 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.120 |  |
| 2026-04-20 09:04:47 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.126 |  |
| 2026-04-20 09:01:51 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)