# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_17:18:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,421 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 17:18:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:08:52 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-15 17:07:34 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:07:04 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-15 17:07:03 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:06:47 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.010 |  |
| 2026-01-15 17:06:44 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:06:39 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:06:20 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-01-15 17:05:34 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.159 |  |
| 2026-01-15 17:05:31 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-01-15 17:05:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.045 |  |
| 2026-01-15 17:05:23 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.031 |  |
| 2026-01-15 17:04:39 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-01-15 17:04:36 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.044 |  |
| 2026-01-15 17:04:25 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-15 17:04:09 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:04:08 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:03:59 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 17:03:32 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:03:31 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:03:09 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 17:03:09 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:02:53 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.034 |  |
| 2026-01-15 17:02:47 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:02:42 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-15 17:02:22 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 17:02:15 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:02:14 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.031 |  |
| 2026-01-15 17:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-15 17:02:12 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:02:07 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.033 |  |
| 2026-01-15 17:01:58 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-01-15 17:01:44 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:01:35 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:01:34 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:01:16 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:00:24 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.060 |  |
| 2026-01-15 17:00:15 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-15 16:23:41 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-15 16:22:14 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 17:08:52 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-15 17:03:59 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 17:04:25 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-15 17:03:09 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 17:02:22 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 17:02:12 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:01:44 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:04:08 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:02:15 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:03:32 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:01:35 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:01:16 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:03:31 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:03:09 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:04:09 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:06:39 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:06:44 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:07:03 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:01:34 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:07:34 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:02:47 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:18:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:04:39 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-01-15 17:02:42 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-15 17:06:47 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.010 |  |
| 2026-01-15 17:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-15 17:07:04 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-15 17:00:15 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-15 17:01:58 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-01-15 17:06:20 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-01-15 17:05:23 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.031 |  |
| 2026-01-15 17:02:14 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.031 |  |
| 2026-01-15 17:05:31 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-01-15 17:02:07 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.033 |  |
| 2026-01-15 17:02:53 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.034 |  |
| 2026-01-15 17:04:36 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.044 |  |
| 2026-01-15 17:05:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.045 |  |
| 2026-01-15 17:00:24 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.060 |  |
| 2026-01-15 17:05:34 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)