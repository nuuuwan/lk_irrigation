# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_01:10:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,429 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 01:10:39 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-23 01:08:07 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-23 01:06:59 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-23 01:06:27 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.067 |  |
| 2026-04-23 01:05:04 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-23 01:04:15 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-23 01:04:12 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-23 01:04:10 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-04-23 01:03:59 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-23 01:03:31 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.044 |  |
| 2026-04-23 01:03:19 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-23 01:03:16 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 01:03:08 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.147 |  |
| 2026-04-23 01:02:50 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-23 01:02:39 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-23 01:02:27 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.258 |  |
| 2026-04-23 01:02:26 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 01:02:18 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-23 01:02:18 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-23 01:02:16 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-04-23 01:02:11 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.083 |  |
| 2026-04-23 01:02:08 | Thanamalwila (Kirindi Oya) | 2.85 | 🟢 Normal | -0.270 |  |
| 2026-04-23 01:02:05 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-23 01:01:40 | Kuda Oya (Kirindi Oya) | 2.37 | 🟢 Normal | -0.129 |  |
| 2026-04-23 01:01:32 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-23 01:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-04-23 00:59:47 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.150 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 23:18:07 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-04-23 01:02:16 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-04-23 01:02:50 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-23 01:03:19 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-23 01:01:32 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-23 01:03:59 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-23 01:10:39 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-23 00:04:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 01:03:16 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 00:32:14 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-23 01:05:04 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-23 01:02:26 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 01:08:07 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-23 01:02:39 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:02:50 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 01:06:59 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-23 01:02:18 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-23 01:04:15 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:04:05 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:12:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-23 01:04:10 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-23 01:04:12 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:52 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 23:05:49 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -0.012 |  |
| 2026-04-23 01:02:18 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-23 01:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-04-22 22:00:50 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-04-23 00:07:57 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.039 |  |
| 2026-04-23 01:03:31 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.044 |  |
| 2026-04-23 01:06:27 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.067 |  |
| 2026-04-23 01:02:11 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.083 |  |
| 2026-04-23 01:01:40 | Kuda Oya (Kirindi Oya) | 2.37 | 🟢 Normal | -0.129 |  |
| 2026-04-23 01:03:08 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.147 |  |
| 2026-04-23 00:59:47 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.150 |  |
| 2026-04-23 01:02:27 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.258 |  |
| 2026-04-23 01:02:08 | Thanamalwila (Kirindi Oya) | 2.85 | 🟢 Normal | -0.270 |  |
| 2026-04-23 00:06:30 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -1.714 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)