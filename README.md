# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_05:03:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,036 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 05:03:33 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-01-14 05:03:18 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:03:15 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:02:59 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:02:46 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-14 05:02:43 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-14 05:02:39 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-01-14 05:02:34 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:02:12 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:01:44 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:01:25 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-14 05:01:23 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.022 |  |
| 2026-01-14 05:01:02 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.152 |  |
| 2026-01-14 04:31:09 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:19:37 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.023 |  |
| 2026-01-14 04:12:29 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-14 04:09:07 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | -0.034 |  |
| 2026-01-14 04:08:30 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-01-14 04:07:33 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:06:35 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:06:25 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-14 04:06:24 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-01-14 04:06:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.071 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 03:14:06 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 6.261 | 🔺 Rising |
| 2026-01-14 03:00:47 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-14 04:06:25 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-14 04:12:29 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-14 05:01:25 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-14 05:02:43 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-14 04:31:09 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:01:19 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:02:59 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:02:12 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:03:18 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:03:54 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:03:37 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:03:15 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:02:33 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:01:54 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:02:34 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:10:45 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:05:03 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:01:31 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:06:35 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:10:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:11:04 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-01-14 04:06:24 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-01-14 04:03:22 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-14 04:02:07 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-01-14 05:02:46 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-14 05:03:33 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-01-13 18:03:19 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-01-14 05:02:39 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-01-14 05:01:23 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.022 |  |
| 2026-01-14 04:00:09 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.022 |  |
| 2026-01-14 04:19:37 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.023 |  |
| 2026-01-14 04:03:37 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.024 |  |
| 2026-01-14 04:09:07 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | -0.034 |  |
| 2026-01-13 18:01:14 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.040 |  |
| 2026-01-14 04:06:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.071 |  |
| 2026-01-14 05:01:02 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.152 |  |
| 2026-01-14 04:05:22 | Horowpothana (Yan Oya) | 3.54 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)